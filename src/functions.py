import datetime #this is used for the datetime.now() which returns date and time now
import time     #this is needed for the scheduled module to work but currently no functions are explicitly used
import schedule #this schedules the tasks so you can have recurring events at specific points in time
import msvcrt   #this used to get constant imput from the keyboard without pressing enter
import ctypes   #this i sused to change the wallpaper

def wallpaper_Changer(wallIndex,wallSource):
    wallIndex=str(wallIndex)
#    wallSource="D:\CODE\PYTHON\WALLPAPER_change\Big_Sur\macOS-Big-Sur-Daylight-Wallpaper-"+wallIndex+".jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallSource, 0)

def check_Time(tA,tB):
    daTime=str(datetime.datetime.now())
    time=int(daTime[11:13])
    if time>>tA and time<<tB:
        return True
    else:
        return False

def time_Dict(wallNum): #wallNum : number of wallpapers
    global timeDict={}
    for i in range(wallNum)
        timeDict.setdefault("w"+str(wallNum),1)

        



