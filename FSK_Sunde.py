#------------Se importan las libreri­as para trabajar------------
import matplotlib.pyplot as plt
import math
import numpy as np
import random 

#--------Se crea la función delta-dirac para trabajar posteriormente aleatoriamente------
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

secuencia=input("Ingrese una cadena de bits: ")
secuencia=str(secuencia)

#Se define el tiempo en el cual se modulará la señal


#---------Se plotean las gráficas de onda---------------
fig, ax=plt.subplots(11,2)

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
#----------------------------------------------------------------------------
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
#__________filtro adaptado  sincronismo perfecto _______

for k in range(0,int(len(secuencia))):
    t=[]
    t=np.linspace(TB*k,((k+1)*TB),1000)
    
    if(int(secuencia[k])==1):
        #la parte del z0
        t=np.linspace(TB*k,((k+1)*TB),1000)
        a=((np.cos(wc*t))/2)*(t-k*TB)
        z=(K1)*(Ac*Ac)*(a)
        z1.append(z)
        ax[0,1].plot(t,z,cors[k])
        ax[4,0].plot(t,z,cors[k])
        #graficando el S&H
        ax[1,0].plot(t,z1[0],cors[k]) 

        ax[1,0].vlines(x=TB*(k+1), ymin=0, ymax=Ac, linewidth=2, color='g')
        ax[1,0].plot(TB*(k+1),Ac, marker="o", color="g")
        ax[1,0].hlines(y=Ac, xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='g')
        if(k<len(secuencia)-1):
            ax[1,0].vlines(x=TB*(k+2), ymin=0, ymax=Ac, linewidth=2, color='g')
         
        
        ax[1,1].vlines(x=TB*(k+1), ymin=0, ymax=1, linewidth=2, color='#6BBD19')
        ax[1,1].hlines(y=1, xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='#6BBD19')
        if(k<len(secuencia)-1):
            ax[1,1].vlines(x=TB*(k+2), ymin=0, ymax=1, linewidth=2, color='#6BBD19')
         
        
        t=np.linspace(TB*(k+1),((k+2)*TB),1000)
        b=((np.cos(wc*t))/2)*((k+2)*TB-t)
        z=(K1)*(Ac*Ac)*(b)
        z1.append(z)
        ax[0,1].plot(t,z,cors[k])
        
        t=np.linspace(TB*k,(((k+1)*(TB))+0.1248),1000)
        a=((np.cos(wc*t))/2)*(t-k*TB)
        z=(K1)*(Ac*Ac)*(a)
        ax[4,0].plot(t,z,cors[k])
        
        z=[]
                  
    else:
        #la parte del z1
        t=np.linspace(TB*k,((k+1)*TB),1000)
        a=((np.cos(wc*t))/2)*(t-k*TB)
        z=-(K1)*(Ac*Ac)*(a)
        ax[0,1].plot(t,z,cors[k])
        
        #plotea el S&H
        ax[1,0].plot(t,np.zeros(1000),cors[k]) 
        
        
        ax[1,0].vlines(x=TB*(k+1), ymin=0, ymax=-Ac, linewidth=2, color='g')
        ax[1,0].plot(TB*(k+1),-Ac, marker="o", color="g")
        ax[1,0].hlines(y=-Ac, xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='g')
        if(k<len(secuencia)-1):
            ax[1,0].vlines(x=TB*(k+2), ymin=0, ymax=-Ac, linewidth=2, color='g')
        
        
        ax[1,1].vlines(x=TB*(k+1), ymin=0, ymax=0, linewidth=2, color='#6BBD19')
        ax[1,1].hlines(y=0, xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='#6BBD19')
        if(k<len(secuencia)-1):
            ax[1,1].vlines(x=TB*(k+2), ymin=0, ymax=0, linewidth=2, color='#6BBD19')
        
        
        z0.append(z)
        z=[]
        t=np.linspace(TB*(k+1),((k+2)*TB),1000)
        b=((np.cos(wc*t))/2)*((k+2)*TB-t)
        z=-(K1)*(Ac*Ac)*(b)
        ax[0,1].plot(t,z,cors[k])
        
        z0.append(z)
        
        t=np.linspace(((TB*k)+0.1248),((k+1)*TB),1000)
        ax[4,0].plot(t,np.zeros(1000),cors[k])
        
        z=[]

#________filtro correlador sincronismo perfecto_________
 
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
        multiplicador1=(K*Ac*np.cos(2*np.pi*(fc+fd)*t))/4+Ac/2
        ax[2,0].plot(t,multiplicador1)
        
        z11=[]
        t=np.linspace(TB*k,((k+1)*TB),1000)
        z11=((K/2)*Ac**2)*((t-k*TB)+(np.sin(2*wc*t))/(2*wc))
        
        ax[2,1].plot(t,z11)
        ax[2,1].vlines(x=TB*(k+1), ymin=0, ymax=Ac, linewidth=2, color='r')
        #salida del S&H
        ax[3,0].vlines(x=TB*(k+1), ymin=0, ymax=Ac, linewidth=2, color='g')
        ax[3,0].plot(TB*(k+1),Ac, marker="o", color="g")
        ax[3,0].hlines(y=Ac, xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='g')
        if(k<len(secuencia)-1):
            
            ax[3,0].vlines(x=TB*(k+2), ymin=0, ymax=Ac, linewidth=2, color='g')
        
        
    else:
        t=np.linspace(TB*k,((k+1)*TB),1000)
        multiplicador2=-(K*Ac*np.cos(2*np.pi*((fc-fd))*t+np.pi))/4-Ac/2
        ax[2,0].plot(t,multiplicador2)
        
        z00=[]
        t=np.linspace(TB*k,((k+1)*TB),1000)
        z00=-((K/2)*Ac**2)*((t-k*TB)+(np.sin(2*wc*t))/(2*wc))

        ax[2,1].plot(t,z00)
        ax[2,1].vlines(x=TB*(k+1), ymin=0, ymax=-Ac, linewidth=2, color='r')
        
        #salida del S&H
        ax[3,0].vlines(x=TB*(k+1), ymin=0, ymax=-Ac, linewidth=2, color='g')
        ax[3,0].plot(TB*(k+1),-Ac, marker="o", color="g")
        ax[3,0].hlines(y=-Ac, xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='g')
        if(k<len(secuencia)-1):
            
            ax[3,0].vlines(x=TB*(k+2), ymin=0, ymax=-Ac, linewidth=2, color='g')
            
#_____________SINCRONISMOS IMPERFECTOS_____________
        
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
tk=[]
epsilon=[]
amplitudes=[]
import math
#_____________filtro adaptado  sincronismo imperfecto ________________

for k in range(0,len(secuencia)): #obtenemos posiciones en el tiempo a trabajar y los valores de las amplitudes
    epsilon.append(round(random.uniform(-0.05,0.05),2)) 
    tk.append((k)+TB*(1+epsilon[k])) #
    ttt=tk[k]
    a=0
    b=0

    if(int(secuencia[k])==1):
        if(epsilon[k]<=0): #si es menor o igual que cero se aplica el 'a' porque es la mitad de la trama
        
            a=((math.cos(wc*ttt))/2)*(ttt-k*TB)
            a=(K1)*(Ac*Ac)*(a)
            amplitudes.append(a)
        else:

            b=((math.cos(wc*ttt))/2)*((k+2)*TB-ttt)
            b=(K1)*(Ac*Ac)*(b)
            amplitudes.append(b)
            

    else:
        if(epsilon[k]<=0): #si es menor o igual que cero se aplica el 'a' porque es la mitad de la trama
        
            a=((math.cos(wc*ttt))/2)*(ttt-k*TB)
            a=-(K1)*(Ac*Ac)*(a)
            amplitudes.append(a)
        else:

            b=((math.cos(wc*ttt))/2)*((k+2)*TB-ttt)
            b=-(K1)*(Ac*Ac)*(b)
            amplitudes.append(b)
        
for k in range(0,len(secuencia)):#se plotea s/h
    if(int(secuencia[k])==1):
        #sample and hold
        ax[4,0].vlines(x=tk[k], ymin=0, ymax=amplitudes[k], linewidth=2, color='g')
        ax[4,0].plot(tk[k],amplitudes[k], marker="o", color="g")    
        
        if(len(secuencia)-1>k):
            #sample and hold
            ax[4,0].hlines(y=amplitudes[k], xmin=tk[k], xmax=tk[k+1], linewidth=2, color='g')
            ax[4,0].vlines(x=tk[k+1], ymin=0, ymax=amplitudes[k], linewidth=2, color='g')
            
        elif(k==len(secuencia)-1):
            ax[4,0].hlines(y=amplitudes[k], xmin=tk[k], xmax=(k+2)*TB, linewidth=2, color='g')
            
    else:
        #sample and hold
        ax[4,0].vlines(x=tk[k], ymin=0, ymax=amplitudes[k], linewidth=2, color='g')
        ax[4,0].plot(tk[k],amplitudes[k], marker="o", color="g")
        
        if(len(secuencia)-1>k):
            #sample and hold
            ax[4,0].hlines(y=amplitudes[k], xmin=tk[k], xmax=tk[k+1], linewidth=2, color='g') 
            ax[4,0].vlines(x=tk[k+1], ymin=0, ymax=amplitudes[k],linewidth=2, color='g')
        elif(k==len(secuencia)-1):
            ax[4,0].hlines(y=amplitudes[k], xmin=tk[k], xmax=(k+2)*TB, linewidth=2, color='g') 
            
Vop=0       
for k in range(0,len(secuencia)): #comparador
    if(amplitudes[k]>=Vop): #si el Vop es superado se considera como 1
        
        #comparador
        ax[4,1].vlines(x=tk[k], ymin=0, ymax=1, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador
            ax[4,1].hlines(y=1, xmin=tk[k], xmax=tk[k+1], linewidth=2, color='g')
            ax[4,1].vlines(x=tk[k+1], ymin=0, ymax=1, linewidth=2, color='g')
        elif(k==len(secuencia)-1):
            ax[4,1].hlines(y=1, xmin=tk[k], xmax=(k+2)*TB, linewidth=2, color='g') 
    else:
        #comparador
        ax[4,1].vlines(x=tk[k], ymin=0, ymax=0, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador 
            ax[4,1].hlines(y=0, xmin=tk[k], xmax=tk[k+1], linewidth=2, color='g') 
            ax[4,1].vlines(x=tk[k+1], ymin=0, ymax=0,linewidth=2, color='g')
        
        elif(k==len(secuencia)-1):
            ax[4,1].hlines(y=0, xmin=tk[k], xmax=(k+2)*TB, linewidth=2, color='g')   

            
#___________filtro correlador sincronismo imperfecto___________

fc=2
fd=0.5
K=2
Ac=1
TB=1
wc=2*np.pi*fc
tk2=[]

amplitudes_correlador=[]
for k in range(0,int(len(secuencia))):
    t=[]
    t=np.linspace(TB*k,((k+1)*TB),1000)
  
    tk2.append((k)+TB*(1+epsilon[k])) #
    
    if(int(secuencia[k])==1):
        t=np.linspace(TB*k,((k+1)*TB),1000)
        multiplicador1=K*Ac*np.cos(2*np.pi*(fc+fd)*t)+K*Ac*Ac
        ax[7,0].plot(t,multiplicador1)
        
        z11=[]
        t=np.linspace(TB*k,((k+1)*TB),1000)
        z11=((K/2)*Ac**2)*((t-k*TB)+(np.sin(2*wc*t))/(2*wc))
        
        ax[7,1].plot(t,z11)
        ax[7,1].vlines(x=TB*(k+1), ymin=0, ymax=Ac, linewidth=2, color='r')
        
        t=tk2[k]
        z=((K/2)*Ac**2)*((t-k*TB)+(np.sin(2*wc*t))/(2*wc))
        amplitudes_correlador.append(z)
        
        
    else:
        t=np.linspace(TB*k,((k+1)*TB),1000)
        multiplicador2=-K*Ac*np.cos(2*np.pi*(fc-fd)*t+np.pi)-K*Ac*Ac
        ax[7,0].plot(t,multiplicador2)
        
        z00=[]
        t=np.linspace(TB*k,((k+1)*TB),1000)
        z00=-((K/2)*Ac**2)*((t-k*TB)+(np.sin(2*wc*t))/(2*wc))

        ax[7,1].plot(t,z00)
        ax[7,1].vlines(x=TB*(k+1), ymin=0, ymax=-Ac, linewidth=2, color='r')
        
        t=tk2[k]
        z=-((K/2)*Ac**2)*((t-k*TB)+(np.sin(2*wc*t))/(2*wc))
        amplitudes_correlador.append(z)

        
for k in range(0,len(secuencia)):#se plotea s/h
    if(int(secuencia[k])==1):
        #sample and hold
        ax[8,0].vlines(x=tk2[k], ymin=0, ymax=amplitudes_correlador[k], linewidth=2, color='g')
        ax[8,0].plot(tk2[k],amplitudes_correlador[k], marker="o", color="g")    
        
        if(len(secuencia)-1>k):
            #sample and hold
            ax[8,0].hlines(y=amplitudes_correlador[k], xmin=tk2[k], xmax=tk2[k+1], linewidth=2, color='g')
            ax[8,0].vlines(x=tk2[k+1], ymin=0, ymax=amplitudes_correlador[k], linewidth=2, color='g')
            
        elif(k==len(secuencia)-1):
            ax[8,0].hlines(y=amplitudes_correlador[k], xmin=tk2[k], xmax=(k+2)*TB, linewidth=2, color='g')
            
    else:
        #sample and hold
        ax[8,0].vlines(x=tk2[k], ymin=0, ymax=amplitudes_correlador[k], linewidth=2, color='g')
        ax[8,0].plot(tk2[k],amplitudes_correlador[k], marker="o", color="g")
        
        if(len(secuencia)-1>k):
            #sample and hold
            ax[8,0].hlines(y=amplitudes_correlador[k], xmin=tk2[k], xmax=tk2[k+1], linewidth=2, color='g') 
            ax[8,0].vlines(x=tk2[k+1], ymin=0, ymax=amplitudes_correlador[k],linewidth=2, color='g')
        elif(k==len(secuencia)-1):
            ax[8,0].hlines(y=amplitudes_correlador[k], xmin=tk2[k], xmax=(k+2)*TB, linewidth=2, color='g') 
            
for k in range(0,len(secuencia)): #comparador
    if(amplitudes_correlador[k]>=Vop): #si el Vop es superado se considera como 1
        
        #comparador
        ax[8,1].vlines(x=tk2[k], ymin=0, ymax=1, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador
            ax[8,1].hlines(y=1, xmin=tk2[k], xmax=tk2[k+1], linewidth=2, color='g')
            ax[8,1].vlines(x=tk2[k+1], ymin=0, ymax=1, linewidth=2, color='g')
        elif(k==len(secuencia)-1):
            ax[8,1].hlines(y=1, xmin=tk2[k], xmax=(k+2)*TB, linewidth=2, color='g') 
    else:
        #comparador
        ax[8,1].vlines(x=tk2[k], ymin=0, ymax=0, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador 
            ax[8,1].hlines(y=0, xmin=tk2[k], xmax=tk2[k+1], linewidth=2, color='g') 
            ax[8,1].vlines(x=tk2[k+1], ymin=0, ymax=0,linewidth=2, color='g')
        
        elif(k==len(secuencia)-1):
            ax[8,1].hlines(y=0, xmin=tk2[k], xmax=(k+2)*TB, linewidth=2, color='g')    
            

#_______________filtro adaptado sincronismo perfecto con ruido gausiano ___________
gammadB=8 
gamma=10**(gammadB/10)
varianza=Ac*Ac/(2*gamma)
amplitudes_con_ruido=[]

for k in range(0,int(len(secuencia))):
    t=[]
    t=np.linspace(TB*k,((k+1)*TB),1000)
    
    if(int(secuencia[k])==1):
        #la parte del z0
        t=np.linspace(TB*k,((k+1)*TB),1000)
        ruido=np.random.uniform(-varianza,+varianza,1000)
        a=((np.cos(wc*t))/2)*(t-k*TB)+ruido
        z=(K1)*(Ac*Ac)*(a)
        amplitudes_con_ruido.append(z[-1])
        ax[5,0].plot(t,z,cors[k])
        
        #graficando el S&H
        ax[5,1].plot(t,z,cors[k]) 

        
        ax[5,1].vlines(x=TB*(k+1), ymin=0, ymax=amplitudes_con_ruido[k], linewidth=2, color='g')
        ax[5,1].plot(TB*(k+1),amplitudes_con_ruido[k], marker="o", color="g")
        ax[5,1].hlines(y=amplitudes_con_ruido[k], xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='g')
        
        if(k<len(secuencia)-1):
            ax[5,1].vlines(x=TB*(k+2), ymin=0, ymax=amplitudes_con_ruido[k], linewidth=2, color='g')
        
        ruido=np.random.uniform(-varianza,+varianza,1000)
        t=np.linspace(TB*(k+1),((k+2)*TB),1000)
        b=((np.cos(wc*t))/2)*((k+2)*TB-t)+ruido
        z=(K1)*(Ac*Ac)*(b)
        
        ax[5,0].plot(t,z,cors[k])
        
        t=np.linspace(TB*k,(((k+1)*(TB))+0.1248),1000)
        a=((np.cos(wc*t))/2)*(t-k*TB)
        z=(K1)*(Ac*Ac)*(a)
        ax[4,0].plot(t,z,cors[k])
        
        z=[]
         
                  
    else:
        #la parte del z1
        ruido=np.random.uniform(-varianza,+varianza,1000)
        t=np.linspace(TB*k,((k+1)*TB),1000)
        a=((np.cos(wc*t))/2)*(t-k*TB)+ruido
        z=-(K1)*(Ac*Ac)*(a)
        amplitudes_con_ruido.append(z[-1])
        ax[5,0].plot(t,z,cors[k])
        
        #plotea el S&H
        ax[5,1].plot(t,(np.zeros(1000)+ruido),cors[k]) 
        
        
        ax[5,1].vlines(x=TB*(k+1), ymin=0, ymax=amplitudes_con_ruido[k], linewidth=2, color='g')
        ax[5,1].plot(TB*(k+1),amplitudes_con_ruido[k], marker="o", color="g")
        ax[5,1].hlines(y=amplitudes_con_ruido[k], xmin=TB*(k+1), xmax=TB*(k+2), linewidth=2, color='g')
        
        if(k<len(secuencia)-1):
            ax[5,1].vlines(x=TB*(k+2), ymin=0, ymax=amplitudes_con_ruido[k], linewidth=2, color='g')
        
        ruido=np.random.uniform(-varianza,+varianza,1000)
        t=np.linspace(TB*(k+1),((k+2)*TB),1000)
        b=((np.cos(wc*t))/2)*((k+2)*TB-t)+ruido
        z=-(K1)*(Ac*Ac)*(b)
        ax[5,0].plot(t,z,cors[k])
        
        z0.append(z)
        
        t=np.linspace(((TB*k)+0.1248),((k+1)*TB),1000)
        ax[4,0].plot(t,np.zeros(1000),cors[k])
        
        z=[]
Vop=0       
for k in range(0,len(secuencia)): #comparador
    if(amplitudes_con_ruido[k]>=Vop): #si el Vop es superado se considera como 1
        #comparador
        ax[6,0].vlines(x=(k+1)*TB, ymin=0, ymax=1, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador
            ax[6,0].hlines(y=1, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g')
            ax[6,0].vlines(x=(k+2)*TB, ymin=0, ymax=1, linewidth=2, color='g')
        elif(k==len(secuencia)-1):
            ax[6,0].hlines(y=1, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g') 
    else:
        #comparador
        ax[6,0].vlines(x=(k+1)*TB, ymin=0, ymax=0, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador 
            ax[6,0].hlines(y=0, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g') 
            ax[6,0].vlines(x=(k+2)*TB, ymin=0, ymax=0,linewidth=2, color='g')
        
        elif(k==len(secuencia)-1):
            ax[6,0].hlines(y=0, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g')   
            
#___________filtro correlado  sincronismo perfecto con ruido gausiano ________
fc=2
fd=0.5
K=2
Ac=1
TB=1
wc=2*np.pi*fc
amplitudes_ruido_correlador=[]
for k in range(0,int(len(secuencia))):
    t=[]
    t=np.linspace(TB*k,((k+1)*TB),1000)
    if(int(secuencia[k])==1):
        t=np.linspace(TB*k,((k+1)*TB),1000)
        ruido=np.random.uniform(-varianza,+varianza,1000) #generacion del ruido
        multiplicador1=((K*Ac*np.cos(2*np.pi*(fc+fd)*t))/4+Ac/2)+ruido
        ax[9,0].plot(t,multiplicador1)
        z11=[]
        
        t=np.linspace(0,TB,1000)
        ruido=np.random.uniform(-varianza,+varianza,1000)
        z11=((K/2)*Ac**2)*((t-K*TB)+(np.sin(2*wc*t))/(2*wc))+Ac*2+ruido
        t=np.linspace(TB*k,((k+1)*TB),1000)
        amplitudes_ruido_correlador.append(z11[-1])
        ax[9,1].plot(t,z11)
        ax[9,1].vlines(x=TB*(k+1), ymin=0, ymax=Ac, linewidth=2, color='r')
        
         
        
    else:
        t=np.linspace(TB*k,((k+1)*TB),1000)
        ruido=np.random.uniform(-varianza,+varianza,1000)
        multiplicador2=-(K*Ac*np.cos(2*np.pi*(fc-fd)*t+np.pi))/4-Ac/2+ruido
        ax[9,0].plot(t,multiplicador2)
        z00=[]
        t=np.linspace(0,TB,1000)
        ruido=np.random.uniform(-varianza,+varianza,1000)
        z00=-((K/2)*Ac**2)*((t-K*TB)+(np.sin(2*-wc*t))/(2*-wc))-Ac*2+ruido
        amplitudes_ruido_correlador.append(z00[-1])
        t=np.linspace(TB*k,((k+1)*TB),1000)
        ax[9,1].plot(t,z00)
        ax[9,1].vlines(x=TB*(k+1), ymin=0, ymax=-Ac, linewidth=2, color='r')
        

    
for k in range(0,len(secuencia)):
    if(int(secuencia[k])==1):
        #sample and hold
        ax[10,0].vlines(x=(k+1)*TB, ymin=0, ymax=amplitudes_ruido_correlador[k], linewidth=2, color='g')
        ax[10,0].plot((k+1)*TB,amplitudes_ruido_correlador[k], marker="o", color="g")    
        
        if(len(secuencia)-1>k):
            #sample and hold
            ax[10,0].hlines(y=amplitudes_ruido_correlador[k], xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g')
            ax[10,0].vlines(x=(k+2)*TB, ymin=0, ymax=amplitudes_ruido_correlador[k], linewidth=2, color='g')
            
        elif(k==len(secuencia)-1):
            ax[10,0].hlines(y=amplitudes_ruido_correlador[k], xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g')
            
    else:
        #sample and hold
        ax[10,0].vlines(x=(k+1)*TB, ymin=0, ymax=amplitudes_ruido_correlador[k], linewidth=2, color='g')
        ax[10,0].plot((k+1)*TB,amplitudes_ruido_correlador[k], marker="o", color="g")
        
        if(len(secuencia)-1>k):
            #sample and hold
            ax[10,0].hlines(y=amplitudes_ruido_correlador[k], xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g') 
            ax[10,0].vlines(x=(k+2)*TB, ymin=0, ymax=amplitudes_ruido_correlador[k],linewidth=2, color='g')
        elif(k==len(secuencia)-1):
            ax[10,0].hlines(y=amplitudes_ruido_correlador[k], xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g') 
    
for k in range(0,len(secuencia)): #comparador
    if(amplitudes_ruido_correlador[k]>=Vop): #si el Vop es superado se considera como 1
        
        #comparador
        ax[10,1].vlines(x=(k+1)*TB, ymin=0, ymax=1, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador
            ax[10,1].hlines(y=1, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g')
            ax[10,1].vlines(x=(k+2)*TB, ymin=0, ymax=1, linewidth=2, color='g')
        elif(k==len(secuencia)-1):
            ax[10,1].hlines(y=1, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g') 
    else:
        #comparador
        ax[10,1].vlines(x=(k+1)*TB, ymin=0, ymax=0, linewidth=2, color='g')
        if(len(secuencia)-1>k):
            #comparador 
            ax[10,1].hlines(y=0, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g') 
            ax[10,1].vlines(x=(k+2)*TB, ymin=0, ymax=0,linewidth=2, color='g')
        
        elif(k==len(secuencia)-1):
            ax[10,1].hlines(y=0, xmin=(k+1)*TB, xmax=(k+2)*TB, linewidth=2, color='g')     
    
    
print(amplitudes) 
print(amplitudes_correlador)
print(tk2)
print(amplitudes_con_ruido)
print(tk)
print(epsilon)
ax[0,0].set_xlabel('Tiempo(u seg)')
ax[0,0].set_ylabel('Amplitud(v)')
ax[0,0].set_title("Señal de entrada")
ax[0,0].grid()

ax[0,1].set_xlabel('Tiempo(u seg)')
ax[0,1].set_ylabel('Amplitud(v)')
ax[0,1].set_title("Salida del Filtro Adaptado con Sincronismo Perfecto sin Ruido Gaussiano")
ax[0,1].grid()

ax[1,0].set_xlabel('Tiempo(u seg)')
ax[1,0].set_ylabel('Amplitud(v)')
ax[1,0].set_title("Salida del Sample and Hold del Filtro Adaptado con Sincronismo Perfecto sin Ruido Gaussiano")
ax[1,0].grid()

ax[1,1].set_xlabel('Tiempo(u seg)')
ax[1,1].set_ylabel('Amplitud(v)')
ax[1,1].set_title("Salida del Comparador del Filtro Correlador con Sincronismo Perfecto sin Ruido Gaussiano")
ax[1,1].grid()

ax[2,0].set_xlabel('Tiempo(u seg)')
ax[2,0].set_ylabel('Amplitud(v)')
ax[2,0].set_title("Salida del Multiplicador del Filtro Correlador con Sincronismo Perfecto sin Ruido Gaussiano")
ax[2,0].grid()

ax[2,1].set_xlabel('Tiempo(u seg)')
ax[2,1].set_ylabel('Amplitud(v)')
ax[2,1].set_title('Salida del Integrador del Filtro Correlador con Sincronismo Perfecto sin Ruido Gaussiano')
ax[2,1].grid()

ax[3,0].set_xlabel('Tiempo(u seg)')
ax[3,0].set_ylabel('Amplitud(v)')
ax[3,0].set_title("Salida del Sample and Hold del Filtro Correlador con Sincronismo Perfecto sin Ruido Gaussiano")
ax[3,0].grid()

ax[4,0].set_xlabel('Tiempo(u seg)')
ax[4,0].set_ylabel('Amplitud(v)')
ax[4,0].set_title('Salida del Sample and Hold Filtro Adaptado con Sincronismo Imperfecto sin Ruido Gaussiano')
ax[4,0].grid()

ax[4,1].set_xlabel('Tiempo(u seg)')
ax[4,1].set_ylabel('Amplitud(v)')
ax[4,1].set_title('Salida del Comparador del Filtro Adaptado Sincronismo Imperfecto sin Ruido Gaussiano')
ax[4,1].grid()

ax[5,0].set_xlabel('Tiempo(u seg)')
ax[5,0].set_ylabel('Amplitud(v)')
ax[5,0].set_title('Salida del Filtro Adaptado Sincronismo Perfecto con Ruido Gaussiano')
ax[5,0].grid()

ax[5,1].set_xlabel('Tiempo(u seg)')
ax[5,1].set_ylabel('Amplitud(v)')
ax[5,1].set_title('Salida del Sample and Hold del Filtro Adaptado con Sincronismo Perfecto con Ruido Gaussiano')
ax[5,1].grid()


ax[6,0].set_xlabel('Tiempo(u seg)')
ax[6,0].set_ylabel('Amplitud(v)')
ax[6,0].set_title('Salida del Comparador del Filtro Adaptado con Sincronismo Perfecto con Ruido Gaussiano')
ax[6,0].grid()

ax[7,0].grid()
ax[7,1].grid()

ax[8,0].set_xlabel('Tiempo(u seg)')
ax[8,0].set_ylabel('Amplitud(v)')
ax[8,0].set_title('Salida del Sample and Hold del Filtro Correlador con Sincronismo Imperfecto sin Ruido Gaussiano')
ax[8,0].grid()

ax[8,1].set_xlabel('Tiempo(u seg)')
ax[8,1].set_ylabel('Amplitud(v)')
ax[8,1].set_title('Salida del Comparador del Filtro Correlador con Sincronismo Imperfecto sin Ruido Gaussiano')
ax[8,1].grid()

ax[9,0].set_xlabel('Tiempo(u seg)')
ax[9,0].set_ylabel('Amplitud(v)')
ax[9,0].set_title('Salida del Multiplicador del Filtro Correlador con Sincronismo Perfecto con Ruido Gaussiano')
ax[9,0].grid()

ax[9,1].set_xlabel('Tiempo(u seg)')
ax[9,1].set_ylabel('Amplitud(v)')
ax[9,1].set_title('Salida del Integrador del Filtro Correlador con Sincronismo Perfecto con Ruido Gaussiano')
ax[9,1].grid()

ax[10,0].set_xlabel('Tiempo(u seg)')
ax[10,0].set_ylabel('Amplitud(v)')
ax[10,0].set_title('Salida del Filtro Correlador Sincronismo Perfecto con Ruido Gaussiano')
ax[10,0].grid()

ax[10,1].set_xlabel('Tiempo(u seg)')
ax[10,1].set_ylabel('Amplitud(v)')
ax[10,1].set_title('Salida del Comparador del Filtro Correlador Sincronismo Perfecto con Ruido Gaussiano')
ax[10,1].grid()

fig.delaxes(ax[3,1])
fig.delaxes(ax[6,1])

