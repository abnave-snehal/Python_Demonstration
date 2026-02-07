
import psutil
import sys
import os
import time
import schedule

def createLog(folderName):
    border="-"*50
    ret=False

    ret=os.path.exists(folderName)

    if(ret == True):
        ret=os.path.isdir(folderName)
        if(ret==False):
            print("Unable to create folder : ")
            return
    else:
        os.mkdir(folderName)
        print("Directory for log file gets created succesfully: ")

    timeStamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(folderName,"Marvellous_%s.log" %timeStamp)
    print("Log file gets created with file name : ",FileName)

    fobj=open(FileName,"w")

    fobj.write(border+"\n")
    fobj.write("----- Marvellous Platform Surveillance System ----")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    fobj.write(border+"\n")
    fobj.write("------------ End of log file ---------------")
    fobj.write(border+"\n")
    
        
def main():
    border="-"*50
    print(border)
    print("----- Marvellous Platform Surveillance System ----")
    print(border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or "--H"):
            print("This script is use to : ")
            print("1: Create automatic logs")
            print("2: Execute periodically")
            print("3: Sends mail with log")
            print("4: Store information about processes")
            print("5: Store information about CPU")
            print("6: Store infromation about RAM usage")
            print("7: Store information about secondary storage")
        elif(sys.argv[2] == "--u" or "--U"):
            print("Use the automation script as")
            print("ScriptNAme.py Timeinterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs") 

        else:
            print("Unable to proceed as there is nno such option")
            print("Please use --h or --u to get more details")

    #python Demo.py 5 Marvellous 
    elif(len(sys.argv)==3):
        print("Inside projects logic : ")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])
        createLog(sys.argv[2])

        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(createLog,sys.argv[2])

        print("Platform surveillance system started sucessfully : ")
        print("Direcotry created with name : ",sys.argv[2])
        print("Time interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop : ")

        # wait till abort   
        while True:
            schedule.run_pending
            time.sleep(1)
    else:
         print("Invalid number of command line arguments")
         print("Unable to proceed as there is nno such option")
         print("Please use --h or --u to get more details")

    print(border)
    print("--------- Thank You For Using Our Script --------- ")
    print(border)

if __name__ == "__main__":
    main()