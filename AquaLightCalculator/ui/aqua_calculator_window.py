# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aqua_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 515)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(506, 515))
        MainWindow.setBaseSize(QtCore.QSize(510, 515))
        MainWindow.setStyleSheet("color: rgb(222, 221, 218);\n"
"background-color: rgb(94, 92, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_power_light = QtWidgets.QWidget()
        self.tab_power_light.setObjectName("tab_power_light")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_power_light)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dsb_flux_bottom = QtWidgets.QDoubleSpinBox(self.tab_power_light)
        self.dsb_flux_bottom.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_flux_bottom.sizePolicy().hasHeightForWidth())
        self.dsb_flux_bottom.setSizePolicy(sizePolicy)
        self.dsb_flux_bottom.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.dsb_flux_bottom.setFrame(False)
        self.dsb_flux_bottom.setReadOnly(True)
        self.dsb_flux_bottom.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dsb_flux_bottom.setAccelerated(False)
        self.dsb_flux_bottom.setMaximum(10000.0)
        self.dsb_flux_bottom.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.dsb_flux_bottom.setObjectName("dsb_flux_bottom")
        self.gridLayout.addWidget(self.dsb_flux_bottom, 5, 1, 1, 1)
        self.lbl_area = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_area.sizePolicy().hasHeightForWidth())
        self.lbl_area.setSizePolicy(sizePolicy)
        self.lbl_area.setObjectName("lbl_area")
        self.gridLayout.addWidget(self.lbl_area, 6, 0, 1, 1)
        self.lbl_flux = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_flux.sizePolicy().hasHeightForWidth())
        self.lbl_flux.setSizePolicy(sizePolicy)
        self.lbl_flux.setObjectName("lbl_flux")
        self.gridLayout.addWidget(self.lbl_flux, 3, 0, 1, 1)
        self.lbl_meter = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_meter.sizePolicy().hasHeightForWidth())
        self.lbl_meter.setSizePolicy(sizePolicy)
        self.lbl_meter.setObjectName("lbl_meter")
        self.gridLayout.addWidget(self.lbl_meter, 4, 2, 1, 1)
        self.lbl_power = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_power.sizePolicy().hasHeightForWidth())
        self.lbl_power.setSizePolicy(sizePolicy)
        self.lbl_power.setObjectName("lbl_power")
        self.gridLayout.addWidget(self.lbl_power, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaxCount(10)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.sb_power = QtWidgets.QSpinBox(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_power.sizePolicy().hasHeightForWidth())
        self.sb_power.setSizePolicy(sizePolicy)
        self.sb_power.setStyleSheet("background-color: rgb(153, 0, 76);")
        self.sb_power.setFrame(False)
        self.sb_power.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_power.setAccelerated(False)
        self.sb_power.setMaximum(1000)
        self.sb_power.setObjectName("sb_power")
        self.gridLayout.addWidget(self.sb_power, 0, 1, 1, 1)
        self.dsb_height = QtWidgets.QDoubleSpinBox(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_height.sizePolicy().hasHeightForWidth())
        self.dsb_height.setSizePolicy(sizePolicy)
        self.dsb_height.setStyleSheet("background-color: rgb(153, 0, 76);")
        self.dsb_height.setFrame(False)
        self.dsb_height.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dsb_height.setAccelerated(False)
        self.dsb_height.setMaximum(100.0)
        self.dsb_height.setSingleStep(0.01)
        self.dsb_height.setObjectName("dsb_height")
        self.gridLayout.addWidget(self.dsb_height, 4, 1, 1, 1)
        self.lbl_luminous = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_luminous.sizePolicy().hasHeightForWidth())
        self.lbl_luminous.setSizePolicy(sizePolicy)
        self.lbl_luminous.setObjectName("lbl_luminous")
        self.gridLayout.addWidget(self.lbl_luminous, 2, 0, 1, 1)
        self.lbl_lux = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_lux.sizePolicy().hasHeightForWidth())
        self.lbl_lux.setSizePolicy(sizePolicy)
        self.lbl_lux.setObjectName("lbl_lux")
        self.gridLayout.addWidget(self.lbl_lux, 7, 2, 1, 1)
        self.lbl_luminous_bottom = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_luminous_bottom.sizePolicy().hasHeightForWidth())
        self.lbl_luminous_bottom.setSizePolicy(sizePolicy)
        self.lbl_luminous_bottom.setObjectName("lbl_luminous_bottom")
        self.gridLayout.addWidget(self.lbl_luminous_bottom, 5, 2, 1, 1)
        self.lbl_lumi_flux_bottom = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_lumi_flux_bottom.sizePolicy().hasHeightForWidth())
        self.lbl_lumi_flux_bottom.setSizePolicy(sizePolicy)
        self.lbl_lumi_flux_bottom.setObjectName("lbl_lumi_flux_bottom")
        self.gridLayout.addWidget(self.lbl_lumi_flux_bottom, 5, 0, 1, 1)
        self.lbl_lumen = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_lumen.sizePolicy().hasHeightForWidth())
        self.lbl_lumen.setSizePolicy(sizePolicy)
        self.lbl_lumen.setObjectName("lbl_lumen")
        self.gridLayout.addWidget(self.lbl_lumen, 3, 2, 1, 1)
        self.sb_efficacy = QtWidgets.QSpinBox(self.tab_power_light)
        self.sb_efficacy.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_efficacy.sizePolicy().hasHeightForWidth())
        self.sb_efficacy.setSizePolicy(sizePolicy)
        self.sb_efficacy.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.sb_efficacy.setFrame(False)
        self.sb_efficacy.setReadOnly(False)
        self.sb_efficacy.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_efficacy.setAccelerated(False)
        self.sb_efficacy.setKeyboardTracking(False)
        self.sb_efficacy.setMaximum(999)
        self.sb_efficacy.setDisplayIntegerBase(10)
        self.sb_efficacy.setObjectName("sb_efficacy")
        self.gridLayout.addWidget(self.sb_efficacy, 2, 1, 1, 1)
        self.sb_flux = QtWidgets.QSpinBox(self.tab_power_light)
        self.sb_flux.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_flux.sizePolicy().hasHeightForWidth())
        self.sb_flux.setSizePolicy(sizePolicy)
        self.sb_flux.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.sb_flux.setFrame(False)
        self.sb_flux.setReadOnly(True)
        self.sb_flux.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_flux.setAccelerated(False)
        self.sb_flux.setKeyboardTracking(False)
        self.sb_flux.setMaximum(100000)
        self.sb_flux.setObjectName("sb_flux")
        self.gridLayout.addWidget(self.sb_flux, 3, 1, 1, 1)
        self.dsb_illuminance = QtWidgets.QDoubleSpinBox(self.tab_power_light)
        self.dsb_illuminance.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_illuminance.sizePolicy().hasHeightForWidth())
        self.dsb_illuminance.setSizePolicy(sizePolicy)
        self.dsb_illuminance.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.dsb_illuminance.setFrame(False)
        self.dsb_illuminance.setReadOnly(True)
        self.dsb_illuminance.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dsb_illuminance.setAccelerated(False)
        self.dsb_illuminance.setMaximum(100000.0)
        self.dsb_illuminance.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.dsb_illuminance.setObjectName("dsb_illuminance")
        self.gridLayout.addWidget(self.dsb_illuminance, 7, 1, 1, 1)
        self.lbl_lm_w = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_lm_w.sizePolicy().hasHeightForWidth())
        self.lbl_lm_w.setSizePolicy(sizePolicy)
        self.lbl_lm_w.setObjectName("lbl_lm_w")
        self.gridLayout.addWidget(self.lbl_lm_w, 2, 2, 1, 1)
        self.lbl_light_source = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_light_source.sizePolicy().hasHeightForWidth())
        self.lbl_light_source.setSizePolicy(sizePolicy)
        self.lbl_light_source.setObjectName("lbl_light_source")
        self.gridLayout.addWidget(self.lbl_light_source, 1, 0, 1, 1)
        self.dsb_surface_area = QtWidgets.QDoubleSpinBox(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_surface_area.sizePolicy().hasHeightForWidth())
        self.dsb_surface_area.setSizePolicy(sizePolicy)
        self.dsb_surface_area.setStyleSheet("background-color: rgb(153, 0, 76);")
        self.dsb_surface_area.setFrame(False)
        self.dsb_surface_area.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dsb_surface_area.setAccelerated(False)
        self.dsb_surface_area.setMaximum(100.0)
        self.dsb_surface_area.setSingleStep(0.01)
        self.dsb_surface_area.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.dsb_surface_area.setObjectName("dsb_surface_area")
        self.gridLayout.addWidget(self.dsb_surface_area, 6, 1, 1, 1)
        self.lbl_meter_square = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_meter_square.sizePolicy().hasHeightForWidth())
        self.lbl_meter_square.setSizePolicy(sizePolicy)
        self.lbl_meter_square.setObjectName("lbl_meter_square")
        self.gridLayout.addWidget(self.lbl_meter_square, 6, 2, 1, 1)
        self.lbl_height = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_height.sizePolicy().hasHeightForWidth())
        self.lbl_height.setSizePolicy(sizePolicy)
        self.lbl_height.setWordWrap(False)
        self.lbl_height.setObjectName("lbl_height")
        self.gridLayout.addWidget(self.lbl_height, 4, 0, 1, 1)
        self.lbl_wats = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_wats.sizePolicy().hasHeightForWidth())
        self.lbl_wats.setSizePolicy(sizePolicy)
        self.lbl_wats.setObjectName("lbl_wats")
        self.gridLayout.addWidget(self.lbl_wats, 0, 2, 1, 1)
        self.lbl_illuminance = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_illuminance.sizePolicy().hasHeightForWidth())
        self.lbl_illuminance.setSizePolicy(sizePolicy)
        self.lbl_illuminance.setObjectName("lbl_illuminance")
        self.gridLayout.addWidget(self.lbl_illuminance, 7, 0, 1, 1)
        self.dsb_illuminance_bottom = QtWidgets.QDoubleSpinBox(self.tab_power_light)
        self.dsb_illuminance_bottom.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_illuminance_bottom.sizePolicy().hasHeightForWidth())
        self.dsb_illuminance_bottom.setSizePolicy(sizePolicy)
        self.dsb_illuminance_bottom.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.dsb_illuminance_bottom.setFrame(False)
        self.dsb_illuminance_bottom.setReadOnly(True)
        self.dsb_illuminance_bottom.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dsb_illuminance_bottom.setAccelerated(False)
        self.dsb_illuminance_bottom.setMaximum(100000.0)
        self.dsb_illuminance_bottom.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.dsb_illuminance_bottom.setObjectName("dsb_illuminance_bottom")
        self.gridLayout.addWidget(self.dsb_illuminance_bottom, 8, 1, 1, 1)
        self.lbl_illuminance_bottom = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_illuminance_bottom.sizePolicy().hasHeightForWidth())
        self.lbl_illuminance_bottom.setSizePolicy(sizePolicy)
        self.lbl_illuminance_bottom.setObjectName("lbl_illuminance_bottom")
        self.gridLayout.addWidget(self.lbl_illuminance_bottom, 8, 0, 1, 1)
        self.lbl_lux_bottom = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_lux_bottom.sizePolicy().hasHeightForWidth())
        self.lbl_lux_bottom.setSizePolicy(sizePolicy)
        self.lbl_lux_bottom.setObjectName("lbl_lux_bottom")
        self.gridLayout.addWidget(self.lbl_lux_bottom, 8, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.lbl_recommendation = QtWidgets.QLabel(self.tab_power_light)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_recommendation.sizePolicy().hasHeightForWidth())
        self.lbl_recommendation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbl_recommendation.setFont(font)
        self.lbl_recommendation.setStyleSheet("color: rgb(143, 240, 164);")
        self.lbl_recommendation.setObjectName("lbl_recommendation")
        self.gridLayout_2.addWidget(self.lbl_recommendation, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_power_light, "")
        self.tab_about = QtWidgets.QWidget()
        self.tab_about.setObjectName("tab_about")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_about)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_about)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_about, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusbar.setStyleSheet("color: rgb(51, 209, 122);")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.sb_power, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.dsb_height)
        MainWindow.setTabOrder(self.dsb_height, self.dsb_surface_area)
        MainWindow.setTabOrder(self.dsb_surface_area, self.sb_flux)
        MainWindow.setTabOrder(self.sb_flux, self.sb_efficacy)
        MainWindow.setTabOrder(self.sb_efficacy, self.dsb_illuminance)
        MainWindow.setTabOrder(self.dsb_illuminance, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.dsb_flux_bottom)
        MainWindow.setTabOrder(self.dsb_flux_bottom, self.dsb_illuminance_bottom)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AquaLight Calculator"))
        self.dsb_flux_bottom.setStatusTip(_translate("MainWindow", "Result luminious flux on the bottom"))
        self.lbl_area.setText(_translate("MainWindow", "Surface area"))
        self.lbl_flux.setText(_translate("MainWindow", "Luminous flux"))
        self.lbl_meter.setText(_translate("MainWindow", "m"))
        self.lbl_power.setText(_translate("MainWindow", "Power of light"))
        self.comboBox.setStatusTip(_translate("MainWindow", "Select light source"))
        self.comboBox.setCurrentText(_translate("MainWindow", "-- select light source --"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-- select light source --"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tungsten incandescent light bulb"))
        self.comboBox.setItemText(2, _translate("MainWindow", "LED"))
        self.comboBox.setItemText(3, _translate("MainWindow", "T5"))
        self.comboBox.setItemText(4, _translate("MainWindow", "T8"))
        self.sb_power.setStatusTip(_translate("MainWindow", "Enter input power of light"))
        self.dsb_height.setStatusTip(_translate("MainWindow", "Enter height from tank bottom to light source"))
        self.lbl_luminous.setText(_translate("MainWindow", "Luminous efficacy (if you know a value, so change it)"))
        self.lbl_lux.setText(_translate("MainWindow", "lx"))
        self.lbl_luminous_bottom.setText(_translate("MainWindow", "lm"))
        self.lbl_lumi_flux_bottom.setText(_translate("MainWindow", "Luminous flux on the tank bottom"))
        self.lbl_lumen.setText(_translate("MainWindow", "lm"))
        self.sb_efficacy.setStatusTip(_translate("MainWindow", "Result luminious efficacy"))
        self.sb_flux.setStatusTip(_translate("MainWindow", "Result luminous flux"))
        self.dsb_illuminance.setStatusTip(_translate("MainWindow", "Result illuminance"))
        self.lbl_lm_w.setText(_translate("MainWindow", "lm/W"))
        self.lbl_light_source.setText(_translate("MainWindow", "Light source"))
        self.dsb_surface_area.setStatusTip(_translate("MainWindow", "Enter surface area"))
        self.lbl_meter_square.setText(_translate("MainWindow", "<html><head/><body><p>m<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.lbl_height.setText(_translate("MainWindow", "Height from tank bottom to light source"))
        self.lbl_wats.setText(_translate("MainWindow", "W"))
        self.lbl_illuminance.setText(_translate("MainWindow", "Illuminance"))
        self.dsb_illuminance_bottom.setStatusTip(_translate("MainWindow", "Result illuminance on the tank bottom"))
        self.lbl_illuminance_bottom.setText(_translate("MainWindow", "Illuminance on the tank bottom"))
        self.lbl_lux_bottom.setText(_translate("MainWindow", "lx"))
        self.lbl_recommendation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Recommendation:</span></p><p>Use a LED light with chromation in range 3500 - 6500 Kelvin.</p><p>Luminous flux should has values in range 60 - 90 lumen on the tank bottom.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_power_light), _translate("MainWindow", "I know the power of light"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
