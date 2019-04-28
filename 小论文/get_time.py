import time

def Time() :
    a = time.time()
    hour = int(a / 3600)
    minute = int((a % 3600) / 60)
