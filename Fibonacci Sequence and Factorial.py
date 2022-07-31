#!/usr/bin/env python
# coding: utf-8

# In[12]:


def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(10)


# In[13]:


def fact(n):
    f=1
    
    for i in range(1,n+1):
        f=f*i
        
    return f
x=6
result=fact(x)
print(result)
        


# In[ ]:




