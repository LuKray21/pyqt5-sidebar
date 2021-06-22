import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from SideBar import SideBar


class MainWindow(QMainWindow):
    resized = pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1024, 600)

        sidebar = SideBar(self)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.resized.emit()

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()