from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap, QMouseEvent, Qt
from PySide2.QtCore import QRect, QTimer

from ui.interesting_ui import Ui_Interesting


class Interesting(QWidget, Ui_Interesting):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.setMouseTracking(True)


        self.mousePos = (0, 0)
        self.isPressed = False

        self.frame = 0
        self.original = QPixmap("./resources/lucifer.png")
        self.pixmaps = [self.original.copy(QRect(i*100, 0, 100, 100)) for i in range(12)]

        self.label.setPixmap(self.pixmaps[self.frame])

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.nextFrame)
        self.timer.start(1000//25)

    def mousePressEvent(self, event: QMouseEvent):
        self.isPressed = True
        self.mousePos = event.x(), event.y()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.isPressed = False

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.RightButton:
            self.close()
        elif event.buttons() & Qt.MiddleButton:
            pass

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.isPressed: self.move(event.globalX() - self.mousePos[0], event.globalY() - self.mousePos[1])

    def nextFrame(self):
        self.frame += 1
        self.frame %= 12
        self.label.setPixmap(self.pixmaps[self.frame])