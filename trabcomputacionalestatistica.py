#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Questão 1
import matplotlib.pyplot as plt

v = []
n= []

a = 5 #inicio
c = 8 #final
m = 2**30
seed = 30

for i in range(10000):
    seed = (a*seed+c)%m
    r = seed/m
    X = a+(c-a)*r

    v.append(X)
    n.append(r)

Med  = (max(v) - min(v))/2 + min(v)
Sig2 = ((max(v) - min(v))**2)/12

print("Mi {}".format(Med)) #Media
print("Sigma² {}".format(Sig2)) #Variancia

plt.hist(v,10)
plt.title("Histograma")
plt.show()

plt.plot(v,n)
plt.title("FDA")
plt.show()


# In[32]:


#Questão 2
import math
import matplotlib.pyplot as plt

v = []
n = []

a = 5
c = 8
m = 2**30
seed = 20
h = 6 #lambda


for i in range(10000):
   seed = (a * seed + c) % m
   r = seed / m
   w = math.log(1-r)/6*(-1)

   v.append(w)
   n.append(r)
   v.sort(reverse=False)
   n.sort(reverse=False)

U = float('%g' % max(v))
O = float('%g' % max(n))
lc = (-1)*math.log(1-O)/U

Med = 1/lc
print("Mi {}".format(Med)) #Media
Sig2 = 1/lc**2
print("Sigma² {}".format(Sig2)) #Variancia

plt.hist(v,10)
plt.title("Histograma")
plt.show()

plt.plot(v,n)
plt.title("FDA")
plt.show()


# In[42]:


#Questão 3
import random
import math
import matplotlib.pyplot as plt

v = []
n = []
alpha = 4
pi = math.pi

for i in range(10000):
    x = random.uniform(0, 1)
    w = 4*math.tan(x*pi - pi/2)

    v.append(w)
    v.sort(reverse=False)
    n.append(x)
    n.sort(reverse=False)  


plt.hist(v)
plt.title("Histograma")
plt.show()

plt.plot(v, n)
plt.title("FDA")
plt.xlim(-1000, 1200)
plt.ylim(0, 1)
plt.show()


# In[36]:


#Questão 4
import matplotlib.pyplot as plt
import numpy as np

Mi, sigma = 5, 2
s = np.random.normal(Mi, sigma, 10000)

#Histograma
count, bins, ignored = plt.hist(s, 20, density=True)

#Curva
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - Mi)**2 / (2 * sigma**2) ))
plt.show()
