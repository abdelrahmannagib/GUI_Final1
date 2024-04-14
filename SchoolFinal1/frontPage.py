from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QMenu, QMessageBox
from ui_Final1 import Ui_MainWindow
import cv2
import numpy as np
from ViolenceRealTime import DetectYacta
#from ViolenceRealTime import *
from PySide6.QtCore import QThread

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Smart School Management System")

        # hide widget menu initially
        self.icon_only_widget.setHidden(True)
        # hide drop down initially
        self.students_dropdown.setHidden(True)

        # connect buttons to switch different pages
        self.home_1.clicked.connect(self.switch_to_home)
        self.home_2.clicked.connect(self.switch_to_home)

        self.students_1.clicked.connect(self.switch_to_students)
        self.students_2.clicked.connect(self.switch_to_students)

        self.student_information.clicked.connect(self.switch_to_studentsInformation)
        self.student_payments.clicked.connect(self.switch_to_studentsPayments)
        self.student_transactions.clicked.connect(self.switch_to_studentsTransactions)

        # self.classMonitoring_1.clicked.connect(self.switch_to_classMonitoring)
        # self.classMonitoring_2.clicked.connect(self.switch_to_classMonitoring)

        self.attendance_1.clicked.connect(self.switch_to_attendance)
        self.attendance_2.clicked.connect(self.switch_to_attendance)

        self.reports_1.clicked.connect(self.switch_to_reports)
        self.reports_2.clicked.connect(self.switch_to_reports)

        # connect buttons to respective context menus
        self.students_1.clicked.connect(self.students_context_menu)

        #open student dialog
        self.addStudent_button.clicked.connect(self.open_addStudent_dialog)

        #connect class monitoring button to its method
        self.classMonitoring_1.clicked.connect(self.switch_to_classMonitoring)
        # self.classMonitoring_2.clicked.connect(self.prepare_for_monitoring)
        self.classMonitoring_2.clicked.connect(self.switch_to_classMonitoring)

        #set the default page to home
        self.switch_to_home()

    # def prepare_for_monitoring(self):
    #     # You can add any preparation steps here before starting the monitoring
    #     self.switch_to_classMonitoring()
    #     # Start the monitoring in a separate thread
    #     self.video_thread = VideoThread()
    #     self.video_thread.start()

    # methods to switch different pages
    def switch_to_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_students(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_studentsInformation(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_studentsPayments(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_studentsTransactions(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_classMonitoring(self):
        DetectYacta()
        self.stackedWidget.setCurrentIndex(5)
        #DetectYacta()
        # # Start capturing frames from the camera
        # cap = cv2.VideoCapture(
        #     0)  # Use 0 for the default camera, or specify the camera index if you have multiple cameras
        #
        # while True:
        #     ret, frame = cap.read()  # Read a frame from the camera
        #     if not ret:
        #         print("Failed to capture frame.")
        #         break
        #
        #     # Pass the frame to the predict_video function for violence detection
        #     self.predict_video_frame(frame)
        #
        #     cv2.imshow('Live Video', frame)  # Display the live video feed
        #
        #     # Check for key press to exit the loop
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break
        #
        # # Release the camera
        # cap.release()
        # cv2.destroyAllWindows()
        #
        # # Method to process a single frame for violence detection






    def switch_to_attendance(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_reports(self):
        self.stackedWidget.setCurrentIndex(7)

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



    # def start_class_monitoring(self):
    #     # Initialize the camera
    #     cap = cv2.VideoCapture(0)
    #
    #     # Check if the camera opened successfully
    #     if not cap.isOpened():
    #         QMessageBox.critical(self, "Error", "Failed to open camera.")
    #         return
    #
    #     try:
    #         while True:
    #             # Capture frame-by-frame
    #             ret, frame = cap.read()
    #
    #             if not ret:
    #                 QMessageBox.critical(self, "Error", "Failed to capture frame.")
    #                 break
    #
    #             # Display the captured frame
    #             cv2.imshow('Live Video', frame)
    #
    #             # Pass the frame to the class monitoring function
    #             predict_video(frame)
    #
    #             # Break the loop if 'q' is pressed
    #             if cv2.waitKey(1) & 0xFF == ord('q'):
    #                 break
    #
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    #
    #     finally:
    #         # Release the camera
    #         cap.release()
    #         # Close OpenCV windows
    #         cv2.destroyAllWindows()



# class VideoThread(QThread):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#     def run(self):
#         # Initialize the camera
#         cap = cv2.VideoCapture(0)
#
#         # Check if the camera opened successfully
#         if not cap.isOpened():
#             QMessageBox.critical(None, "Error", "Failed to open camera.")
#             return
#
#         try:
#             while True:
#                 # Capture frame-by-frame
#                 ret, frame = cap.read()
#
#                 if not ret:
#                     QMessageBox.critical(None, "Error", "Failed to capture frame.")
#                     break
#
#                 # Display the captured frame
#                 cv2.imshow('Live Video', frame)
#
#                 # Pass the frame to the class monitoring function
#                 predict_video(frame)
#
#                 # Break the loop if 'q' is pressed
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break
#
#         except Exception as e:
#             QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")
#
#         finally:
#             # Release the camera
#             cap.release()
#             # Close OpenCV windows
#             cv2.destroyAllWindows()