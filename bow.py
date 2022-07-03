from conversion import *
from math import sqrt
from projectile import Projectile

class Bow:
  def __init__(self, drawLength, drawLengthUnits, restingStringOffsetFromArrowRest, restingStringOffsetFromArrowRestUnits, drawWeight, drawWeightUnits):
    self.workOnArrow = toNewtons(drawWeight, drawWeightUnits) * (toMeters(drawLength, drawLengthUnits) - toMeters(restingStringOffsetFromArrowRest, restingStringOffsetFromArrowRestUnits))

  def launch(self, arrow, theta, thetaUnits):
    vMag = sqrt(2 * self.workOnArrow / arrow.mass)
    # print('arrow launched at %fm/s' % vMag)
    proj = Projectile(0, 0, theta, thetaUnits, vMag, arrow.Cd, arrow.Ax, arrow.Ay, arrow.mass)
    return proj.start(0.0001)
   
   