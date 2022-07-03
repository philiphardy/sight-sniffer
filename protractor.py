from conversion import *
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
    # print('meters =', meters)
    # print('x = ', x)
    # print('theta = ', toDegrees(theta, 'rad'))
    # print('thetaStep = ', toDegrees(thetaStep, 'rad'))

  # print('theta(%dyds) = %fdeg' % (toYards(dist, distUnits), toDegrees(theta, 'rad')))

  return theta