# -*- coding: utf-8 -*-
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#%%
# Valores lidos pelo hotspot do notebook
rssi_values_notebook = {"rssi" : list(),
               "distance" : list(),
               }

# bem próximo
rssi_values_notebook["rssi"].extend([-35, -37, -37])
rssi_values_notebook["distance"].extend([0,0,0])

# 0.5m
rssi_values_notebook["rssi"].extend([-41, -42, -39])
rssi_values_notebook["distance"].extend([0.5, 0.5, 0.5])

# 1m
rssi_values_notebook["rssi"].extend([-42, -42, -41])
rssi_values_notebook["distance"].extend([1, 1, 1])

# 1.5m
rssi_values_notebook["rssi"].extend([-51, -51, -53])
rssi_values_notebook["distance"].extend([1.5, 1.5, 1.5])

# 2m
rssi_values_notebook["rssi"].extend([-55, -53, -52])
rssi_values_notebook["distance"].extend([2, 2, 2])

# 2.5m
rssi_values_notebook["rssi"].extend([-64, -55, -51])
rssi_values_notebook["distance"].extend([2.5, 2.5, 2.5])

# 3m
rssi_values_notebook["rssi"].extend([-56, -55, -62])
rssi_values_notebook["distance"].extend([3, 3, 3])

# 3.5m
rssi_values_notebook["rssi"].extend([-63, -63, -64])
rssi_values_notebook["distance"].extend([3.5, 3.5, 3.5])

# 4m
rssi_values_notebook["rssi"].extend([-69, -62, -62])
rssi_values_notebook["distance"].extend([4, 4, 4])

# 4.5m
rssi_values_notebook["rssi"].extend([-70, -66, -70])
rssi_values_notebook["distance"].extend([4.5, 4.5, 4.5])

# 5m
rssi_values_notebook["rssi"].extend([-74, -74, -72])
rssi_values_notebook["distance"].extend([5, 5, 5])

#%%
# generate 2d classification dataset
df_notebook = pd.DataFrame(data=rssi_values_notebook) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

X_notebook = pd.DataFrame(data = df_notebook, columns=['rssi'])
y_notebook = pd.DataFrame(data = df_notebook, columns=['distance'])

#%%
# Treinamento do modelo usando regressão linear
# https://www.datageeks.com.br/regressao-linear/
model_distance_notebook = LinearRegression()
model_distance_notebook.fit(X_notebook,y_notebook)

y_notebook_pred = model_distance_notebook.predict(X_notebook)

# metricas
print("\nNotebook")
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_notebook - y_notebook_pred)))
print("Residual sum of squares: %.2f" % np.mean((y_notebook - y_notebook_pred)**2))
print("R2-score: %.2f\n" % r2_score(y_notebook, y_notebook_pred))

#%%

plt.plot(y_notebook, X_notebook, 'ro', y_notebook_pred, X_notebook)
plt.xlabel('Distance (m)')
plt.ylabel('RSSI (dBm)')
plt.title("Notebook-hotspot distance")

############################# Roteador ###########################

#%%
# Valores lidos pelo roteador
rssi_values_router = {"rssi" : list(),
               "distance" : list(),
               }

# bem próximo
rssi_values_router["rssi"].extend([-35, -35, -35])
rssi_values_router["distance"].extend([0,0,0])

# 0.5m
rssi_values_router["rssi"].extend([-39, -40, -39])
rssi_values_router["distance"].extend([0.5, 0.5, 0.5])

# 1m
rssi_values_router["rssi"].extend([-37, -37, -37])
rssi_values_router["distance"].extend([1, 1, 1])

# 1.5m
rssi_values_router["rssi"].extend([-53, -52, -51])
rssi_values_router["distance"].extend([1.5, 1.5, 1.5])

# 2m
rssi_values_router["rssi"].extend([-46, -47, -47])
rssi_values_router["distance"].extend([2, 2, 2])

# 2.5m
rssi_values_router["rssi"].extend([-51, -51, -51])
rssi_values_router["distance"].extend([2.5, 2.5, 2.5])

# 3m
rssi_values_router["rssi"].extend([-61, -59, -59])
rssi_values_router["distance"].extend([3, 3, 3])

# 3.5m
rssi_values_router["rssi"].extend([-58, -58, -58])
rssi_values_router["distance"].extend([3.5, 3.5, 3.5])

# 4m
rssi_values_router["rssi"].extend([-62, -64, -64])
rssi_values_router["distance"].extend([4, 4, 4])

# 4.5m
rssi_values_router["rssi"].extend([-62, -62, -62])
rssi_values_router["distance"].extend([4.5, 4.5, 4.5])

# 5m
rssi_values_router["rssi"].extend([-58, -58, -58])
rssi_values_router["distance"].extend([5, 5, 5])

#%%
# generate 2d classification dataset
df_router = pd.DataFrame(data=rssi_values_router) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

X_router = pd.DataFrame(data = df_router, columns=['rssi'])
y_router = pd.DataFrame(data = df_router, columns=['distance'])

#%%
# Treinamento do modelo usando regressão linear
# https://www.datageeks.com.br/regressao-linear/
model_distance_router = LinearRegression()
model_distance_router.fit(X_router,y_router)

y_router_pred = model_distance_router.predict(X_router)

# metricas
print("Router")
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_router - y_router_pred)))
print("Residual sum of squares: %.2f" % np.mean((y_router - y_router_pred)**2))
print("R2-score: %.2f\n" % r2_score(y_router, y_router_pred))

#%%

plt.plot(y_router, X_router, 'ro', y_router_pred, X_router)
plt.xlabel('Distance (m)')
plt.ylabel('RSSI (dBm)')
plt.title("Router distance")

############################# Repetidora ###########################

#%%
# Valores lidos pela repetidora
rssi_values_repeater = {"rssi" : list(),
               "distance" : list(),
               }

# bem próximo
rssi_values_repeater["rssi"].extend([-27, -27, -27])
rssi_values_repeater["distance"].extend([0,0,0])

# 0.5m
rssi_values_repeater["rssi"].extend([-34, -34, -33])
rssi_values_repeater["distance"].extend([0.5, 0.5, 0.5])

# 1m
rssi_values_repeater["rssi"].extend([-36, -36, -36])
rssi_values_repeater["distance"].extend([1, 1, 1])

# 1.5m
rssi_values_repeater["rssi"].extend([-36, -35, -35])
rssi_values_repeater["distance"].extend([1.5, 1.5, 1.5])

# 2m
rssi_values_repeater["rssi"].extend([-39, -39, -38])
rssi_values_repeater["distance"].extend([2, 2, 2])

# 2.5m
rssi_values_repeater["rssi"].extend([-39, -39, -39])
rssi_values_repeater["distance"].extend([2.5, 2.5, 2.5])

# 3m
rssi_values_repeater["rssi"].extend([-40, -38, -39])
rssi_values_repeater["distance"].extend([3, 3, 3])

# 3.5m
rssi_values_repeater["rssi"].extend([-40, -40, -38])
rssi_values_repeater["distance"].extend([3.5, 3.5, 3.5])

# 4m
rssi_values_repeater["rssi"].extend([-40, -41, -41])
rssi_values_repeater["distance"].extend([4, 4, 4])

# 4.5m
rssi_values_repeater["rssi"].extend([-44, -44, -44])
rssi_values_repeater["distance"].extend([4.5, 4.5, 4.5])

# 5m
rssi_values_repeater["rssi"].extend([-42, -42, -43])
rssi_values_repeater["distance"].extend([5, 5, 5])

#%%
# generate 2d classification dataset
df_repeater = pd.DataFrame(data=rssi_values_repeater) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

X_repeater = pd.DataFrame(data = df_repeater, columns=['rssi'])
y_repeater = pd.DataFrame(data = df_repeater, columns=['distance'])

#%%
# Treinamento do modelo usando regressão linear
# https://www.datageeks.com.br/regressao-linear/
model_distance_repeater = LinearRegression()
model_distance_repeater.fit(X_repeater,y_repeater)

y_repeater_pred = model_distance_repeater.predict(X_repeater)

# metricas
print("Repeater")
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_repeater - y_repeater_pred)))
print("Residual sum of squares: %.2f" % np.mean((y_repeater - y_repeater_pred)**2))
print("R2-score: %.2f\n" % r2_score(y_repeater, y_repeater_pred))

#%%

plt.plot(y_repeater, X_repeater, 'ro', y_repeater_pred, X_repeater)
plt.xlabel('Distance (m)')
plt.ylabel('RSSI (dBm)')
plt.title("Repeater distance")

#%%
# Salvando os modelos
import pickle

filename = "distance_linear_regression.sav"
pickle.dump(model_distance_notebook, open("notebook_" + filename, 'wb'))
pickle.dump(model_distance_router, open("router_" + filename, 'wb'))
pickle.dump(model_distance_repeater, open("repeater_" + filename, 'wb'))