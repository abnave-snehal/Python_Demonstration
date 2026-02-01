import hashlib

def CalculateChkSum(fileName):
    fobj=open(fileName,"rb")   #read in binary mode

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():

    checkSum=CalculateChkSum("Demo.txt")

    print("Checksum is : ",checkSum)

if __name__ == "__main__":
    main()