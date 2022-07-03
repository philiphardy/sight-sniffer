shouldLog = False

def log(*args):
  if shouldLog:
    print(*args)
