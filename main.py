import os
import subprocess
try:
    import psutil
except:
    os.system('py -m pip install psutil')
    import psutil


currentBIOS = os.system('powershell Get-CimInstance -ClassName Win32_BIOS')
# The following is left here because this is stupid and it doesn't work so anyone that ever needs this
# is able to see the above line so you can use that instead! :)
# subprocess.Popen(['Get-CimInstance', '-ClassName', 'Win32_BIOS'], shell=True)

print(currentBIOS)

currentPCStuff = os.system('powershell Get-CimInstance -ClassName Win32_OperatingSystem')
print(currentPCStuff)

for processes in psutil.process_iter(['pid', 'name', 'username']):
    print(processes.info)


print("Split!")
# Deprecated I need to use: https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/07-working-with-wmi?view=powershell-7.4
a = os.system('powershell Get-CimInstance')
print(a)

# try:
#     for things in range(len(programstring)):
#         print(programstring.Popen('\\r\\r\\n')[6:][things])
# except:
#     print('Split!')