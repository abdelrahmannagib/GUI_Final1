from PySide6.QtWidgets import QApplication
from SchoolFinal1.frontPage import MySideBar
import sys
#import RealTime
app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()
