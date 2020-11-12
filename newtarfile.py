import datetime
import os
import tarfile
import shutil

from dateutil.relativedelta import relativedelta

#tartype='week'
tartype='day'

def newfile(filenm):
  f = open(filenm,'w')
  f.write("test")
  f.close()

def makfolder(container):
  print(container)
  for i in range(3):
    mydir = './' + container +'/candata/p_key=vin/p_num=' + str(i)
    os.makedirs(mydir)
    for i in range(1):
      newfile(mydir + "/file" + str(i) + ".txt")

def maktarfile(tarfilenm):
  tar = tarfile.open(tarfilenm + ".tar.gz","w:gz")
  for root,dir,files in os.walk("./"):
    if root != "./":
      for file in files:
        fullpath = os.path.join(root,file)
        tar.add(fullpath)
  tar.close()
  for root,dir,files in os.walk("./"):
    for subdir in dir:
      shutil.rmtree(subdir)


dt_now = datetime.datetime.now()

dt_from= dt_now - relativedelta(days=10)
dt_to= dt_now - relativedelta(days=2)
#print(dt_from,dt_to)
yr,weekNumber,weekDay = dt_from.isocalendar()
weekno = str(yr) + str(weekNumber)
ywd = weekno + str(weekDay)
tarflg = False

while dt_from <= dt_to:
  yr,weekNumber,weekDay = dt_from.isocalendar()
#  print(yr,weekNumber,weekDay,dt_from)
  weeknotmp = str(yr) + str(weekNumber)
  ywdtmp = weeknotmp + str(weekDay)
  if tartype == 'week' and weekno != weeknotmp:
    tarflg = True
    tarnm = weekno
    weekno = weeknotmp
  elif tartype == 'day' and ywd != ywdtmp:
    tarflg = True
    tarnm = dt_from.strftime("%Y-%m-%d")
    ywd = ywdtmp
  makfolder(dt_from.strftime("r%Y-%m-%d-%H%M"))
  if tarflg == True:
    maktarfile(tarnm)
    tarflg = False
  dt_from += relativedelta(minutes=1)
