import platform
import socket 
import psutil
from datetime import datetime

def system_information():
    print("=" * 45)
    print("IT OPERATIONS MONITOR")
    print ("=" * 45)

    print("Computer:", socket.gethostname())
    print("Operating System:", platform.system())
    print("OS Version:", platform.release())
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("\n--- SYSTEM PERFORMANCE ---")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")

    print("\n--- SYSTEM HEALTH ---")

    if cpu > 85:
        print("WARNING: High CPU Usage!")
    else:
        print("CPU Status: Normal")

    if memory.percent > 85:
        print("WARNING: High RAM Usage!")
    else:
        print("RAM Status: Normal")

    if disk.percent > 90:
        print("WARNING: Disk Space Running Low!")
    else:
        print("Disk Status: Normal")

    print("=" * 45)

if __name__ == "__main__":
    system_information()
    