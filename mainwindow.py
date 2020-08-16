from ui.mainwindow import *
import numpy as np
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import scipy.signal as signal
from numpy import linspace, logspace, cos, sin, heaviside, log10, floor, zeros, ones

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from TFunction import TFunction
from PyQt5 import QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    ###Funciones
        functionList = [TFunction() for x in range(5)]

    ###Frame Import Function
        #Variables
        self.selectedImportFunction = 0

        # Clickeables
        self.spicebtn.clicked.connect(self.importSpice)
        self.digilentbtn.clicked.connect(self.importDigilent)
        self.probebtn.clicked.connect(self.importCSV)
        self.importf1.clicked.connect(lambda: self.selectImportFunction(0))
        self.importf2.clicked.connect(lambda: self.selectImportFunction(1))
        self.importf3.clicked.connect(lambda: self.selectImportFunction(2))
        self.importf4.clicked.connect(lambda: self.selectImportFunction(3))
        self.importf5.clicked.connect(lambda: self.selectImportFunction(4))

    ###Frame Transfer Function
        #Variables
        self.selectedTransferFunction = 0
        self.numerator = [0.0]
        self.denominator = [0.0]
        self.updateEquationLabel()

        #Validación de coeficiente
        self.coefvalue.setValidator(QtGui.QDoubleValidator(-10e12, 10e12, 8, self))
        self.coeforder.setValidator(QtGui.QIntValidator(0, 100, self))

        #Clickeables
        self.addcoefficient.clicked.connect(self.addCoefficient)
        self.acceptequation.clicked.connect(self.acceptEquation)
        self.eraseequation.clicked.connect(self.eraseEquation)
        self.transferf1.clicked.connect(lambda: self.selectTransferFunction(0))
        self.transferf2.clicked.connect(lambda: self.selectTransferFunction(1))
        self.transferf3.clicked.connect(lambda: self.selectTransferFunction(2))
        self.transferf4.clicked.connect(lambda: self.selectTransferFunction(3))
        self.transferf5.clicked.connect(lambda: self.selectTransferFunction(4))
        self.checknumerator.clicked.connect(self.selectNumerator)
        self.checkdenominator.clicked.connect(self.selectDenominator)
        self.transferf1.setChecked(True)
        self.checknumerator.setChecked(True)

    ###Frame Visualización
        # Variables
        self.viewFunctions = (False, False, False, False, False)
        self.viewPoints = (False, False, False, False, False)

        # Clickeables
        self.saveamp.clicked.connect(self.saveAmplitudePlot)
        self.savephase.clicked.connect(self.savePhasePlot)
        self.saveboth.clicked.connect(self.saveFullPlot)
        self.checkf1.clicked.connect(self.updatePlots)
        self.checkf2.clicked.connect(self.updatePlots)
        self.checkf3.clicked.connect(self.updatePlots)
        self.checkf4.clicked.connect(self.updatePlots)
        self.checkf5.clicked.connect(self.updatePlots)
        self.checkp1.clicked.connect(self.updatePlots)
        self.checkp2.clicked.connect(self.updatePlots)
        self.checkp3.clicked.connect(self.updatePlots)
        self.checkp4.clicked.connect(self.updatePlots)
        self.checkp5.clicked.connect(self.updatePlots)

    # Amplitude Plot
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.axes1 = self.figure1.add_subplot()
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout1.addWidget(self.toolbar1)
        self.layout1.addWidget(self.canvas1)
        canvas_index1 = self.ampplot.addWidget(self.canvas1)
        self.ampplot.setCurrentIndex(canvas_index1)

    # Phase Plot
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.axes2 = self.figure2.add_subplot()
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.layout2 = QtWidgets.QVBoxLayout()
        self.layout2.addWidget(self.toolbar2)
        self.layout2.addWidget(self.canvas2)
        canvas_index2 = self.phaseplot.addWidget(self.canvas2)
        self.phaseplot.setCurrentIndex(canvas_index2)

    ####Funciones

    ###Frame Import Function

    def importSpice(self):
        #TO-DO
        return

    def importDigilent(self):
        # TO-DO
        return

    def importCSV(self):
        # TO-DO
        return

    def selectImportFunction(self, x):
        self.importf1.setChecked( x==0 )
        self.importf2.setChecked( x==1 )
        self.importf3.setChecked( x==2 )
        self.importf4.setChecked( x==3 )
        self.importf5.setChecked( x==4 )

    ###Frame Transfer Function

    def selectTransferFunction(self, x):
        self.transferf1.setChecked( x==0 )
        self.transferf2.setChecked( x==1 )
        self.transferf3.setChecked( x==2 )
        self.transferf4.setChecked( x==3 )
        self.transferf5.setChecked( x==4 )
        self.updateEquationLabel()

    def selectNumerator(self):
        self.checknumerator.setChecked(True)
        self.checkdenominator.setChecked(False)

    def selectDenominator(self):
        self.checknumerator.setChecked(False)
        self.checkdenominator.setChecked(True)

    def addCoefficient(self):
        order = int(self.coeforder.text())
        value = float(self.coefvalue.text())
        if self.checknumerator.isChecked():
            while len(self.numerator) <= order:
                self.numerator.append(0)
            self.numerator[order] = value
        else:
            while len(self.denominator) <= order:
                self.denominator.append(0)
            self.denominator[order] = value
        self.updateEquationLabel()

    def updateEquationLabel(self):
        numeratorstr = str(self.numerator[0])
        denominatorstr = str(self.denominator[0])

        coefsnum = 1
        coefsden = 1

        for i in range(1, len(self.numerator)):
            if abs(self.numerator[i]) > 1e-10:
                coefsnum += 1
                numeratorstr = str(self.numerator[i]) + "·s" + self.exponentString(i) + "+" + numeratorstr
        for i in range(1, len(self.denominator)):
            if abs(self.denominator[i]) > 1e-10:
                coefsden += 1
                denominatorstr = str(self.denominator[i]) + "·s" + self.exponentString(i) + " + " + denominatorstr
        self.numlabel.setText(numeratorstr)
        self.denlabel.setText(denominatorstr)

        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        if len(self.numlabel.text()) >= 40:
            font.setPointSize(13 - len(self.numlabel.text())//8)
        self.numlabel.setFont(font)
        font.setPointSize(10)
        if len(self.denlabel.text()) >= 40:
            font.setPointSize(13 - len(self.denlabel.text()) // 8)
        self.denlabel.setFont(font)

    def exponentString(self, x):
        exponents = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
        x = int(x)
        expstr = exponents[x % 10]
        x = int(floor(x/10))
        while x >= 1:
            expstr = exponents[x % 10] + expstr
            x = int(floor(x/10))
        return expstr

    def acceptEquation(self):
        # TO-DO
        return

    def eraseEquation(self):
        # TO-DO
        return

    ###Frame Plots
    def saveAmplitudePlot(self):
        # TO-DO
        return
    def savePhasePlot(self):
        # TO-DO
        return
    def saveFullPlot(self):
        # TO-DO
        return
    def updatePlots(self):
        # TO-DO
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()