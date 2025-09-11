import pandas as pd
df = pd.read_csv('pokemon_primera_gen_limpio.csv')

#promedio, mediana y desviacion estandar de ataque tipo 1 
ataque_stats = df.groupby('Tipo 1') ['Ataque'].agg(['mean', 'median', 'std'])
print('Promedio, mediana y desviacion estandar de ataque por Tipo 1:')
print(ataque_stats)

#Tipo con mayor promedio de velocidad
velocidad_promedio = df.groupby('Tipo 1')['Velocidad'].mean()
tipo_mayor_velocidad = velocidad_promedio.idxmax()
print(f'\nTipo con mayor promedio de velocidad: {tipo_mayor_velocidad} ({velocidad_promedio[tipo_mayor_velocidad]:.2f})')


#Pokmon con mayor y menor PS por tipo 1
mayor_ps = df.loc[df.groupby('Tipo 1')['PS'].idxmax()][['Tipo 1', 'Nombre', 'PS']]
menor_ps = df.loc[df.groupby('Tipo 1')['PS'].idxmin()][['Tipo 1', 'Nombre', 'PS']]
print('\nPokémon con mayor PS por Tipo 1:')
print(mayor_ps)
print('\nPokémon con menor PS por Tipo 1:')
print(menor_ps)


