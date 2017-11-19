import pandas as pd
import numpy as np
from sklearn.utils import shuffle


df1 = pd.read_csv("2012_merged.csv")
df2 = pd.read_csv("2013_merged.csv")
df3 = pd.read_csv("2014_merged.csv")

labels = ["year", "county", "state", "copd_prev", "asthma_prev", "tobacco_prev", "med_income_5y", "perc_below_poverty_1y", "perc_below_poverty_5y", "unemployment_1y", "unemployment_5y", "apc_percent_diff"]
df1_sub = df1[labels]
df2_sub = df2[labels]
df3_sub = df3[labels]

merged = df1_sub.append(df2_sub)
merged = merged.append(df3_sub)
merged = shuffle(merged)
merged.to_csv("all_years_merged.csv", index=False)
