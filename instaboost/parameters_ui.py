# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'echo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Echo(object):
    def setupUi(self, Echo):
        Echo.setObjectName("Echo")
        Echo.resize(407, 450)
        self.lineEdit = QtWidgets.QLineEdit(Echo)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 199, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Echo)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 90, 199, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Echo)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 150, 199, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Echo)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 180, 199, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Echo)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 210, 199, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Echo)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 240, 199, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(Echo)
        self.label.setGeometry(QtCore.QRect(30, 60, 91, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Echo)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 91, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Echo)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 71, 20))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Echo)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 71, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Echo)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 71, 20))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Echo)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 71, 20))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(Echo)
        self.line.setGeometry(QtCore.QRect(20, 140, 341, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(Echo)
        self.label_7.setGeometry(QtCore.QRect(40, 120, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(Echo)
        self.line_2.setGeometry(QtCore.QRect(20, 290, 341, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(Echo)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Echo)
        self.label_9.setGeometry(QtCore.QRect(50, 300, 71, 20))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Echo)
        self.label_10.setGeometry(QtCore.QRect(130, 370, 201, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(Echo)
        self.textEdit.setGeometry(QtCore.QRect(130, 300, 221, 71))
        self.textEdit.setObjectName("textEdit")
        self.startButton = QtWidgets.QPushButton(Echo)
        self.startButton.setGeometry(QtCore.QRect(260, 410, 75, 23))
        self.startButton.setObjectName("startButton")
        self.label_11 = QtWidgets.QLabel(Echo)
        self.label_11.setGeometry(QtCore.QRect(110, 20, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Echo)
        QtCore.QMetaObject.connectSlotsByName(Echo)

    def retranslateUi(self, Echo):
        _translate = QtCore.QCoreApplication.translate
        Echo.setWindowTitle(_translate("Echo", "Instaboost"))
        self.label.setText(_translate("Echo", "Login Instagram:"))
        self.label_2.setText(_translate("Echo", "Senha Instagram:"))
        self.label_3.setText(_translate("Echo", "Likes"))
        self.label_4.setText(_translate("Echo", "Comentarios:"))
        self.label_5.setText(_translate("Echo", "Follows:"))
        self.label_6.setText(_translate("Echo", "Unfollows:"))
        self.label_7.setText(_translate("Echo", "Quantidade por dia de:"))
        self.label_8.setText(_translate("Echo", "Tags"))
        self.label_9.setText(_translate("Echo", "Tags:"))
        self.label_10.setText(_translate("Echo", ""))
        self.textEdit.setHtml(_translate("Echo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">#like4like #follow4follow #f4f #instaboost #animal #gopro</span></p></body></html>"))
        self.startButton.setText(_translate("Echo", "Começar"))
        self.lineEdit_3.setText(_translate("Echo", "1500"))
        #self.lineEdit_4.setText(_translate("Echo", "0"))
        self.lineEdit_5.setText(_translate("Echo", "1500"))
        self.lineEdit_6.setText(_translate("Echo", "200"))
        self.lineEdit_4.setPlaceholderText(_translate("Echo", "Em manutenção"))
        self.lineEdit.setPlaceholderText(_translate("Echo", "Usuario do Instagram"))
        self.lineEdit_2.setPlaceholderText(_translate("Echo", "Senha do Instagram"))
        self.label_11.setText(_translate("Echo", "Parametros Instaboost"))


