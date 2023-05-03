# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1160, 800)
        Form.setStyleSheet(u"#Form{border-image: url(:/img/main2.jpg);}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 40, 821, 181))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox_3.setFont(font)
        self.widget_3 = QWidget(self.groupBox_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 20, 66, 58))
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ZhengzhoucheckBox_3 = QCheckBox(self.widget_3)
        self.ZhengzhoucheckBox_3.setObjectName(u"ZhengzhoucheckBox_3")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.ZhengzhoucheckBox_3.setFont(font1)

        self.gridLayout_5.addWidget(self.ZhengzhoucheckBox_3, 0, 0, 1, 1)

        self.Changsha2checkBox_4 = QCheckBox(self.widget_3)
        self.Changsha2checkBox_4.setObjectName(u"Changsha2checkBox_4")
        self.Changsha2checkBox_4.setFont(font1)

        self.gridLayout_5.addWidget(self.Changsha2checkBox_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.widget_4 = QWidget(self.groupBox_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 10, 141, 71))
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SuzhoucheckBox_6 = QCheckBox(self.widget_4)
        self.SuzhoucheckBox_6.setObjectName(u"SuzhoucheckBox_6")
        self.SuzhoucheckBox_6.setFont(font1)

        self.gridLayout_3.addWidget(self.SuzhoucheckBox_6, 0, 0, 1, 1)

        self.HangzhoucheckBox_8 = QCheckBox(self.widget_4)
        self.HangzhoucheckBox_8.setObjectName(u"HangzhoucheckBox_8")
        self.HangzhoucheckBox_8.setFont(font1)

        self.gridLayout_3.addWidget(self.HangzhoucheckBox_8, 0, 1, 1, 1)

        self.JinancheckBox_5 = QCheckBox(self.widget_4)
        self.JinancheckBox_5.setObjectName(u"JinancheckBox_5")
        self.JinancheckBox_5.setFont(font1)

        self.gridLayout_3.addWidget(self.JinancheckBox_5, 1, 0, 1, 1)

        self.ShanghaicheckBox_7 = QCheckBox(self.widget_4)
        self.ShanghaicheckBox_7.setObjectName(u"ShanghaicheckBox_7")
        self.ShanghaicheckBox_7.setFont(font1)

        self.gridLayout_3.addWidget(self.ShanghaicheckBox_7, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.widget_5 = QWidget(self.groupBox_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(9, 19, 151, 61))
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.GuiyangcheckBox_10 = QCheckBox(self.widget_5)
        self.GuiyangcheckBox_10.setObjectName(u"GuiyangcheckBox_10")
        self.GuiyangcheckBox_10.setFont(font1)

        self.gridLayout_4.addWidget(self.GuiyangcheckBox_10, 0, 0, 1, 1)

        self.ChongqingcheckBox_11 = QCheckBox(self.widget_5)
        self.ChongqingcheckBox_11.setObjectName(u"ChongqingcheckBox_11")
        self.ChongqingcheckBox_11.setFont(font1)

        self.gridLayout_4.addWidget(self.ChongqingcheckBox_11, 0, 1, 1, 1)

        self.ChengducheckBox_9 = QCheckBox(self.widget_5)
        self.ChengducheckBox_9.setObjectName(u"ChengducheckBox_9")
        self.ChengducheckBox_9.setFont(font1)

        self.gridLayout_4.addWidget(self.ChengducheckBox_9, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 156, 78))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Beijing1checkBox = QCheckBox(self.widget_2)
        self.Beijing1checkBox.setObjectName(u"Beijing1checkBox")

        self.gridLayout_2.addWidget(self.Beijing1checkBox, 0, 0, 1, 1)

        self.Beijing3checkBox = QCheckBox(self.widget_2)
        self.Beijing3checkBox.setObjectName(u"Beijing3checkBox")
        self.Beijing3checkBox.setFont(font1)

        self.gridLayout_2.addWidget(self.Beijing3checkBox, 0, 1, 1, 1)

        self.HuhehaotecheckBox_2 = QCheckBox(self.widget_2)
        self.HuhehaotecheckBox_2.setObjectName(u"HuhehaotecheckBox_2")
        self.HuhehaotecheckBox_2.setFont(font1)

        self.gridLayout_2.addWidget(self.HuhehaotecheckBox_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)

        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 1, 1)

        self.groupBox_6 = QGroupBox(self.widget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font)
        self.XiancheckBox_13 = QCheckBox(self.groupBox_6)
        self.XiancheckBox_13.setObjectName(u"XiancheckBox_13")
        self.XiancheckBox_13.setGeometry(QRect(19, 22, 87, 25))
        self.XiancheckBox_13.setFont(font1)

        self.gridLayout.addWidget(self.groupBox_6, 1, 2, 1, 1)

        self.verticalWidget = QWidget(Form)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(150, 220, 271, 371))
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.queryVlBtn = QPushButton(self.verticalWidget)
        self.queryVlBtn.setObjectName(u"queryVlBtn")

        self.verticalLayout.addWidget(self.queryVlBtn)

        self.vlbListWidget = QListWidget(self.verticalWidget)
        self.vlbListWidget.setObjectName(u"vlbListWidget")

        self.verticalLayout.addWidget(self.vlbListWidget)

        self.gridWidget = QWidget(Form)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setGeometry(QRect(420, 220, 281, 371))
        self.gridLayout_6 = QGridLayout(self.gridWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.listenerListWidget = QListWidget(self.gridWidget)
        self.listenerListWidget.setObjectName(u"listenerListWidget")

        self.gridLayout_6.addWidget(self.listenerListWidget, 3, 1, 1, 2)

        self.addListenerBtn = QPushButton(self.gridWidget)
        self.addListenerBtn.setObjectName(u"addListenerBtn")

        self.gridLayout_6.addWidget(self.addListenerBtn, 1, 1, 1, 2)

        self.label = QLabel(self.gridWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 2, 1, 1, 1)

        self.gridWidget1 = QWidget(Form)
        self.gridWidget1.setObjectName(u"gridWidget1")
        self.gridWidget1.setGeometry(QRect(700, 220, 271, 371))
        self.gridLayout_7 = QGridLayout(self.gridWidget1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.addVMButton = QPushButton(self.gridWidget1)
        self.addVMButton.setObjectName(u"addVMButton")

        self.gridLayout_7.addWidget(self.addVMButton, 2, 0, 1, 1)

        self.vmlistWidget = QListWidget(self.gridWidget1)
        self.vmlistWidget.setObjectName(u"vmlistWidget")

        self.gridLayout_7.addWidget(self.vmlistWidget, 4, 0, 1, 1)

        self.label_2 = QLabel(self.gridWidget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u534e\u4e2d\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.ZhengzhoucheckBox_3.setText(QCoreApplication.translate("Form", u"\u90d1\u5dde", None))
        self.Changsha2checkBox_4.setText(QCoreApplication.translate("Form", u"\u957f\u6c992", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u534e\u4e1c\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.SuzhoucheckBox_6.setText(QCoreApplication.translate("Form", u"\u82cf\u5dde", None))
        self.HangzhoucheckBox_8.setText(QCoreApplication.translate("Form", u"\u676d\u5dde", None))
        self.JinancheckBox_5.setText(QCoreApplication.translate("Form", u"\u6d4e\u5357", None))
        self.ShanghaicheckBox_7.setText(QCoreApplication.translate("Form", u"\u4e0a\u6d771", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u897f\u5357\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.GuiyangcheckBox_10.setText(QCoreApplication.translate("Form", u"\u8d35\u9633", None))
        self.ChongqingcheckBox_11.setText(QCoreApplication.translate("Form", u"\u91cd\u5e86", None))
        self.ChengducheckBox_9.setText(QCoreApplication.translate("Form", u"\u6210\u90fd", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u534e\u5317\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.Beijing1checkBox.setText(QCoreApplication.translate("Form", u"\u5317\u4eac1", None))
        self.Beijing3checkBox.setText(QCoreApplication.translate("Form", u"\u5317\u4eac3", None))
        self.HuhehaotecheckBox_2.setText(QCoreApplication.translate("Form", u"\u547c\u548c\u6d69\u7279", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u534e\u5357\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u897f\u5317\u5730\u533a\u53ef\u7528\u8282\u70b9", None))
        self.XiancheckBox_13.setText(QCoreApplication.translate("Form", u"\u897f\u5b89", None))
        self.queryVlBtn.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u6240\u9009\u8282\u70b9\u7684\u5f39\u6027\u8d1f\u8f7d\u5747\u8861\u5217\u8868", None))
        self.addListenerBtn.setText(QCoreApplication.translate("Form", u"\u5feb\u6377\u6dfb\u52a0\u76d1\u542c\u5668\u4ee5\u53ca\u540e\u7aef\u670d\u52a1\u5668", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8d1f\u8f7d\u5747\u8861\u6240\u7ed1\u5b9a\u7684\u76d1\u542c\u5668\u4ee5\u53ca\u540e\u7aef\u670d\u52a1\u5668", None))
        self.addVMButton.setText(QCoreApplication.translate("Form", u"\u6279\u91cf\u6dfb\u52a0\u4e1a\u52a1\u4e3b\u673a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u540e\u7aef\u670d\u52a1\u5668\u6240\u7ed1\u5b9a\u7684\u4e1a\u52a1\u4e3b\u673a\u5217\u8868\u4ee5\u53ca\u7aef\u53e3\u6570", None))
    # retranslateUi

