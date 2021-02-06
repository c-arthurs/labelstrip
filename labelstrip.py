# DEPLOY MAC
# sudo pyinstaller -F --windowed -p /Users/callum/callum/labelstrip/scripts --add-data "/Users/callum/callum/labelstrip/scripts:scripts" --icon=scripts/icon.icns labelstrip.py
# Windows
# pyinstaller -F --windowed --hidden-import=configparser -p C:/Users/callum/labelstrip/scripts --add-data "C:/Users/callum/labelstrip/scripts;scripts" --icon=scripts/icon.ico labelstrip.py

from scripts import anonymise_slide_py3
import qdarkgraystyle
import sys
import os
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import subprocess

if not hasattr(sys, "_MEIPASS"):
    sys._MEIPASS = '.'  # for running locally

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi(sys._MEIPASS + os.sep + "scripts" + os.sep + "MainWindow_layout.ui", self)  # for deployment
        self.statusBar()
        self.setWindowTitle('LABELSTRIP')
        self.setWindowOpacity(0.96)
        self.runbutton.clicked.connect(lambda: self.run())
        self.show()

    def run(self):
        print("running")
        path = QFileDialog.getExistingDirectory(parent=self, caption='Open file')
        # path = "/Users/callum/Desktop/stripname"
        if path:
            files = [i for i in os.listdir(path) if i.endswith(".svs")]
            self.progressBar.setMaximum(len(files))
            print(files)
            for i in range(len(files)):
                print(path+os.sep+files[i])
                anonymise_slide_py3._main(path+os.sep+files[i])
                self.progressBar.setValue(i+1)
                QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()

    # style sheet - https://github.com/mstuttgart/qdarkgraystyle
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())

    sys.exit(app.exec_())
