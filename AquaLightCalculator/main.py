import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from AquaLightCalculator.controller.aqua_calculator import MainWindow


def run():
    app = QApplication(sys.argv)
    app.setApplicationName("AquaLight Calculator")
    app.setWindowIcon(QIcon("fish.ico"))
    app.setApplicationVersion("1.0.1")
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
