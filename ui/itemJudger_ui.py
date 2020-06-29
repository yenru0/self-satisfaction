# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'itemJudger.ui'
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



class Ui_judger(object):
    def setupUi(self, judger):
        if not judger.objectName():
            judger.setObjectName(u"judger")
        judger.resize(260, 74)
        self.verticalLayout_2 = QVBoxLayout(judger)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(judger)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.title)

        self.remainer = QProgressBar(judger)
        self.remainer.setObjectName(u"remainer")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        self.remainer.setFont(font1)
        self.remainer.setStyleSheet(u"QProgressBar {\n"
"     border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     background-color: white;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: rgb(0, 170, 255);\n"
" }")
        self.remainer.setValue(24)
        self.remainer.setAlignment(Qt.AlignCenter)
        self.remainer.setTextVisible(True)

        self.verticalLayout_2.addWidget(self.remainer)


        self.retranslateUi(judger)

        QMetaObject.connectSlotsByName(judger)
    # setupUi

    def retranslateUi(self, judger):
        judger.setWindowTitle(QCoreApplication.translate("judger", u"Form", None))
        self.title.setText(QCoreApplication.translate("judger", u"$subject", None))
        self.remainer.setFormat(QCoreApplication.translate("judger", u"%v", None))
    # retranslateUi

