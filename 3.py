import pandas as pd 
df = pd.read_csv('pokemon_primera_gen_limpio.csv')

#Moda, mediana y promedio de la columna de ataque
mediana_ataque = df['Ataque'].median() 
print("\n\n---------------------------Mediana de todos los ataques de pokemons---------------------------\n\n", mediana_ataque) 

promedio_ataque = df['Ataque'].mean()
print("\n\n---------------------------Promedio de todos los ataques de pokemons---------------------------\n\n", promedio_ataque)

moda_ataque = df['Ataque'].mode()
print("\n\n---------------------------Moda de todos los ataques de pokemons---------------------------\n\n", moda_ataque)



# Pokémon con mayor defensa
mayor_defensa = df.loc[df['Defensa'].idxmax()]
print("\n\n---------------------------Pokemon con mayor defensa---------------------------\n\n", mayor_defensa['Nombre'], "-", mayor_defensa['Defensa'])

# Pokémon con menor velocidad
menor_velocidad = df.loc[df['Velocidad'].idxmin()]
print("\n\n---------------------------Pokemon con menor velocidad---------------------------\n\n", menor_velocidad['Nombre'], "-", menor_velocidad['Velocidad'])


#pokemon con dos tipos
dos_tipos = df[df['Tipo 2'].notna() & (df['Tipo 2'] !='')]
print(dos_tipos[['Nombre', 'Tipo 1', 'Tipo 2']])
