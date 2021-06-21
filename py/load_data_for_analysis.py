import pandas as pd
import numpy as np

READ_PATH = "D:/data/Data Science/proj/champ_cup_winner/data/championship/"

df_champ_all = pd.read_csv(READ_PATH + "champ_all.csv")

df_cup_all = pd.read_csv(READ_PATH + "cup.csv")

df_cup_winners_with_code = pd.read_csv(READ_PATH + "cup_winners_with_codes.csv", sep = ";")

# adding columns for team codes to cup winners by year table
df_cup_all['Cup_winner_code'] = None
df_cup_all['Cup_runner_up_code']  = None

print(df_champ_all["champ_all"][100])

print(df_cup_all)

# loaded as string from pdf
# cup winners standing was entered manually into csv
print(df_cup_winners_with_code)

print(df_cup_all["Champion"][3])

print(type(df_cup_all["Champion"][3]))

print(df_cup_winners_with_code['TEAM_CODE'].str.find(df_cup_winners_with_code['TEAM_CODE'][3]))

print(df_cup_winners_with_code['TEAM_CODE'][3])

print(type(df_cup_winners_with_code['TEAM_CODE'][3]))

#df_champ_all["champ_all"][100]
#df_cup_winners_with_code['TEAM_CODE'].str.find(df_champ_all["champ_all"][100]["TeamCode"][0])

#df_cup_winners_with_code[df_cup_winners_with_code['FRANCHISE'].str.contains(df_cup_all["Champion"][2])]

#df_cup_all.dropna(inplace = True)

print("CUP WINNERS")

# filling cup winner and runner-up codes
for i in range(len(df_cup_all)):
    print(df_cup_all["Champion"][i])
    print(df_cup_all["Runner-Up"][i])

    ind_found_cup_winner = df_cup_winners_with_code["FRANCHISE"].str.contains(str(df_cup_all["Champion"][i]))
    if ind_found_cup_winner.any():
        df_cup_all["Cup_winner_code"][i] = df_cup_winners_with_code["TEAM_CODE"][ind_found_cup_winner]
        if df_cup_all["Cup_winner_code"][i] is not None:
            print('Cup Winner Not None')
            df_cup_all["Cup_winner_code"][i] = df_cup_all["Cup_winner_code"][i].item()
            #print(df_cup_all["Cup_winner_code"][i].item())
        #print(df_cup_winners_with_code["TEAM_CODE"][ind_found_cup_winner])
        #print(type(df_cup_all["Cup_winner_code"][i]))
        #print(df_cup_all["Cup_winner_code"][i])

    ind_found_cup_runner_up = df_cup_winners_with_code["FRANCHISE"].str.contains(str(df_cup_all["Runner-Up"][i]))
    if ind_found_cup_runner_up.any():
        df_cup_all["Cup_runner_up_code"][i] = df_cup_winners_with_code["TEAM_CODE"][ind_found_cup_runner_up]
        #print(df_cup_winners_with_code["TEAM_CODE"][ind_found_cup_runner_up])
        if df_cup_all["Cup_runner_up_code"][i] is not None:
            print('Cup Runner-Up Not None')
            df_cup_all["Cup_runner_up_code"][i] = df_cup_all["Cup_runner_up_code"][i].item()

    # filling cup winners and runners-up wit team codes
    #df_cup_all["Cup_winner_code"] = df_cup_winners_with_code["TEAM_CODE"][ df_cup_winners_with_code["FRANCHISE"].str.contains(str(df_cup_all["Champion"][i])) ].item()
    #df_cup_all["Runner_up_code"] = df_cup_winners_with_code["TEAM_CODE"][ df_cup_winners_with_code["FRANCHISE"].str.contains(str(df_cup_all["Runner-Up"][i])) ].item()

    #print(str(df_cup_all["Champion"][i]).split())
    #print(str(df_cup_all["Runner-Up"][i]).split())
    #df_cup_all["Cup_winner_split"][i] = df_cup_all["Champion"][i].split()
    #f_cup_all["Cup_runner_up_split"][i] = df_cup_all["Runner-Up"][i].split()
    #print(df_cup_all["Champion"][i].split())
    #cup_row["Cup_winner_code"] = cup_row["Champion"]
    #print(entry['Champion'])
    #print(entry['Runner-Up'])

print("REF")

# for search of team codes
#df_cup_winners_with_code['FRANCHISE_SPLIT'] = None
#for i in range(len(df_cup_winners_with_code)):
    #print(df_cup_winners_with_code['FRANCHISE'][i].split())
    #df_cup_winners_with_code['FRANCHISE_SPLIT'][i] = df_cup_winners_with_code['FRANCHISE'][i].split()
    #print(str(df_cup_winners_with_code['FRANCHISE'][i]).split())

#print(df_cup_winners_with_code["TEAM_CODE"][df_cup_winners_with_code["FRANCHISE"].str.contains(df_cup_all["Champion"][2])])

#print(type(df_cup_winners_with_code["TEAM_CODE"][df_cup_winners_with_code["FRANCHISE"].str.contains(df_cup_all["Champion"][2])]))

#print(df_cup_winners_with_code["TEAM_CODE"][df_cup_winners_with_code["FRANCHISE"].str.contains(df_cup_all["Champion"][2])].item())

#print(df_cup_all.to_string())

df_cup_all.to_csv(READ_PATH + "cup_all_codes.csv")