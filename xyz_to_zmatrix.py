#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:42:28 2019

@author: mansi
"""

import math  
   
filename = "Water.xyz"
atoms = []
c = []
xyz = open(filename)
n_atoms = int(xyz.readline())
title = xyz.readline()

for line in xyz:
    atom,x,y,z = line.split()
    atoms.append(atom)
    c.append([float(x), float(y), float(z)])
xyz.close()
    
print("filename:         %s" % filename)
print("title:            %s" % title)
print("number of atoms:  %d" % n_atoms)
print(atoms)
print(c)
    
    

r1 = ((c[0][0]-c[1][0])**2 + (c[0][1]-c[1][1])**2 + (c[0][2]-c[1][2])**2)**0.5
print(r1)
r2 = ((c[1][0]-c[2][0])**2 + (c[1][1]-c[2][1])**2 + (c[1][2]-c[2][2])**2)**0.5
print(r2)
r3 = ((c[0][0]-c[2][0])**2 + (c[0][1]-c[2][1])**2 + (c[0][2]-c[2][2])**2)**0.5
print(r3) 




if (0.95 <= r1 <= 1.00):
    print("H-O bond forms")
    m1 = math.acos(((r2)**2 + (r3)**2 - (r1)**2)/ (2*r3*r2))
    h1 = (180/math.pi)*m1
    
    if (100.00 <= h1 <= 115.00):
        print (h1)
    else:
        print (".")
        
else:
    print("H-O bond doesnt form.")
    m1 = math.acos(((r2)**2 + (r3)**2 - (r1)**2)/ (2*r3*r2))
    h1 = (180/math.pi)*m1
    print (h1)
    if (100.00 <= h1 <= 115.00):
        print (h1)
    else:
        print (".")
    

if (0.95 <= r2 <= 1.00):
    print("O-H bond forms")
    m2 = math.acos(((r1)**2 + (r3)**2 - (r2)**2)/ (2*r1*r3))
    h2 = (180/math.pi)*m2
    
    if (100.00 <= h2 <= 115.00):
        print (h2)
    else:
        print (".")
        
else:
    print("O-H bond doesnt form.")
    m2 = math.acos(((r1)**2 + (r3)**2 - (r2)**2)/ (2*r1*r3))
    h2 = (180/math.pi)*m2
    
    if (100.00 <= h2 <= 115.00):
        print (h2)
    else:
        print (".")
    

    
if (0.95 <= r3 <= 1.00):
    print("H-H bond forms")
    m3 = math.acos(((r1)**2 + (r2)**2 - (r3)**2)/ (2*r1*r2))
    h3 = (180/math.pi)*m3
    
    if (100.00 <= h3 <= 115.00):
        print (h3)
    else:
        print (".")
else:
    print("H-H bond doesnt form.")
    m3 = math.acos(((r1)**2 + (r2)**2 - (r3)**2)/ (2*r1*r2))
    h3 = (180/math.pi)*m3
    
    if (100.00 <= h3 <= 115.00):
        print (h3)
    else:
        print (".")
        
        
a1 = c[0][0]
a2 = c[0][1]
a3 = c[0][2] 
b1 = c[1][0]
b2 = c[1][1]
b3 = c[1][2]
c1 = c[2][0]
c2 = c[2][1]
c3 = c[2][2]

n1x = (((b3-b1)*(c2-c1))-((c3-c1)*(b2-b1)))
n1y = ((-(a3-a1)*(c2-c1))+((c3-c1)*(a2-a1)))
n1z = (((a3-a1)*(b2-b1))-((b3-b1)*(a3-a1)))
    
n2x = (((b3-b1)*(c3-c2))-((c3-c1)*(b3-b2)))
n2y = ((-(a3-a1)*(c3-c2))+((c3-c1)*(a3-a2)))
n2z = (((a3-a1)*(b3-b2))-((b3-b1)*(a3-a1)))

d1 = ((n1x)**2 + (n1y)**2 + (n1z)**2)**0.5
d2 = ((n2x)**2 + (n2y)**2 + (n2z)**2)**0.5


s = math.acos((abs((n1x*n2x)+(n1y*n2y)+(n1z*n2z)))/(d1*d2))

print(s)

print ("\n\n")
print ("O1")
print ("H2 1", r1)
print ("H3 1", r2, "2", h3)

    
    
