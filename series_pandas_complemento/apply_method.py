import pandas as pd

def convert_upper(value):
    return value.upper()

nba_players_name = pd.read_csv(f'C:\\DataFiles\\nba_players.csv',sep=';', usecols=['Name']).squeeze()

result = nba_players_name.apply(convert_upper).head()

print(result)