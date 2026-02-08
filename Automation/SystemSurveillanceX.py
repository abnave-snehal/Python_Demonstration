
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
    fobj.write("----- Marvellous Platform Surveillance System ----"+"\n")
    fobj.write("\n Log created at : "+time.ctime()+"\n")
    fobj.write(border+"\n\n")


    fobj.write("---------- System Report ---------- \n")

    # print("CPU Usages: ",psutil.cpu_percent())
    fobj.write("CPU Usgae : %s %%\n" %psutil.cpu_percent())
    fobj.write(border+"\n")

    mem=psutil.virtual_memory()
    # print("RAM usage :",mem.percent)
    fobj.write("RAM Usage : %s %%\n" %mem.percent)
    fobj.write(border+"\n")

    fobj.write("\n Disk Usage Report \n")
    fobj.write(border+"\n")
    
    for part in psutil.disk_partitions():
        try:
            usage=psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
                #drive kuthle           # kiti vaparle ahet

            fobj.write("%s -> %s %% used \n" %(part.mountpoint,usage.percent))
        except:
            pass
    fobj.write(border+"\n")

    net=psutil.net_io_counters()
    fobj.write("\nNetwork Usage Reoprt\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(border+"\n")

    #Process LOG
    Data=ProcessScan()

    
    
    fobj.write(border+"\n")
    fobj.write("------------ End of log file ---------------")
    fobj.write(border+"\n")


def ProcessScan():
    listProcess=[]

#Warm up for  CPU percent just like 1st cup of tea
for proc in psutil.process_iter():
    try:
        proc.cpu_percent()
    except:
        pass

    time.sleep(0.2)

    for proc in psutil.process_iter():  #proc is dict key value pair
        try:
            info=proc.as_dict(attrs=["pid","name","username","status","create_time"])
            # Convert create_time
            try:
                info["create_time"]=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"]="NA"

            info["cpu_percent"]=proc.cpu_percent(None)
            info["memory_percent"]=proc.memory_percent()

            listProces.append(info)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listProcess

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