# -*- coding: utf-8 -*-
"""teste_cubic_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10b6mpuvUN4tg3R9rtyLwSeGHgrBWZoSr
"""

# -*- coding: utf-8 -*-
#%%
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from math import sqrt
from sklearn.preprocessing import PolynomialFeatures

from dominio import *
from teste_1 import *

#%%

poly3 = PolynomialFeatures(degree = 3)

# load the model from disk
file_name = "distance_cubic_regression.sav"
notebook_model = pickle.load(open("notebook_" + file_name, 'rb'))   # ponto A
repeater_model = pickle.load(open("repeater_" + file_name, 'rb'))   # ponto B
router_model = pickle.load(open("router_" + file_name, 'rb'))       # ponto C

#%%
df_notebook = pd.DataFrame(data=rssi_values_notebook) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
X_notebook = pd.DataFrame(data = df_notebook, columns=['rssi'])

X_notebook_poly3 = poly3.fit_transform(X_notebook)

df_repeater = pd.DataFrame(data=rssi_values_repeater) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
X_repeater = pd.DataFrame(data = df_repeater, columns=['rssi'])

X_repeater_poly3 = poly3.fit_transform(X_repeater)

df_router = pd.DataFrame(data=rssi_values_router) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
X_router = pd.DataFrame(data = df_router, columns=['rssi'])

X_router_poly3 = poly3.fit_transform(X_router)

e = notebook_model.predict(X_notebook_poly3)    # Distancias a partir do ponto A
f = repeater_model.predict(X_repeater_poly3)    # Distancias a partir do ponto B
g = router_model.predict(X_router_poly3)        # Distancias a partir do ponto C

#%%
e_real = [d/2]*6
e_real.extend([sqrt((d/2)**2 + (d/2)**2)]*6)
e_real.extend([sqrt((2*d/3)**2 + (d/3)**2)]*6)
e_real = pd.DataFrame(data = e_real, columns=['distance'])

e_pred = pd.DataFrame(data= e, columns=['distance'])
print("Erros no modelo do notebook:")
print("Mean absolute error: %.2f" % np.mean(np.absolute( e_real - e_pred)))
print("Residual sum of squares: %.2f" % np.mean((e_real - e_pred)**2))
print("R2-score: %.2f" % r2_score(e_real, e_pred))


#%%
f_real = [d/2]*6
f_real.extend([sqrt((d/2)**2 + (d/2)**2)]*6)
f_real.extend([sqrt((2*d/3)**2 + (d/3)**2)]*6)
f_real = pd.DataFrame(data= f_real, columns=['distance'])

f_pred = pd.DataFrame(data= f, columns=['distance'])
print("Erros no modelo da repetidora:")
print("Mean absolute error: %.2f" % np.mean(np.absolute( f_real - f_pred)))
print("Residual sum of squares: %.2f" % np.mean((f_real - f_pred)**2))
print("R2-score: %.2f" % r2_score(f_real, f_pred))

#%%
g_real = [sqrt((d/2)**2 + (d)**2)]*6
g_real.extend([sqrt((d/2)**2 + (d/2)**2)]*6)
g_real.extend([sqrt((d - 2*d/3)**2 + (d - d/3)**2)]*6)
g_real = pd.DataFrame(data= g_real, columns=['distance'])

g_pred = pd.DataFrame(data= g, columns=['distance'])
print("Erros no modelo do roteador:")
print("Mean absolute error: %.2f" % np.mean(np.absolute( g_real - g_pred)))
print("Residual sum of squares: %.2f" % np.mean((g_real - g_pred)**2))
print("R2-score: %.2f" % r2_score(g_real, g_pred))

#%%
x = list()
y = list()
p = q = r = d
for i in range(e.size):
    x.append( (e[i]**2 - f[i]**2 + p**2)/(2*p) )
    y.append( (e[i]**2 - g[i]**2 + q**2 + r**2)/(2*r) - x[i]*q/r)


#%%
x_real = pd.DataFrame(data = points, columns=['x'])
x_pred = pd.DataFrame(data = x, columns=['x'])

print("X:")
print("Mean absolute error: %.2f" % np.mean(np.absolute(x_real - x_pred)))
print("Residual sum of squares: %.2f" % np.mean((x_real - x_pred)**2))
print("R2-score: %.2f" % r2_score(x_real, x_pred))


y_real = pd.DataFrame(data = points, columns=['y'])
y_pred = pd.DataFrame(data = y, columns=['y'])

print("Y:")
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_real - y_pred)))
print("Residual sum of squares: %.2f" % np.mean((y_real - y_pred)**2))
print("R2-score: %.2f" % r2_score(y_real, y_pred))

#%%
# Os pontos vermelhos são os pontos de aferição reais, os pontos azuis são os pontos preditos e os pontos verdes são os pontos de wifi
plt.plot( x_real, y_real, 'ro', x_pred, y_pred, 'bs', A[0], A[1], 'g^', B[0], B[1], 'g^', C[0], C[1], 'g^')