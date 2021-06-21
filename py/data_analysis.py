import pandas as pd
import numpy as np
import json

READ_PATH = "D:/data/Data Science/proj/champ_cup_winner/data/championship/"

df_champ_all = pd.read_csv(READ_PATH + "champ_all.csv")

df_cup_all = pd.read_csv(READ_PATH + "cup_winner_cleaned.csv", sep = ";")

df_champ_json = json.load(open(READ_PATH + "champ_all.json"))

#print(pd.DataFrame({0: df["1918"]["TeamCode"]}))
#print(pd.DataFrame(df["2019"]["TeamCode"]))

df_champ_year = pd.DataFrame({"TeamCode": df_champ_json["2019"]["TeamCode"]})
print(type(df_champ_year))

print(type(df_champ_year["TeamCode"]))

print(type([df_champ_year["TeamCode"]]))

#print(df_champ_year.loc[df_champ_year["TeamCode"] == "STL"].index.get_loc())

#print(type(df_champ_year[df_champ_year["TeamCode"] == "STL"]))

print(type(df_champ_year["TeamCode"] == "STL"))

print(type(df_champ_year[df_champ_year["TeamCode"] == "STL"].index.values))

print(df_champ_year.loc[df_champ_year["TeamCode"] == "STL"].index.values.item())

place = df_champ_year.loc[df_champ_year["TeamCode"] == "STL"].index.values.item() + 1

#print(type(df_champ_year["TeamCode"].str.find("STL")))

# No 1920 cup winner!

# adding columns for team codes to cup winners by year table
df_cup_all["Cup_winner_place"] = None
df_cup_all["Cup_runner_up_place"]  = None
df_cup_all["Num_teams"] = None

print(len(df_champ_json))

print(len(df_cup_all))

print(df_cup_all)

for i in range(len(df_cup_all)):
    # get corresponding cup winner and runner-up codes
    cup_winner_code = df_cup_all["Cup_winner_code"][i]
    cup_runner_up_code = df_cup_all["Cup_runner_up_code"][i]
    print(cup_winner_code)
    print(cup_runner_up_code)

    year = df_cup_all['Year'][i]
    year_champ = year - 1
    print(year)

    #print(year)
    #print(year_champ)
    #print(df_champ_json[str(year_champ)]["TeamCode"])
    df_champ_year_team_code = pd.DataFrame({"TeamCode": df_champ_json[str(year_champ)]["TeamCode"]})
    print(df_champ_year_team_code)
    place_cup_winner = df_champ_year_team_code.loc[cup_winner_code == df_champ_year_team_code["TeamCode"]].index.values.item() + 1
    print(place_cup_winner)
    place_cup_runner_up = df_champ_year_team_code.loc[cup_runner_up_code == df_champ_year_team_code["TeamCode"]].index.values.item() + 1
    print(place_cup_runner_up)
    #print(place_cup_winner, place_cup_runner_up)

    df_cup_all["Cup_winner_place"][i] = place_cup_winner
    df_cup_all["Cup_runner_up_place"][i] = place_cup_runner_up
    df_cup_all["Num_teams"][i] = len(df_champ_year_team_code["TeamCode"])

df_cup_all.to_csv(READ_PATH + "cup_winners_with_champ_places.csv")

print(df_cup_all.to_string())