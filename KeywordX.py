def EmployeeInfo(Name,Age,City,Salary):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)


def main():
  #Keyword Arguments
  EmployeeInfo(Age=26,Name="Rahul",City="Pune",Salary=None)

if __name__== "__main__":
    main()