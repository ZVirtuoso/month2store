# from PyQt5.Qt import *
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello")
window.resize(500, 500)
window.move(400,200)

label = QLabel(window)

window.show()
sys.exit(app.exec_())
