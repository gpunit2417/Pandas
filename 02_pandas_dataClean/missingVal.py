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
# df['age'].fillna(df['age'].mean(), inplace = True)
# print(df)

# rename() function renames the column names... the column name is case sensitive... name cannot be passed instead we need to pass Name.
# df.rename(columns={'Fullname':'Name'}, inplace = True)
# print(df)

# way to drop first row and column together
# df.iloc[row, column] is the syntax
# to delete first row df.iloc[1:, :]
# to delete first column df.iloc[:, 1:]
# new_df = df.iloc[1:, 1:]
# print(new_df)

# drop any specific columns
df.drop(columns=['Name'], inplace=True)
print(df)