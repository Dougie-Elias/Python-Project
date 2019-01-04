# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:40:22 2018

@author: Dougie
"""

from scipy import *
from scipy.linalg import *
from numpy import*
from pylab import*

#class Mesh:
    #def __init__(self,mesh):
        
class Mesh:
    def __init__(self,mesh):
        self.mesh=mesh
        #self.elements=mesh[1]
    def __repr__(self):
        return '{}'.format(self.mesh)
    """def __jacobian__():
       
    def __minimum_angle__():
       
    def __determinant__():  
       
    def __total_area__():
       
    def __mesh_figure__():"""    

n=0
with open("coord2.txt","r") as coordinates:
   for line in coordinates:
        if n==0:
            X_coord=line.split()
        if n ==1:
            Y_coord=line.split()
        n+=1
        
i=0        
with open('elementnode2.txt','r') as data_element:
    for line in data_element:
        if i==0:
            Ele_1=line.split()
        if i==1:
            Ele_2=line.split()
        if i==2:
            Ele_3=line.split()
        i+=1

Xplot=[float(X_coord[n]) for n in range(20)]
Yplot=[float(Y_coord[n]) for n in range(20)]
plot(Xplot,Yplot,'gx')

Coord_Matrix=array([Xplot,Yplot])

#print(Coord_Matrix)
IniTuple=Coord_Matrix,Element_Matrix
Ele_nums1=[int(float(Ele_1[n])) for n in range(26)]
Ele_nums2=[int(float(Ele_2[n])) for n in range(26)]
Ele_nums3=[int(float(Ele_3[n])) for n in range(26)]
Element_Matrix=array([Ele_nums1,Ele_nums2,Ele_nums3])

zz=Mesh(IniTuple)


#Question 2
#print([zz.mesh[0][0][zz.mesh[1][0][1]]]) #Attempting to use the calss







