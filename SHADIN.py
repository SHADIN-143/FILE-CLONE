# Owner ● SHADIN-143
os.system('git pull')
os.system('pip uninstall requests -y');os.system('pip install requests')
bit = platform.architecture()[0]
if bit=='64bit':
    import SHADIN
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
