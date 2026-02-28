import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:/Elevvo_ML/archive/StudentPerformanceFactors.csv")
print(df.head())
print("Missing values in each column:")
print(df.isnull().sum())
print("\nData Information:")
print(df.info())
