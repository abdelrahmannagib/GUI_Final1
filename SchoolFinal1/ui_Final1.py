# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexLatest.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1358, 921)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(14, 6, 1291, 822))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.widget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(14, 13, 106);\n"
"}\n"
"QPushButton{\n"
"	border: none;\n"
"	height: 30px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/Icons/school (6).png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 30, -1, -1)
        self.home_1 = QPushButton(self.icon_only_widget)
        self.home_1.setObjectName(u"home_1")
        icon = QIcon()
        icon.addFile(u":/Icons/home (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Icons/home (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.home_1.setIcon(icon)
        self.home_1.setIconSize(QSize(20, 16))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.home_1)

        self.students_1 = QPushButton(self.icon_only_widget)
        self.students_1.setObjectName(u"students_1")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/education (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/Icons/education (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.students_1.setIcon(icon1)
        self.students_1.setIconSize(QSize(20, 20))
        self.students_1.setCheckable(True)
        self.students_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.students_1)

        self.classMonitoring_1 = QPushButton(self.icon_only_widget)
        self.classMonitoring_1.setObjectName(u"classMonitoring_1")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/classroom (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/Icons/classroom (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.classMonitoring_1.setIcon(icon2)
        self.classMonitoring_1.setIconSize(QSize(20, 20))
        self.classMonitoring_1.setCheckable(True)
        self.classMonitoring_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.classMonitoring_1)

        self.attendance_1 = QPushButton(self.icon_only_widget)
        self.attendance_1.setObjectName(u"attendance_1")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/calendar (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/Icons/calendar (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.attendance_1.setIcon(icon3)
        self.attendance_1.setIconSize(QSize(18, 18))
        self.attendance_1.setCheckable(True)
        self.attendance_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.attendance_1)

        self.reports_1 = QPushButton(self.icon_only_widget)
        self.reports_1.setObjectName(u"reports_1")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/report (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/Icons/report (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.reports_1.setIcon(icon4)
        self.reports_1.setIconSize(QSize(20, 20))
        self.reports_1.setCheckable(True)
        self.reports_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.reports_1)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 463, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 2, 1)

        self.icon_text_widget = QWidget(self.widget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(0, 820))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(14, 13, 106);\n"
"	color: #bbbbbc;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border: none;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/Icons/school (6).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.home_2 = QPushButton(self.icon_text_widget)
        self.home_2.setObjectName(u"home_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.home_2.setFont(font1)
        self.home_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -70px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"	/*font-color: #fec701;*/\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/home (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/Icons/home (3).png", QSize(), QIcon.Normal, QIcon.On)
        icon5.addFile(u":/Icons/home (3).png", QSize(), QIcon.Active, QIcon.On)
        self.home_2.setIcon(icon5)
        self.home_2.setIconSize(QSize(16, 16))
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.home_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.students)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.students_2 = QPushButton(self.students)
        self.students_2.setObjectName(u"students_2")
        self.students_2.setMinimumSize(QSize(0, 0))
        self.students_2.setFont(font1)
        self.students_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -40px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Frame 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.students_2.setIcon(icon6)
        self.students_2.setIconSize(QSize(100, 100))
        self.students_2.setCheckable(True)
        self.students_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.students_2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students_dropdown)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.student_information = QPushButton(self.students_dropdown)
        self.student_information.setObjectName(u"student_information")
        self.student_information.setStyleSheet(u"QPushButton{\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fec701;\n"
"}")
        self.student_information.setCheckable(True)
        self.student_information.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.student_information)

        self.student_payments = QPushButton(self.students_dropdown)
        self.student_payments.setObjectName(u"student_payments")
        self.student_payments.setStyleSheet(u"QPushButton{\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fec701;\n"
"}")
        self.student_payments.setCheckable(True)
        self.student_payments.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.student_payments)

        self.student_transactions = QPushButton(self.students_dropdown)
        self.student_transactions.setObjectName(u"student_transactions")
        self.student_transactions.setStyleSheet(u"QPushButton{\n"
"	padding-left: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fec701;\n"
"}")
        self.student_transactions.setCheckable(True)
        self.student_transactions.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.student_transactions)


        self.verticalLayout_2.addWidget(self.students_dropdown)


        self.verticalLayout_3.addWidget(self.students)

        self.classMonitoring_2 = QPushButton(self.icon_text_widget)
        self.classMonitoring_2.setObjectName(u"classMonitoring_2")
        self.classMonitoring_2.setFont(font1)
        self.classMonitoring_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"}")
        self.classMonitoring_2.setIcon(icon2)
        self.classMonitoring_2.setIconSize(QSize(20, 20))
        self.classMonitoring_2.setCheckable(True)
        self.classMonitoring_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.classMonitoring_2)

        self.attendance_2 = QPushButton(self.icon_text_widget)
        self.attendance_2.setObjectName(u"attendance_2")
        self.attendance_2.setFont(font1)
        self.attendance_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -40px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"}")
        self.attendance_2.setIcon(icon3)
        self.attendance_2.setIconSize(QSize(18, 18))
        self.attendance_2.setCheckable(True)
        self.attendance_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.attendance_2)

        self.reports_2 = QPushButton(self.icon_text_widget)
        self.reports_2.setObjectName(u"reports_2")
        self.reports_2.setFont(font1)
        self.reports_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -60px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"}")
        self.reports_2.setIcon(icon4)
        self.reports_2.setIconSize(QSize(20, 20))
        self.reports_2.setCheckable(True)
        self.reports_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.reports_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 379, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 2, 1)

        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(841, 0))
        self.header_widget.setStyleSheet(u"background-color: rgb(14, 13, 106);")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/burger-bar (3).png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/Icons/burger-bar (6).png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(386, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left:15px;\n"
"	border: 1px solid #bbbbbc;\n"
"	border-radius: 15px;\n"
"	color: #ffffff;\n"
"	/*background-color: rgb(187, 187, 188);*/\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.header_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"/*border:  1px solid #bbbbbc;*/\n"
"/*background-color: rgb(187, 187, 188);*/")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/magnifying-glass (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon8)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.header_widget, 0, 2, 1, 1)

        self.main_sceen_widget = QWidget(self.widget)
        self.main_sceen_widget.setObjectName(u"main_sceen_widget")
        self.main_sceen_widget.setMinimumSize(QSize(841, 741))
        self.main_sceen_widget.setMaximumSize(QSize(16777215, 741))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif Collection"])
        self.main_sceen_widget.setFont(font2)
        self.main_sceen_widget.setStyleSheet(u"background-color: #ffffff;")
        self.stackedWidget = QStackedWidget(self.main_sceen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 991, 721))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 190, 171, 51))
        font3 = QFont()
        font3.setPointSize(25)
        self.label.setFont(font3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 190, 211, 51))
        self.label_5.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 311, 51))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.studentInfo_table = QTableWidget(self.page_4)
        if (self.studentInfo_table.columnCount() < 10):
            self.studentInfo_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.studentInfo_table.setObjectName(u"studentInfo_table")
        self.studentInfo_table.setGeometry(QRect(-10, 120, 1001, 511))
        self.studentInfo_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #0e0d6a;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #b0edfb;\n"
"	background-color: #ececec;\n"
"}")
        self.studentInfo_table.setAlternatingRowColors(True)
        self.widget1 = QWidget(self.page_4)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(2, 80, 791, 37))
        self.horizontalLayout_5 = QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addStudent_button = QPushButton(self.widget1)
        self.addStudent_button.setObjectName(u"addStudent_button")
        self.addStudent_button.setMinimumSize(QSize(0, 35))
        self.addStudent_button.setMaximumSize(QSize(16777215, 35))
        self.addStudent_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #af8501;\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/add-friend2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addStudent_button.setIcon(icon9)
        self.addStudent_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.addStudent_button)

        self.select_gender = QComboBox(self.widget1)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 35))
        self.select_gender.setMaximumSize(QSize(16777215, 35))
        self.select_gender.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #af8501;\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: #af8501;\n"
"	color: #ffffff; \n"
"	height: 30px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"	/*selection-background-color: #0192ef;*/\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	selection-background-color: #0192ef;\n"
"}")

        self.horizontalLayout_5.addWidget(self.select_gender)

        self.select_class = QComboBox(self.widget1)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(0, 35))
        self.select_class.setMaximumSize(QSize(16777215, 35))
        self.select_class.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #af8501;\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: #af8501;\n"
"	color: #ffffff; \n"
"	height: 30px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	selection-background-color: #0192ef;\n"
"}")

        self.horizontalLayout_5.addWidget(self.select_class)

        self.search_student = QLineEdit(self.widget1)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMinimumSize(QSize(150, 35))
        self.search_student.setMaximumSize(QSize(16777215, 35))
        self.search_student.setStyleSheet(u"QLineEdit{\n"
"	padding-left:15px;\n"
"	border: 1px solid #0e0d6a;\n"
"	border-radius: 15px;\n"
"	/*background-color: rgb(187, 187, 188);*/\n"
"}")

        self.horizontalLayout_5.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 180, 371, 51))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 180, 401, 51))
        self.label_9.setFont(font3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_10 = QLabel(self.page_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(190, 180, 331, 51))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_11 = QLabel(self.page_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 190, 251, 51))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_12 = QLabel(self.page_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 200, 201, 51))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_9)

        self.gridLayout.addWidget(self.main_sceen_widget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.students_2.toggled.connect(self.students_dropdown.setHidden)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.students_2.toggled.connect(self.students_1.setChecked)
        self.classMonitoring_2.toggled.connect(self.classMonitoring_1.setChecked)
        self.attendance_2.toggled.connect(self.attendance_1.setChecked)
        self.reports_2.toggled.connect(self.reports_1.setChecked)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.home_1.setText("")
        self.students_1.setText("")
        self.classMonitoring_1.setText("")
        self.attendance_1.setText("")
        self.reports_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Smart School", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.students_2.setText("")
        self.student_information.setText(QCoreApplication.translate("MainWindow", u"Students Information", None))
        self.student_payments.setText(QCoreApplication.translate("MainWindow", u"Students Payments", None))
        self.student_transactions.setText(QCoreApplication.translate("MainWindow", u"Students Transactions", None))
        self.classMonitoring_2.setText(QCoreApplication.translate("MainWindow", u"  Class Monitoring", None))
        self.attendance_2.setText(QCoreApplication.translate("MainWindow", u"  Attendance", None))
        self.reports_2.setText(QCoreApplication.translate("MainWindow", u"  Reports", None))
        self.pushButton.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here...", None))
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Students Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Students Information", None))
        ___qtablewidgetitem = self.studentInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.studentInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem2 = self.studentInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.studentInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.studentInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None));
        ___qtablewidgetitem5 = self.studentInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem6 = self.studentInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem7 = self.studentInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem8 = self.studentInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem9 = self.studentInfo_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.addStudent_button.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Kindergarten (KG) 1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Kindergarten (KG) 2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.select_class.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.select_class.setItemText(9, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.select_class.setItemText(10, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.select_class.setItemText(11, QCoreApplication.translate("MainWindow", u"Grade 9", None))
        self.select_class.setItemText(12, QCoreApplication.translate("MainWindow", u"Grade 10", None))
        self.select_class.setItemText(13, QCoreApplication.translate("MainWindow", u"Grade 11", None))
        self.select_class.setItemText(14, QCoreApplication.translate("MainWindow", u"Grade 12", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Students...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Students Payments Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Students Transactions Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Class Monitoring Page", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Attendance Page", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reports Page", None))
    # retranslateUi

