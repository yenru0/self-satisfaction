from PySide2.QtWidgets import QMainWindow, QLabel, QWidget, QRubberBand, QStyle, QLayout, QStyleFactory, QSpacerItem, QSizePolicy
from PySide2.QtGui import Qt, QMouseEvent, QPixmap, QPalette, QBrush, QColor, QFont, QFontMetrics
from PySide2.QtCore import QEvent, QObject, QRect, QTimer, QTextCodec

import datetime

from ui.main_ui import Ui_MainWindow
from ui.itemJudger import ItemJudger
from ui.interesting import Interesting


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, preference, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("self-satisfaction")

        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.central.setAutoFillBackground(True)
        self.interestings = []

        self.mousePos: tuple = (0, 0)
        self.isPressed: bool = False

        self.count = len(preference["elements"])
        self.listItemJudget = []

        for i, elem in enumerate(preference["elements"]):
            v = ItemJudger(elem["title"], datetime.datetime.strptime(elem["finish"], "%Y-%m-%d-%H-%M-%S"), maxRemain=int(elem["maxRemain"]),
                           display_fmt=elem["display_fmt"], parent=self.central)
            v.setObjectName(f"itemJudger{i}")
            self.centralLayout.addWidget(v)
            self.listItemJudget.append(v)

        tnp = self.central.palette()
        tnp.setColor(self.central.backgroundRole(), QColor(*map(int, preference["background_color"].split())))
        self.central.setPalette(tnp)

        self.centralLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def mousePressEvent(self, event: QMouseEvent):
        self.isPressed = True
        self.mousePos = event.x(), event.y()
        if event.buttons() & Qt.MiddleButton:
            for i, w in enumerate(self.interestings[::-1]):
                if not w.isVisible():
                    del self.interestings[i]
            print(len(self.interestings))
            t = Interesting()
            t.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
            t.setWindowTitle("lucifer")
            t.show()
            self.interestings.append(t)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.isPressed = False

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.RightButton:
            self.close()
        elif event.buttons() & Qt.MiddleButton:
            pass

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.isPressed: self.move(event.globalX() - self.mousePos[0], event.globalY() - self.mousePos[1])


