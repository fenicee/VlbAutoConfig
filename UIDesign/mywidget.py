# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mywidget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_myWidget(object):
    # 获取绝对路径


    # 因为styleSheet里正斜杠才管用，我要把反斜杠转化为正斜杠


    def setupUi(self, myWidget):
        url_father = os.path.dirname(os.path.abspath(__file__))
        url = ""
        for i in url_father:
            if (i == "\\"):
                url = url + "/"
            else:
                url = url + i
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(950, 441)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(myWidget.sizePolicy().hasHeightForWidth())
        myWidget.setSizePolicy(sizePolicy)
        myWidget.setAutoFillBackground(False)
        myWidget.setStyleSheet("background-image: url("+url+"/img/background.png);")
        self.username = QLabel(myWidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(508, 80, 81, 31))
        self.username.setMouseTracking(False)
        self.username.setStyleSheet(u"background:transparent;\n"
"font: 75 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.password = QLabel(myWidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(508, 120, 81, 31))
        self.password.setStyleSheet(u"background:transparent;\n"
"font: 75 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.logpushButton = QPushButton(myWidget)
        self.logpushButton.setObjectName(u"logpushButton")
        self.logpushButton.setGeometry(QRect(709, 160, 81, 31))
        self.logpushButton.setStyleSheet(u"background:transparent;\n"
"font: 75 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.logpushButton.setCheckable(True)
        self.logpushButton.setChecked(False)
        self.logpushButton.setAutoDefault(True)
        self.logpushButton.setFlat(True)
        self.resetpushButton = QPushButton(myWidget)
        self.resetpushButton.setObjectName(u"resetpushButton")
        self.resetpushButton.setGeometry(QRect(598, 160, 81, 31))
        self.resetpushButton.setStyleSheet(u"background:transparent;\n"
"font: 75 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.secretKeylineEdit = QLineEdit(myWidget)
        self.secretKeylineEdit.setObjectName(u"secretKeylineEdit")
        self.secretKeylineEdit.setGeometry(QRect(598, 120, 191, 31))
        self.secretKeylineEdit.setStyleSheet(u"background:transparent;")
        self.secretKeylineEdit.setEchoMode(QLineEdit.Password)
        self.accessKeylineEdit = QLineEdit(myWidget)
        self.accessKeylineEdit.setObjectName(u"accessKeylineEdit")
        self.accessKeylineEdit.setGeometry(QRect(598, 80, 191, 31))
        self.accessKeylineEdit.setStyleSheet(u"background:transparent;")
        self.textEdit = QTextEdit(myWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(500, 211, 321, 101))
        self.textEdit.setStyleSheet(u"background:transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)

        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"myWidget", None))
        self.username.setText(QCoreApplication.translate("myWidget", u"Accesskey", None))
        self.password.setText(QCoreApplication.translate("myWidget", u"Secretkey", None))
        self.logpushButton.setText(QCoreApplication.translate("myWidget", u"\u767b\u5f55", None))
        self.resetpushButton.setText(QCoreApplication.translate("myWidget", u"\u91cd\u7f6e", None))
        self.textEdit.setHtml(QCoreApplication.translate("myWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:10pt; font-weight:600;\">Accesskey\u548cSecretkey\u7684\u83b7\u53d6\u65b9\u6cd5\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:10pt; font-weight:72;\">\u767b\u5f55\u79fb\u52a8\u4e91\u5b98\u7f51\uff08https://ecloud.10086.cn),\u641c\u7d22\u201c\u4e91API&quot;\u8fdb\u5165\u63a7\u5236\u53f0\u754c\u9762\uff0c\u70b9"
                        "\u51fb\u201d\u521b\u5efa\u201c\uff0c\u6309\u7167\u63d0\u793a\u4e0b\u8f7d\u8868\u683c\uff0c\u4e0b\u8f7d\u7684\u8868\u683c\u5185\u5373\u662fAccesskey\u548cSecretkey\u3002</span></p></body></html>", None))
    # retranslateUi

