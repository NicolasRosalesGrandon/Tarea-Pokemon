import pandas as pd
df = pd.read_csv('pokemon_primera_gen_limpio.csv')

#crear la columna "poder total" como suma de ataque, defensa, velocidad y PS
df['Poder Total'] = df['Ataque'] + df['Defensa'] + df['Velocidad'] + df['PS']

#ordenar el data frae por poder total de mayor a menor
df = df.sort_values(by= 'Poder Total', ascending=False)

print(df[['Nombre', 'Ataque', 'Defensa', 'Velocidad', 'PS', 'Poder Total']]. head() )