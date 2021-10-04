# -*- coding: utf-8 -*-
#%%
import pandas as pd

#%%
rssi_values = {"notebook-hotspot" : list(),
               "@2830" : list(),
               "@2830_Ext" : list(),
               "position" : list()}


rssi_values["notebook-hotspot"].extend([-42,-45,-44,-78,-79,-76])
rssi_values["@2830"].extend([-78,-79,-76,-78,-79,-76])
rssi_values["@2830_Ext"].extend([-78,-79,-76,-42,-45,-44])
rssi_values["position"].extend([1,1,1,5,5,5])

df = pd.DataFrame(data=rssi_values) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

#%%
# generate 2d classification dataset
X = pd.DataFrame(data = df, columns=['notebook-hotspot', '@2830', '@2830_Ext'])
y = pd.DataFrame(data = df, columns=['position'])

#%%
# https://www.datageeks.com.br/regressao-linear/
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)

y_pred = model.predict(X)
