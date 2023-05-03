/********************************************************************************
** Form generated from reading UI file 'main.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAIN_H
#define UI_MAIN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout;
    QFrame *frame_2;
    QWidget *layoutWidget1;
    QGridLayout *gridLayout;
    QGroupBox *groupBox;
    QWidget *layoutWidget_2;
    QGridLayout *gridLayout_2;
    QCheckBox *checkBox_2;
    QCheckBox *checkBox;
    QGroupBox *groupBox_3;
    QWidget *layoutWidget_3;
    QGridLayout *gridLayout_5;
    QCheckBox *checkBox_3;
    QCheckBox *checkBox_4;
    QGroupBox *groupBox_2;
    QWidget *layoutWidget_4;
    QGridLayout *gridLayout_3;
    QCheckBox *checkBox_6;
    QCheckBox *checkBox_8;
    QCheckBox *checkBox_5;
    QCheckBox *checkBox_7;
    QGroupBox *groupBox_6;
    QCheckBox *checkBox_13;
    QGroupBox *groupBox_5;
    QCheckBox *checkBox_12;
    QGroupBox *groupBox_4;
    QWidget *layoutWidget_5;
    QGridLayout *gridLayout_4;
    QCheckBox *checkBox_10;
    QCheckBox *checkBox_11;
    QCheckBox *checkBox_9;
    QWidget *layoutWidget2;
    QVBoxLayout *verticalLayout;
    QFrame *frame;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(1050, 680);
        Form->setStyleSheet(QString::fromUtf8(""));
        layoutWidget = new QWidget(Form);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(0, 0, 991, 611));
        horizontalLayout = new QHBoxLayout(layoutWidget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        frame_2 = new QFrame(layoutWidget);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(5);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
        frame_2->setSizePolicy(sizePolicy);
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        layoutWidget1 = new QWidget(frame_2);
        layoutWidget1->setObjectName(QString::fromUtf8("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(30, 330, 701, 221));
        gridLayout = new QGridLayout(layoutWidget1);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        groupBox = new QGroupBox(layoutWidget1);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        QFont font;
        font.setFamily(QString::fromUtf8("\345\276\256\350\275\257\351\233\205\351\273\221"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        groupBox->setFont(font);
        layoutWidget_2 = new QWidget(groupBox);
        layoutWidget_2->setObjectName(QString::fromUtf8("layoutWidget_2"));
        layoutWidget_2->setGeometry(QRect(10, 30, 101, 61));
        gridLayout_2 = new QGridLayout(layoutWidget_2);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        checkBox_2 = new QCheckBox(layoutWidget_2);
        checkBox_2->setObjectName(QString::fromUtf8("checkBox_2"));
        QFont font1;
        font1.setFamily(QString::fromUtf8("\345\276\256\350\275\257\351\233\205\351\273\221"));
        font1.setPointSize(12);
        font1.setBold(false);
        font1.setWeight(50);
        checkBox_2->setFont(font1);

        gridLayout_2->addWidget(checkBox_2, 1, 0, 1, 1);

        checkBox = new QCheckBox(layoutWidget_2);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));
        checkBox->setFont(font1);

        gridLayout_2->addWidget(checkBox, 0, 0, 1, 1);


        gridLayout->addWidget(groupBox, 0, 0, 1, 1);

        groupBox_3 = new QGroupBox(layoutWidget1);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        groupBox_3->setFont(font);
        layoutWidget_3 = new QWidget(groupBox_3);
        layoutWidget_3->setObjectName(QString::fromUtf8("layoutWidget_3"));
        layoutWidget_3->setGeometry(QRect(10, 30, 81, 61));
        gridLayout_5 = new QGridLayout(layoutWidget_3);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        gridLayout_5->setContentsMargins(0, 0, 0, 0);
        checkBox_3 = new QCheckBox(layoutWidget_3);
        checkBox_3->setObjectName(QString::fromUtf8("checkBox_3"));
        checkBox_3->setFont(font1);

        gridLayout_5->addWidget(checkBox_3, 0, 0, 1, 1);

        checkBox_4 = new QCheckBox(layoutWidget_3);
        checkBox_4->setObjectName(QString::fromUtf8("checkBox_4"));
        checkBox_4->setFont(font1);

        gridLayout_5->addWidget(checkBox_4, 1, 0, 1, 1);


        gridLayout->addWidget(groupBox_3, 0, 1, 1, 1);

        groupBox_2 = new QGroupBox(layoutWidget1);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        groupBox_2->setFont(font);
        layoutWidget_4 = new QWidget(groupBox_2);
        layoutWidget_4->setObjectName(QString::fromUtf8("layoutWidget_4"));
        layoutWidget_4->setGeometry(QRect(10, 30, 141, 71));
        gridLayout_3 = new QGridLayout(layoutWidget_4);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        checkBox_6 = new QCheckBox(layoutWidget_4);
        checkBox_6->setObjectName(QString::fromUtf8("checkBox_6"));
        checkBox_6->setFont(font1);

        gridLayout_3->addWidget(checkBox_6, 0, 0, 1, 1);

        checkBox_8 = new QCheckBox(layoutWidget_4);
        checkBox_8->setObjectName(QString::fromUtf8("checkBox_8"));
        checkBox_8->setFont(font1);

        gridLayout_3->addWidget(checkBox_8, 0, 1, 1, 1);

        checkBox_5 = new QCheckBox(layoutWidget_4);
        checkBox_5->setObjectName(QString::fromUtf8("checkBox_5"));
        checkBox_5->setFont(font1);

        gridLayout_3->addWidget(checkBox_5, 1, 0, 1, 1);

        checkBox_7 = new QCheckBox(layoutWidget_4);
        checkBox_7->setObjectName(QString::fromUtf8("checkBox_7"));
        checkBox_7->setFont(font1);

        gridLayout_3->addWidget(checkBox_7, 1, 1, 1, 1);


        gridLayout->addWidget(groupBox_2, 1, 0, 1, 1);

        groupBox_6 = new QGroupBox(layoutWidget1);
        groupBox_6->setObjectName(QString::fromUtf8("groupBox_6"));
        groupBox_6->setFont(font);
        checkBox_13 = new QCheckBox(groupBox_6);
        checkBox_13->setObjectName(QString::fromUtf8("checkBox_13"));
        checkBox_13->setGeometry(QRect(20, 40, 87, 25));
        checkBox_13->setFont(font1);

        gridLayout->addWidget(groupBox_6, 1, 2, 1, 1);

        groupBox_5 = new QGroupBox(layoutWidget1);
        groupBox_5->setObjectName(QString::fromUtf8("groupBox_5"));
        groupBox_5->setFont(font);
        checkBox_12 = new QCheckBox(groupBox_5);
        checkBox_12->setObjectName(QString::fromUtf8("checkBox_12"));
        checkBox_12->setGeometry(QRect(20, 40, 87, 25));
        checkBox_12->setFont(font1);

        gridLayout->addWidget(groupBox_5, 0, 2, 1, 1);

        groupBox_4 = new QGroupBox(layoutWidget1);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        groupBox_4->setFont(font);
        layoutWidget_5 = new QWidget(groupBox_4);
        layoutWidget_5->setObjectName(QString::fromUtf8("layoutWidget_5"));
        layoutWidget_5->setGeometry(QRect(11, 32, 151, 61));
        gridLayout_4 = new QGridLayout(layoutWidget_5);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        gridLayout_4->setContentsMargins(0, 0, 0, 0);
        checkBox_10 = new QCheckBox(layoutWidget_5);
        checkBox_10->setObjectName(QString::fromUtf8("checkBox_10"));
        checkBox_10->setFont(font1);

        gridLayout_4->addWidget(checkBox_10, 0, 0, 1, 1);

        checkBox_11 = new QCheckBox(layoutWidget_5);
        checkBox_11->setObjectName(QString::fromUtf8("checkBox_11"));
        checkBox_11->setFont(font1);

        gridLayout_4->addWidget(checkBox_11, 0, 1, 1, 1);

        checkBox_9 = new QCheckBox(layoutWidget_5);
        checkBox_9->setObjectName(QString::fromUtf8("checkBox_9"));
        checkBox_9->setFont(font1);

        gridLayout_4->addWidget(checkBox_9, 1, 0, 1, 1);


        gridLayout->addWidget(groupBox_4, 1, 1, 1, 1);

        layoutWidget2 = new QWidget(frame_2);
        layoutWidget2->setObjectName(QString::fromUtf8("layoutWidget2"));
        layoutWidget2->setGeometry(QRect(20, 0, 941, 321));
        verticalLayout = new QVBoxLayout(layoutWidget2);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        frame = new QFrame(layoutWidget2);
        frame->setObjectName(QString::fromUtf8("frame"));
        QSizePolicy sizePolicy1(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy1.setHorizontalStretch(1);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy1);
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        pushButton = new QPushButton(frame);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(0, 0, 131, 51));

        verticalLayout->addWidget(frame);


        horizontalLayout->addWidget(frame_2);

        pushButton_2 = new QPushButton(Form);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(20, 620, 131, 51));
        pushButton_3 = new QPushButton(Form);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setGeometry(QRect(280, 620, 131, 51));

        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        groupBox->setTitle(QCoreApplication::translate("Form", "\345\215\216\345\214\227\345\234\260\345\214\272\345\217\257\347\224\250\350\212\202\347\202\271", nullptr));
        checkBox_2->setText(QCoreApplication::translate("Form", "\345\221\274\345\222\214\346\265\251\347\211\271", nullptr));
        checkBox->setText(QCoreApplication::translate("Form", "\345\214\227\344\272\2543", nullptr));
        groupBox_3->setTitle(QCoreApplication::translate("Form", "\345\215\216\344\270\255\345\234\260\345\214\272\345\217\257\347\224\250\350\212\202\347\202\271", nullptr));
        checkBox_3->setText(QCoreApplication::translate("Form", "\351\203\221\345\267\236", nullptr));
        checkBox_4->setText(QCoreApplication::translate("Form", "\351\225\277\346\262\2312", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("Form", "\345\215\216\344\270\234\345\234\260\345\214\272\345\217\257\347\224\250\350\212\202\347\202\271", nullptr));
        checkBox_6->setText(QCoreApplication::translate("Form", "\350\213\217\345\267\236", nullptr));
        checkBox_8->setText(QCoreApplication::translate("Form", "\346\235\255\345\267\236", nullptr));
        checkBox_5->setText(QCoreApplication::translate("Form", "\346\265\216\345\215\227", nullptr));
        checkBox_7->setText(QCoreApplication::translate("Form", "\344\270\212\346\265\267", nullptr));
        groupBox_6->setTitle(QCoreApplication::translate("Form", "\350\245\277\345\214\227\345\234\260\345\214\272\345\217\257\347\224\250\350\212\202\347\202\271", nullptr));
        checkBox_13->setText(QCoreApplication::translate("Form", "\350\245\277\345\256\211", nullptr));
        groupBox_5->setTitle(QCoreApplication::translate("Form", "\345\215\216\345\215\227\345\234\260\345\214\272\345\217\257\347\224\250\350\212\202\347\202\271", nullptr));
        checkBox_12->setText(QCoreApplication::translate("Form", "\345\271\277\345\267\2363", nullptr));
        groupBox_4->setTitle(QCoreApplication::translate("Form", "\350\245\277\345\215\227\345\234\260\345\214\272\345\217\257\347\224\250\350\212\202\347\202\271", nullptr));
        checkBox_10->setText(QCoreApplication::translate("Form", "\350\264\265\351\230\263", nullptr));
        checkBox_11->setText(QCoreApplication::translate("Form", "\351\207\215\345\272\206", nullptr));
        checkBox_9->setText(QCoreApplication::translate("Form", "\346\210\220\351\203\275", nullptr));
        pushButton->setText(QCoreApplication::translate("Form", "\344\270\200\343\200\201\351\200\211\346\213\251\350\212\202\347\202\271", nullptr));
        pushButton_2->setText(QCoreApplication::translate("Form", "\344\272\214\343\200\201\350\256\242\350\264\255", nullptr));
        pushButton_3->setText(QCoreApplication::translate("Form", "\344\270\211\343\200\201\350\256\242\350\264\255\344\277\241\346\201\257\346\237\245\350\257\242", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAIN_H
