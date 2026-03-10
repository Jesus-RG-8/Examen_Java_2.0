import pandas as pd
from pandas.core.interchange.from_dataframe import  primitive_column_to_ndarray
nba_players_df = pd.read_csv(f'C:\\DataFiles\\nba_players.csv',sep=';',usecols=['Name']).head(5)

nba_players_copy = nba_players_df.squeeze().copy()
nba_players_view = nba_players_df.squeeze()


nba_players_copy.iloc[0] = 'Lemna'
nba_players_view.iloc[0] = 'UVTV'


print("DataFrame original:")
print(nba_players_df)

print("\nCopia modificada:")
print(nba_players_copy)

print("\nVista modificada:")
print(nba_players_view)