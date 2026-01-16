# type: ignore

import os, sys
sys.path.append('')
import numpy as np 
import c4dynamics as c4d 
from matplotlib import pyplot as plt 
plt.style.use('dark_background')  
plt.switch_backend('TkAgg')



# every example should be self contained. 
runerrors = False
saveimages = False   
viewimages = False 





c4d.cprint('vel_mag()', 'c')
s = c4d.state(vx = 7, vy = 24)
print(s.vel_mag())
# 25.0

s = c4d.state(x = 100, y = 0, vx = -10, vy = 7)
print(s.vel_mag())
# 12.2


s = c4d.state(x = 100, y = 0)
print(s.vel_mag())
# TypeError: state must have at least one velocity coordinate (vx, vy, or vz)


