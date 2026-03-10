import pandas as pd

nba_players = pd.read_csv(r'C:\\DataFiles\\nba_players.csv',sep=';', usecols=['Name']).squeeze()

single_value = nba_players.iloc[15]
print(single_value)

multi_values = nba_players.iloc[:15].tolist()
multi_values_2 = nba_players.iloc[:15]
print(multi_values)
print(len(multi_values))

print(type(multi_values))
print(type(multi_values_2))