#!\C:\Users\User\AppData\Local\Python\bin\python.exe
#If this script does'nt execute directly change the above directory with your python executable.
# "where python" to get address of python executable


import time
import subprocess

def exiting():
    time.sleep(2)
    print("Exiting...")
    time.sleep(2)

print('''
    =================================================
    Welcome to Scheduled Shutdown By "M Arif Manzoor"
    =================================================

    < Enter "ABORT" to cancel a Scheduled Shutdown >
    
''')



delay = input("Delay In Seconds : ")


time.sleep(3)
if delay == "ABORT":
    subprocess.run("shutdown -a")
    print("Shutdown Aborting...")
    exiting()
else:
    try:
        subprocess.run("shutdown -s -t " + delay , shell=True)
        time.sleep(2)
        print("Shutdown Scheduled!")
        exiting()
    except:
        print("ERROR : INCORRECT DELAY FORMAT!")
        exiting()



