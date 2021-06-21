from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import requests

DRIVER_PATH = 'D:/driver/chromedriver/chromedriver.exe'

SAVE_PATH = "D:/data/Data Science/proj/champ_cup_winner/data/championship/"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

for year in range(2019, 1916, -1):
    url = "https://www.nhl.com/standings/" + str(year) + "/league"
    
    response = requests.get(url)

    if(200 == response.status_code):
        driver.get(url)
        file_save = SAVE_PATH + str(year) + ".html"
        with open(file_save, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            f.close()

driver.quit()