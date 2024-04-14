# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentDialog2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_StudentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(545, 584)
        self.setStyleSheet(u"QDialog{\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid #52452a;\n"
"	border-radius: 8px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"	border: 1px solid #67708f;\n"
"	border-radius: 5px;\n"
"	padding-left: 15px;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 1px solid #67708f;\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: #52452a;\n"
"	color: #ffffff; \n"
"	height: 30px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	/*selection-background-color: #0192ef;*/\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	selection-background-color: #0192ef;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(14, 13, 106);\n"
"}")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 241, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 450, 441, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.uploadPhoto_Button = QPushButton(self.widget)
        self.uploadPhoto_Button.setObjectName(u"uploadPhoto_Button")
        self.uploadPhoto_Button.setMinimumSize(QSize(0, 30))
        self.uploadPhoto_Button.setMaximumSize(QSize(16777215, 30))
        self.uploadPhoto_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(1, 146, 239);\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.uploadPhoto_Button)

        self.takePhoto_Button = QPushButton(self.widget)
        self.takePhoto_Button.setObjectName(u"takePhoto_Button")
        self.takePhoto_Button.setMinimumSize(QSize(0, 30))
        self.takePhoto_Button.setMaximumSize(QSize(16777215, 30))
        self.takePhoto_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(1, 146, 239);\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.takePhoto_Button)

        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 551, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 70, 511, 371))
        self.verticalLayout_9 = QVBoxLayout(self.widget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.widget1)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.name_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.widget1)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setMinimumSize(QSize(0, 30))
        self.gender_comboBox.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_7)

        self.class_comboBox = QComboBox(self.widget1)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setMinimumSize(QSize(0, 30))
        self.class_comboBox.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_6.addWidget(self.class_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.widget1)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")
        self.dob_dateEdit.setMinimumSize(QSize(0, 30))
        self.dob_dateEdit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_9)

        self.admission_dateEdit = QDateEdit(self.widget1)
        self.admission_dateEdit.setObjectName(u"admission_dateEdit")
        self.admission_dateEdit.setMinimumSize(QSize(0, 30))
        self.admission_dateEdit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_8.addWidget(self.admission_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_5)

        self.address_lineEdit = QLineEdit(self.widget1)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(0, 35))
        self.address_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.address_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.phone_lineEdit = QLineEdit(self.widget1)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 35))
        self.phone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.phone_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.email_lineEdit = QLineEdit(self.widget1)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.email_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.widget2 = QWidget(self)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(320, 520, 211, 37))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_Button = QPushButton(self.widget2)
        self.saveStudent_Button.setObjectName(u"saveStudent_Button")
        self.saveStudent_Button.setMinimumSize(QSize(0, 35))
        self.saveStudent_Button.setMaximumSize(QSize(16777215, 35))
        self.saveStudent_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: #fec701;\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.saveStudent_Button)

        self.cancel_Button = QPushButton(self.widget2)
        self.cancel_Button.setObjectName(u"cancel_Button")
        self.cancel_Button.setMinimumSize(QSize(0, 35))
        self.cancel_Button.setMaximumSize(QSize(16777215, 35))
        self.cancel_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: #bbbbbc;\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cancel_Button)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Students Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"Add New Student", None))
        self.uploadPhoto_Button.setText(QCoreApplication.translate("StudentsDialog", u"Upload Photo", None))
        self.takePhoto_Button.setText(QCoreApplication.translate("StudentsDialog", u"Take Photo", None))
        self.label_2.setText(QCoreApplication.translate("StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("StudentsDialog", u"Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("StudentsDialog", u"Class", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Kindergarten (KG) 1", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Kindergarten (KG) 2", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StudentsDialog", u"Grade 1", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StudentsDialog", u"Grade 2", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StudentsDialog", u"Grade 3", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StudentsDialog", u"Grade 4", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StudentsDialog", u"Grade 5", None))
        self.class_comboBox.setItemText(7, QCoreApplication.translate("StudentsDialog", u"Grade 6", None))
        self.class_comboBox.setItemText(8, QCoreApplication.translate("StudentsDialog", u"Grade 7", None))
        self.class_comboBox.setItemText(9, QCoreApplication.translate("StudentsDialog", u"Grade 8", None))
        self.class_comboBox.setItemText(10, QCoreApplication.translate("StudentsDialog", u"Grade 9", None))
        self.class_comboBox.setItemText(11, QCoreApplication.translate("StudentsDialog", u"Grade 10", None))
        self.class_comboBox.setItemText(12, QCoreApplication.translate("StudentsDialog", u"Grade 11", None))
        self.class_comboBox.setItemText(13, QCoreApplication.translate("StudentsDialog", u"Grade 12", None))

        self.label_8.setText(QCoreApplication.translate("StudentsDialog", u"Date Of Birth", None))
        self.label_9.setText(QCoreApplication.translate("StudentsDialog", u"Admission Date", None))
        self.label_5.setText(QCoreApplication.translate("StudentsDialog", u"Address", None))
        self.label_3.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number", None))
        self.label_4.setText(QCoreApplication.translate("StudentsDialog", u"Email ", None))
        self.saveStudent_Button.setText(QCoreApplication.translate("StudentsDialog", u"Add Student", None))
        self.cancel_Button.setText(QCoreApplication.translate("StudentsDialog", u"Cancel", None))
    # retranslateUi

