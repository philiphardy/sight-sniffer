from conversion import *
from math import pi

class Arrow:
  def __init__(self, weight, weightUnits, length, lengthUnits, diameter, diameterUnits, Cd):
    self.mass = toKilograms(weight, weightUnits)
    self.length = toMeters(length, lengthUnits)
    self.Ax = pi * (toMeters(diameter, diameterUnits) / 2) ** 2
    self.Ay = toMeters(diameter, diameterUnits) * self.length
    self.Cd = Cd