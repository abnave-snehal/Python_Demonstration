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

    # Split the data into X & Y
    X=df[['TV','radio','newspaper']]
    Y=df['sales']

    print("Indepdent Variables : ", X.shape)
    print("Depdent Vairables : ",Y.shape)

    # Split the data for training and testing
    X_train,X_test,Y_train,Y_test=train_test_split(
        X,
        Y,
        test_size=0.1,
        random_state=42
    )

    model=LinearRegression()

    model.fit(X_train,Y_train)

    y_pred=model.predict(X_test)

    print("Testing Data : ")
    print(X_test)

    print("Predicted values : ")
    print(y_pred)

    print("Actual Values ")
    print(Y_test)

    print("Coefficient : ")
    print(model.coef_)

    print("Intercept : ")
    print(model.intercept_)   # intercept means C ie.(y=mx+C)




if __name__ == "__main__":
    main()