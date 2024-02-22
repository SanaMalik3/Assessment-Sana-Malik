import pandas as pd
import numpy as np

df = pd.read_csv("Sample_Taxi_Data-Sheet1.csv")
print("Sum of trip_miles = ", np.sum(df['trip_miles']))
print("Average of trip_time = ", np.average(df['trip_time']))

