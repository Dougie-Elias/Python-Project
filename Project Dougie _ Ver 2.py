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
    def __init__(self,coordinate_matrix,element_matrix):
        self.mesh=coordinate_matrix,element_matrix
    def __repr__(self):
        return '{}'.format(self.mesh)
    def jacobian(self,E): #E is the element you want to choose
       a,b,c=self.mesh[1][0][E]-1,self.mesh[1][1][E]-1,self.mesh[1][2][E]-1 #"-1" to correct for numbering 
       Jac_of_Transf=array([[self.mesh[0][0][b]-self.mesh[0][0][a],self.mesh[0][0][c]-self.mesh[0][0][a]],
                            [self.mesh[0][1][b]-self.mesh[0][1][a],self.mesh[0][0][c]-self.mesh[0][1][a]]])       
       return linalg.det(Jac_of_Transf)
    #def __minimum_angle__():
    
    def I_Omega(self,f):
        def x(Xi,Etta,a,b,c):
            return self.mesh[0][0][a]+(self.mesh[0][0][b]-self.mesh[0][0][a])*Xi+(self.mesh[0][0][c]-self.mesh[0][0][a])*Etta
        def y(Xi,Etta,a,b,c):
            return self.mesh[0][1][a]+(self.mesh[0][1][b]-self.mesh[0][1][a])*Xi+(self.mesh[0][1][c]-self.mesh[0][1][a])*Etta
        def g(Xi,Etta):
            return f(x(Xi,Etta,a,b,c),(y(Xi,Etta,a,b,c)))
        Sum_I=0
        for i in range(0,len(self.mesh[1][0])):
            a,b,c=self.mesh[1][0][i]-1,self.mesh[1][1][i]-1,self.mesh[1][2][i]-1
            I_i=abs(self.determinant()[i])*0.5*()
            
        return None
        
    def determinant(self):  
       L=[self.jacobian(i) for i in range(0,len(self.mesh[1][0]))]
       return L    
    """def __total_area__():
       
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

Xplot=[float(X_coord[n]) for n in range(len(X_coord))]
Yplot=[float(Y_coord[n]) for n in range(20)]

plot(Xplot,Yplot,'gx')

Coord_Matrix=array([Xplot,Yplot])

#print(Coord_Matrix)


Ele_nums1=[int(float(Ele_1[n])) for n in range(26)]
Ele_nums2=[int(float(Ele_2[n])) for n in range(26)]
Ele_nums3=[int(float(Ele_3[n])) for n in range(26)]

Element_Matrix=array([Ele_nums1,Ele_nums2,Ele_nums3])

zz=Mesh(Coord_Matrix,Element_Matrix)


#Question 2
#print([zz.mesh[0][0][zz.mesh[1][0][1]]]) #Attempting to use the calss
print(zz.mesh[1])
a,b,c=zz.mesh[1][0][0]-1,zz.mesh[1][1][0]-1,zz.mesh[1][2][0]-1
Jac_of_Transf=array([[zz.mesh[0][0][b]-zz.mesh[0][0][a],zz.mesh[0][0][c]-zz.mesh[0][0][a]],
                     [zz.mesh[0][1][b]-zz.mesh[0][1][a],zz.mesh[0][0][c]-zz.mesh[0][1][a]]])
print(linalg.det(Jac_of_Transf))

print(zz.jacobian(0))
print(zz)

#print(zz.determinant())
Xi=None
Etta=None
def f(x,y):
    return x+y

z=Xi+Etta

Xi=1
Etta=2
print(z)