import pandas as ps
df = ps.DataFrame({'Name': ['punit', 'goyal', None], 'age': [22, None, 23]})
print(df.head().to_string())

# dropna() function check for a NaN value.. if present it will remove the entire row
# data = df.dropna()
# print(data)

# df['Name'] != '' checks for an empty string
# data = df[(df['Name'] != '') & (df['age'].notna())]
# print(data)

#way to check for a None string value
# data = df[df['Name'].notna()]
# print(data)

# fillna() fills the missing value with the specified value
# in this case the missing value will be filled by the mean of the other values of the age column
df['age'].fillna(df['age'].mean(), inplace = True)
print(df)