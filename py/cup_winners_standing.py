# Used to find team codes for further reference between championship and cup winner records
import pandas as pd

#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

#import requests

#DRIVER_PATH = 'D:/driver/chromedriver/chromedriver.exe'

SAVE_PATH = "D:/data/Data Science/proj/champ_cup_winner/data/championship/"

#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")

#driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#url = "https://records.nhl.com/standings/playoff-standings"

#response = requests.get(url)

#if(200 == response.status_code):
#    driver.get(url)
#    file_save = SAVE_PATH + "cup_winners_standings.html"
#    with open(file_save, "w", encoding="utf-8") as f:
#        f.write(driver.page_source)
#        f.close()

#driver.quit()

# Didn't work. Saved file didn't have resulting html table.

# Load manually saved page from browser
#df_cw_standing = pd.read_html(SAVE_PATH + "cup_winners_standings_from_browser.html")

#print(df_cw_standing)

# Manually saved page also didn't work

from tabula import read_pdf

df_cw_standing = read_pdf(SAVE_PATH + "NHL Records - Playoff Team Records.pdf")

# Manually entered codes based on downloaded table and https://en.wikipedia.org/wiki/Template:NHL_team_abbreviations
team_codes = ["MTL", "TOR", "DET", "BOS", "CHI", "EDM", "PIT", "NYI", "NYR", "SLE", "NJD", "COL", "LAK", "MMR", "PHI", "TBL", "ANA", "CGY", "CAR", "DAL", "STL", "WSH"]


# pdf worked
print(df_cw_standing[0]["FRANCHISE"])

team_name_split = {}
i = 0
for team_name in df_cw_standing[0]["FRANCHISE"]:
    print(team_name)
    print(team_name.split())
    team_name_split.update({i:team_name.split()})
    i = i + 1

print(team_name_split)

df_cw_standing[0]["TEAM_CODES"]  = team_codes

# only integer indices were saved by this manner
#df_cw_standing[0]["TEAM_NAME_SPLIT"]  = team_name_split

print(type(df_cw_standing))

# was saved as a string
pd.DataFrame({"cup_winners_standing": df_cw_standing}).to_csv(SAVE_PATH + "cup_winners_standing.csv")

# cup winners standing with team codes was entered manually afterwards