#!/usr/bin/python3
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from checker import UpdateChecker


check = UpdateChecker()
check.URL = "http://127.0.0.1:8000/update.xml"
oldVersion = check.getVersion("oldVersion")
currentVersion = check.getVersion("currentVersion")
message = check.getMessage("message")


class AppForm(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.create_main_frame()

    def create_main_frame(self):
        page = QWidget()

        self.button = QPushButton('Check', page)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.button)
        page.setLayout(vbox1)
        self.setCentralWidget(page)

        self.connect(self.button, SIGNAL("clicked()"), self.clicked)

    def clicked(self):
        if oldVersion != currentVersion:
            QMessageBox.about(self, "Update Checker",
                              "Version %s %s Your version: %s" %
                              (currentVersion, message, oldVersion))
        else:
            QMessageBox.about(self, "Update Checker",
                              "Your system is up to date")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = AppForm()
    form.setMinimumSize(500, 100)
    form.move(QApplication.desktop().screen(
    ).rect().center() - form.rect().center())
    form.setWindowTitle("Update Checker")
    form.show()
    app.exec_()
