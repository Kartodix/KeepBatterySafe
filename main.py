import psutil
import ctypes  # An included library with Python install.   

bat = psutil.sensors_battery()
appName = "KeepBatterySafe"

def batteryLevel(bat):
    return bat.percent

def pluggedOrNot(bat):
    plugged = bat.power_plugged
    return True if plugged else False

# plug nom
if(batteryLevel(bat)<25 and pluggedOrNot(bat)==False):
    message = "Plug your PC now ! " + str(batteryLevel(bat)) + "%"
    ctypes.windll.user32.MessageBoxW(0, message, appName, 1)

# unplug now
if(batteryLevel(bat)==100 and pluggedOrNot(bat)==True):
    message = "Unplug your PC now ! " + str(batteryLevel(bat)) + "%"
    ctypes.windll.user32.MessageBoxW(0, message, appName, 1)

# prevent plug
if(batteryLevel(bat)<=30 and pluggedOrNot(bat)==False):
    message = str(batteryLevel(bat)) + "%! You soon should plug your PC!"
    ctypes.windll.user32.MessageBoxW(0, message, appName, 1)
