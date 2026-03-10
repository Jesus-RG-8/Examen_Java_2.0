import pandas as pd

# Serie
nba_players = pd.read_csv('C:\\DataFiles\\nba_players.csv', sep=';', usecols=['Name']).squeeze()

result_from_a = nba_players.sort_values()
result_from_z = nba_players.sort_values(ascending=False)

print(f'De la letra A a la letra Z: \n{result_from_a}')
print(f'De la letra Z a la letra A: \n{result_from_z}')