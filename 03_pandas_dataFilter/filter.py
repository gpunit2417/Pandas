import pandas as p
df = p.DataFrame({
    'EmpId' : [123, 134, 135, 145, 156, 173],
    'EmpName': ['Rohan', 'Surender', 'Aradhana', 'Monika', 'Punit', 'Naren'],
    "Salary" : [40000, 35000, 65000, 45000, 70000, 56000],
    "Department": ['MBA', 'Finance', 'Testing', 'Developer', 'Developer', 'Law']
})

print(df.to_string())
print("************************\n")


# below two lines are same 
# filterData = df[df.EmpId > 135]
# filterData = df[df["EmpId"] > 135]
# print(filterData)

# filtered data using == sign
# filterData = df[df.EmpName == "Punit"]
# print(filterData)

# select particular columns from a dataframe
# data = df[["EmpName", "Salary"]]
# print(data)

# unique value in a column
# print(df["Department"].unique())

# sort the data 
# new_df = df.sort_values(by=["Salary"], ascending=False)
# print(new_df)

# one hot-encoding
# new = p.get_dummies(df, columns=["Salary"])
# print(new)

# applied a function
df["newSalary"] = df['Salary'].apply(lambda x: x*2)
print(df)