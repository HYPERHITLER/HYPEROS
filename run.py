import os, platform
print(' CHECKING FOR UPDATES')
os.system('git pull')
bit = platform.architecture()[0]
if bit == '32bit':
    from data import HYPER32
elif bit == '64bit':
    from data import HYPER64
else: print(" YOUR DEVICE DOESN'T SUPPORT MY TOOL")
  
