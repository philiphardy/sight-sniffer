from conversion import *
from log import log
from math import pi

def findTheta(dist, distUnits, bow, arrow, startTheta=0, startThetaUnits='deg'):
  meters = toMeters(dist, distUnits)
  theta = toRadians(startTheta, startThetaUnits)
  thetaStep = toRadians(1, 'deg')

  projection = bow.launch(arrow, theta, 'rad')
  x = projection['x']

  accuracy = 0.01

  while abs(x - meters) > accuracy:
    if x == meters:
      break
    elif x > meters:
      theta -= thetaStep
      thetaStep /= 2

    theta += thetaStep
    projection = bow.launch(arrow, theta, 'rad')
    x = projection['x']
    log('meters =', meters)
    log('x = ', x)
    log('theta = ', toDegrees(theta, 'rad'))
    log('thetaStep = ', toDegrees(thetaStep, 'rad'))

  log('theta(%dyds) = %fdeg' % (toYards(dist, distUnits), toDegrees(theta, 'rad')))

  return theta