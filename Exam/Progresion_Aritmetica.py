import pandas as pd


def validar_progresion_aritmetica(lista_numeros):
    # Convertimos la lista a una Serie de Pandas
    serie = pd.Series(lista_numeros)

    # Calculamos las diferencias entre números consecutivos
    # .diff() genera: [NaN, elemento2-elemento1, elemento3-elemento2, ...]
    diferencias = serie.diff().dropna()

    # Verificamos si todos los valores en 'diferencias' son iguales
    es_aritmetica = diferencias.nunique() == 1

    if es_aritmetica:
        d = diferencias.iloc[0]
        print(f"La serie es una Progresión Aritmética con diferencia d = {d}")
    else:
        print("La serie NO es una Progresión Aritmética")

    return es_aritmetica


# Pruebas
print("Prueba 1 (2, 4, 6, 14):")
validar_progresion_aritmetica([2, 4, 6, 8])

print("\nPrueba 2 (1, 3, 7, 10):")
validar_progresion_aritmetica([1, 3, 7, 10])