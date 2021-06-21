import pandas as pd
import json

READ_PATH = "D:/data/Data Science/proj/champ_cup_winner/data/championship/"

dict_champ = {}

# 2004-2005 was a lockout season, hence no data
for year in (list(range(2019, 2004, -1)) + list((range(2003, 1916, -1)))):
    print(year)
    df_champ = pd.read_html(READ_PATH + str(year) + ".html")
    dict_champ[year] = df_champ[9].to_dict()
    list_team_code = []
    for team_name in df_champ[9]["National Hockey LeagueNHL"]:
        list_team_code.append(team_name.strip()[-3:])
    dict_champ[year]["TeamCode"] = list_team_code

print(type(dict_champ))
json.dump(dict_champ, open(READ_PATH + "champ_all.json", "w"))

df_champ_all = pd.DataFrame({"champ_all": dict_champ})

# NOTE: converted rows to strings
df_champ_all.to_csv(READ_PATH + "champ_all.csv")