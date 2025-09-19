import pandas as pd
employee_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\employee_data.csv")

print(employee_df.head(3))
print(employee_df["Name"].count())

print(employee_df["Department"].value_counts().max())


print(employee_df.loc[employee_df["Salary"]==employee_df["Salary"].max(),"City"])


print(employee_df[employee_df["Experience"]>5])

print(employee_df.sort_values(by= "Salary",ascending=False))

employee_df["Bonus"]=employee_df["Salary"]*1.10
print(employee_df)

Departments=employee_df.groupby(by="Department")
print(Departments["Experience"].mean())
print(Departments["Salary"].mean())