import datetime
import os
import tarfile
import shutil

from dateutil.relativedelta import relativedelta

dt_now = datetime.datetime.now()
dt_ago = dt_now - relativedelta(days=1)

def newfile(filenm):
  f = open(filenm,'w')
  f.write("test")
  f.close()

while dt_ago <= dt_now:
  container = dt_ago.strftime("r%Y-%m-%d-%H%M")
  for i in range(96):
    mydir = './' + container +'/candata/p_key=vin/p_num=' + str(i)
    os.makedirs(mydir)
    for i in range(3):
      newfile(mydir + "/file" + str(i) + ".txt")
  dt_ago += relativedelta(minutes=1)

tar = tarfile.open("tartest.tar.gz","w:gz")
for root,dir,files in os.walk("./"):
  for file in files:
    fullpath = os.path.join(root,file)
    tar.add(fullpath)
tar.close()
for root,dir,files in os.walk("./"):
  for subdir in dir:
    shutil.rmtree(subdir)

