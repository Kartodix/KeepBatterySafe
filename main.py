import psutil
from win10toast import ToastNotifier

bat = psutil.sensors_battery()
notifier = ToastNotifier()
appName = "KeepBatterySafe"

def batteryLevel(bat):
    return bat.percent

def pluggedOrNot(bat):
    plugged = bat.power_plugged
    return True if plugged else False

if(batteryLevel(bat)<25 and pluggedOrNot(bat)==False):
    message = "Plug your PC now ! " + str(batteryLevel(bat)) + "%"
    notifier.show_toast(appName, message)

if(batteryLevel(bat)==100 and pluggedOrNot(bat)==True):
    message = "Unplug your PC now ! " + str(batteryLevel(bat)) + "%"
    notifier.show_toast(appName, message)