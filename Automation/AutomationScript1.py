import sys


def main():
    border="-"*40
    print(border)
    print("--------- Marvellous Automation --------")
    print(border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform _____")
            print("This is a automation script : ")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as : ")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : ______")
            print("Argument2 : ______")

        else:
            print("Use the given flags as : ")
            print("--u : Used to disply the usage")
            print("--h : used to disply help")
    else:
        print("Invalid number of command line arguments : ")
        print("Use the given flags as : ")
        print("--u : Used to disply the usage")
        print("--h : used to disply help")

    print(border)
    print("----- Thank you for using our script -----")
    print("--------- Marvellous Infosystems ---------")
    print(border)

if __name__ == "__main__":
    main()