import pandas as pd

df = pd.DataFrame({'Name': ['Punit', 'Rishabh', 'Sumit'], 'Age': [23, 25, 23], 'Passed': ['No', 'Yes', 'No']})

writeToCSVFile = df.to_csv("C:\\Users\\HP\\Desktop\\data1.csv", index = False)

dataFetch = pd.read_csv("C:\\Users\\HP\\Desktop\\data1.csv")
print(dataFetch)