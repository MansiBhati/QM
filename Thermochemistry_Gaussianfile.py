#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:20:12 2019

@author: mansi
"""

import math
import matplotlib.pyplot as plt 

fr= open('co2-nh3hf.log','r')

for liner in fr:
    if " Sum of electronic and thermal Enthalpies= " in liner:
        H_r = float(liner.split('\n')[0].split('=         ')[1])
    if "Sum of electronic and thermal Free Energies= " in liner:
        G_r = float(liner.split('\n')[0].split('=         ')[1])
        
fts= open('ts1_hf.log','r')

for linets in fts:
    if " Sum of electronic and thermal Enthalpies= " in linets:
        H_ts = float(linets.split('\n')[0].split('=         ')[1])
    if "Sum of electronic and thermal Free Energies= " in linets:
        G_ts = float(linets.split('\n')[0].split('=         ')[1]) 
        
fp= open('nh2coohhf.log','r')

for linep in fp:
    if "Sum of electronic and thermal Enthalpies= " in linep:
        H_p = float(linep.split('\n')[0].split('=         ')[1])
        
kb = 1.3807*10**(-23)
T = 298.15
h = 6.6261*10**(-34)
R = 1.987

E_a = (H_ts - H_r)*627.503

RE = (H_p - H_r)*627.503

G = (G_ts - G_r)*627.503*10**3 

k = (kb*T* math.exp(-G/(R*T)))/h    


x = [2,4,6] 
y = [H_r, H_ts, H_p] 
  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 1, 
         marker='o', markerfacecolor='blue', markersize=12, label="line1")
  
plt.tick_params(axis='x', which='both', bottom=False, top=False, 
                labelbottom=False)

plt.ylabel('Energy (kcal/mol)') 
plt.title('Energy Profile') 


col_labels = ['HF']
row_labels = ['Activation Energy', 'Reaction Energy', 'Rate Constant']
table_vals = [[E_a], [RE], [k]]

the_table = plt.table(cellText=table_vals,
                      colWidths=[0.1] * 4,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc='bottom')
the_table.scale(4, 1)
plt.subplots_adjust(left=0.2, bottom=0.2)
plt.show()
print (H_r)