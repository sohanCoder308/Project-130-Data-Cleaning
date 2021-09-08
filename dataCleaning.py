import pandas as pd

df = pd.read_csv("dwarf_stars.csv")
print("Before removing unwanted columns ", df.columns)

# The below code is not working for stars data csv as it 
# has duplicate columns and unnamed columns -->
# del df["Unnamed: 0"]
# del df["Unnamed: 6"]
# del df["Star_name.1"]
# del df["Distance.1"]
# del df["Mass.1"]
# del df["Radius.1"]
# del df["Luminosity"]

# This code is working -->
df.drop(['Unnamed: 0', 'Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1', 'Luminosity'], axis = 1, inplace = True)
print("After removing unwanted columns ", df.columns)

# The below is code to also remove the rows with null and error giving values
final_data = df.dropna()
final_data.reset_index(drop=True, inplace=True)
final_data.head(5)

final_data.to_csv("final_stars_sorted_cleaned_data.csv")