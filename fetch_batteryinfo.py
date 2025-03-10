import os

try:
    import psutil
except as e:
    os.system("pip install psutil")
    import psutil

def get_battery_info():
    battery = psutil.sensors_battery()
    
    if battery is None:
        print("Battery information is not available.")
        return

    print(f"Battery Percentage: {battery.percent}%")
    print(f"Charging Status: {'Plugged In' if battery.power_plugged else 'Not Charging'}")
    
    if not battery.power_plugged:
        print(f"Estimated Time Remaining: {battery.secsleft // 60} minutes")

if __name__ == "__main__":
    get_battery_info()

