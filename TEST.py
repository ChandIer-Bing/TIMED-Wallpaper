import datetime
import schedule
import time
import msvcrt

def job():
        print("hello")
def kill_job():
        a= msvcrt.getch()
        if a=="k":
                schedule.clear()

a=str(datetime.datetime.now())
a=int(a[11:13])
print(a)
timeA=3
timeB=7
timeNow=5
if timeNow>timeA and timeNow<timeB:
        print("yes")

schedule.every(3).seconds.do(job)
schedule.every(1).seconds.do(kill_job)

while True:
        schedule.run_pending()
        time.sleep(0.1)
       
