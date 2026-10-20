import shutil
import sys

THRESHOLD = 80
PATHS = ["/" ,"/home/jenkins/agent","/tmp"]
alert_found = False

for path in PATHS:
    try:
        usage = shutil.disk_usage(path)
    except FileNotFoundError:
        print(f"{path} not found")
        alert_found = True
        continue

    total_gb = usage.total/1024**3
    used_gb = usage.used/1024**3
    free_gb = usage.free/1024**3
    usage_percent = (usage.used/usage.total)*100

    if usage_percent > THRESHOLD:
        alert_found = True
        status = "ALERT"
    else:
        status = "OK"

    print(f" path is :{path} total: {total_gb:.2f} GB  used: {used_gb:.2f} GB  free: {free_gb:.2f} GB")
    print(status)

sys.exit(1 if alert_found else 0)
