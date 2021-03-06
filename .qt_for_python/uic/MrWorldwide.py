# Form implementation generated from reading ui file 'c:\Users\Nicholas\Documents\GitHub\MrWorldwide\MrWorldwide.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(778, 327)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/MrWorldwide.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(20, 20, 171, 291))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.logo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/gui_resources/MrWorldwide.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(420, 260, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.langFileEntryCounter = QtWidgets.QLCDNumber(Dialog)
        self.langFileEntryCounter.setGeometry(QtCore.QRect(250, 262, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.langFileEntryCounter.setFont(font)
        self.langFileEntryCounter.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.langFileEntryCounter.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.langFileEntryCounter.setLineWidth(1)
        self.langFileEntryCounter.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.langFileEntryCounter.setProperty("intValue", 0)
        self.langFileEntryCounter.setObjectName("langFileEntryCounter")
        self.sourceLangBox = QtWidgets.QComboBox(Dialog)
        self.sourceLangBox.setGeometry(QtCore.QRect(340, 10, 91, 22))
        self.sourceLangBox.setEditable(True)
        self.sourceLangBox.setCurrentText("")
        self.sourceLangBox.setMaxVisibleItems(10)
        self.sourceLangBox.setObjectName("sourceLangBox")
        self.sourceLangSelectLabel = QtWidgets.QLabel(Dialog)
        self.sourceLangSelectLabel.setGeometry(QtCore.QRect(240, 10, 91, 21))
        self.sourceLangSelectLabel.setObjectName("sourceLangSelectLabel")
        self.targetLangSelectLabel = QtWidgets.QLabel(Dialog)
        self.targetLangSelectLabel.setGeometry(QtCore.QRect(240, 40, 91, 21))
        self.targetLangSelectLabel.setObjectName("targetLangSelectLabel")
        self.targetLangBox = QtWidgets.QComboBox(Dialog)
        self.targetLangBox.setGeometry(QtCore.QRect(340, 40, 91, 22))
        self.targetLangBox.setEditable(True)
        self.targetLangBox.setCurrentText("")
        self.targetLangBox.setMaxVisibleItems(10)
        self.targetLangBox.setObjectName("targetLangBox")
        self.langFileEntryCounterLabel = QtWidgets.QLabel(Dialog)
        self.langFileEntryCounterLabel.setGeometry(QtCore.QRect(230, 300, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.langFileEntryCounterLabel.setFont(font)
        self.langFileEntryCounterLabel.setScaledContents(True)
        self.langFileEntryCounterLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.langFileEntryCounterLabel.setObjectName("langFileEntryCounterLabel")
        self.progressBarLabel = QtWidgets.QLabel(Dialog)
        self.progressBarLabel.setGeometry(QtCore.QRect(426, 232, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBarLabel.setFont(font)
        self.progressBarLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.progressBarLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBarLabel.setObjectName("progressBarLabel")
        self.openFileButton = QtWidgets.QPushButton(Dialog)
        self.openFileButton.setGeometry(QtCore.QRect(610, 80, 75, 23))
        self.openFileButton.setObjectName("openFileButton")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(690, 80, 75, 23))
        self.startButton.setObjectName("startButton")
        self.lineBreak = QtWidgets.QFrame(Dialog)
        self.lineBreak.setGeometry(QtCore.QRect(390, 250, 3, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineBreak.setFont(font)
        self.lineBreak.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lineBreak.setLineWidth(1)
        self.lineBreak.setMidLineWidth(10)
        self.lineBreak.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.lineBreak.setObjectName("lineBreak")
        self.targetLocationBox = QtWidgets.QLineEdit(Dialog)
        self.targetLocationBox.setGeometry(QtCore.QRect(570, 10, 181, 20))
        self.targetLocationBox.setReadOnly(True)
        self.targetLocationBox.setObjectName("targetLocationBox")
        self.targetLocationLabel = QtWidgets.QLabel(Dialog)
        self.targetLocationLabel.setGeometry(QtCore.QRect(470, 10, 91, 20))
        self.targetLocationLabel.setObjectName("targetLocationLabel")
        self.lineBreak2 = QtWidgets.QFrame(Dialog)
        self.lineBreak2.setGeometry(QtCore.QRect(240, 60, 501, 21))
        self.lineBreak2.setMidLineWidth(3)
        self.lineBreak2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.lineBreak2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lineBreak2.setObjectName("lineBreak2")
        self.description = QtWidgets.QLabel(Dialog)
        self.description.setGeometry(QtCore.QRect(240, 80, 241, 151))
        self.description.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.description.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.description.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.description.setLineWidth(1)
        self.description.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.description.setOpenExternalLinks(True)
        self.description.setObjectName("description")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(690, 290, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.abortButton = QtWidgets.QPushButton(Dialog)
        self.abortButton.setGeometry(QtCore.QRect(610, 290, 75, 23))
        self.abortButton.setObjectName("abortButton")
        self.fileSelectionBox = QtWidgets.QLineEdit(Dialog)
        self.fileSelectionBox.setGeometry(QtCore.QRect(570, 40, 181, 20))
        self.fileSelectionBox.setReadOnly(True)
        self.fileSelectionBox.setObjectName("fileSelectionBox")
        self.selectedFileLabel = QtWidgets.QLabel(Dialog)
        self.selectedFileLabel.setGeometry(QtCore.QRect(470, 40, 91, 20))
        self.selectedFileLabel.setObjectName("selectedFileLabel")
        self.logBoxScrollArea = QtWidgets.QScrollArea(Dialog)
        self.logBoxScrollArea.setGeometry(QtCore.QRect(490, 110, 271, 121))
        self.logBoxScrollArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.logBoxScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.logBoxScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.logBoxScrollArea.setWidgetResizable(True)
        self.logBoxScrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.logBoxScrollArea.setObjectName("logBoxScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 252, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logBox = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.logBox.setScaledContents(True)
        self.logBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.logBox.setWordWrap(True)
        self.logBox.setIndent(0)
        self.logBox.setObjectName("logBox")
        self.verticalLayout.addWidget(self.logBox)
        self.logBoxScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.targetLocationButton = QtWidgets.QPushButton(Dialog)
        self.targetLocationButton.setGeometry(QtCore.QRect(490, 80, 111, 23))
        self.targetLocationButton.setObjectName("targetLocationButton")
        self.configButton = QtWidgets.QPushButton(Dialog)
        self.configButton.setGeometry(QtCore.QRect(420, 290, 91, 23))
        self.configButton.setObjectName("configButton")

        self.retranslateUi(Dialog)
        self.sourceLangBox.setCurrentIndex(-1)
        self.targetLangBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mr. Worldwide, by AnonymousHacker1279"))
        self.sourceLangSelectLabel.setText(_translate("Dialog", "Source Language"))
        self.targetLangSelectLabel.setText(_translate("Dialog", "Target Language"))
        self.langFileEntryCounterLabel.setText(_translate("Dialog", "Language File Entries"))
        self.progressBarLabel.setText(_translate("Dialog", "Idle"))
        self.openFileButton.setText(_translate("Dialog", "Open File"))
        self.startButton.setText(_translate("Dialog", "Start"))
        self.targetLocationBox.setText(_translate("Dialog", "No location selected."))
        self.targetLocationLabel.setText(_translate("Dialog", "Target Location"))
        self.description.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mr. Worldwide is a program designed by</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/AnonymousHacker1279\"><span style=\" text-decoration: underline; color:#0000ff;\">AnonymousHacker1279</span></a> that aims to </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">automatically generate translations for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Minecraft language files.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It\'s quite simple to use:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Select your input and target languages</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Select the target location to put the new</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    file at</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Click Start. The program will then begin</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    translating your file.</p></body></html>"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.abortButton.setText(_translate("Dialog", "Abort"))
        self.fileSelectionBox.setText(_translate("Dialog", "No file selected."))
        self.selectedFileLabel.setText(_translate("Dialog", "Selected File"))
        self.logBox.setText(_translate("Dialog", "No log information available. "))
        self.targetLocationButton.setText(_translate("Dialog", "Target Location"))
        self.configButton.setText(_translate("Dialog", "Configuration"))
