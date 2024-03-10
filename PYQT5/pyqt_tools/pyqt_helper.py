from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(500, 500)

    def setup_label(self, title):
        self.label = QLabel(self)
        self.label.setText(title)
        self.label.move(100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window('Hello World')
    window.setup_label('Bye World')
    window.show()
    sys.exit(app.exec_())
