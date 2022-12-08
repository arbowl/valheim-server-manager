import subprocess
from PyQt6.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow

from valheim_gui import Ui_manager_window


def start_server():

    return


def update_server():
    
    return


if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    gui = Ui_manager_window()
    gui.setupUi(window)
    gui.start_button.clicked.connect(start_server)
    gui.start_button.clicked.connect(update_server)
    window.show()
    app.exec()
