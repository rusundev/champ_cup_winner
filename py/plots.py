import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from itertools import compress

READ_PATH = "D:/data/Data Science/proj/champ_cup_winner/data/championship/"

df_cup_place = pd.read_csv(READ_PATH + "cup_winners_with_champ_places.csv")

#print(df_cup_place)

plt.scatter(df_cup_place['Year'], df_cup_place['Num_teams'], marker = 'o', color = 'b')

plt.scatter(df_cup_place['Year'], df_cup_place['Cup_winner_place'], marker = '^', color = 'r')

plt.scatter(df_cup_place['Year'], df_cup_place['Cup_runner_up_place'], marker = 'v', color = 'g')

plt.xticks(np.arange(1915, 2025, 5))

plt.yticks(np.arange(0, 35, 5))

font_title = {'family':'serif','color':'blue','size':20}
font_axis_label = {'family':'serif','color':'darkred','size':15}

plt.xlabel('Cup Year', fontdict = font_axis_label)
plt.ylabel('Number of Teams; Cup Winner Place, Runner-up Place', fontdict = font_axis_label)
plt.title('Number of Teams, Cup Winner and Runner-up Places in NHL by Cup Year', fontdict = font_title)
plt.legend(['Number of Teams', 'Winner Regular Season Place', 'Runner-up Regular Season Place'])

plt.grid()

plt.show()

# Plot of cup winner's place is higher or lower than that of runner-up
place_diff = df_cup_place['Cup_winner_place'] - df_cup_place['Cup_runner_up_place']

place_diff_plus = list(compress(df_cup_place['Year'], place_diff < 0))

place_diff_minus = list(compress(df_cup_place['Year'], place_diff > 0))

place_diff_plus_num = len(place_diff_plus)

place_diff_minus_num = len(place_diff_minus)

plt.subplot(2, 1, 1)

plt.pie([place_diff_plus_num, place_diff_minus_num], colors = ['r', 'g'])
plt.legend(["Higher: " + str(place_diff_plus_num), "Lower: " + str(place_diff_minus_num)])
#plt.title("Cup Winner Regular Season Place is Higher or Lower Than That of Runner-up?")

plt.subplot(2, 1, 2)

plt.scatter(place_diff_plus, np.repeat(10, place_diff_plus_num), marker = '+', color = 'r')
plt.scatter(place_diff_minus, np.repeat(-10, place_diff_minus_num), marker = '_', color = 'g')
plt.xticks(np.arange(1915, 2025, 5))
plt.yticks([-10, 10], ["Lower", "Higher"])
plt.xlabel("Cup Year")
plt.ylabel('Cup Winner Regular Season Place is Higher?')
#plt.title("Cup Winners' Regular Season Place is Higher?")
plt.legend(["Higher", "Lower"], loc = 'center right')
plt.grid()

plt.suptitle('Cup Winner vs. Runner-up Regular Season Place')
plt.show()


plt.subplot(2, 1, 1)
plt.hist(df_cup_place['Cup_winner_place'], bins = np.arange(0, 19) + 0.5, ec = "k", color = "red")
plt.xticks(np.arange(1, 19, 1))
plt.grid()
plt.xlabel("Regular Season Place")
plt.ylabel('Number of Occurences')
plt.title("Cup Winner Regular Season Places")

plt.subplot(2, 1, 2)
plt.hist(df_cup_place['Cup_runner_up_place'], bins = np.arange(0, 19) + 0.5, ec = "k", color = "green")
plt.xticks(np.arange(1, 19, 1))
plt.yticks(np.arange(0, 24, 2))
plt.grid()
plt.xlabel("Regular Season Place")
plt.ylabel('Number of Occurences')
plt.title("Runner-up Regular Season Places")

plt.suptitle('Cup Winner and Runner-up Regular Season Places Histograms')
plt.show()

df_cup_place['Cup_winner_place'].describe()

df_cup_place['Cup_runner_up_place'].describe()