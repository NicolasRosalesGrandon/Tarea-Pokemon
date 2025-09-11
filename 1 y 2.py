import pandas as pd 

df = pd.read_csv('pokemon_primera_gen_limpio.csv')

print(df) #muestra todos los datos del archivo

fuego = df[df['Tipo 1'] == 'Fuego'][['Nombre', 'Tipo 1', 'Ataque', 'Velocidad']]
print(fuego) #muestra los pokemones de tipo fuego con sus respectivas columnas


