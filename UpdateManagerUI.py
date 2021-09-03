# Form implementation generated from reading ui file '.\UpdateManager.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(468, 304)
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(10, 10, 171, 281))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.logo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/gui_resources/Updates.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.currentVersionLabel = QtWidgets.QLabel(Dialog)
        self.currentVersionLabel.setGeometry(QtCore.QRect(210, 10, 121, 31))
        self.currentVersionLabel.setObjectName("currentVersionLabel")
        self.currentVersionBox = QtWidgets.QLabel(Dialog)
        self.currentVersionBox.setGeometry(QtCore.QRect(330, 10, 91, 31))
        self.currentVersionBox.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.currentVersionBox.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.currentVersionBox.setLineWidth(1)
        self.currentVersionBox.setObjectName("currentVersionBox")
        self.checkUpdatesButton = QtWidgets.QPushButton(Dialog)
        self.checkUpdatesButton.setGeometry(QtCore.QRect(250, 270, 121, 23))
        self.checkUpdatesButton.setObjectName("checkUpdatesButton")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(380, 270, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.changelogBoxScrollArea = QtWidgets.QScrollArea(Dialog)
        self.changelogBoxScrollArea.setGeometry(QtCore.QRect(190, 130, 271, 121))
        self.changelogBoxScrollArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.changelogBoxScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.changelogBoxScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.changelogBoxScrollArea.setWidgetResizable(True)
        self.changelogBoxScrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.changelogBoxScrollArea.setObjectName("changelogBoxScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 252, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.changelogBox = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.changelogBox.setScaledContents(True)
        self.changelogBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.changelogBox.setWordWrap(True)
        self.changelogBox.setIndent(0)
        self.changelogBox.setObjectName("changelogBox")
        self.verticalLayout.addWidget(self.changelogBox)
        self.changelogBoxScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.latestVersionLabel = QtWidgets.QLabel(Dialog)
        self.latestVersionLabel.setGeometry(QtCore.QRect(210, 50, 121, 31))
        self.latestVersionLabel.setObjectName("latestVersionLabel")
        self.latestVersionBox = QtWidgets.QLabel(Dialog)
        self.latestVersionBox.setGeometry(QtCore.QRect(330, 50, 91, 31))
        self.latestVersionBox.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.latestVersionBox.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.latestVersionBox.setLineWidth(1)
        self.latestVersionBox.setObjectName("latestVersionBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 105, 271, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update Manager - Mr. Worldwide"))
        self.currentVersionLabel.setText(_translate("Dialog", "Current Version"))
        self.currentVersionBox.setText(_translate("Dialog", "v1.0.0"))
        self.checkUpdatesButton.setText(_translate("Dialog", "Check for Updates"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.changelogBox.setText(_translate("Dialog", "No changelog available."))
        self.latestVersionLabel.setText(_translate("Dialog", "Latest Version"))
        self.latestVersionBox.setText(_translate("Dialog", "v1.0.0"))
        self.label.setText(_translate("Dialog", "Latest Version Changelog"))