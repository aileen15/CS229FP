import pandas as pd
import numpy as np

year = "2015"

df1 = pd.read_csv(year + "/" + year + "_copd_apc.csv")
df2 = pd.read_csv(year + "/" + year + "_copd_prev.csv")
df3 = pd.read_csv(year + "/" + year + "_asthma_prev.csv")
df4 = pd.read_csv(year + "/" + year + "_tobacco_prev.csv")
df5 = pd.read_csv(year + "/" + "med_income_5y_" + year + ".csv")
df6 = pd.read_csv(year + "/" + "perc_below_poverty_1y_" + year + ".csv")
df7 = pd.read_csv(year + "/" + "perc_below_poverty_5y_" + year + ".csv")
df8 = pd.read_csv(year + "/" + "unemployment_1y_" + year + ".csv")
df9 = pd.read_csv(year + "/" + "unemployment_5y_" + year + ".csv")


df5["state"] = map(lambda x: str(x).upper().strip(), df5["state"])
df6["state"] = map(lambda x: str(x).upper().strip(), df6["state"])
df7["state"] = map(lambda x: str(x).upper().strip(), df7["state"])
df8["state"] = map(lambda x: str(x).upper().strip(), df8["state"])
df9["state"] = map(lambda x: str(x).upper().strip(), df9["state"])


df1["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df1["county"])
df2["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df2["county"])
df3["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df3["county"])
df4["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df4["county"])
df5["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df5["county"])
df6["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df6["county"])
df7["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df7["county"])
df8["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df8["county"])
df9["county"] = map(lambda x: str(x).rsplit(' ', 1)[0], df9["county"])


one_year_features = ["num_days_rain", "perc_cultivated_land_use", "perc_forest_cover", "perc_park_proximity", "rural_urban", "total_pollutants", "acetaldehyde", "benzene", "formaldehyde"]
one_year_dfs = []
for feature in one_year_features:
	df = pd.read_csv("CDC_Data/one_year/" + feature + ".csv")
	df["state"] = map(lambda x: str(x).upper().strip(), df["state"])
	one_year_dfs.append(df)
	df.to_csv(year + "/" + year + "_" + feature + ".csv", index=False)

df1_labels = ["year", "county", "state", "copd_apc_" + year]
df2_labels = ["year", "county", "state", "copd_prev"]
df3_labels = ["year", "county", "state", "asthma_prev"]
df4_labels = ["year", "county", "state", "tobacco_prev"]
df5_labels = ["year", "county", "state", "med_income_5y"]
df6_labels = ["year", "county", "state", "perc_below_poverty_1y"]
df7_labels = ["year", "county", "state", "perc_below_poverty_5y"]
df8_labels = ["year", "county", "state", "unemployment_1y"]
df9_labels = ["year", "county", "state", "unemployment_5y"]


filter_features = ["copd_apc_" + year, "copd_prev", "asthma_prev", "tobacco_prev", "med_income_5y", "perc_below_poverty_1y", "perc_below_poverty_5y", "unemployment_1y", "unemployment_5y"]

df1_sub = df1[df1_labels]
df2_sub = df2[df2_labels]
df3_sub = df3[df3_labels]
df4_sub = df4[df4_labels]
df5_sub = df5[df5_labels]
df6_sub = df6[df6_labels]
df7_sub = df7[df7_labels]
df8_sub = df8[df8_labels]
df9_sub = df9[df9_labels]

merged = df1_sub.merge(df2_sub, on=["year", "county", "state"], how="outer").fillna("")
merged = merged.merge(df3_sub, on=["year", "county", "state"], how="outer").fillna("")
merged = merged.merge(df4_sub, on=["year", "county", "state"], how="outer").fillna("")
merged = merged.merge(df5_sub, on=["year", "county", "state"], how="outer").fillna("")
merged = merged.merge(df6_sub, on=["year", "county", "state"], how="outer").fillna("")
merged = merged.merge(df7_sub, on=["year", "county", "state"], how="outer").fillna("")
merged = merged.merge(df8_sub, on=["year", "county", "state"], how="outer").fillna("")
merged = merged.merge(df9_sub, on=["year", "county", "state"], how="outer").fillna("")


for i in range(0, len(one_year_features)):
	merged = merged.merge(one_year_dfs[i], on=["county", "state"], how="outer").fillna("")

label = "copd_apc_" + year
merged = merged[merged[label] != '']

'''
filter_features = filter_features + one_year_features
filter_features.remove("unemployment_5y")
filter_features.remove("benzene")
for label in filter_features:
    merged = merged[merged[label] != '']
'''
merged = merged.drop_duplicates(subset = ["county", "state"])
merged.to_csv(year + "/" + year + "_merged.csv", index=False)



