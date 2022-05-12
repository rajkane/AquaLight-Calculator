from AquaLightCalculator.controller import *
from AquaLightCalculator.ui.aqua_calculator_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.__actions()
        self.__calculate_flux()
        self.statusBar().showMessage("Ready")

    def __actions(self):
        self.sb_power.valueChanged.connect(self.__power)
        self.sb_power.valueChanged.connect(self.__calculate_flux)
        self.comboBox.currentIndexChanged.connect(self.__set_source)
        self.comboBox.currentIndexChanged.connect(self.__calculate_flux)
        self.sb_efficacy.valueChanged.connect(self.__luminous_efficacy)
        self.sb_efficacy.valueChanged.connect(self.__calculate_flux)
        self.sb_flux.valueChanged.connect(self.__luminous_flux)
        self.sb_flux.valueChanged.connect(self.__calculate_flux_bottom)
        self.sb_flux.valueChanged.connect(self.__calculate_iluminance)
        self.dsb_height.valueChanged.connect(self.__height)
        self.dsb_height.valueChanged.connect(self.__calculate_flux_bottom)
        self.dsb_flux_bottom.valueChanged.connect(self.__luminous_flux_bottom)
        self.dsb_flux_bottom.valueChanged.connect(self.__calculate_iluminance_bottom)
        self.dsb_surface_area.valueChanged.connect(self.__surface_area)
        self.dsb_surface_area.valueChanged.connect(self.__calculate_iluminance)
        self.dsb_surface_area.valueChanged.connect(self.__calculate_iluminance_bottom)
        self.dsb_illuminance.valueChanged.connect(self.__illuminance)
        self.dsb_illuminance_bottom.valueChanged.connect(self.__illuminance_bottom)

    def __power(self):
        if self.sb_power.value() == 0:
            self.sb_power.setStyleSheet("background-color: rgb(153, 0, 76);")
        else:
            self.sb_power.setStyleSheet("background-color: rgb(0, 102, 0);")
    
    def __luminous_efficacy(self):
        if self.sb_efficacy.value() == 0:
            self.sb_efficacy.setStyleSheet("background-color: rgb(192, 28, 40);")
        else:
            self.sb_efficacy.setStyleSheet("background-color: rgb(38, 162, 105);")

    def __luminous_flux(self):
        if self.sb_flux.value() == 0:
            self.sb_flux.setStyleSheet("background-color: rgb(192, 28, 40);")
        else:
            self.sb_flux.setStyleSheet("background-color: rgb(38, 162, 105);")

    def __height(self):
        if self.dsb_height.value() == 0:
            self.dsb_height.setStyleSheet("background-color: rgb(153, 0, 76);")
        else:
            self.dsb_height.setStyleSheet("background-color: rgb(0, 102, 0);")

    def __luminous_flux_bottom(self):
        if 60 <= self.dsb_flux_bottom.value() <= 90:
            self.dsb_flux_bottom.setStyleSheet("background-color: rgb(38, 162, 105);")
        else:
            self.dsb_flux_bottom.setStyleSheet("background-color: rgb(192, 28, 40);")

    def __surface_area(self):
        if self.dsb_surface_area.value() == 0:
            self.dsb_surface_area.setStyleSheet("background-color: rgb(153, 0, 76);")
        else:
            self.dsb_surface_area.setStyleSheet("background-color: rgb(0, 102, 0);")

    def __illuminance(self):
        if self.dsb_illuminance.value() == 0:
            self.dsb_illuminance.setStyleSheet("background-color: rgb(192, 28, 40);")
        else:
            self.dsb_illuminance.setStyleSheet("background-color: rgb(38, 162, 105);")

    def __illuminance_bottom(self):
        if self.dsb_illuminance_bottom.value() == 0:
            self.dsb_illuminance_bottom.setStyleSheet("background-color: rgb(192, 28, 40);")
        else:
            self.dsb_illuminance_bottom.setStyleSheet("background-color: rgb(38, 162, 105);")

    def __set_source(self, source):
        if source == 0:
            self.sb_efficacy.setValue(0)
        elif source == 1:
            self.sb_efficacy.setValue(14)
        elif source == 2:
            self.sb_efficacy.setValue(90)
        elif source == 3:
            self.sb_efficacy.setValue(99)
        elif source == 4:
            self.sb_efficacy.setValue(90)

    def __calculate_flux(self):
        power = self.sb_power.value()
        efficacy = self.sb_efficacy.value()
        if power != 0 and efficacy != 0:
            self.sb_flux.setValue(power * efficacy)
            # self.statusBar().showMessage(f"The flux equal {self.sb_flux.value()} lumen")
        else:
            self.sb_flux.setValue(0)
            # self.statusBar().showMessage(f"Ready")

    def __calculate_flux_bottom(self):
        flux = self.sb_flux.value()
        height = self.dsb_height.value()
        part = ((height / 0.1) + 1) * 2
        if height != 0 and part != 0:
            flux_bottom = flux / part
            self.dsb_flux_bottom.setValue(flux_bottom)
            if 60.00 <= flux_bottom <= 90.00:
                self.statusBar().showMessage(f"The light is set correctly")
            else:
                self.statusBar().showMessage(f"The flux at the bottom equal {self.dsb_flux_bottom.value()} lumen")
        else:
            self.dsb_flux_bottom.setValue(0)
            self.statusBar().showMessage(f"Ready")

    def __calculate_iluminance(self):
        flux = self.sb_flux.value()
        area = self.dsb_surface_area.value()
        if area != 0:
            self.dsb_illuminance.setValue(flux / area)
        else:
            self.dsb_illuminance.setValue(0)

    def __calculate_iluminance_bottom(self):
        flux_bottom = self.dsb_flux_bottom.value()
        area = self.dsb_surface_area.value()
        if area != 0:
            self.dsb_illuminance_bottom.setValue(round(flux_bottom / area, 2))
        else:
            self.dsb_illuminance_bottom.setValue(0)
