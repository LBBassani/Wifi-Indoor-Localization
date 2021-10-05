# -*- coding: utf-8 -*-
#%%
import pickle
import pandas as pd
import numpy as np

#%%

# load the model from disk
file_name = "distance_linear_regression.sav"
notebook_model = pickle.load(open("notebook_" + file_name, 'rb'))   # ponto A
repeater_model = pickle.load(open("repeater_" + file_name, 'rb'))   # ponto B
router_model = pickle.load(open("router_" + file_name, 'rb'))       # ponto C


#%%
# Constantes do domínio
d = 5.3845
A = (0,0)   # ponto A : notebook-hotspot
B = (d, 0)  # ponto B : repeater
C = (d, d)  # ponto C : router

D1 = (d/2,0)        # Ponto de aferição perto do espelho
D2 = (d/2, d/2)     # Ponto de aferição no corredor
D3 = (2*d/3, d/3)   # Ponto de aferição perto da mesa

#%%
# Aferições
rssi_values_notebook = {"rssi" : list(),
                        "pontos_x" : list(),
                        "pontos_y" : list()
                        }

# No ponto D1
rssi_values_notebook["rssi"].extend([-68, -65, -63, -66, -71, -71])
rssi_values_notebook["pontos_x"].extend([D1[0], D1[0], D1[0], D1[0], D1[0], D1[0]])
rssi_values_notebook["pontos_y"].extend([D1[1], D1[1], D1[1], D1[1], D1[1], D1[1]])

# No ponto D2
rssi_values_notebook["rssi"].extend([-72, -70, -73, -70, -70, -71])
rssi_values_notebook["pontos_x"].extend([D2[0], D2[0], D2[0], D2[0], D2[0], D2[0]])
rssi_values_notebook["pontos_y"].extend([D2[1], D2[1], D2[1], D2[1], D2[1], D2[1]])

# No ponto D3
rssi_values_notebook["rssi"].extend([-69, -72, -73, -73, -71, -77])
rssi_values_notebook["pontos_x"].extend([D3[0], D3[0], D3[0], D3[0], D3[0], D3[0]])
rssi_values_notebook["pontos_y"].extend([D3[1], D3[1], D3[1], D3[1], D3[1], D3[1]])

rssi_values_router = {"rssi" : list(),
                        "pontos_x" : list(),
                        "pontos_y" : list()
                        }

# No ponto D1
rssi_values_router["rssi"].extend([-57, -61, -62, -61, -63, -61])
rssi_values_router["pontos_x"].extend([D1[0], D1[0], D1[0], D1[0], D1[0], D1[0]])
rssi_values_router["pontos_y"].extend([D1[1], D1[1], D1[1], D1[1], D1[1], D1[1]])

# No ponto D2
rssi_values_router["rssi"].extend([-57, -57, -56, -57, -57, -56])
rssi_values_router["pontos_x"].extend([D2[0], D2[0], D2[0], D2[0], D2[0], D2[0]])
rssi_values_router["pontos_y"].extend([D2[1], D2[1], D2[1], D2[1], D2[1], D2[1]])

# No ponto D3
rssi_values_router["rssi"].extend([-53, -52, -53, -53, -54, -53])
rssi_values_router["pontos_x"].extend([D3[0], D3[0], D3[0], D3[0], D3[0], D3[0]])
rssi_values_router["pontos_y"].extend([D3[1], D3[1], D3[1], D3[1], D3[1], D3[1]])

rssi_values_repeater = {"rssi" : list(),
                        "pontos_x" : list(),
                        "pontos_y" : list()
                        }

# No ponto D1
rssi_values_repeater["rssi"].extend([-54, -37, -37, -38, -37, -40])
rssi_values_repeater["pontos_x"].extend([D1[0], D1[0], D1[0], D1[0], D1[0], D1[0]])
rssi_values_repeater["pontos_y"].extend([D1[1], D1[1], D1[1], D1[1], D1[1], D1[1]])

# No ponto D2
rssi_values_repeater["rssi"].extend([-48, -49, -49, -49, -48, -48])
rssi_values_repeater["pontos_x"].extend([D2[0], D2[0], D2[0], D2[0], D2[0], D2[0]])
rssi_values_repeater["pontos_y"].extend([D2[1], D2[1], D2[1], D2[1], D2[1], D2[1]])

# No ponto D3
rssi_values_repeater["rssi"].extend([-48, -50, -50, -48, -49, -51])
rssi_values_repeater["pontos_x"].extend([D3[0], D3[0], D3[0], D3[0], D3[0], D3[0]])
rssi_values_repeater["pontos_y"].extend([D3[1], D3[1], D3[1], D3[1], D3[1], D3[1]])

#%%
df_notebook = pd.DataFrame(data=rssi_values_notebook) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
X_notebook = pd.DataFrame(data = df_notebook, columns=['rssi'])

df_repeater = pd.DataFrame(data=rssi_values_repeater) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
X_repeater = pd.DataFrame(data = df_repeater, columns=['rssi'])

df_router = pd.DataFrame(data=rssi_values_router) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
X_router = pd.DataFrame(data = df_router, columns=['rssi'])

e = notebook_model.predict(X_notebook)    # Distancias a partir do ponto A
f = repeater_model.predict(X_repeater)    # Distancias a partir do ponto B
g = router_model.predict(X_router)        # Distancias a partir do ponto C


#%%
x = list()
y = list()
p = q = r = d
for i in range(e.size):
    x.append((e[i]**2 - f[i]**2 + p**2)/2*d)
    y.append((e[i]**2 - g[i]**2 + q**2 + r**2)/2*r - x[i]*q/r)



