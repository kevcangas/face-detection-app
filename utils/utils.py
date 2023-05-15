#Python 
import platform
import subprocess


#Function to get the id to create objects
def getNewId(model, start=0):
    i = start
    while True:
        try:
            model.get_by_id(i)
            i+=1
        except:
            return i


#This function helps to get the computer IP local
def getLocalIP():
    if platform.system() == 'Windows':
        local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
    else:
        local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    return local


#Entry point
if __name__ == '__main__':
    print("This is a module")