import pandas as pd

nba_players = pd.read_csv(filepath_or_buffer=r'C:\DataFiles\nba_players.csv',sep=';' ,usecols=['DRtg']).squeeze()
some_values = nba_players.iloc[:5]

addition_1 = some_values + 10
addition_2 = some_values.add(10)

print("Realización de una suma")
print(some_values)
print(addition_1)
print(addition_2)

# Restas
print("Realización de una resta")
subtract_1 = some_values - 10
subtract_2 = some_values.sub(10)

print(subtract_1)
print(subtract_2)

# Multiplicaciones
print("Realización de una multiplicacion")
mult_1 = some_values * 10
mult_2 = some_values.mul(10)

print(mult_1)
print(mult_2)

# diviciones
print("Realización de una divicion")
div_1 = some_values / 10
div_2 = some_values.div(10)

print(div_1)
print(div_2)