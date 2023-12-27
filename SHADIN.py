import os,time,platform
import os, platform, time, sys
print(' [\x1b[38;5;48m●\033[1;37m]\x1b[38;5;46m CHECKING UPDATE...!\033[1;37m [\x1b[38;5;48m–\033[1;37m]\033[1;37m')
time.sleep(5)
os.system('clear')
print('\033[1;97m[\x1b[38;5;48m●\033[1;37m] \x1b[38;5;50mJOIN MY PUBLIC GROUP ')
time.sleep(0.1)
os.system(f'xdg-open https://facebook.com/groups/354277300393287/')
os.system('clear')
print('\x1b[38;5;46mLoding...\x1b[38;5;197m[\x1b[38;5;46mSHADIN-143\x1b[38;5;197m]\x1b[38;5;46m')
os.system('pip uninstall requests -y');os.system('pip install requests')
bit = platform.architecture()[0]
if bit=='64bit':
    import SHADIN
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
