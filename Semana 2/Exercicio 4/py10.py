#Python Tutorial: OS Module - Use Underlying Operating System Functionality

import os

from datetime import datetime

os.chdir('home/atual')

mod_time = os.stat('demo.txt').st_mtime
#print(datetime.fromtimestamp(mod_time)

for dirpath, dirnames, filenames in os.walk('home/atual'):
    print('CurrentPath', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
    print()
    
    
################
print(os.path.splitext('home/atual/texto.txt'))
