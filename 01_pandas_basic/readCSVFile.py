import pandas as pd

fileData = pd.read_csv("C:\\Users\\HP\\Desktop\\data.csv")
print(fileData)
print("*********************")
# print(fileData.head())
# print("*********************")
# print(fileData.head(7))
# print("*********************")
# print(fileData.tail())
# print("*********************")
# print(fileData.tail(7))
# print("*********************")
# print(fileData.shape)         #will give you the no of rows and columns
# print(fileData.describe())    #will give the mathematical stats of the numerical columns like mean, max, min, count, 25%, 50%, 75%.
print(fileData.info())          #will give the stats regarding the database like no of rows and columns, dataframe type, datatype of row and column