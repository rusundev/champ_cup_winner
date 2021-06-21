import pandas as pd

READ_PATH = "D:/data/Data Science/proj/champ_cup_winner/data/championship/"

url = "https://www.hockey-reference.com/playoffs/"

df_cup = pd.read_html(url)[0]

#print(df_cup)

df_cup.to_csv(READ_PATH + "cup.csv")

df_cup_all = pd.read_csv(READ_PATH + "cup.csv")
print(df_cup_all['Champion'][4])

# No 1920 cup winner!