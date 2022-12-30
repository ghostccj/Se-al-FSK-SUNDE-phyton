#------------Se importan las librerÃ­as para trabajar------------
import matplotlib.pyplot as plt
import math
import numpy as np
import random 

#--------Se crea la funciÃ³n delta-dirac para trabajar posteriormente aleatoriamente------
def delta(n):
    if n == 0:
        return 1
    else:
        return 0

M=2 #Dato 
n=1 #Logaritmo base 2 de M
Ac=1 # Amplitud de la portadora
theta=0 #Sin fase
fb=2 #frecuencia de bit
fs=2 #fb=fs debido a que M=2
Ts=1/fs #Se halla Ts como inversa del periodo fs
fc=fb*2 #Valor fc
wc=2*math.pi*fc #Frecuencia radial
#intervalos=5 
TB=Ts/n

fig, ax=plt.subplots(2,2)
fig.set_size_inches(25,25)
fig.tight_layout(pad=4)

TB=1
K1=2
fc=2
Ac=1
wc=2*np.pi*fc
a=[]
b=[]
cors=["r","m","b","y","violet","brown","k","grey","w","pink","c","g"]
z1=[]
z0=[]


secuencia=input("Ingrese una cadena de bits: ")
secuencia=str(secuencia)

fc=2
fd=0.5
K=2
Ac=1
TB=1
wc=2*np.pi*fc

for k in range(0,int(len(secuencia))):
    t=[]
    t=np.linspace(TB*k,((k+1)*TB),1000)
    if(int(secuencia[k])==1):
        t=np.linspace(TB*k,((k+1)*TB),1000)
        multiplicador1=(K*Ac*np.cos(2*np.pi*(fc+fd)*t))
        ax[0,0].plot(t,multiplicador1)
     
        
    else:
        t=np.linspace(TB*k,((k+1)*TB),1000)
        multiplicador2=(K*Ac*np.cos(2*np.pi*((fc-fd))*t))
        ax[0,0].plot(t,multiplicador2)
        
        
        
        
        
        
        
        
        
        
        
        
        
fig0, ax=plt.subplots(4,2)
fig0.set_size_inches(25,25)
fig0.tight_layout(pad=4)

fig1, ax1=plt.subplots(3,2)
fig1.set_size_inches(25,25)
fig1.tight_layout(pad=4)

fig2, ax2=plt.subplots(4,2)
fig2.set_size_inches(25,25)
fig2.tight_layout(pad=4)