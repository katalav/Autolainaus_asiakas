# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import testpictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 1080)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setToolTipDuration(-3000)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(51, 167, 181);")
        self.actionedellinen = QAction(MainWindow)
        self.actionedellinen.setObjectName(u"actionedellinen")
        icon = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionedellinen.setIcon(icon)
        self.actionKaikki = QAction(MainWindow)
        self.actionKaikki.setObjectName(u"actionKaikki")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.namesFrame = QFrame(self.centralwidget)
        self.namesFrame.setObjectName(u"namesFrame")
        self.namesFrame.setGeometry(QRect(30, 190, 941, 501))
        self.namesFrame.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.savePushButton = QPushButton(self.namesFrame)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(600, 400, 161, 61))
        self.savePushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"font: 28pt \"Segoe UI\";")
        self.readIdLineEdit = QLineEdit(self.namesFrame)
        self.readIdLineEdit.setObjectName(u"readIdLineEdit")
        self.readIdLineEdit.setGeometry(QRect(60, 220, 231, 71))
        self.readIdLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 22pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.keyBarcodeLineEdit = QLineEdit(self.namesFrame)
        self.keyBarcodeLineEdit.setObjectName(u"keyBarcodeLineEdit")
        self.keyBarcodeLineEdit.setGeometry(QRect(390, 220, 231, 71))
        self.keyBarcodeLineEdit.setStyleSheet(u"font: 28pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.readIdLabel = QLabel(self.namesFrame)
        self.readIdLabel.setObjectName(u"readIdLabel")
        self.readIdLabel.setGeometry(QRect(70, 140, 211, 51))
        self.readIdLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"background-color: rgb(0, 33, 72);")
        self.readIdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.keyBarcodeLabel = QLabel(self.namesFrame)
        self.keyBarcodeLabel.setObjectName(u"keyBarcodeLabel")
        self.keyBarcodeLabel.setGeometry(QRect(400, 140, 211, 51))
        self.keyBarcodeLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"background-color: rgb(0, 33, 72);")
        self.keyBarcodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.keyBarcodeReturnLineEdit = QLineEdit(self.namesFrame)
        self.keyBarcodeReturnLineEdit.setObjectName(u"keyBarcodeReturnLineEdit")
        self.keyBarcodeReturnLineEdit.setGeometry(QRect(390, 220, 231, 71))
        self.keyBarcodeReturnLineEdit.setStyleSheet(u"font: 28pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lenderNameLabel = QLabel(self.namesFrame)
        self.lenderNameLabel.setObjectName(u"lenderNameLabel")
        self.lenderNameLabel.setGeometry(QRect(30, 220, 281, 71))
        self.lenderNameLabel.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 33, 72);")
        self.lenderNameLabel.setScaledContents(False)
        self.lenderNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.carsInfoStatusLabel = QLabel(self.namesFrame)
        self.carsInfoStatusLabel.setObjectName(u"carsInfoStatusLabel")
        self.carsInfoStatusLabel.setGeometry(QRect(370, 220, 281, 71))
        self.carsInfoStatusLabel.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 33, 72);")
        self.carsInfoStatusLabel.setScaledContents(False)
        self.carsInfoStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateLabel = QLabel(self.namesFrame)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(120, 310, 151, 41))
        self.dateLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";")
        self.calendarLabel = QLabel(self.namesFrame)
        self.calendarLabel.setObjectName(u"calendarLabel")
        self.calendarLabel.setGeometry(QRect(80, 310, 31, 41))
        self.calendarLabel.setPixmap(QPixmap(u":/png/calendar.drawio"))
        self.calendarLabel.setScaledContents(True)
        self.timeLabel = QLabel(self.namesFrame)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(520, 310, 121, 41))
        self.timeLabel.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.clockLabel = QLabel(self.namesFrame)
        self.clockLabel.setObjectName(u"clockLabel")
        self.clockLabel.setGeometry(QRect(460, 310, 41, 41))
        self.clockLabel.setPixmap(QPixmap(u":/png/clock.drawio"))
        self.clockLabel.setScaledContents(True)
        self.carPhotoLabel = QLabel(self.namesFrame)
        self.carPhotoLabel.setObjectName(u"carPhotoLabel")
        self.carPhotoLabel.setGeometry(QRect(640, 210, 251, 191))
        self.carPhotoLabel.setPixmap(QPixmap(u"../../../Pictures/XUX682.png"))
        self.carPhotoLabel.setScaledContents(True)
        self.saveReturnPushButton = QPushButton(self.namesFrame)
        self.saveReturnPushButton.setObjectName(u"saveReturnPushButton")
        self.saveReturnPushButton.setGeometry(QRect(600, 400, 161, 61))
        self.saveReturnPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"font: 28pt \"Segoe UI\";")
        self.teacherLabel = QLabel(self.centralwidget)
        self.teacherLabel.setObjectName(u"teacherLabel")
        self.teacherLabel.setGeometry(QRect(20, 20, 151, 151))
        self.teacherLabel.setPixmap(QPixmap(u"uiPictures/teacher.png"))
        self.teacherLabel.setScaledContents(True)
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(400, 20, 281, 71))
        self.statusLabel.setStyleSheet(u"font: 28pt \"Segoe UI\";\n"
"color: rgb(0, 33, 72);")
        self.statusLabel.setScaledContents(False)
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.takeCarPushButton = QPushButton(self.centralwidget)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(280, 100, 211, 61))
        self.takeCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeCarPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Segoe UI\";")
        self.returnCarPushButton = QPushButton(self.centralwidget)
        self.returnCarPushButton.setObjectName(u"returnCarPushButton")
        self.returnCarPushButton.setGeometry(QRect(560, 100, 211, 61))
        self.returnCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnCarPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);\n"
"font: 24pt \"Segoe UI\";")
        self.goBackPushButton = QPushButton(self.centralwidget)
        self.goBackPushButton.setObjectName(u"goBackPushButton")
        self.goBackPushButton.setGeometry(QRect(690, 100, 251, 61))
        font1 = QFont()
        font1.setPointSize(24)
        self.goBackPushButton.setFont(font1)
        self.goBackPushButton.setStyleSheet(u"\n"
"background-color: rgb(0, 33, 72);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/png/uiPictures/goBackArrow.drawio", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.goBackPushButton.setIcon(icon1)
        self.goBackPushButton.setIconSize(QSize(24, 24))
        self.startFrame = QFrame(self.centralwidget)
        self.startFrame.setObjectName(u"startFrame")
        self.startFrame.setGeometry(QRect(100, 180, 821, 541))
        self.startFrame.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.startFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.startFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.vapaanaLabel = QLabel(self.startFrame)
        self.vapaanaLabel.setObjectName(u"vapaanaLabel")
        self.vapaanaLabel.setGeometry(QRect(90, 30, 121, 31))
        self.vapaanaLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";")
        self.ajossaLabel = QLabel(self.startFrame)
        self.ajossaLabel.setObjectName(u"ajossaLabel")
        self.ajossaLabel.setGeometry(QRect(540, 30, 81, 41))
        self.ajossaLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";")
        self.availablePlainTextEdit = QPlainTextEdit(self.startFrame)
        self.availablePlainTextEdit.setObjectName(u"availablePlainTextEdit")
        self.availablePlainTextEdit.setGeometry(QRect(50, 110, 311, 311))
        self.availablePlainTextEdit.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.availablePlainTextEdit.setReadOnly(True)
        self.rentedPlainTextEdit = QPlainTextEdit(self.startFrame)
        self.rentedPlainTextEdit.setObjectName(u"rentedPlainTextEdit")
        self.rentedPlainTextEdit.setGeometry(QRect(430, 100, 311, 321))
        self.rentedPlainTextEdit.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.rentedPlainTextEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.actionedellinen.setText(QCoreApplication.translate("MainWindow", u"Lopeta", None))
#if QT_CONFIG(shortcut)
        self.actionedellinen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionKaikki.setText(QCoreApplication.translate("MainWindow", u"Kaikki", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.readIdLineEdit.setText("")
        self.keyBarcodeLineEdit.setText("")
        self.readIdLabel.setText(QCoreApplication.translate("MainWindow", u"Lue ajokortti", None))
        self.keyBarcodeLabel.setText(QCoreApplication.translate("MainWindow", u"Lue avain", None))
        self.keyBarcodeReturnLineEdit.setText("")
        self.lenderNameLabel.setText("")
        self.carsInfoStatusLabel.setText("")
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"31.01.2025", None))
        self.calendarLabel.setText("")
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"09:51", None))
        self.clockLabel.setText("")
        self.carPhotoLabel.setText("")
        self.saveReturnPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.teacherLabel.setText("")
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Autonlainaus", None))
        self.takeCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.returnCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Palautus", None))
        self.goBackPushButton.setText(QCoreApplication.translate("MainWindow", u"Kumoa", None))
        self.vapaanaLabel.setText(QCoreApplication.translate("MainWindow", u"Vapaana", None))
        self.ajossaLabel.setText(QCoreApplication.translate("MainWindow", u"Ajossa", None))
    # retranslateUi

