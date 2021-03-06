# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlotTool(object):
    def setupUi(self, PlotTool):
        PlotTool.setObjectName("PlotTool")
        PlotTool.resize(1280, 700)
        PlotTool.setWindowOpacity(1.0)
        PlotTool.setAutoFillBackground(False)
        PlotTool.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(PlotTool)
        self.centralwidget.setObjectName("centralwidget")
        self.frameimport = QtWidgets.QFrame(self.centralwidget)
        self.frameimport.setGeometry(QtCore.QRect(10, 10, 211, 161))
        self.frameimport.setFrameShape(QtWidgets.QFrame.Box)
        self.frameimport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameimport.setLineWidth(3)
        self.frameimport.setObjectName("frameimport")
        self.importlabel = QtWidgets.QLabel(self.frameimport)
        self.importlabel.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.importlabel.setFont(font)
        self.importlabel.setObjectName("importlabel")
        self.importf1 = QtWidgets.QRadioButton(self.frameimport)
        self.importf1.setGeometry(QtCore.QRect(10, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importf1.setFont(font)
        self.importf1.setIconSize(QtCore.QSize(16, 16))
        self.importf1.setChecked(True)
        self.importf1.setObjectName("importf1")
        self.spicebtn = QtWidgets.QPushButton(self.frameimport)
        self.spicebtn.setGeometry(QtCore.QRect(120, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spicebtn.setFont(font)
        self.spicebtn.setStyleSheet("background-color: rgb(235, 235, 235);\n"
" border-style: solid;\n"
" border-width:5px;\n"
" border-color: rgb(220, 220, 220);")
        self.spicebtn.setAutoDefault(False)
        self.spicebtn.setDefault(False)
        self.spicebtn.setFlat(False)
        self.spicebtn.setObjectName("spicebtn")
        self.importf2 = QtWidgets.QRadioButton(self.frameimport)
        self.importf2.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importf2.setFont(font)
        self.importf2.setIconSize(QtCore.QSize(16, 16))
        self.importf2.setChecked(False)
        self.importf2.setObjectName("importf2")
        self.importf3 = QtWidgets.QRadioButton(self.frameimport)
        self.importf3.setGeometry(QtCore.QRect(10, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importf3.setFont(font)
        self.importf3.setIconSize(QtCore.QSize(16, 16))
        self.importf3.setChecked(False)
        self.importf3.setObjectName("importf3")
        self.probebtn = QtWidgets.QPushButton(self.frameimport)
        self.probebtn.setGeometry(QtCore.QRect(120, 90, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.probebtn.setFont(font)
        self.probebtn.setStyleSheet("background-color: rgb(235, 235, 235);\n"
" border-style: solid;\n"
" border-width:5px;\n"
" border-color: rgb(220, 220, 220);")
        self.probebtn.setAutoDefault(False)
        self.probebtn.setDefault(False)
        self.probebtn.setFlat(False)
        self.probebtn.setObjectName("probebtn")
        self.importf4 = QtWidgets.QRadioButton(self.frameimport)
        self.importf4.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importf4.setFont(font)
        self.importf4.setIconSize(QtCore.QSize(16, 16))
        self.importf4.setChecked(False)
        self.importf4.setObjectName("importf4")
        self.importf5 = QtWidgets.QRadioButton(self.frameimport)
        self.importf5.setGeometry(QtCore.QRect(10, 130, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importf5.setFont(font)
        self.importf5.setIconSize(QtCore.QSize(16, 16))
        self.importf5.setChecked(False)
        self.importf5.setObjectName("importf5")
        self.frametransfer = QtWidgets.QFrame(self.centralwidget)
        self.frametransfer.setGeometry(QtCore.QRect(230, 10, 661, 161))
        self.frametransfer.setFrameShape(QtWidgets.QFrame.Box)
        self.frametransfer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frametransfer.setLineWidth(3)
        self.frametransfer.setObjectName("frametransfer")
        self.transferencialabel = QtWidgets.QLabel(self.frametransfer)
        self.transferencialabel.setGeometry(QtCore.QRect(10, 10, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.transferencialabel.setFont(font)
        self.transferencialabel.setLineWidth(3)
        self.transferencialabel.setObjectName("transferencialabel")
        self.line = QtWidgets.QFrame(self.frametransfer)
        self.line.setGeometry(QtCore.QRect(310, 90, 341, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.numlabel = QtWidgets.QLabel(self.frametransfer)
        self.numlabel.setGeometry(QtCore.QRect(315, 66, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        self.numlabel.setFont(font)
        self.numlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numlabel.setObjectName("numlabel")
        self.transferf1 = QtWidgets.QRadioButton(self.frametransfer)
        self.transferf1.setGeometry(QtCore.QRect(10, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transferf1.setFont(font)
        self.transferf1.setIconSize(QtCore.QSize(16, 16))
        self.transferf1.setChecked(True)
        self.transferf1.setObjectName("transferf1")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(PlotTool)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.transferf1)
        self.transferf3 = QtWidgets.QRadioButton(self.frametransfer)
        self.transferf3.setGeometry(QtCore.QRect(10, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transferf3.setFont(font)
        self.transferf3.setIconSize(QtCore.QSize(16, 16))
        self.transferf3.setChecked(False)
        self.transferf3.setObjectName("transferf3")
        self.buttonGroup_2.addButton(self.transferf3)
        self.transferf2 = QtWidgets.QRadioButton(self.frametransfer)
        self.transferf2.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transferf2.setFont(font)
        self.transferf2.setIconSize(QtCore.QSize(16, 16))
        self.transferf2.setChecked(False)
        self.transferf2.setObjectName("transferf2")
        self.buttonGroup_2.addButton(self.transferf2)
        self.denlabel = QtWidgets.QLabel(self.frametransfer)
        self.denlabel.setGeometry(QtCore.QRect(315, 106, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        self.denlabel.setFont(font)
        self.denlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.denlabel.setObjectName("denlabel")
        self.acceptequation = QtWidgets.QPushButton(self.frametransfer)
        self.acceptequation.setGeometry(QtCore.QRect(310, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acceptequation.setFont(font)
        self.acceptequation.setStyleSheet("background-color: rgb(235, 235, 235);\n"
" border-style: solid;\n"
" border-width:5px;\n"
" border-color: rgb(220, 220, 220);")
        self.acceptequation.setAutoDefault(False)
        self.acceptequation.setDefault(False)
        self.acceptequation.setFlat(False)
        self.acceptequation.setObjectName("acceptequation")
        self.eraseequation = QtWidgets.QPushButton(self.frametransfer)
        self.eraseequation.setGeometry(QtCore.QRect(580, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eraseequation.setFont(font)
        self.eraseequation.setStyleSheet("background-color: rgb(235, 235, 235);\n"
" border-style: solid;\n"
" border-width:5px;\n"
" border-color: rgb(220, 220, 220);")
        self.eraseequation.setAutoDefault(False)
        self.eraseequation.setDefault(False)
        self.eraseequation.setFlat(False)
        self.eraseequation.setObjectName("eraseequation")
        self.transferf4 = QtWidgets.QRadioButton(self.frametransfer)
        self.transferf4.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transferf4.setFont(font)
        self.transferf4.setIconSize(QtCore.QSize(16, 16))
        self.transferf4.setChecked(False)
        self.transferf4.setObjectName("transferf4")
        self.buttonGroup_2.addButton(self.transferf4)
        self.transferf5 = QtWidgets.QRadioButton(self.frametransfer)
        self.transferf5.setGeometry(QtCore.QRect(10, 130, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transferf5.setFont(font)
        self.transferf5.setIconSize(QtCore.QSize(16, 16))
        self.transferf5.setChecked(False)
        self.transferf5.setObjectName("transferf5")
        self.buttonGroup_2.addButton(self.transferf5)
        self.label = QtWidgets.QLabel(self.frametransfer)
        self.label.setGeometry(QtCore.QRect(130, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frametransfer)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.addcoefficient = QtWidgets.QPushButton(self.frametransfer)
        self.addcoefficient.setGeometry(QtCore.QRect(120, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addcoefficient.setFont(font)
        self.addcoefficient.setStyleSheet("background-color: rgb(235, 235, 235);\n"
" border-style: solid;\n"
" border-width:5px;\n"
" border-color: rgb(220, 220, 220);")
        self.addcoefficient.setAutoDefault(False)
        self.addcoefficient.setDefault(False)
        self.addcoefficient.setFlat(False)
        self.addcoefficient.setObjectName("addcoefficient")
        self.coeforder = QtWidgets.QLineEdit(self.frametransfer)
        self.coeforder.setGeometry(QtCore.QRect(130, 70, 51, 31))
        self.coeforder.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.coeforder.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.coeforder.setAlignment(QtCore.Qt.AlignCenter)
        self.coeforder.setObjectName("coeforder")
        self.coefvalue = QtWidgets.QLineEdit(self.frametransfer)
        self.coefvalue.setGeometry(QtCore.QRect(190, 70, 81, 31))
        self.coefvalue.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.coefvalue.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.coefvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.coefvalue.setObjectName("coefvalue")
        self.checknumerator = QtWidgets.QRadioButton(self.frametransfer)
        self.checknumerator.setGeometry(QtCore.QRect(210, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checknumerator.setFont(font)
        self.checknumerator.setIconSize(QtCore.QSize(16, 16))
        self.checknumerator.setChecked(True)
        self.checknumerator.setObjectName("checknumerator")
        self.buttonGroup = QtWidgets.QButtonGroup(PlotTool)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checknumerator)
        self.checkdenominator = QtWidgets.QRadioButton(self.frametransfer)
        self.checkdenominator.setGeometry(QtCore.QRect(210, 130, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkdenominator.setFont(font)
        self.checkdenominator.setIconSize(QtCore.QSize(16, 16))
        self.checkdenominator.setChecked(False)
        self.checkdenominator.setObjectName("checkdenominator")
        self.buttonGroup.addButton(self.checkdenominator)
        self.frameplotconfig = QtWidgets.QFrame(self.centralwidget)
        self.frameplotconfig.setGeometry(QtCore.QRect(900, 10, 371, 161))
        self.frameplotconfig.setFrameShape(QtWidgets.QFrame.Box)
        self.frameplotconfig.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameplotconfig.setLineWidth(3)
        self.frameplotconfig.setObjectName("frameplotconfig")
        self.plotlabel = QtWidgets.QLabel(self.frameplotconfig)
        self.plotlabel.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.plotlabel.setFont(font)
        self.plotlabel.setObjectName("plotlabel")
        self.checkf5 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkf5.setEnabled(False)
        self.checkf5.setGeometry(QtCore.QRect(20, 130, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkf5.setFont(font)
        self.checkf5.setObjectName("checkf5")
        self.checkf3 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkf3.setEnabled(False)
        self.checkf3.setGeometry(QtCore.QRect(20, 90, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkf3.setFont(font)
        self.checkf3.setObjectName("checkf3")
        self.checkf1 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkf1.setEnabled(False)
        self.checkf1.setGeometry(QtCore.QRect(20, 50, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkf1.setFont(font)
        self.checkf1.setCheckable(True)
        self.checkf1.setObjectName("checkf1")
        self.checkf4 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkf4.setEnabled(False)
        self.checkf4.setGeometry(QtCore.QRect(20, 110, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkf4.setFont(font)
        self.checkf4.setObjectName("checkf4")
        self.checkf2 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkf2.setEnabled(False)
        self.checkf2.setGeometry(QtCore.QRect(20, 70, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkf2.setFont(font)
        self.checkf2.setObjectName("checkf2")
        self.pointslabel = QtWidgets.QLabel(self.frameplotconfig)
        self.pointslabel.setGeometry(QtCore.QRect(140, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.pointslabel.setFont(font)
        self.pointslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pointslabel.setObjectName("pointslabel")
        self.checkp1 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkp1.setEnabled(False)
        self.checkp1.setGeometry(QtCore.QRect(160, 50, 16, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkp1.setFont(font)
        self.checkp1.setText("")
        self.checkp1.setObjectName("checkp1")
        self.checkp2 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkp2.setEnabled(False)
        self.checkp2.setGeometry(QtCore.QRect(160, 70, 16, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkp2.setFont(font)
        self.checkp2.setText("")
        self.checkp2.setObjectName("checkp2")
        self.checkp3 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkp3.setEnabled(False)
        self.checkp3.setGeometry(QtCore.QRect(160, 90, 16, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkp3.setFont(font)
        self.checkp3.setText("")
        self.checkp3.setObjectName("checkp3")
        self.checkp4 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkp4.setEnabled(False)
        self.checkp4.setGeometry(QtCore.QRect(160, 110, 16, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkp4.setFont(font)
        self.checkp4.setText("")
        self.checkp4.setObjectName("checkp4")
        self.checkp5 = QtWidgets.QCheckBox(self.frameplotconfig)
        self.checkp5.setEnabled(False)
        self.checkp5.setGeometry(QtCore.QRect(160, 130, 16, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkp5.setFont(font)
        self.checkp5.setText("")
        self.checkp5.setObjectName("checkp5")
        self.originlabel = QtWidgets.QLabel(self.frameplotconfig)
        self.originlabel.setGeometry(QtCore.QRect(200, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.originlabel.setFont(font)
        self.originlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.originlabel.setObjectName("originlabel")
        self.origin1 = QtWidgets.QLabel(self.frameplotconfig)
        self.origin1.setGeometry(QtCore.QRect(200, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.origin1.setFont(font)
        self.origin1.setAlignment(QtCore.Qt.AlignCenter)
        self.origin1.setObjectName("origin1")
        self.origin2 = QtWidgets.QLabel(self.frameplotconfig)
        self.origin2.setGeometry(QtCore.QRect(200, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.origin2.setFont(font)
        self.origin2.setAlignment(QtCore.Qt.AlignCenter)
        self.origin2.setObjectName("origin2")
        self.origin3 = QtWidgets.QLabel(self.frameplotconfig)
        self.origin3.setGeometry(QtCore.QRect(200, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.origin3.setFont(font)
        self.origin3.setAlignment(QtCore.Qt.AlignCenter)
        self.origin3.setObjectName("origin3")
        self.origin4 = QtWidgets.QLabel(self.frameplotconfig)
        self.origin4.setGeometry(QtCore.QRect(200, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.origin4.setFont(font)
        self.origin4.setAlignment(QtCore.Qt.AlignCenter)
        self.origin4.setObjectName("origin4")
        self.origin5 = QtWidgets.QLabel(self.frameplotconfig)
        self.origin5.setGeometry(QtCore.QRect(200, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.origin5.setFont(font)
        self.origin5.setAlignment(QtCore.Qt.AlignCenter)
        self.origin5.setObjectName("origin5")
        self.nogrid = QtWidgets.QRadioButton(self.frameplotconfig)
        self.nogrid.setGeometry(QtCore.QRect(280, 50, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nogrid.setFont(font)
        self.nogrid.setChecked(False)
        self.nogrid.setObjectName("nogrid")
        self.simplegrid = QtWidgets.QRadioButton(self.frameplotconfig)
        self.simplegrid.setGeometry(QtCore.QRect(280, 70, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.simplegrid.setFont(font)
        self.simplegrid.setChecked(False)
        self.simplegrid.setObjectName("simplegrid")
        self.fullgrid = QtWidgets.QRadioButton(self.frameplotconfig)
        self.fullgrid.setGeometry(QtCore.QRect(280, 90, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fullgrid.setFont(font)
        self.fullgrid.setChecked(True)
        self.fullgrid.setObjectName("fullgrid")
        self.originlabel_2 = QtWidgets.QLabel(self.frameplotconfig)
        self.originlabel_2.setGeometry(QtCore.QRect(290, 30, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.originlabel_2.setFont(font)
        self.originlabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.originlabel_2.setObjectName("originlabel_2")
        self.updatebtn1 = QtWidgets.QPushButton(self.frameplotconfig)
        self.updatebtn1.setGeometry(QtCore.QRect(280, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.updatebtn1.setFont(font)
        self.updatebtn1.setStyleSheet("background-color: rgb(235, 235, 235);\n"
" border-style: solid;\n"
" border-width:5px;\n"
" border-color: rgb(220, 220, 220);")
        self.updatebtn1.setAutoDefault(False)
        self.updatebtn1.setDefault(False)
        self.updatebtn1.setFlat(False)
        self.updatebtn1.setObjectName("updatebtn1")
        self.frameplot = QtWidgets.QFrame(self.centralwidget)
        self.frameplot.setGeometry(QtCore.QRect(10, 180, 1261, 511))
        self.frameplot.setFrameShape(QtWidgets.QFrame.Box)
        self.frameplot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameplot.setLineWidth(3)
        self.frameplot.setObjectName("frameplot")
        self.frameplotsetup = QtWidgets.QFrame(self.frameplot)
        self.frameplotsetup.setGeometry(QtCore.QRect(1160, 10, 91, 491))
        self.frameplotsetup.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameplotsetup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameplotsetup.setLineWidth(2)
        self.frameplotsetup.setObjectName("frameplotsetup")
        self.editaylabel = QtWidgets.QLineEdit(self.frameplotsetup)
        self.editaylabel.setGeometry(QtCore.QRect(10, 322, 81, 20))
        self.editaylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editaylabel.setObjectName("editaylabel")
        self.editaxlabel = QtWidgets.QLineEdit(self.frameplotsetup)
        self.editaxlabel.setGeometry(QtCore.QRect(10, 272, 81, 20))
        self.editaxlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editaxlabel.setObjectName("editaxlabel")
        self.fxlabel = QtWidgets.QLabel(self.frameplotsetup)
        self.fxlabel.setGeometry(QtCore.QRect(10, 350, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.fxlabel.setFont(font)
        self.fxlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fxlabel.setObjectName("fxlabel")
        self.aylabel = QtWidgets.QLabel(self.frameplotsetup)
        self.aylabel.setGeometry(QtCore.QRect(10, 300, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.aylabel.setFont(font)
        self.aylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.aylabel.setObjectName("aylabel")
        self.axlabel = QtWidgets.QLabel(self.frameplotsetup)
        self.axlabel.setGeometry(QtCore.QRect(10, 250, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.axlabel.setFont(font)
        self.axlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.axlabel.setObjectName("axlabel")
        self.editfylabel = QtWidgets.QLineEdit(self.frameplotsetup)
        self.editfylabel.setGeometry(QtCore.QRect(10, 422, 81, 20))
        self.editfylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editfylabel.setObjectName("editfylabel")
        self.editfxlabel = QtWidgets.QLineEdit(self.frameplotsetup)
        self.editfxlabel.setGeometry(QtCore.QRect(10, 372, 81, 20))
        self.editfxlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editfxlabel.setObjectName("editfxlabel")
        self.fylabel = QtWidgets.QLabel(self.frameplotsetup)
        self.fylabel.setGeometry(QtCore.QRect(10, 400, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.fylabel.setFont(font)
        self.fylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fylabel.setObjectName("fylabel")
        self.titlelabel = QtWidgets.QLabel(self.frameplotsetup)
        self.titlelabel.setGeometry(QtCore.QRect(10, 200, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.titlelabel.setFont(font)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setObjectName("titlelabel")
        self.edittitle = QtWidgets.QLineEdit(self.frameplotsetup)
        self.edittitle.setGeometry(QtCore.QRect(10, 222, 81, 20))
        self.edittitle.setText("")
        self.edittitle.setAlignment(QtCore.Qt.AlignCenter)
        self.edittitle.setObjectName("edittitle")
        self.updatebtn2 = QtWidgets.QPushButton(self.frameplotsetup)
        self.updatebtn2.setGeometry(QtCore.QRect(10, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.updatebtn2.setFont(font)
        self.updatebtn2.setStyleSheet("background-color: rgb(235, 235, 235);\n"
" border-style: solid;\n"
" border-width:5px;\n"
" border-color: rgb(220, 220, 220);")
        self.updatebtn2.setAutoDefault(False)
        self.updatebtn2.setDefault(False)
        self.updatebtn2.setFlat(False)
        self.updatebtn2.setObjectName("updatebtn2")
        self.fymin = QtWidgets.QLineEdit(self.frameplotsetup)
        self.fymin.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.fymin.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.fymin.setAlignment(QtCore.Qt.AlignCenter)
        self.fymin.setObjectName("fymin")
        self.aymin = QtWidgets.QLineEdit(self.frameplotsetup)
        self.aymin.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.aymin.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.aymin.setAlignment(QtCore.Qt.AlignCenter)
        self.aymin.setObjectName("aymin")
        self.aymax = QtWidgets.QLineEdit(self.frameplotsetup)
        self.aymax.setGeometry(QtCore.QRect(50, 20, 41, 21))
        self.aymax.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.aymax.setAlignment(QtCore.Qt.AlignCenter)
        self.aymax.setObjectName("aymax")
        self.fymax = QtWidgets.QLineEdit(self.frameplotsetup)
        self.fymax.setGeometry(QtCore.QRect(50, 70, 41, 21))
        self.fymax.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.fymax.setAlignment(QtCore.Qt.AlignCenter)
        self.fymax.setObjectName("fymax")
        self.fyrangelabel = QtWidgets.QLabel(self.frameplotsetup)
        self.fyrangelabel.setGeometry(QtCore.QRect(10, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.fyrangelabel.setFont(font)
        self.fyrangelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fyrangelabel.setObjectName("fyrangelabel")
        self.ayrangelabel = QtWidgets.QLabel(self.frameplotsetup)
        self.ayrangelabel.setGeometry(QtCore.QRect(10, 0, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.ayrangelabel.setFont(font)
        self.ayrangelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ayrangelabel.setObjectName("ayrangelabel")
        self.checkhertz = QtWidgets.QRadioButton(self.frameplotsetup)
        self.checkhertz.setGeometry(QtCore.QRect(10, 150, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkhertz.setFont(font)
        self.checkhertz.setChecked(True)
        self.checkhertz.setObjectName("checkhertz")
        self.axmax = QtWidgets.QLineEdit(self.frameplotsetup)
        self.axmax.setGeometry(QtCore.QRect(50, 120, 41, 21))
        self.axmax.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.axmax.setAlignment(QtCore.Qt.AlignCenter)
        self.axmax.setObjectName("axmax")
        self.axrangelabel = QtWidgets.QLabel(self.frameplotsetup)
        self.axrangelabel.setGeometry(QtCore.QRect(10, 100, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.axrangelabel.setFont(font)
        self.axrangelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.axrangelabel.setObjectName("axrangelabel")
        self.checkrad = QtWidgets.QRadioButton(self.frameplotsetup)
        self.checkrad.setGeometry(QtCore.QRect(10, 170, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkrad.setFont(font)
        self.checkrad.setObjectName("checkrad")
        self.axmin = QtWidgets.QLineEdit(self.frameplotsetup)
        self.axmin.setGeometry(QtCore.QRect(10, 120, 41, 21))
        self.axmin.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.axmin.setAlignment(QtCore.Qt.AlignCenter)
        self.axmin.setObjectName("axmin")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frameplot)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.amplayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.amplayout.setContentsMargins(0, 0, 0, 0)
        self.amplayout.setObjectName("amplayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frameplot)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 10, 561, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.phaselayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.phaselayout.setContentsMargins(0, 0, 0, 0)
        self.phaselayout.setObjectName("phaselayout")
        self.frametransfer.raise_()
        self.frameimport.raise_()
        self.frameplot.raise_()
        self.frameplotconfig.raise_()
        PlotTool.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotTool)
        QtCore.QMetaObject.connectSlotsByName(PlotTool)

    def retranslateUi(self, PlotTool):
        _translate = QtCore.QCoreApplication.translate
        PlotTool.setWindowTitle(_translate("PlotTool", "Plot Tool"))
        self.importlabel.setText(_translate("PlotTool", "Importar Datos"))
        self.importf1.setText(_translate("PlotTool", "Función 1"))
        self.spicebtn.setText(_translate("PlotTool", "SPICE"))
        self.importf2.setText(_translate("PlotTool", "Función 2"))
        self.importf3.setText(_translate("PlotTool", "Función 3"))
        self.probebtn.setText(_translate("PlotTool", "Scope\n"
"CSV"))
        self.importf4.setText(_translate("PlotTool", "Función 4"))
        self.importf5.setText(_translate("PlotTool", "Función 5"))
        self.transferencialabel.setText(_translate("PlotTool", "Ecuación de Transferencia"))
        self.numlabel.setText(_translate("PlotTool", "0.0"))
        self.transferf1.setText(_translate("PlotTool", "Función 1"))
        self.transferf3.setText(_translate("PlotTool", "Función 3"))
        self.transferf2.setText(_translate("PlotTool", "Función 2"))
        self.denlabel.setText(_translate("PlotTool", "0.0"))
        self.acceptequation.setText(_translate("PlotTool", "Aceptar"))
        self.eraseequation.setText(_translate("PlotTool", "Borrar"))
        self.transferf4.setText(_translate("PlotTool", "Función 4"))
        self.transferf5.setText(_translate("PlotTool", "Función 5"))
        self.label.setText(_translate("PlotTool", "Orden"))
        self.label_2.setText(_translate("PlotTool", "Valor"))
        self.addcoefficient.setText(_translate("PlotTool", "Agregar"))
        self.coeforder.setText(_translate("PlotTool", "0"))
        self.coefvalue.setText(_translate("PlotTool", "0"))
        self.checknumerator.setText(_translate("PlotTool", "Numer."))
        self.checkdenominator.setText(_translate("PlotTool", "Denom."))
        self.plotlabel.setText(_translate("PlotTool", "Visualización"))
        self.checkf5.setText(_translate("PlotTool", "Ver Función 5"))
        self.checkf3.setText(_translate("PlotTool", "Ver Función 3"))
        self.checkf1.setText(_translate("PlotTool", "Ver Función 1"))
        self.checkf4.setText(_translate("PlotTool", "Ver Función 4"))
        self.checkf2.setText(_translate("PlotTool", "Ver Función 2"))
        self.pointslabel.setText(_translate("PlotTool", "Puntos"))
        self.originlabel.setText(_translate("PlotTool", "Origen"))
        self.origin1.setText(_translate("PlotTool", "Vacío"))
        self.origin2.setText(_translate("PlotTool", "Vacío"))
        self.origin3.setText(_translate("PlotTool", "Vacío"))
        self.origin4.setText(_translate("PlotTool", "Vacío"))
        self.origin5.setText(_translate("PlotTool", "Vacío"))
        self.nogrid.setText(_translate("PlotTool", "Nada"))
        self.simplegrid.setText(_translate("PlotTool", "Simple"))
        self.fullgrid.setText(_translate("PlotTool", "Completa"))
        self.originlabel_2.setText(_translate("PlotTool", "Grilla"))
        self.updatebtn1.setText(_translate("PlotTool", "Actualizar"))
        self.editaylabel.setText(_translate("PlotTool", "|H(s)| dB"))
        self.editaxlabel.setText(_translate("PlotTool", "f [Hz]"))
        self.fxlabel.setText(_translate("PlotTool", "Fase x label"))
        self.aylabel.setText(_translate("PlotTool", "Amp. y label"))
        self.axlabel.setText(_translate("PlotTool", "Amp. x label"))
        self.editfylabel.setText(_translate("PlotTool", "Grados"))
        self.editfxlabel.setText(_translate("PlotTool", "f [Hz]"))
        self.fylabel.setText(_translate("PlotTool", "Fase y label"))
        self.titlelabel.setText(_translate("PlotTool", "Título"))
        self.updatebtn2.setText(_translate("PlotTool", "Actualizar"))
        self.fymin.setText(_translate("PlotTool", "-200"))
        self.aymin.setText(_translate("PlotTool", "-200"))
        self.aymax.setText(_translate("PlotTool", "200"))
        self.fymax.setText(_translate("PlotTool", "200"))
        self.fyrangelabel.setText(_translate("PlotTool", "Rango fase"))
        self.ayrangelabel.setText(_translate("PlotTool", "Rango amp."))
        self.checkhertz.setText(_translate("PlotTool", "Hertz"))
        self.axmax.setText(_translate("PlotTool", "1e6"))
        self.axrangelabel.setText(_translate("PlotTool", "Rango frec."))
        self.checkrad.setText(_translate("PlotTool", "Rad / seg"))
        self.axmin.setText(_translate("PlotTool", "1e0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotTool = QtWidgets.QMainWindow()
    ui = Ui_PlotTool()
    ui.setupUi(PlotTool)
    PlotTool.show()
    sys.exit(app.exec_())
