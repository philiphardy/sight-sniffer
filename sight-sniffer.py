#!python
from arrow import *
from bow import *
from math import sin
from protractor import *

import matplotlib.pyplot as plt

def main():

  numPins = 4

  realPinOffsets = { 
    '32': 3.5/16, 
    '43': 1/4, 
    '54': 3/8, 
    '52': 13/16
  }
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
      pinOffsets.append(pinOffsetInches)

      pinKey = str(i+3) + str(i + 2)
      if pinKey in realPinOffsets:
        realDiff = realPinOffsets[pinKey] - pinOffsetInches
        realDiffs.append(realDiff)
        totalDiff += abs(realDiff)
        print('\tpinOffset%d%d = %fin\t(diffReal = %fin)' % (i + 3, i + 2, pinOffsetInches, realDiff))
      else:
        print('\tpinOffset%d%d = %fin' % (i + 3, i + 2, pinOffsetInches))

    pinOffset = 2 * arrow.length * sin((pinThetas[3] - pinThetas[0]) / 2)
    pinOffsetInches = toInches(pinOffset, 'm')
    pinOffsets.append(pinOffsetInches)

    realDiff = realPinOffsets['52'] - pinOffsetInches
    realDiffs.append(realDiff)
    totalDiff += abs(realDiff)
    print('\tpinOffset52 = %fin\t(diffReal = %fin)' % (pinOffsetInches, realDiff))

    print('\n\ttotalDiff = ', totalDiff)
    dc += 0.25

  plt.style.use('_mpl-gallery')

  x = ['20->30pin', '30 -> 40 pin', '40 -> 50 pin', '20 -> 50 pin']
  plt.scatter(x, realPinOffsets.values(), color='red')
  plt.scatter(x, pinOffsets, color='blue')
  plt.show()

if __name__ == '__main__':
  main()