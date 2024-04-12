import time
import math

def timing(timer):
    seconds = timer*60
    while seconds > 0:
        print (seconds)
        seconds -= 1
        time.sleep(1)


timer = float(input("Enter the time that you want to set a timer or countdown for in minutes:::"))
timing(timer)