from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog
import PyQt6.QtCore as QtCore
import PyQt6.QtGui as QtGui
import sys, time, json, requests, traceback, configparser, os
import MrWorldwideUI, ConfigurationUI, UpdateManagerUI

version = "v1.0.0"

class LangTypes:
	ENGLISH = "English"
	ARABIC = "Arabic"
	CHINESE = "Chinese"
	DUTCH = "Dutch"
	FRENCH = "French"
	GERMAN = "German"
	HINDI = "Hindi"
	INDONESIAN = "Indonesian"
	IRISH = "Irish"
	ITALIAN = "Italian"
	JAPANESE = "Japanese"
	KOREAN = "Korean"
	POLISH = "Polish"
	PORTUGUESE = "Portuguese"
	RUSSIAN = "Russian"
	SPANISH = "Spanish"
	TURKISH = "Turkish"
	UKRANIAN = "Ukranian"
	VIETNAMESE = "Vietnamese"

class WorkerSignals(QtCore.QObject):
	callback = QtCore.pyqtSignal(str)


class Worker(QtCore.QRunnable):
	def __init__(self, fn, *args, **kwargs):
		super(Worker, self).__init__()

		# Store constructor arguments (re-used for processing)
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()

		# Add the callback to our kwargs
		self.kwargs['progressCallback'] = self.signals.callback

	@QtCore.pyqtSlot()
	def run(self):

		# Retrieve args/kwargs here; and fire processing using them
		try:
			result = self.fn(*self.args, **self.kwargs)
		except:
			print(traceback.print_exc())
		else:
			self.signals.callback.emit(result)

def readConfigurationFile(config):
	try:
		configFile = open("config.ini")
		configFile.close()
		return config.read("config.ini")
	except:
		config['general'] = {}
		config['general']['libretranslate_mirror'] = 'https://translate.astian.org/translate'

		config['defaults'] = {}
		config['defaults']['default_source_language'] = LangTypes.ENGLISH
		config['defaults']['default_target_language'] = LangTypes.SPANISH

		with open('config.ini', 'w') as configFile:
			config.write(configFile)
			configFile.close()
			return config

class MrWorldwide(QWidget, MrWorldwideUI.Ui_Dialog, QtCore.QThread):

	selectedFile = ""
	selectedTargetLocation = ""
	sourceFileKeys = []
	sourceFileValues = []
	totalLangFileLines = 0
	shouldAbort = False

	def run(self):
		# Setup resources
		logo = QtGui.QPixmap(resource_path("gui_resources/MrWorldwide.png"))
		icon = QtGui.QIcon(resource_path("gui_resources/MrWorldwide.png"))

		# Set the logos and images
		self.setWindowIcon(icon) # TODO: Custom icon
		self.logo.setPixmap(logo)

		self.config = configparser.ConfigParser()
	
		readConfigurationFile(self.config)

		# Setup button actions
		self.closeButton.clicked.connect(self.closeEvent)
		self.abortButton.clicked.connect(self.abortEvent)
		self.startButton.clicked.connect(self.preTranslate)
		self.openFileButton.clicked.connect(self.openFileEvent)
		self.targetLocationButton.clicked.connect(self.selectFileLocationEvent)
		self.configButton.clicked.connect(self.openConfiguration)

		# Setup dropdown boxes
		self.sourceLangBox.addItems([LangTypes.ENGLISH, LangTypes.ARABIC, LangTypes.CHINESE, LangTypes.DUTCH, LangTypes.FRENCH, LangTypes.GERMAN, LangTypes.HINDI, LangTypes.INDONESIAN, LangTypes.IRISH, LangTypes.ITALIAN, LangTypes.JAPANESE, LangTypes.KOREAN, LangTypes.POLISH, LangTypes.PORTUGUESE, LangTypes.RUSSIAN, LangTypes.SPANISH, LangTypes.TURKISH, LangTypes.UKRANIAN, LangTypes.VIETNAMESE])
		self.targetLangBox.addItems([LangTypes.ENGLISH, LangTypes.ARABIC, LangTypes.CHINESE, LangTypes.DUTCH, LangTypes.FRENCH, LangTypes.GERMAN, LangTypes.HINDI, LangTypes.INDONESIAN, LangTypes.IRISH, LangTypes.ITALIAN, LangTypes.JAPANESE, LangTypes.KOREAN, LangTypes.POLISH, LangTypes.PORTUGUESE, LangTypes.RUSSIAN, LangTypes.SPANISH, LangTypes.TURKISH, LangTypes.UKRANIAN, LangTypes.VIETNAMESE])
	
		self.sourceLangBox.setCurrentText(self.config["defaults"]["default_source_language"])
		self.targetLangBox.setCurrentText(self.config["defaults"]["default_target_language"])

		self.apiMirror = self.config["general"]["libretranslate_mirror"]

	# Open the configuration GUI
	def openConfiguration(self, event):
		self.configurationDialog = ConfigurationDialog()
		self.configurationDialog.setup(self)
		self.configurationDialog.show()

	# Refresh the configuration
	def refreshConfiguration(self):
		readConfigurationFile(self.config)
		self.sourceLangBox.setCurrentText(self.config["defaults"]["default_source_language"])
		self.targetLangBox.setCurrentText(self.config["defaults"]["default_target_language"])
		self.apiMirror = self.config["general"]["libretranslate_mirror"]

	# Close event, for handling closing of the program
	def closeEvent(self, event):
		global app
		self.close()
		app.exit()

	# Abort event, for shutting down translation functions
	def abortEvent(self, event):
		global shouldAbort
		global totalLangFileLines
		self.shouldAbort = True
		self.progressBar.setValue(0)
		self.progressBarLabel.setText("Idle")
		self.logAction("ABORT: Translation process canceled.")


	# Open file event, for selecting a language file and starting the read process
	def openFileEvent(self, event):
		self.totalLangFileLines = 0
		self.selectedFile = QFileDialog.getOpenFileName(self, 'Select a Minecraft language file', '','JSON Files (*.json)')[0]
		self.fileSelectionBox.setText(str(self.selectedFile))
		self.readLangFile()

	# Select output file location event, for setting the target location
	def selectFileLocationEvent(self, event):
		self.selectedTargetLocation = QFileDialog.getSaveFileName(self, 'Select an output location', 'target.json','JSON Files (*.json)')[0]
		self.targetLocationBox.setText(str(self.selectedTargetLocation))
	
	# Read a language file and get the keys, values, and set various content on the GUI
	def readLangFile(self):
		global sourceFileValues
		global totalLangFileLines
		self.sourceFileValues = []
		self.sourceFileKeys = []
		# Read input JSON and make it usable
		startReadInputTime = time.time()
		if self.selectedFile != "":
			with open(self.selectedFile, 'r') as f:
				data = json.load(f)
				self.sourceFileKeys = data.keys()
				for item in data:
					if self.shouldAbort:
						return
					self.sourceFileValues.append(data[item])
					self.totalLangFileLines = self.totalLangFileLines + 1
			self.logAction("Reading input file took " + str(((time.time() - startReadInputTime) * 1000).__round__(3)) + " ms.")
			self.langFileEntryCounter.display(self.totalLangFileLines)
			self.logAction("Found " + str(self.totalLangFileLines) + " entries.")

	def preTranslate(self, event):
		global totalLangFileLines
		global selectedFile
		global selectedTargetLocation
		canProceed = True
		self.shouldAbort = False
		if self.selectedFile == "":
			self.logAction("ERROR: No language file selected.")
			canProceed = False
		elif self.totalLangFileLines == 0:
			self.logAction("ERROR: The selected language file is empty.")
			canProceed = False
		elif self.selectedTargetLocation == "":
			self.logAction("ERROR: No target location specified.")
			canProceed = False
		elif self.sourceLangBox.currentText() == self.targetLangBox.currentText():
			self.logAction("ERROR: Target language is the same as the source")
			canProceed = False
		if canProceed:
			self.logAction("Beginning translations with a source language of " + self.sourceLangBox.currentText() + " and a target language of " + self.targetLangBox.currentText())
			self.logAction("Using LibreTranslate mirror: " + self.config["general"]["libretranslate_mirror"])
			self.disableButtonsDuringTranslations()
			self.threadpool = QtCore.QThreadPool()
			self.worker = Worker(self.startTranslations)
			self.worker.signals.callback.connect(self.threadCallbackHandler)
			self.threadpool.start(self.worker)

	def disableButtonsDuringTranslations(self):
		self.startButton.setDisabled(True)
		self.openFileButton.setDisabled(True)
		self.targetLocationButton.setDisabled(True)
		self.closeButton.setDisabled(True)
		self.configButton.setDisabled(True)

	def enableButtonsAfterTranslations(self):
		self.startButton.setDisabled(False)
		self.openFileButton.setDisabled(False)
		self.targetLocationButton.setDisabled(False)
		self.closeButton.setDisabled(False)
		self.configButton.setDisabled(False)

	def threadCallbackHandler(self, callback):
		try:
			exec(callback)
		except:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			exctype, value, traceback.format_exc()
			app.exit()

	def startTranslations(self, progressCallback):
		global sourceFileValues
		global totalLangFileLines
		global shouldAbort
		progressCallback.emit('self.progressBarLabel.setText("Starting translations")')
		# Set query headers
		headers = {
			'accept': 'application/json',
			'Content-Type': 'application/x-www-form-urlencoded',
		}
		# Really inefficient but it works ??\_(???)_/??
		startQueryTime = time.time()
		responseJSON = []
		progressCallback.emit('self.progressBarLabel.setText("Translating...")')
		itemLoopIteration = 1
		try:
			requests.post(self.config["general"]["libretranslate_mirror"], headers=headers, data=None)
			hasFailedResolve = False
		except:
			requests.post('https://translate.astian.org/translate', headers=headers, data=None)
			progressCallback.emit('self.logAction("Failed to resolve LibreTranslate mirror. Defaulting to https://translate.astian.org/translate")')
			hasFailedResolve = True
		for item in self.sourceFileValues:
			if self.shouldAbort:
				return
			# Setup the progress bar, by mapping the total translation count to 100
			progressCallback.emit('self.progressBar.setValue(int(((' + str(itemLoopIteration) + ' / self.totalLangFileLines) * 100).__round__(0)))')
			# Set query data
			data = {
				'q': item,
				'source': self.getLangIdentifier(self.sourceLangBox.currentText()),
				'target': self.getLangIdentifier(self.targetLangBox.currentText())
			}
			# Send the query and get the response
			if hasFailedResolve == True:
				response = requests.post('https://translate.astian.org/translate', headers=headers, data=data)
			else:
				response = requests.post(self.config["general"]["libretranslate_mirror"], headers=headers, data=data)
			responseData = json.loads(response.content.decode(response.encoding))["translatedText"]
			responseJSON.append(str(responseData).rstrip('"').replace('\u00ab', '').lstrip('"').replace('\u00bb', ''))
			itemLoopIteration = itemLoopIteration + 1

		progressCallback.emit('self.logAction("Query time was " + str(time.time() - ' + str(startQueryTime) + ') + " seconds.")')
		progressCallback.emit('self.progressBarLabel.setText("Translations complete")')
		progressCallback.emit('self.saveToFile(' + str(responseJSON) + ')')
		

	# Save the JSON data to file
	def saveToFile(self, responseJSON):
		global sourceFileKeys
		global shouldAbort
		self.progressBarLabel.setText("Writing to file...")
		self.progressBar.setValue(0)
		with open(self.targetLocationBox.text(), 'w', encoding="UTF-8") as f:
			compiledDict = dict()
			responseJSONList = list(responseJSON)
			currentIteration = 0
			for item in self.sourceFileKeys:
				if self.shouldAbort:
					return
				compiledDict.update({item: str(responseJSONList[currentIteration])})
				currentIteration = currentIteration + 1
				progBarVal = int(((currentIteration / self.totalLangFileLines) * 100).__round__(0))
				self.progressBar.setValue(progBarVal)
			json.dump(compiledDict, f, separators=(',', ': '), indent="	", ensure_ascii=False)
		self.enableButtonsAfterTranslations()
		self.logAction("Translations written to file.")
		self.progressBarLabel.setText("All tasks completed.")

	# Log information to the console
	def logAction(self, text: str):
		if self.logBox.text() == "No log information available. ":
			self.logBox.setText("")
			preparedLogText = ">> " + text
		else:
			preparedLogText = self.logBox.text() + "\n>> " + text
		self.logBox.setText(preparedLogText)
		self.logBoxScrollArea.verticalScrollBar().setValue(self.logBoxScrollArea.verticalScrollBar().maximum())

	def getLangIdentifier(self, lang):
		if lang == LangTypes.ENGLISH:
			return "en"
		if lang == LangTypes.ARABIC:
			return "ar"
		if lang == LangTypes.CHINESE:
			return "zh"
		if lang == LangTypes.DUTCH:
			return "nl"
		if lang == LangTypes.FRENCH:
			return "fr"
		if lang == LangTypes.GERMAN:
			return "de"
		if lang == LangTypes.HINDI:
			return "hi"
		if lang == LangTypes.INDONESIAN:
			return "id"
		if lang == LangTypes.IRISH:
			return "ga"
		if lang == LangTypes.ITALIAN:
			return "it"
		if lang == LangTypes.JAPANESE:
			return "ja"
		if lang == LangTypes.KOREAN:
			return "ko"
		if lang == LangTypes.POLISH:
			return "pl"
		if lang == LangTypes.PORTUGUESE:
			return "pt"
		if lang == LangTypes.RUSSIAN:
			return "ru"
		if lang == LangTypes.SPANISH:
			return "es"
		if lang == LangTypes.TURKISH:
			return "tr"
		if lang == LangTypes.UKRANIAN:
			return "uk"
		if lang == LangTypes.VIETNAMESE:
			return "vi"

	# Initialize the program
	def __init__(self, parent=None):
		global app
		super(MrWorldwide, self).__init__(parent)
		self.setupUi(self)
		self.run()


class ConfigurationDialog(QWidget, ConfigurationUI.Ui_Dialog):
	def __init__(self, parent=None):
		super(ConfigurationDialog, self).__init__(parent)
		self.setupUi(self)
		self.run()
	
	def run(self):
		# Setup resources
		logo = QtGui.QPixmap(resource_path("gui_resources/Configuration.png"))
		icon = QtGui.QIcon(resource_path("gui_resources/Configuration.png"))

		# Set the logos and images
		self.setWindowIcon(icon) # TODO: Custom icon
		self.logo.setPixmap(logo)

		# Read configuration
		self.config = configparser.ConfigParser()
		readConfigurationFile(self.config)
		# Setup dropdown boxes
		self.defaultSourceLangBox.addItems([LangTypes.ENGLISH, LangTypes.ARABIC, LangTypes.CHINESE, LangTypes.DUTCH, LangTypes.FRENCH, LangTypes.GERMAN, LangTypes.HINDI, LangTypes.INDONESIAN, LangTypes.IRISH, LangTypes.ITALIAN, LangTypes.JAPANESE, LangTypes.KOREAN, LangTypes.POLISH, LangTypes.PORTUGUESE, LangTypes.RUSSIAN, LangTypes.SPANISH, LangTypes.TURKISH, LangTypes.UKRANIAN, LangTypes.VIETNAMESE])
		self.defaultTargetLangBox.addItems([LangTypes.ENGLISH, LangTypes.ARABIC, LangTypes.CHINESE, LangTypes.DUTCH, LangTypes.FRENCH, LangTypes.GERMAN, LangTypes.HINDI, LangTypes.INDONESIAN, LangTypes.IRISH, LangTypes.ITALIAN, LangTypes.JAPANESE, LangTypes.KOREAN, LangTypes.POLISH, LangTypes.PORTUGUESE, LangTypes.RUSSIAN, LangTypes.SPANISH, LangTypes.TURKISH, LangTypes.UKRANIAN, LangTypes.VIETNAMESE])

		# Apply current configuration
		self.apiMirror.setText(self.config["general"]["libretranslate_mirror"])
		self.defaultSourceLangBox.setCurrentText(self.config["defaults"]["default_source_language"])
		self.defaultTargetLangBox.setCurrentText(self.config["defaults"]["default_target_language"])

		# Setup button actions
		self.closeButton.clicked.connect(self.closeEvent)
		self.applyButton.clicked.connect(self.applyEvent)
		self.updateButton.clicked.connect(self.openUpdateManager)

	# Setup variables
	def setup(self, parent):
		self.parent = parent

	# Close event, for handling closing of the program
	def closeEvent(self, event):
		self.close()

	# Update event, for opening the update manager
	# Open the configuration GUI
	def openUpdateManager(self, event):
		self.updateManagerDialog = UpdateManagerDialog()
		self.updateManagerDialog.setup(self)
		self.updateManagerDialog.show()

	# Apply event, for handling applying of configurations
	def applyEvent(self, event):
		self.config = configparser.ConfigParser()
		self.config['general'] = {}
		self.config['general']['libretranslate_mirror'] = self.apiMirror.text()

		self.config['defaults'] = {}
		self.config['defaults']['default_source_language'] = self.defaultSourceLangBox.currentText()
		self.config['defaults']['default_target_language'] = self.defaultTargetLangBox.currentText()

		with open('config.ini', 'w') as configFile:
			self.config.write(configFile)
			configFile.close()
		self.parent.refreshConfiguration()
		self.close()

class UpdateManagerDialog(QWidget, UpdateManagerUI.Ui_Dialog):
	def __init__(self, parent=None):
		super(UpdateManagerDialog, self).__init__(parent)
		self.setupUi(self)
		self.run()
	
	def run(self):
		# Setup resources
		logo = QtGui.QPixmap(resource_path("gui_resources/Updates.png"))
		icon = QtGui.QIcon(resource_path("gui_resources/Updates.png"))

		# Set the logos and images
		self.setWindowIcon(icon) # TODO: Custom icon
		self.logo.setPixmap(logo)

		# Setup button actions
		self.closeButton.clicked.connect(self.closeEvent)
		self.checkUpdatesButton.clicked.connect(self.checkForUpdatesEvent)

		global version
		self.currentVersionBox.setText(version)

	# Setup variables
	def setup(self, parent):
		self.parent = parent

	# Close event, for handling closing of the program
	def closeEvent(self, event):
		self.close()

	# Check for updates event
	def checkForUpdatesEvent(self, event):
		self.updateData = json.loads(requests.get("https://raw.githubusercontent.com/AnonymousHacker1279/MrWorldwide/master/update.json").text)
		self.latestVersionBox.setText(self.updateData["latest"])
		self.changelogBox.setText(self.updateData["changelog"] + "\n\nDownload the update here: " + self.updateData["link"])
		

def main():
	global app
	app = QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False)
	app.setStyle("Fusion")
	form = MrWorldwide()
	form.show()
	app.exec()

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath('.'), relative_path)

if __name__ == '__main__':
	main()