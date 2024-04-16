import cv2
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication,  QMenu, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, \
    QTableWidgetItem, QRadioButton, QCheckBox, QLabel, QHeaderView, QSizePolicy
# from PyQt6  QApplication,  QMenu, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, \
#     QTableWidgetItem, QRadioButton
from ui_Final2 import Ui_MainWindow
from ViolenceRealTime import *
from ViolenceRealTime import DetectYacta
from PySide6.QtCore import Qt

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Smart School Management System")


        self.icon_text_widget.setHidden(True)

        # connect buttons to switch different pages
        self.home_1.clicked.connect(self.switch_to_home)
        self.home_2.clicked.connect(self.switch_to_home)

        self.students_1.clicked.connect(self.switch_to_students)
        self.students_2.clicked.connect(self.switch_to_students)

        self.classMonitoring_1.clicked.connect(self.switch_to_classMonitoring)
        self.classMonitoring_2.clicked.connect(self.switch_to_classMonitoring)

        self.attendance_1.clicked.connect(self.switch_to_attendance)
        self.attendance_2.clicked.connect(self.switch_to_attendance)

        self.reports_1.clicked.connect(self.switch_to_reports)
        self.reports_2.clicked.connect(self.switch_to_reports)
        # self.reports_2.clicked.connect(self.change_text)


        # # connect buttons to respective context menus
        # self.students_1.clicked.connect(self.students_context_menu)

        #open student dialog
        self.addStudent_button.clicked.connect(self.open_addStudent_dialog)

        #connect class monitoring button to its method
        # self.classMonitoring_1.clicked.connect(self.switch_to_classMonitoring)
        # # self.classMonitoring_2.clicked.connect(self.prepare_for_monitoring)
        # self.classMonitoring_2.clicked.connect(self.switch_to_classMonitoring)

        # #display video button in reports page
        # self.layout = QVBoxLayout()
        # self.setLayout(self.layout)
        #
        # self.display_video_btn = QPushButton('&Display Video')
        # self.layout.addWidget(self.display_video_btn)
        #
        # self.violence_reports_table = QTableWidget(3, 3)
        # self.violence_reports_table.setStyleSheet("QAbstractItemView::inicator {width: 25px; height: 25px;}"
        #                                           "QTableWidget:: item {width: 500px; height: 40px;}")
        #
        # self.layout.addWidget(self.violence_reports_table)
        #
        # for row in range (3):
        #     for col in range(3):
        #         if col % 3 == 0:
        #             item = QTableWidgetItem('Item {0}-{1}'.format(row, col))
        #             item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        #             item.setCheckState(Qt.CheckState.Unchecked)
        #             self.violence_reports_table.setItem(row, col, item)
        #         else:
        #             self.table.setItem(row, col, QTableWidgetItem('Item {0}-{1}'.format(row, col)))
        #


        #set the default page to home
        self.switch_to_home()

    # def prepare_for_monitoring(self):
    #     # You can add any preparation steps here before starting the monitoring
    #     self.switch_to_classMonitoring()
    #     # Start the monitoring in a separate thread
    #     self.video_thread = VideoThread()
    #     self.video_thread.start()

    # def change_text(self):
    #     self.reports_2.setText("Reports >")

    # methods to switch different pages
    def switch_to_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_students(self):
        self.stackedWidget.setCurrentIndex(1)


    def switch_to_classMonitoring(self):
        DetectYacta()
        self.stackedWidget.setCurrentIndex(2)


    def switch_to_attendance(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_reports(self):
        self.stackedWidget.setCurrentIndex(4)
        # self.create_reports_page()
        # self.violence_reoprts_table

    # def create_reports_page(self):
    #     # Create the layout for the reports page
    #     reports_page_layout = QVBoxLayout()
    #
    #     # Page label
    #     violence_reports_label = QLabel("Violence Reports")
    #     violence_reports_label.setStyleSheet("font-size: 25px; color: #0e0d6a; font-weight: bold; padding-bottom: 30px;")
    #     reports_page_layout.addWidget(violence_reports_label)
    #
    #     # Create the display video button and add it to the layout
    #     display_video_btn = QPushButton('Display Video')
    #     display_video_btn.setStyleSheet("background-color: #af8501; color: #ffffff; border-radius: 5px; border: none; "
    #                                     "font-weight: bold; font-size: 12px; padding-left: 10px; padding-right: 10px;"
    #                                     "width: 120px; height: 35px;")
    #     display_video_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    #     reports_page_layout.addWidget(display_video_btn)
    #
    #     # Create the table widget
    #     violence_reports_table = QTableWidget(3, 3)
    #     violence_reports_table.setStyleSheet("QAbstractItemView::indicator {width: 25px; height: 25px;}"
    #                                          "QTableWidget::item {width: 500px; height: 40px;}")
    #     violence_reports_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #     violence_reports_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    #     violence_reports_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    #
    #     # Populate the table with items
    #     for row in range(3):
    #         # Create radio button for each row
    #         radio_button = QRadioButton()
    #         violence_reports_table.setCellWidget(row, 0, radio_button)
    #         for col in range(1, 5):
    #             item = QTableWidgetItem('Item {0}-{1}'.format(row, col))
    #             violence_reports_table.setItem(row, col, item)
    #
    #     # Set header properties
    #     header = violence_reports_table.horizontalHeader()
    #     header.setStyleSheet("background-color: #0e0d6a; color: #ffffff; font-weight: bold;")
    #     # Set column names
    #     violence_reports_table.setHorizontalHeaderLabels(["", "ID", "Date", "", ""])
    #
    #     # Add the table widget to the layout
    #     reports_page_layout.addWidget(violence_reports_table)
    #
    #     # Set the layout for the reports page
    #     self.stackedWidget.widget(7).setLayout(reports_page_layout)  # Assuming index 7 is the reports page

    # methods to show context menus
    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1,
                                      ["Students Information", "Students Payments",
                                       "Students Transactions"])

    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu(self)

        # set style for the menu
        menu.setStyleSheet("""
                        QMenu{
                            background-color: #0192ef;
                            color: #0e0d6a;
                            /*border: 1px solid #0e0d6a;*/
                            /*border-radius:15px;*/
                            }
                        QMenu:selected{
                            background-color: #52452a;
                            color: #fec701;
                            }    

                        """)

        # add actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        # show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()

        if text == "Students Information":
            self.switch_to_studentsInformation()
        elif text == "Students Payments":
            self.switch_to_studentsPayments()
        elif text == "Students Transactions":
            self.switch_to_studentsTransactions()


    #Open dialog for inserting new students
    def open_addStudent_dialog(self):
        from StudentDialog import Ui_StudentsDialog
        #instantiate and show the dialog
        addStudent_dialog = Ui_StudentsDialog(self)
        result = addStudent_dialog.exec() #This will block until the dialog is closed

        if result == Ui_StudentsDialog.accepted:
            #if the dialog was accepted (user clicked add student button)
            pass



# class DoubleButtonWidgetStudents(QWidget):
#     def __init__(self, row_index, row_data):
#         super().__init__()
#
#         #store the row index and row data as an instance in variables
#         self.row_index = row_index
#         self.row_data = row_data
#
#         #get student variables from the tuple
#         self.student_name = self.row_data[0]
#         self.student_id = self.row_data[1]
#
#         layout = QHBoxLayout(self)
#
#         #create display video button
#         self.display_video_btn = QPushButton("", self)
#         self.display_video_btn.setStyleSheet("background-color : #fec701")
#         self.display_video_btn.setFixedSize(61, 31)
#
#         #set icon for the button
#         icon = QIcon(":/Icons/ad-blocker (2).png")
#         self.display_video_btn.setIcon(icon)
#
#         layout .addWidget(self.display_video_btn)

