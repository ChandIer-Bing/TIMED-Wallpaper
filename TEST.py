import datetime
import schedule
import time
import msvcrt
import ctypes
import random
import os

currentWall=int(1)
#<<<<-GOOFS->>>>
""" def job():
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
        """

#<<<<-TIMED OF DAY WALLPAPER CHANGE->>>>
""" def job1(message):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\CODE\PYTHON\WALLPAPER_change\Big_Sur\macOS-Big-Sur-Daylight-Wallpaper-3.jpg" , 0)
        print ("look dad i did ",message)

schedule.every().day.at("22:51").do(job1, message="change the wallpaper!")

while True:
        schedule.run_pending()
        time.sleep(1) """


#<<<<-RNG ->>>>
def RNG(wallpaperNum,prev):     #wallpaperNum: number of wallpapers, prev:previus wallpaper
        i=random.randint(1,wallpaperNum)
        while i==prev:
                i=random.randint(1,wallpaperNum)
        return i

""" A=input("how many wallpapers?\n")
A=int(A)
#print(type(A))
3
B=input("which was the last one?\n")
B=int(B)
#print(type(B))
print(RNG(A,B))
 """

##<<<<-TIMED RNG WALLPAPER CHANGE->>>>
""" def changeWall(message,wallIndex): #wallindex: index of the wallpaper that is going to be shown
        wallIndex=str(wallIndex)
        wallpaperSource="D:\CODE\PYTHON\WALLPAPER_change\Big_Sur\macOS-Big-Sur-Daylight-Wallpaper-"+wallIndex+".jpg"
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaperSource, 0)
        print ("look dad! i did ",message)

def topJob():
        global currentWall
        currentWall=RNG(8,currentWall)
        changeWall("change the wallpaper! to wallpaper"+str(currentWall),currentWall)


schedule.every(3).seconds.do(topJob)
#schedule.every(3).seconds.do(print,currentWall)
#schedule.every(3).seconds.do(currentWall=RNG)

while True:
        schedule.run_pending()
        time.sleep(1)

 """
 #<<<<-FOLDERS TESTING ->>>>

#print(os.path.isabs('C:\\Users\\raton\\Pictures\\WIDE wallpapers\\Big_Sur'))
#print(os.path.isdir('C:\\Users\\raton\\Pictures\\WIDE wallpapers\\Big_Sur'))
#print(os.path.isfile('C:\\Users\\raton\\Pictures\\WIDE wallpapers\\Big_Sur'))
#print(os.listdir('C:\\Users\\raton\\Pictures\\WIDE wallpapers\\Big_Sur'))
wallpapers=os.listdir('C:\\Users\\raton\\Pictures\\WIDE wallpapers\\Big_Sur')
print(wallpapers)
#print(len(wallpapers),type(len(wallpapers)))
len
