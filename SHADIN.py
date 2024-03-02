import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import SHADIN
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
