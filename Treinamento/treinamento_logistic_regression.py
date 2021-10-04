# -*- coding: utf-8 -*-
#%%
import pandas as pd

#%%
rssi_values = {"notebook-hotspot" : list(),
               "@2830" : list(),
               "@2830_Ext" : list(),
               "position" : list()}

#%%
rssi_values["notebook-hotspot"].extend([-42,-45,-44,-78,-79,-76])
rssi_values["@2830"].extend([-78,-79,-76,-78,-79,-76])
rssi_values["@2830_Ext"].extend([-78,-79,-76,-42,-45,-44])
rssi_values["position"].extend([1,1,1,5,5,5])

df = pd.DataFrame(data=rssi_values) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

#%%
# https://machinelearningmastery.com/make-predictions-scikit-learn/
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MultiLabelBinarizer

#%%
# generate 2d classification dataset
X = pd.DataFrame(data = df, columns=['notebook-hotspot', '@2830', '@2830_Ext'])
y = pd.DataFrame(data = df, columns=['position'])

#%%
y = MultiLabelBinarizer().fit_transform(y)

#%%
# fit final model
model = LogisticRegression()
model.fit(X, y.values.ravel()) # https://stackoverflow.com/questions/34165731/a-column-vector-y-was-passed-when-a-1d-array-was-expected

#%%
ynew = model.predict_proba(X)
