import psutil
from win10toast import ToastNotifier

bat = psutil.sensors_battery()
toaster = ToastNotifier()

def batteryLevel(bat):
    return bat.percent

def pluggedOrNot(bat):
    plugged = bat.power_plugged
    return True if plugged else False

if(batteryLevel(bat)<23 and pluggedOrNot(bat)==False):
    # notify
    print("Plug your PC now !")

if(batteryLevel(bat)==100 and pluggedOrNot(bat)==True):
    # notify
    print("Unplug your pc now !")

toaster.show_toast("Hello world")