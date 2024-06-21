import window
import random
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow


class New_Ui_MainWindow(window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.StartButton.clicked.connect(self.start_button_clicked)
        self.PauseButton.clicked.connect(self.pause_button_clicked)

    def start_button_clicked(self):
        self.timer.start(10)

    def update_label(self):
        self.num = random.randint(1, 400)
        self.label_3.setText(str(self.num).zfill(3))

    def pause_button_clicked(self):
        self.timer.stop()
        self.label_3.setText(str(self.num).zfill(3))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    mainUi = New_Ui_MainWindow()
    mainUi.setupUi(win)
    win.show()
    sys.exit(app.exec_())
