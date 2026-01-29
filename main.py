import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTime,QTimer,Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_lable = QLabel("12:00:00",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("digital clock")
        self.setGeometry(600,400,300,100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_lable)
        self.setLayout(vbox)

        self.time_lable.setAlignment(Qt.AlignCenter)
        self.time_lable.setStyleSheet("font-size : 150px;"
                                      "color : hsl(111 , 100% , 50%);")
        self.setStyleSheet("background-color : black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_lable.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())