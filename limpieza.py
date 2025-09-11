import pandas as pd

# Carga archivo orginal 
df = pd.read_csv('pokemon_primera_gen.csv')

#Correccion 1: Magnemite / Magneton (quitar "Acero", quedar solo electrico) 
mask_magnet = df['Nombre'].isin(['Magnemite', 'Magneton'])
df.loc[mask_magnet, 'Tipo 1'] = 'Eléctrico'
df.loc[mask_magnet, 'Tipo 2'] = ''  

#Correccion 2: linea Clefairy/Jigglypuff y Mr. Mime (quitar "Hada") 
#Clefairy, Clefable, Jigglypuff, Wigglytuff a Normal
#Mr Mime a Psíquico
fairy_line = ['Clefairy', 'Clefable', 'Jigglypuff', 'Wigglytuff']
df.loc[df['Nombre'].isin(fairy_line), 'Tipo 1'] = 'Normal'
df.loc[df['Nombre'].isin(fairy_line), 'Tipo 2'] = ''

df.loc[df['Nombre'] == 'Mr. Mime', 'Tipo 1'] = 'Psíquico'
df.loc[df['Nombre'] == 'Mr. Mime', 'Tipo 2'] = ''


# Tildes faltantes en tipos
normaliza = {'Psiquico': 'Psíquico', 'Electrico': 'Eléctrico', 'Dragon': 'Dragón'}
df['Tipo 1'] = df['Tipo 1'].replace(normaliza)
df['Tipo 2'] = df['Tipo 2'].replace(normaliza)


# Guarda dataset limpio
df.to_csv('pokemon_primera_gen_limpio.csv', index=False)
print('OK: Guardado como pokemon_primera_gen_clean.csv')
