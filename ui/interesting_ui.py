# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interesting.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Interesting(object):
    def setupUi(self, Interesting):
        if not Interesting.objectName():
            Interesting.setObjectName(u"Interesting")
        Interesting.resize(100, 100)
        Interesting.setStyleSheet(u"QWidget {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.gridLayout = QGridLayout(Interesting)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Interesting)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Interesting)

        QMetaObject.connectSlotsByName(Interesting)
    # setupUi

    def retranslateUi(self, Interesting):
        Interesting.setWindowTitle(QCoreApplication.translate("Interesting", u"Form", None))
        self.label.setText("")
    # retranslateUi

