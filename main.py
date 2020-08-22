import psutil, ctypes, time, schedule

bat = psutil.sensors_battery()
appName = "KeepBatterySafe"

def batteryLevel(bat):
    return bat.percent

def pluggedOrNot(bat):
    return True if bat.power_plugged else False

def check():
    # plug now
    if(batteryLevel(bat)<25 and pluggedOrNot(bat)==False):
        message = "Plug your PC now ! " + str(batteryLevel(bat)) + "%"
        ctypes.windll.user32.MessageBoxW(0, message, appName, 1)

    # unplug now
    if(batteryLevel(bat)==100 and pluggedOrNot(bat)==True):
        message = "Unplug your PC now ! " + str(batteryLevel(bat)) + "%"
        ctypes.windll.user32.MessageBoxW(0, message, appName, 1)

    # prevent plug
    if(batteryLevel(bat)<=35 and batteryLevel(bat)>25 and pluggedOrNot(bat)==False):
        message = str(batteryLevel(bat)) + "%! You soon should plug your PC!"
        ctypes.windll.user32.MessageBoxW(0, message, appName, 1)

schedule.every(5).minutes.do(check)

while True:
    print("KeepBatterySafe Launched")
    schedule.run_pending()
    time.sleep(1)