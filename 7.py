import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon_primera_gen_limpio.csv')



# Tipos con mayor ataque o defensa (estadistica)
stats = df.groupby('Tipo 1')[['Ataque', 'Defensa']].mean()
print(stats)

# Correlacion entre ataque y velocidad 
corr = df['Ataque'].corr(df['Velocidad'])
print(f"\nCoeficiente de correlacion entre Ataque y Velocidad: {corr:.2f}")

# Dispersion de PS por tipo (desviacion estandar)
ps_std = df.groupby('Tipo 1')['PS'].std()
print('\nDesviacion estandar de PS por Tipo 1:')
print(ps_std)

# Boxplot para identificar outliers en ataque y PS 
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
df.boxplot(column='Ataque')
plt.title('Boxplot de Ataque')
plt.subplot(1,2,2)
df.boxplot(column='PS')
plt.title('Boxplot de PS')
plt.tight_layout()
plt.show()