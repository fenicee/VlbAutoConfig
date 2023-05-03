/********************************************************************************
** Form generated from reading UI file 'mywidget.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MYWIDGET_H
#define UI_MYWIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_myWidget
{
public:
    QLabel *username;
    QLabel *password;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QTextEdit *textEdit;

    void setupUi(QWidget *myWidget)
    {
        if (myWidget->objectName().isEmpty())
            myWidget->setObjectName(QString::fromUtf8("myWidget"));
        myWidget->resize(945, 443);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(myWidget->sizePolicy().hasHeightForWidth());
        myWidget->setSizePolicy(sizePolicy);
        myWidget->setStyleSheet(QString::fromUtf8("background-image: url(:/img/background.png);"));
        username = new QLabel(myWidget);
        username->setObjectName(QString::fromUtf8("username"));
        username->setGeometry(QRect(508, 80, 81, 31));
        username->setMouseTracking(false);
        username->setStyleSheet(QString::fromUtf8("background:transparent;\n"
"font: 75 12pt \"\345\276\256\350\275\257\351\233\205\351\273\221\";"));
        password = new QLabel(myWidget);
        password->setObjectName(QString::fromUtf8("password"));
        password->setGeometry(QRect(508, 120, 81, 31));
        password->setStyleSheet(QString::fromUtf8("background:transparent;\n"
"font: 75 12pt \"\345\276\256\350\275\257\351\233\205\351\273\221\";"));
        pushButton = new QPushButton(myWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(709, 160, 81, 31));
        pushButton->setStyleSheet(QString::fromUtf8("background:transparent;\n"
"font: 75 12pt \"\345\276\256\350\275\257\351\233\205\351\273\221\";"));
        pushButton_2 = new QPushButton(myWidget);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(598, 160, 81, 31));
        pushButton_2->setStyleSheet(QString::fromUtf8("background:transparent;\n"
"font: 75 12pt \"\345\276\256\350\275\257\351\233\205\351\273\221\";"));
        lineEdit = new QLineEdit(myWidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(598, 120, 191, 31));
        lineEdit->setStyleSheet(QString::fromUtf8("background:transparent;"));
        lineEdit->setEchoMode(QLineEdit::Password);
        lineEdit_2 = new QLineEdit(myWidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(598, 80, 191, 31));
        lineEdit_2->setStyleSheet(QString::fromUtf8("background:transparent;"));
        textEdit = new QTextEdit(myWidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setGeometry(QRect(528, 210, 281, 111));
        textEdit->setStyleSheet(QString::fromUtf8("background:transparent;"));
        textEdit->setFrameShape(QFrame::NoFrame);

        retranslateUi(myWidget);

        QMetaObject::connectSlotsByName(myWidget);
    } // setupUi

    void retranslateUi(QWidget *myWidget)
    {
        myWidget->setWindowTitle(QCoreApplication::translate("myWidget", "myWidget", nullptr));
        username->setText(QCoreApplication::translate("myWidget", "Accesskey", nullptr));
        password->setText(QCoreApplication::translate("myWidget", "Secretkey", nullptr));
        pushButton->setText(QCoreApplication::translate("myWidget", "\347\231\273\345\275\225", nullptr));
        pushButton_2->setText(QCoreApplication::translate("myWidget", "\351\207\215\347\275\256", nullptr));
        textEdit->setHtml(QCoreApplication::translate("myWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\345\276\256\350\275\257\351\233\205\351\273\221'; font-size:10pt; font-weight:600;\">Accesskey\345\222\214Secretkey\347\232\204\350\216\267\345\217\226\346\226\271\346\263\225\357\274\232</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\345\276\256\350\275\257\351\233\205\351\273\221'; font-size:10pt; font-weight:72;\">\347\231\273\345\275\225\347\247\273\345\212\250\344\272\221\345\256\230\347\275\221\357\274\210https://e"
                        "cloud.10086.cn),\346\220\234\347\264\242\342\200\234\344\272\221API&quot;\350\277\233\345\205\245\346\216\247\345\210\266\345\217\260\347\225\214\351\235\242\357\274\214\347\202\271\345\207\273\342\200\235\345\210\233\345\273\272\342\200\234\357\274\214\346\214\211\347\205\247\346\217\220\347\244\272\344\270\213\350\275\275\350\241\250\346\240\274\357\274\214\344\270\213\350\275\275\347\232\204\350\241\250\346\240\274\345\206\205\345\215\263\346\230\257Accesskey\345\222\214Secretkey\343\200\202</span></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class myWidget: public Ui_myWidget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MYWIDGET_H
