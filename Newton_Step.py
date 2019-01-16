#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import subprocess
c=10
n=2
w=0.01
w1=1.2
w2=0.5
alpha=1
theta=0.001
delmax=np.inf

x=np.ones(n)

x


# In[2]:



def compute_C(n,c):
    C=np.zeros([n,n])
    for i in range(n):
        C[i][i]=(pow(c,(i)/(n-1)))
    return C


# In[3]:


def fSq(x):
    
    C=compute_C(n,c)
    f=np.dot(np.transpose(x),C)
    fsq=np.dot(f,x)
    fsq
    return fsq


# In[4]:


def fHole(x):
    fhole=1-np.exp(-fSq(x))
    return fhole


# In[5]:


print(fSq(x))
print(fHole(x))


# In[6]:


C=compute_C(n,c)

def gradient(x):
    val=np.dot(np.transpose(C),x)+np.dot(C,x)
    dict={'fSq': val,'fHole':np.exp(-fSq(x))*val}
    return dict
    
    


# In[7]:


gradient


# In[8]:


def compute_grad_descent(x1,func):
    grad=gradient(x1)
    grad=grad[func.__name__]
    delta=-(grad/np.linalg.norm(grad))  
    Cinv=np.linalg.inv(C)
    delta=np.dot(Cinv,delta)
    print(delta)
    alpha=1
    theta=10
    print(w)
    i=0
    
    with open('data1.dat','w') as file:
        while np.linalg.norm(alpha*delta) <theta :
            st=''
            grad=gradient(x1)
            grad=grad[func.__name__]
            delta=-(grad/np.linalg.norm(grad))  # generally we don not normalize in Newton step but here the hessian is not positive definite hence norm 
            Cinv=np.linalg.inv(C)
            delta=np.dot(Cinv,delta)
            while func(x1+alpha*delta) > func(x1) +(w*(np.dot(np.transpose(grad),alpha*delta))) :

                    alpha=w2*alpha
            for val in x1:
                
                st=st+str(val)+" "
         
                
            st=st+str(func(x1))+" "
            st=st+'\n'
            file.write(st)
            
            x1=x1+alpha*delta  
            
            alpha=min(w1*alpha,delmax)
            i=i+1
            if i==10:
                break
            

    return x1,alpha,delta


# In[9]:


#compute_grad_descent(x,fSq)


# In[10]:


compute_grad_descent(x,fHole)


# In[11]:


plot = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE)


# In[12]:



plot.communicate(b'''
set isosamples 50, 50
set contour
f(x,y) = x*x+10*y*y
#f(x,y) = 1 - exp(-x*x-10*y*y)
splot [-1:1][-1:1] f(x,y)
pause 2
unset contour
splot [-3:3][-3:3] f(x,y), 'data1.dat' with lines lt rgb "#00FF00"
pause 50
''')


# In[ ]:




