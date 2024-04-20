import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# tenemos un data set de unos cuantos paises , lo vamos a cargar
url = "https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv"
df = pd.read_csv(url, encoding="ISO-8859-1")



#1 al inicio el dataset viene con una columna inecesario que se llama ' Unnamed: 0' y como no tiene ningun dato revelante vamos a eliminarla
df.drop(columns=['Unnamed: 0'], inplace=True)

# see how many country per region
print(df['region'].value_counts())
#print(df.groupby(['region'])['country'].count())

"""

    Index(['country', 'region', 'gdp', 'school', 'adfert', 'chldmort', 'life',
       'pop', 'urban', 'femlab', 'literacy', 'co2', 'gini']
"""

#   ¿Cuántos países tienen índices de CO_2 mayores que el promedio?
df['co2_x_encima'] = np.where(df['co2'] > df['co2'].mean(), 1, 0)
print(df['co2_x_encima'].value_counts()[1])
# asi te devuelve los datos enteros de aquellos paises con  un nivel de co2 por encima del promedio y para ver el tamaño como siempre usamos la funcion  len | value_counts() que devuelve la cantidad de valores unicos
#print(len(cantidad))
"""
    resultado_bool = df['co2'] > df['co2'].mean() # devuelve vdd o falso en base a los resultados pero igual si queremos ver los paises que si superan el promedio solo hay que pasarle al dataframe como lo que es : Un booleano que tiene quee filtrar y devolver los valores ddonde el resultado salio positivo
    #print(df[resultado_bool])

"""
#    ¿Que se puede decir del alfabetismo en áfrica o europa?
"""
    Lo que podriamos hacer es buscar el promedio de personsa alfabetizadas por regiones
    y luego compararlo para tener una idea del margen que existe
"""
df_africa = df[df['region'] == 'Africa']
df_europa = df[df['region'] == 'Europe']
literacy_diff = np.where(df_africa['literacy'].mean() > df_europa['literacy'].mean(), 'Tasa de alfabetismo de Africa superior a la de Europa', 'Tasa de alfabetismo inferior')
print(literacy_diff) # la tasa de alfabetismo de africa no es superior a la de euroa



# Ahora utilizaremos gráficos de barras para observar comparaciones de comportamiento de regiones versus el resto del mundo.Ya habíamos creado los filtros de df_africa y df_europa, con esto vamos a comparar la mortalidad infantil.

df_euafr = df.loc[df['region'].isin(['Europe', 'Africa'])]
sns.barplot(data=df_euafr, x='region', y='chldmort', errorbar=None)
plt.title('Tasa mortalidad infantil entre Africa y Europa !')
plt.xlabel('Continente')
plt.ylabel('Tasa de Mortalidad')
plt.savefig('chldmort_afr_eu.png')

# Comparacion entre el nivel de alfabetismo
df_america = df[df['region'] == 'Americas']
df_resto_mundo = df[~df['region'].isin(['Europe', 'Africa', 'Americas'])]
alfabetismo_america = df_america['literacy'].mean()
alfabetismo_africa = df_africa['literacy'].mean()
alfabetismo_europa = df_europa['literacy'].mean()
alfabetismo_resto_mundo = df_resto_mundo['literacy'].mean()

sns.catplot(x=['Americas', 'Africa', 'Europa',  'Resto del mundo'], y=[alfabetismo_america, alfabetismo_africa, alfabetismo_europa, alfabetismo_resto_mundo], kind='bar')
plt.title('Alfabetismo Por Regiones')
plt.savefig('alfabetismo_regiones.png')

#z ahora queremos ver la distribucion de escuelas en el munddo
sns.catplot(x=df['region'], y=df['school'], kind='box')
plt.title('Distribucion de escuelas')
#plt.show()
plt.savefig('Escuelas_distribucion.png')


# vamos a limpiar el dato, eliminando las filas sin un dato revelante
df_limpio = df.dropna()

#Teniendo data adecuada, procedemos a observar la dispersión de los años de escolaridad sobre el grado de alfabetismo
sns.scatterplot(x=df_limpio['school'], y=df_limpio['literacy'])
plt.title('Escolaridad _ Grade Alfabetismo')
plt.savefig('escolaridad_regiones.png')


