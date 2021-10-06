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
points = { "x" : list(),
          "y" : list(),
          }
points["x"].extend([D1[0], D1[0], D1[0], D1[0], D1[0], D1[0]])
points["y"].extend([D1[1], D1[1], D1[1], D1[1], D1[1], D1[1]])

points["x"].extend([D2[0], D2[0], D2[0], D2[0], D2[0], D2[0]])
points["y"].extend([D2[1], D2[1], D2[1], D2[1], D2[1], D2[1]])

points["x"].extend([D3[0], D3[0], D3[0], D3[0], D3[0], D3[0]])
points["y"].extend([D3[1], D3[1], D3[1], D3[1], D3[1], D3[1]])
