# This code creates the getTemperature() function that you will use in your own code
# to get simulated temperature values.  You do not need to edit it.
import time
import random

def getTemperature():
    time.sleep(0.1)
    if random.random() < 0.05:
        return -200
    else:
        return random.randint(-20, 120)