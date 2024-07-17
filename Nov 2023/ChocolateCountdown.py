import time
import math

def timing(timer):
    seconds = timer*1
    while seconds > -1:
        print (seconds)
        seconds -= 1
        time.sleep(1)
    print("Blast Off!")

timer = float(input("Enter the time that you want to set a timer in seconds:::"))
timing(timer)