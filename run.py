import os, platform
print(' CHECKING FOR UPDATES')
os.system('git pull')
print(' THIS TOOL IS BEING MAINTENANCE TRY AGAIN FEW MOMENT LATER')
exit()
bit = platform.architecture()[0]
if bit == '32bit':
    from data import HYPER32
elif bit == '64bit':
    from data import HYPER64
else: print(" YOUR DEVICE DOESN'T SUPPORT MY TOOL")
  
