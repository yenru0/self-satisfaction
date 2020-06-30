from PySide2.QtWidgets import QWidget, QProgressBar
from PySide2.QtCore import QTimer

import datetime

from ui.itemJudger_ui import Ui_judger


class ItemJudger(QWidget, Ui_judger):
    def __init__(self, title, finish: datetime.datetime, maxRemain=3000000000, display_fmt="ms", parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.display_fmt = display_fmt
        self.finish = finish
        self.maxRemain = maxRemain
        self.remainer.setMaximum(maxRemain // 1000)
        self.setTitle(title)


        self.timerUpdate = QTimer(self)
        self.timerUpdate.timeout.connect(self.updateRemainer)

        if self.display_fmt in ("ms", "xms"):
            self.timerUpdate.start(47)
        elif self.display_fmt in("sec", "xsec"):
            self.timerUpdate.start(900)
        elif self.display_fmt in ("min", "xmin"):
            self.timerUpdate.start(5000)
        elif self.display_fmt in ("hour", "xhr"):
            self.timerUpdate.start(5000)
        elif self.display_fmt in ("day", "xday"):
            self.timerUpdate.start(10000)
        else:
            self.display_fmt = "ms"
            self.timerUpdate.start(47)



        self.updateRemainer()




    def setTitle(self, title):
        self.title.setText(title)

    def updateRemainer(self):
        # var for calculating progressBar
        pt = (self.finish - datetime.datetime.now()) / datetime.timedelta(seconds=1)
        if pt < 0:
            pt = 0
        elif pt > self.maxRemain:
            pt = self.maxRemain

        if self.display_fmt in ("ms", "xms"):
            t = int((self.finish - datetime.datetime.now()) / datetime.timedelta(milliseconds=1))
        elif self.display_fmt in ("sec", "xsec"):
            t = int((self.finish - datetime.datetime.now()) / datetime.timedelta(seconds=1))
        elif self.display_fmt in ("min", "xmin"):
            t = int((self.finish - datetime.datetime.now()) / datetime.timedelta(minutes=1))
        elif self.display_fmt in ("hour", "xhr"):
            t = int((self.finish - datetime.datetime.now()) / datetime.timedelta(hours=1))
        elif self.display_fmt in ("day", "xday"):
            t = int((self.finish - datetime.datetime.now()) / datetime.timedelta(days=1))
        else:
            t = int((self.finish - datetime.datetime.now()) / datetime.timedelta(milliseconds=1))


        if self.display_fmt in ("xms", "xsec", "xmin", "xhr", "xday"):
            t = format(t, "X")
        else:
            t = str(t)
        self.remainer.setValue(self.maxRemain // 1000 - pt)
        self.remainer.setFormat(str(t))


