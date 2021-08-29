#!/usr/bin/env python
# coding: utf-8

# # List Comprehension, Function, Class

# Criando uma lista de temperaturas em Celsius e convertendo para Fahrenheit usando list comprehension

# In[24]:


temp_celsius = [30.4,40.3,33.4,44.5]

temp_fahrenheit = list([round((x * 1.8)+32,2) for x in temp_celsius])


# In[10]:


print(temp_fahrenheit)


# Criando uma função que converte para Fahrenheit todos os elementos de uma lista usando list comprehension

# In[11]:


def to_fahrenheit(lista):
    return list([round((x * 1.8)+32,2) for x in lista])


# In[12]:


print(to_fahrenheit(temp_celsius))


# Criando uma função que converte uma temperatura para Fahreinheit e aplicando list comprehension para aplicar a função em todos os elementos de uma lista

# In[13]:


def to_fahrenheit2(number):
    return round((number * 1.8)+32,2)


# In[14]:


print([to_fahrenheit2(x) for x in temp_celsius])


# Criando uma função lambda e armazenando em uma variável, para depois aplicar em um elemento e convert-lo para Fahreinheit

# In[15]:


convert_fahrenheit = lambda x : round((x * 1.8)+32, 2)


# In[16]:


convert_fahrenheit(33.4)


# Criando uma classe com um método e chamando o método

# In[17]:


class curso:
    def __init__(self):
        self.instrutores = ['rodrigo', 'thiago']
    
    def imprima_instrutores(self):
        [print(instrutor) for instrutor in self.instrutores]


# In[18]:


meu_curso = curso()


# In[19]:


meu_curso.imprima_instrutores()

