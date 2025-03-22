import pandas as p
df = p.DataFrame({
    'EmpId' : [123, 134, 135, 145, 156, 173],
    'EmpName': ['Rohan', 'Surender', 'Aradhana', 'Monika', 'Punit', 'Naren'],
    "Salary" : [40000, 35000, 65000, 45000, 70000, 56000],
    "Department": ['MBA', 'Finance', 'Testing', 'Developer', 'Developer', 'Law']
})

print(df.to_string())
print("************************\n")

df2 = p.DataFrame({
    'EmpId' : [123, 134, 135, 145, 156],
    'EmpName': ['Rohan', 'Surender', 'Aradhana', 'Monika', 'Punit'],
    "Married": ["yes", 'yes', 'no', 'no', 'no']
})

mergedData = p.merge(df, df2, how='cross')
mergedData1 = p.merge(df, df2, how='left', on='EmpId')
mergedData2 = p.merge(df, df2, how='right', on='EmpId')
mergedData3 = p.merge(df, df2, how='outer', on='EmpId')
mergedData4 = p.merge(df, df2, how='inner', on='EmpId')
print(mergedData)
print("************************\n")
print(mergedData1)
print("************************\n")
print(mergedData2)
print("************************\n")
print(mergedData3)
print("************************\n")
print(mergedData4)
print("************************\n")