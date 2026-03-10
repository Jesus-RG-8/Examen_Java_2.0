import pandas as pd

# Leer el archivo CSV y seleccionar solo la columna 'Name'
nba_players_name = pd.read_csv('C:\\DataFiles\\nba_players.csv', sep=';', usecols=['Name']).squeeze()
nba_players_age = pd.read_csv('C:\\DataFiles\\nba_players.csv', sep=';', usecols=  ['AGE']  ).squeeze()

df = pd.read_csv(r"C:\DataFiles\nba_players.csv", sep=',', encoding='latin-1')
print(df.columns.tolist())


print(f'\nombre de los jugadores : \n{nba_players_name}')
print(f'\nedad de los jugadores : \n{nba_players_age}')

print(f'Función LEN: {len(nba_players_name)}')
print(f'Función TYPE: {type(nba_players_name)}')
print(f'Función SORTED: {sorted(nba_players_age)}')
print(f'Función MAX: {max(nba_players_age)}')
print(f'Función MIN: {min(nba_players_age)}')