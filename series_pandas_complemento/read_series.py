import pandas as pd

# Leer el archivo CSV y seleccionar solo la columna 'Name'
nba_players = pd.read_csv('C:\\DataFiles\\nba_players.csv', sep=',', usecols=  ['Name']  ).squeeze()

# Funcion describe
print(f'la funcion dexcribe con una serie {nba_players.describe()}')

#funcion head
print(f'los primeros 5 nombres son : \n {nba_players.head()}')

print(f'\n\nlos primeros 5 nombres son : \n {nba_players.head(10)}')

#funcion tail
print(f'\n\nultimos 5 elementos de una serie : {nba_players.tail()}')
print(f'\n\nultimos 10 elementos de una serie : {nba_players.tail(10)}')