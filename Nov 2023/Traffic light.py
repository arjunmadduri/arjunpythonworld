traffic_light = str(input("Enter the status of the traffic light red/yellow/green: "))
if traffic_light=="red":
    print("XXXXXXXX STOP!!! XXXXXXXX")
elif traffic_light=="yellow":
    print("XXXXXXXX START YOUR VEHICLE & BE READY TO GO!! XXXXXXXX")
elif traffic_light=="green":
    print("XXXXXXXX GO!! XXXXXXXX")
else:
    print("XXXXXXXX Invalid Traffic Light Value XXXXXXXX")