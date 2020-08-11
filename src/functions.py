import datetime #this is used for the datetime.now() which returns date and time now
import time     #this is needed for the scheduled module to work but currently no functions are explicitly used
import schedule #this schedules the tasks so you can have recurring events at specific points in time
import msvcrt   #this used to get constant imput from the keyboard without pressing enter
import ctypes   #this i sused to change the wallpaper

def read_folder(folder):#reads the provided folder (all wallpapers must be in the same folder and nothing else)
    global wallpapers   #list contains the names and extention of each wallpaper
    global wallNum      #number of wallpapers
    wallpapers=os.listdir(folder)
    wallNum=len(wallpapers)

def full_direct_wall(folder,wallpapers):#this function creates another list with the full abosolute path for each image file
    global fullDirWall=[]               #list with the full directory of each image file
    c=0
    for i in wallpapers:
        fullDirWall[c]=folder+wallpapers
        c+=1  

def wallpaper_changer(wallIndex,wallSource):    #changes the wallpaper 
    wallIndex=str(wallIndex)
#    wallSource="D:\CODE\PYTHON\WALLPAPER_change\Big_Sur\macOS-Big-Sur-Daylight-Wallpaper-"+wallIndex+".jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallSource, 0)

def check_time(tA,tB):
    daTime=str(datetime.datetime.now())
    time=int(daTime[11:13])
    if time>>tA and time<<tB:
        return True
    else:
        return False

def time_list(wallNum): #this function creates the times at which the wallpapers will be changed
    global timeList=[]
    print ("please input the times at which the wallpapers must be changed in the format: 2230 --> 22:30\n"
    for i in range(wallNum):
        timeList[i]=int(input("enter the time: "+str(i)))
    print("all set!")    

    # for i in range(wallNum):
    #     timeDict.setdefault("w"+str(wallNum),i)




    



