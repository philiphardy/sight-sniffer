#!python
from arrow import *
from bow import *
from math import sin
from protractor import *

import matplotlib.pyplot as plt

def main():

  numPins = 4

  realPinOffsets = [3.5/16, 1/4, 3/8, 13/16]
  totalDiff = 0

  drawWeight = 51.2
  print('\nweight =', drawWeight)

  dc = 9.15
  while dc <= 9.15:
    print('drag coefficient =', dc)
    arrow = Arrow(23, 'g', 27, 'in', 7, 'mm', dc)
    bow = Bow(29, 'in', 8.25, 'in', drawWeight, 'lb')
    
    pinThetas = [findTheta((i + 2) * 10, 'yd', bow, arrow) for i in range(numPins)]
    pinOffsets = []
    realDiffs = []

    for i in range(numPins - 1):
      pinOffset = 2 * arrow.length * sin((pinThetas[i + 1] - pinThetas[i]) / 2)
      pinOffsetInches = toInches(pinOffset, 'm')
      realDiff = realPinOffsets[i] - pinOffsetInches
      realDiffs.append(realDiff)
      totalDiff += abs(realDiff)
      print('\tpinOffset%d%d = %fin\t(diffReal = %fin)' % (i + 3, i + 2, pinOffsetInches, realDiff))
      pinOffsets.append(pinOffsetInches)

    pinOffset = 2 * arrow.length * sin((pinThetas[numPins - 1] - pinThetas[0]) / 2)
    pinOffsetInches = toInches(pinOffset, 'm')
    realDiff = realPinOffsets[3] - pinOffsetInches
    realDiffs.append(realDiff)
    totalDiff += abs(realDiff)
    print('\tpinOffset52 = %fin\t(diffReal = %fin)' % (pinOffsetInches, realPinOffsets[3] - pinOffsetInches))
    pinOffsets.append(pinOffsetInches)

    print('\n\ttotalDiff = ', totalDiff)
    dc += 0.25

  # plt.style.use('_mpl-gallery')

  # x = [20, 30, 40, 50]
  # plt.scatter(x, realPinOffsets, color='red')
  # plt.scatter(x, pinOffsets, color='blue')
  # plt.show()

if __name__ == '__main__':
  main()