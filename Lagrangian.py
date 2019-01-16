#!/usr/bin/env python
# coding: utf-8

# In[181]:


import numpy as np
from matplotlib import pyplot as plt


# In[182]:


def get_lagrangian(l):
    f,g,x,L=[],[],[],[]
    
    
    for l_val in l:
        x_val=get_x(l_val)
        x.append(x_val)
        
        g_val=get_gx(x_val)
        g.append(g_val)
        
        
        f_val=get_fx(x_val)
        f.append(f_val)
        
        
        L_val=f_val + l_val*g_val #x_val**2+1 +l_val*(x_val-2)*(x_val-4)
        L.append(L_val)
        
        
        print(" lambda={} | x= {} | L={}| f(x)={} | g(x)={}".format(l_val,x_val,L_val,f_val,g_val))
        
    fig=plt.figure()
    plt.subplot(1,4,1)
    plt.xlabel('x')
    plt.ylabel('L')
    plt.plot(x,L,marker="+",markersize=10)
    plt.subplot(1,4,2)
    plt.xlabel('lambda')
    plt.ylabel('L')
    plt.plot(l,L,marker="+",markersize=10)
    plt.subplot(1,4,3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x,f,marker="+",markersize=10)
    plt.subplot(1,4,4)
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.plot(x,g,marker="+",markersize=10)
    #return L
    plt.show()


# In[183]:


def get_x(l):#we get the below expression for lambda on setting dL/dx =0
    x=3*l/(1+l)
    return x

def get_fx(x):
    return x**2+1
def get_gx(x):
    return (x-2)*(x-4)


# In[184]:


l=range(0,10) #different lamda values

get_lagrangian(l)


# In[215]:


def get_lagrangian_curve(x):
    f,g,L=[],[],[]
    l=range(0,10)
    
    for l_val in l:
        
        for x_val in x:
        
        
            f_val=get_fx(x_val)
            f.append(f_val)
            g_val=get_gx(x_val)
            g.append(g_val)
        
            L_val=f_val + l_val*g_val #x_val**2+1 +l_val*(x_val-2)*(x_val-4)
            L.append(L_val)
        
            
        plt.plot(x,L,marker="+",markersize=10)
        L=[]

     


# In[216]:


x=range(-2,10)
get_lagrangian_curve(x)


# In[217]:


def get_dual(l):
    f,g,L=[],[],[]
    for l_val in l :
        x_val=get_x(l_val)
        f_val=get_fx(x_val)
        f.append(f_val)
        g_val=get_gx(x_val)
        g.append(g_val)

        L_val=f_val + l_val*g_val #x_val**2+1 +l_val*(x_val-2)*(x_val-4)
        L.append(L_val)
    plt.plot(l,L,marker="+",markersize=10)
        


# In[218]:


get_dual(l)
# this plot clearly shows argmax of dual =2 and value of dual at this lambda=2 


# In[ ]:




