#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
import ftrobopy
from TxtStyle import *

class FtcGuiApplication(TxtApplication):
    def __init__(self, args):
        TxtApplication.__init__(self, args)

        # create the empty main window
        self.w = TxtWindow("Temperature")
        layout = QVBoxLayout()
        
        self.lblResistance = QLabel("Resistance (Ohm):")
        layout.addWidget(self.lblResistance)
        
        self.qlcdResistance = QLCDNumber()
        layout.addWidget(self.qlcdResistance)

        self.lblTemperatureC = QLabel("Temperature (°C):")
        layout.addWidget(self.lblTemperatureC)
        
        self.qlcdTemperatureC = QLCDNumber()
        self.qlcdTemperatureC.setSmallDecimalPoint(True)
        layout.addWidget(self.qlcdTemperatureC)
        
        self.lblTemperatureF = QLabel("Temperature (°F):")
        layout.addWidget(self.lblTemperatureF)
        
        self.qlcdTemperatureF = QLCDNumber()
        self.qlcdTemperatureF.setSmallDecimalPoint(True)
        layout.addWidget(self.qlcdTemperatureF)        
        
        self.w.centralWidget.setLayout(layout)
        
        self.txt=ftrobopy.ftrobopy('auto')
        M = [ self.txt.C_MOTOR, self.txt.C_MOTOR, self.txt.C_OUTPUT, self.txt.C_OUTPUT ]
        I = [ (self.txt.C_RESISTOR, self.txt.C_ANALOG ),
              (self.txt.C_SWITCH, self.txt.C_DIGITAL ),
              (self.txt.C_SWITCH, self.txt.C_DIGITAL ),
              (self.txt.C_SWITCH, self.txt.C_DIGITAL ),
              (self.txt.C_SWITCH, self.txt.C_DIGITAL ),
              (self.txt.C_SWITCH, self.txt.C_DIGITAL ),
              (self.txt.C_SWITCH, self.txt.C_DIGITAL ),
              (self.txt.C_SWITCH, self.txt.C_DIGITAL ) ]
        self.txt.setConfig(M, I)
        self.txt.updateConfig()
        
        self.ntcResistor = self.txt.resistor(1)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTemperature)
        self.timer.start(250)
        
        self.w.show()
        self.exec_()
        
    def updateTemperature(self):          
        self.qlcdResistance.display(self.ntcResistor.value())
        tempC=self.ntcResistor.ntcTemperature()
        tempF=tempC * 1.8 + 32
        self.qlcdTemperatureC.display(tempC)  
        self.qlcdTemperatureF.display(tempF)          

        
if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
