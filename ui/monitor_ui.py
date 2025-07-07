# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monitor.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 700)
        MainWindow.setMinimumSize(QSize(950, 700))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    /*background: #545655;*/\n"
"    color: white;\n"
"    font: 14px \"Montserrat\";\n"
"}\n"
"\n"
"\n"
"QWidget {\n"
"    background: #545655;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: #6BCDE3;\n"
"    font: 14px \"Montserrat\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#labelSystemMonitor, #labelNetworkSpeed {\n"
"	color: white;\n"
"    font: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#cpu_L, #ram_L, #disk_L, #gpu_L, #network_L, #Download_L, #Upload_L, #Ping_L, #PublicIP_L, #LocalIP_L, #MacAddr_L  {\n"
"	color: white;\n"
"    font: 14px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background: #6BCDE3;\n"
"    font: 14px \"Montserrat\";\n"
"    font-weight: bold;\n"
"    min-width: 200px;\n"
"    min-height: 30px;\n"
"    max-width: 200px;\n"
"    max-height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#chart_widget {\n"
"    background-color: #424443;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f"
                        " \u0432\u0438\u0434\u0436\u0435\u0442\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 (QChartView) */\n"
"QChartView {\n"
"    background-color: #424443;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #6BCDE3;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0432\u043d\u0443\u0442\u0440\u0438 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 */\n"
"QChartView QChart {\n"
"    background-color: transparent;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QChartView QLegend {\n"
"    background-color: transparent;\n"
"    color: #6BCDE3;\n"
"    font: 12px \"Montserrat\";\n"
"    border: none;\n"
"}\n"
"\n"
"QChartView QAbstractAxis {\n"
"    color: #6BCDE3;\n"
"    grid-line-color: #545655;\n"
"}\n"
"\n"
"QChartView QValueAxis {\n"
"    label-color: #FFFFFF;\n"
"    title-color: #6BCDE3;\n"
"    font: 12px \"Montserrat\";\n"
"}\n"
"\n"
"QChartView QLineSeries {\n"
"    color: #6BCDE3;  /* \u041e\u0441\u043d\u043e\u0432\u043d\u043e"
                        "\u0439 \u0446\u0432\u0435\u0442 */\n"
"    alternate-color: #5ABDD3;  /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 */\n"
"    width: 2px;  /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u043b\u0438\u043d\u0438\u0438 */\n"
"}")
        self.actionWord = QAction(MainWindow)
        self.actionWord.setObjectName(u"actionWord")
        self.actiontxt = QAction(MainWindow)
        self.actiontxt.setObjectName(u"actiontxt")
        self.actionpdf = QAction(MainWindow)
        self.actionpdf.setObjectName(u"actionpdf")
        self.actionhtml = QAction(MainWindow)
        self.actionhtml.setObjectName(u"actionhtml")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_11 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_20 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_9.addWidget(self.label_18)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.PublicIP_L = QLabel(self.centralwidget)
        self.PublicIP_L.setObjectName(u"PublicIP_L")

        self.horizontalLayout_9.addWidget(self.PublicIP_L)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_10.addWidget(self.label_20)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.LocalIP_L = QLabel(self.centralwidget)
        self.LocalIP_L.setObjectName(u"LocalIP_L")

        self.horizontalLayout_10.addWidget(self.LocalIP_L)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_11.addWidget(self.label_21)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.MacAddr_L = QLabel(self.centralwidget)
        self.MacAddr_L.setObjectName(u"MacAddr_L")

        self.horizontalLayout_11.addWidget(self.MacAddr_L)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_19)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_10 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_22 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_22)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_12 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.labelSystemMonitor = QLabel(self.centralwidget)
        self.labelSystemMonitor.setObjectName(u"labelSystemMonitor")

        self.horizontalLayout_12.addWidget(self.labelSystemMonitor)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_37 = QLabel(self.centralwidget)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_31.addWidget(self.label_37)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_48)

        self.cpu_L = QLabel(self.centralwidget)
        self.cpu_L.setObjectName(u"cpu_L")

        self.horizontalLayout_31.addWidget(self.cpu_L)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_49)


        self.verticalLayout_4.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_15 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_15)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_38 = QLabel(self.centralwidget)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_32.addWidget(self.label_38)

        self.horizontalSpacer_50 = QSpacerItem(37, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_50)

        self.ram_L = QLabel(self.centralwidget)
        self.ram_L.setObjectName(u"ram_L")

        self.horizontalLayout_32.addWidget(self.ram_L)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_51)


        self.verticalLayout_4.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_16 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_16)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_39 = QLabel(self.centralwidget)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_33.addWidget(self.label_39)

        self.horizontalSpacer_52 = QSpacerItem(39, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_52)

        self.disk_L = QLabel(self.centralwidget)
        self.disk_L.setObjectName(u"disk_L")

        self.horizontalLayout_33.addWidget(self.disk_L)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_53)


        self.verticalLayout_4.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_17 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_17)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_40 = QLabel(self.centralwidget)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_34.addWidget(self.label_40)

        self.horizontalSpacer_54 = QSpacerItem(39, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_54)

        self.gpu_L = QLabel(self.centralwidget)
        self.gpu_L.setObjectName(u"gpu_L")

        self.horizontalLayout_34.addWidget(self.gpu_L)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_55)


        self.verticalLayout_4.addLayout(self.horizontalLayout_34)

        self.verticalSpacer_18 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_18)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_41 = QLabel(self.centralwidget)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_35.addWidget(self.label_41)

        self.horizontalSpacer_56 = QSpacerItem(8, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_56)

        self.network_L = QLabel(self.centralwidget)
        self.network_L.setObjectName(u"network_L")

        self.horizontalLayout_35.addWidget(self.network_L)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_57)


        self.verticalLayout_4.addLayout(self.horizontalLayout_35)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout)

        self.horizontalSpacer_18 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.labelNetworkSpeed = QLabel(self.centralwidget)
        self.labelNetworkSpeed.setObjectName(u"labelNetworkSpeed")

        self.horizontalLayout_13.addWidget(self.labelNetworkSpeed)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.Download_L = QLabel(self.centralwidget)
        self.Download_L.setObjectName(u"Download_L")

        self.horizontalLayout_6.addWidget(self.Download_L)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.horizontalSpacer_7 = QSpacerItem(34, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.Upload_L = QLabel(self.centralwidget)
        self.Upload_L.setObjectName(u"Upload_L")

        self.horizontalLayout_7.addWidget(self.Upload_L)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_8.addWidget(self.label_16)

        self.horizontalSpacer_8 = QSpacerItem(53, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.Ping_L = QLabel(self.centralwidget)
        self.Ping_L.setObjectName(u"Ping_L")

        self.horizontalLayout_8.addWidget(self.Ping_L)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.start_test_B = QPushButton(self.centralwidget)
        self.start_test_B.setObjectName(u"start_test_B")

        self.verticalLayout_2.addWidget(self.start_test_B)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_13)


        self.horizontalLayout_15.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_21)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_19)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.chart_widget = QWidget(self.centralwidget)
        self.chart_widget.setObjectName(u"chart_widget")
        self.chart_widget.setMinimumSize(QSize(650, 200))

        self.horizontalLayout.addWidget(self.chart_widget)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalSpacer_12 = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_12)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_5 = QMenu(self.menu)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.menu_5.menuAction())
        self.menu_5.addAction(self.actionWord)
        self.menu_5.addAction(self.actiontxt)
        self.menu_5.addAction(self.actionpdf)
        self.menu_5.addAction(self.actionhtml)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionWord.setText(QCoreApplication.translate("MainWindow", u"Word", None))
        self.actiontxt.setText(QCoreApplication.translate("MainWindow", u"txt", None))
        self.actionpdf.setText(QCoreApplication.translate("MainWindow", u"pdf", None))
        self.actionhtml.setText(QCoreApplication.translate("MainWindow", u"html", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Public IP:", None))
        self.PublicIP_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Local IP:", None))
        self.LocalIP_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a \u0430\u0434\u0440\u0435\u0441:", None))
        self.MacAddr_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.labelSystemMonitor.setText(QCoreApplication.translate("MainWindow", u"System monitor", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.cpu_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"RAM:", None))
        self.ram_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Disk:", None))
        self.disk_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"GPU:", None))
        self.gpu_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Network:", None))
        self.network_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.labelNetworkSpeed.setText(QCoreApplication.translate("MainWindow", u"Network speed", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Download:", None))
        self.Download_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Upload:", None))
        self.Upload_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ping:", None))
        self.Ping_L.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.start_test_B.setText(QCoreApplication.translate("MainWindow", u"Start test", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

