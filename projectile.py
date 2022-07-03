from conversion import *
from log import log
from math import cos, sin

p = 1.225
g = 9.81

class Projectile:
  def __init__(self, startX, startY, launchAngle, launchAngleUnits, vMag, Cd, Ax, Ay, m):
    self.launchRad = toRadians(launchAngle, launchAngleUnits)
    self.vx0 = vMag * cos(self.launchRad)
    self.vy0 = vMag * sin(self.launchRad)
    self.startX = startX
    self.startY = startY
    self.Cd = Cd
    self.Ax = Ax
    self.Ay = Ay
    self.m = m
    self.Dx = p * Cd * Ax / 2
    self.Dy = p * Cd * Ay / 2
    log('projectile initial x-velocity will be %fm/s' % self.vx0)
    log('projectile initial y-velocity will be %fm/s' % self.vy0)

  def start(self, step: int) -> dict:
    t = 0
    vx = self.vx0
    vy = self.vy0
    ax = -(self.Dx / self.m) * vx * self.vx0
    ay = -g - (self.Dy / self.m) * vy * self.vy0
    x = self.startX
    y = self.startY

    while t == 0 or y > 0:
      ax = -(self.Dx / self.m) * vx * self.vx0
      ay = -g - (self.Dy / self.m) * vy * self.vy0
      vx += ax * step
      vy += ay * step
      x += vx * step + (ax / 2) * step ** 2
      y += vy * step + (ay / 2) * step ** 2
      t += step
      log('ay = %f' % ay)
      log('ax = %f' % ax)
      log('vx = %f' % vx)
      log('vy = %f' % vy)
      log('y(%f) = %f' % (t, y))
      log('x(%f) = %f' % (t, x))

    log('x(%f) = %f, y(%f) = %f' % (t, x, t, y))
    return { 't': t, 'ax': ax, 'ay': ay, 'vy': vy, 'vx': vx, 'x': x, 'y': y, 'step': step, 'launchRad': self.launchRad }