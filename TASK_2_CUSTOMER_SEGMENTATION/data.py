import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:\Elevvo_ML\dataset_of task2\Mall_Customers.csv")
print(df.head())
print("Missing values in each column:")
print(df.isnull().sum())
print("\nData Information:")
print(df.info())
print("missing data : ")
print(df.isnull().sum())