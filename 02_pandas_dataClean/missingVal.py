import pandas as ps
df = ps.DataFrame({'Name': ['punit', 'aastha', ''], 'age': [22, 21, 23]})
print(df.head().to_string())

# dropna() function check for a NaN value.. if present it will remove the entire row
# data = df.dropna()
# print(data)

