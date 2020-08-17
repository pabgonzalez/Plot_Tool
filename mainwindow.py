from ui.mainwindow import *
import numpy as np
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QRadioButton, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import scipy.signal as signal
from numpy import linspace, logspace, cos, sin, heaviside, log10, floor, zeros, ones

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from TFunction import TFunction
from PyQt5 import QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_PlotTool):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    ###Funciones
        self.functionList = [TFunction(), TFunction(), TFunction(), TFunction(), TFunction()]

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
        self.coefvalue.setValidator(QtGui.QDoubleValidator(-10e16, 10e16, 8, self))
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
        self.updatebtn1.clicked.connect(self.updatePlots)

    # Plot configurations
        self.axmin.setValidator(QtGui.QDoubleValidator(1e-16, 1e20, 8, self))
        self.axmax.setValidator(QtGui.QDoubleValidator(1e-16, 1e20, 8, self))
        self.aymin.setValidator(QtGui.QDoubleValidator(1e-16, 1e20, 8, self))
        self.aymax.setValidator(QtGui.QDoubleValidator(1e-16, 1e20, 8, self))
        self.fymin.setValidator(QtGui.QIntValidator(-1000, 1000, self))
        self.fymax.setValidator(QtGui.QIntValidator(-1000, 1000, self))
        self.updatebtn2.clicked.connect(self.updatePlots)

    # Amplitude Plot
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.axes1 = self.figure1.subplots()
        self.amplayout.addWidget(NavigationToolbar(self.canvas1, self))
        self.amplayout.addWidget(self.canvas1)

        self.axes1.set_xscale('log')
        self.axes1.set_yscale('log')

    # Phase Plot
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.axes2 = self.figure2.subplots()
        self.phaselayout.addWidget(NavigationToolbar(self.canvas2, self))
        self.phaselayout.addWidget(self.canvas2)

        self.axes2.set_xscale('log')

        self.updateEquationLabel()
        self.updateEquationList()
        self.updatePlots()

    ####Funciones

    ###Frame Import Function

    def importSpice(self):
        #TO-DO

        self.origin1.setText(self.functionList[0].origin)
        self.origin2.setText(self.functionList[1].origin)
        self.origin3.setText(self.functionList[2].origin)
        self.origin4.setText(self.functionList[3].origin)
        self.origin5.setText(self.functionList[4].origin)

    def importDigilent(self):
        # TO-DO

        self.origin1.setText(self.functionList[0].origin)
        self.origin2.setText(self.functionList[1].origin)
        self.origin3.setText(self.functionList[2].origin)
        self.origin4.setText(self.functionList[3].origin)
        self.origin5.setText(self.functionList[4].origin)

    def importCSV(self):
        # TO-DO

        self.origin1.setText(self.functionList[0].origin)
        self.origin2.setText(self.functionList[1].origin)
        self.origin3.setText(self.functionList[2].origin)
        self.origin4.setText(self.functionList[3].origin)
        self.origin5.setText(self.functionList[4].origin)

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
        self.numerator = self.functionList[x].num
        self.denominator = self.functionList[x].den
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
            if abs(self.numerator[i]) > 1e-20:
                coefsnum += 1
                numeratorstr = str(self.numerator[i]) + "·s" + self.exponentString(i) + "+" + numeratorstr
        for i in range(1, len(self.denominator)):
            if abs(self.denominator[i]) > 1e-20:
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
        index = 0
        index = 1 if self.transferf2.isChecked() else index
        index = 2 if self.transferf3.isChecked() else index
        index = 3 if self.transferf4.isChecked() else index
        index = 4 if self.transferf5.isChecked() else index

        nonzero = False
        for c in self.denominator:
            if abs(c) > 1e-20:
                nonzero = True

        if nonzero:
            name = QInputDialog.getText(self, 'Crear función', 'Nombre de la función:')
            if len(name) < 1:
                name = "Función " + str(index+1)
            self.functionList[index].setEquation(self.numerator, self.denominator, name)
            self.updateEquationList()
            self.checkf1.setChecked(True if self.transferf1.isChecked() else self.checkf1.isChecked())
            self.checkf2.setChecked(True if self.transferf2.isChecked() else self.checkf2.isChecked())
            self.checkf3.setChecked(True if self.transferf3.isChecked() else self.checkf3.isChecked())
            self.checkf4.setChecked(True if self.transferf4.isChecked() else self.checkf4.isChecked())
            self.checkf5.setChecked(True if self.transferf5.isChecked() else self.checkf5.isChecked())
            self.updatePlots()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("El denominador debe ser distinto de cero")
            msgBox.setWindowTitle("Advertencia")
            x = msgBox.exec()

    def updateEquationList(self):
        self.origin1.setText(self.functionList[0].origin)
        self.origin2.setText(self.functionList[1].origin)
        self.origin3.setText(self.functionList[2].origin)
        self.origin4.setText(self.functionList[3].origin)
        self.origin5.setText(self.functionList[4].origin)
        self.checkf1.setEnabled(self.functionList[0].origin != 'Vacío')
        self.checkf2.setEnabled(self.functionList[1].origin != 'Vacío')
        self.checkf3.setEnabled(self.functionList[2].origin != 'Vacío')
        self.checkf4.setEnabled(self.functionList[3].origin != 'Vacío')
        self.checkf5.setEnabled(self.functionList[4].origin != 'Vacío')
        self.checkp1.setEnabled(self.functionList[0].origin != 'Ecuación' and self.checkf1.isEnabled())
        self.checkp2.setEnabled(self.functionList[1].origin != 'Ecuación' and self.checkf2.isEnabled())
        self.checkp3.setEnabled(self.functionList[2].origin != 'Ecuación' and self.checkf3.isEnabled())
        self.checkp4.setEnabled(self.functionList[3].origin != 'Ecuación' and self.checkf4.isEnabled())
        self.checkp5.setEnabled(self.functionList[4].origin != 'Ecuación' and self.checkf5.isEnabled())

    def eraseEquation(self):
        index = 0
        index = 1 if self.transferf2.isChecked() else index
        index = 2 if self.transferf3.isChecked() else index
        index = 3 if self.transferf4.isChecked() else index
        index = 4 if self.transferf5.isChecked() else index
        self.numerator = [0]
        self.denominator = [0]
        self.functionList[index].eraseEquation()
        self.origin1.setText(self.functionList[0].origin)
        self.origin2.setText(self.functionList[1].origin)
        self.origin3.setText(self.functionList[2].origin)
        self.origin4.setText(self.functionList[3].origin)
        self.origin5.setText(self.functionList[4].origin)

    ###Frame Plots
    def updatePlots(self):
        self.axes1.clear()
        self.axes2.clear()
        fview = [self.checkf1.isChecked(), self.checkf2.isChecked(), self.checkf3.isChecked(), self.checkf4.isChecked(), self.checkf5.isChecked()]
        pview = [self.checkp1.isChecked(), self.checkp2.isChecked(), self.checkp3.isChecked(), self.checkp4.isChecked(), self.checkp5.isChecked()]
        for i in range(len(self.functionList)):
            if fview[i]:
                f = self.functionList[i]
                if f.origin == "Ecuación":
                    H = signal.TransferFunction(f.num[::-1], f.den[::-1])
                    x = logspace(floor(log10(float(self.axmin.text()))), floor(log10(float(self.axmax.text()))), num=1000)
                    Bode = signal.bode(H, x)
                    freq = Bode[0] / (2 * np.pi)
                    markerstyle = 'D' if pview[i] else ""
                    self.axes1.loglog(freq, Bode[1], label=str(f.name), marker=markerstyle)
                    self.axes2.semilogx(freq, Bode[2], label=str(f.name), marker=markerstyle)
                if f.origin == "Spice":
                    pass
                if f.origin == "Digilent":
                    pass
                if f.origin == "CSV":
                    pass

        '''if reset:
            left, right = self.axes1.xlim()
            self.axmin.setText(str(left))
            self.axmax.setText(str(right))
            left, right = self.axes1.ylim()
            self.aymin.setText(str(left))
            self.aymax.setText(str(right))
            left, right = self.axes2.xlim()
            self.fxmin.setText(str(left))
            self.fxmax.setText(str(right))
            left, right = self.axes2.ylim()
            self.fymin.setText(str(left))
            self.fymax.setText(str(right))
        else:'''
        self.axes1.set_xlim(float(self.axmin.text()), float(self.axmax.text()))
        self.axes1.set_ylim(float(self.aymin.text()), float(self.aymax.text()))
        self.axes2.set_xlim(float(self.axmin.text()), float(self.axmax.text()))
        self.axes2.set_ylim(float(self.fymin.text()), float(self.fymax.text()))

        self.axes1.set_xlabel(self.editaxlabel.text())
        self.axes1.set_ylabel(self.editaylabel.text())
        self.axes1.set_title(self.edittitle.text())
        self.axes2.set_xlabel(self.editfxlabel.text())
        self.axes2.set_ylabel(self.editfylabel.text())
        self.axes2.set_title(self.edittitle.text())

        self.axes1.grid(False, which='both')
        self.axes2.grid(False, which='both')
        if self.simplegrid.isChecked():
            self.axes1.grid(True, which='major')
            self.axes2.grid(True, which='major')
        if self.fullgrid.isChecked():
            self.axes1.grid(True, which='both')
            self.axes2.grid(True, which='both')

        self.axes1.legend()
        self.axes2.legend()
        self.canvas1.draw()
        self.canvas2.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()