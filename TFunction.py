import numpy as np

class TFunction():
    def __init__(self):
        self.origin = "Vacío"
        self.name = "Función"
        self.num = [0]
        self.den = [0]
        self.data = 0

    def setEquation(self, num, den, name):
        self.origin = "Ecuación"
        self.num = num.copy()
        self.den = den.copy()
        self.name = name

    def eraseEquation(self):
        if self.origin == "Ecuación":
            self.__init__()
