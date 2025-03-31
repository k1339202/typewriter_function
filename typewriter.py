import sys
import time

def typewriter(string)
  for char in string:
    # Change these to increase the effect variance
    #                    v   v
    time.sleep(uniform(0.1,0.25))
    sys.stdout.write(char)
    sys.stdout.flush()
