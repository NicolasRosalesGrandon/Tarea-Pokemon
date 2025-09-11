import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon_primera_gen_limpio.csv')

# Histograma de los valores de ataque
plt.hist(df['Ataque'], bins=20, color='blue', edgecolor='black')
plt.title('Distribucion de valores de ataque de Pokemon de Primera Generacion')
plt.xlabel('Valor de ataque')
plt.ylabel('Numero de Pokemons')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Grafico de dispersion entre ataque y velocidad
plt.scatter(df['Ataque'], df['Velocidad'], color='red', alpha=0.6)
plt.title('Dispersion entre ataque y velocidad de Pokemon de Primera Generacion')
plt.xlabel('Ataque')
plt.ylabel('Velocidad')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Boxplot de los PS por tipo principal (Tipo 1)
plt.figure(figsize=(10,6))
df.boxplot(column='PS', by='Tipo 1', grid=False)
plt.title('Boxplot de PS por tipo principal (Tipo 1)')
plt.suptitle('')
plt.xlabel('Tipo principal (Tipo 1)')
plt.ylabel('PS')
plt.xticks(rotation=45)
plt.show()

# Diagrama de violin de la defensa por tipo principal (Tipo 1)
plt.figure(figsize=(10,6))
sns.violinplot(x='Tipo 1', y='Defensa', data=df)
plt.title('Distribucion de la defensa por tipo principal (Diagrama de violin)')
plt.xlabel('Tipo principal (Tipo 1)')
plt.ylabel('Defensa')
plt.xticks(rotation=45)
plt.show()