from math import pi

def toMeters(value, unit):
  if unit == 'm':
    return value
  if unit == 'in':
    return value * 0.0254
  if unit == 'cm':
    return value * 0.01
  if unit == 'mm':
    return value * 0.001
  if unit == 'yd':
    return value * 0.9144
  raiseException(unit)

def toYards(value, unit):
  if unit == 'm':
    return value / 0.9144
  if unit == 'yd':
    return value
  raiseException(unit)

def toInches(value, unit):
  if unit == 'm':
    return value * 39.3701102362
  if unit == 'yd':
    return value * 36
  if unit == 'in':
    return value
  raiseException(unit)

def toKilograms(value, unit):
  if unit == 'g':
    return value * 0.001
  if unit == 'kg':
    return value
  raiseException(unit)

def toNewtons(value, unit):
  if unit == 'lb':
    return value * 4.44822
  if unit == 'N':
    return value
  raiseException(unit)

def toDegrees(value, unit):
  if unit == 'deg':
    return value
  if unit == 'rad':
    return value * 180 / pi 
  raiseException(unit)

def toRadians(value, unit):
  if unit == 'deg':
    return value * pi / 180
  if unit == 'rad':
    return value
  raiseException(unit)

def raiseException(unit):
    raise Exception('Unknown unit \'%s\'' % unit)