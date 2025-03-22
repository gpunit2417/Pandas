import pandas as pd

fileData = pd.read_csv("C:\\Users\\HP\\Desktop\\data.csv")
print(fileData)
print("*********************")
print(fileData.head())
print("*********************")
print(fileData.head(7))
print("*********************")
print(fileData.tail())
print("*********************")
print(fileData.tail(7))
print("*********************")