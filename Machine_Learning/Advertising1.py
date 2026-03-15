import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    df=pd.read_csv("Advertising.csv")

    # Data cleaning index removed
    print(df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)  # inplace menas
    print(df.shape)

if __name__ == "__main__":
    main()