import pandas as pd

def main():
    data=[11.0,21.0,51.0,101.0,111.0]
    
    sobj=pd.Series(data)

    print(sobj)

if __name__ == "__main__":
    main()