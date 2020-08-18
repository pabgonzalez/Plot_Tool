import numpy as np

class TFunction():
    def __init__(self):
        self.origin = "Vacío"
        self.name = "Función"
        self.num = [0]
        self.den = [0]
        # Datos obtenidos de los parsers
        self.parse_abs = []
        self.parse_phase = []
        self.parse_freq = []

    def setParsedTF(self, parse_abs, parse_phase, parse_freq, origin, name):
        self.origin = origin
        self.parse_abs = parse_abs
        self.parse_phase = parse_phase
        self.parse_freq = parse_freq
        self.name = name

    def setEquation(self, num, den, name):
        self.origin = "Ecuación"
        self.num = num.copy()
        self.den = den.copy()
        self.name = name

    def eraseEquation(self):
        if self.origin == "Ecuación":
            self.__init__()
