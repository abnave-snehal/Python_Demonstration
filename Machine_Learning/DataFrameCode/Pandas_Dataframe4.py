import pandas as pd

def main():
    data={
        "Name":["Sagar","Amit","Pooja"],
        "Age":[23,25,25],
        "City":["Pune","Mumbai","Satara"]
    }

    dobj=pd.DataFrame(data)

    print(dobj.loc[0])   # fetch specific row
    

if __name__ == "__main__":
    main()