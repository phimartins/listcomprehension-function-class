# List Comprehension, Function, Class

Criando uma lista de temperaturas em Celsius e convertendo para Fahrenheit usando list comprehension


```python
temp_celsius = [30.4,40.3,33.4,44.5]

temp_fahrenheit = list([round((x * 1.8)+32,2) for x in temp_celsius])
```


```python
print(temp_fahrenheit)
```

    [86.72, 104.54, 92.12, 112.1]
    

Criando uma função que converte para Fahrenheit todos os elementos de uma lista usando list comprehension


```python
def to_fahrenheit(lista):
    return list([round((x * 1.8)+32,2) for x in lista])
```


```python
print(to_fahrenheit(temp_celsius))
```

    [86.72, 104.54, 92.12, 112.1]
    

Criando uma função que converte uma temperatura para Fahreinheit e aplicando list comprehension para aplicar a função em todos os elementos de uma lista


```python
def to_fahrenheit2(number):
    return round((number * 1.8)+32,2)
```


```python
print([to_fahrenheit2(x) for x in temp_celsius])
```

    [86.72, 104.54, 92.12, 112.1]
    

Criando uma função lambda e armazenando em uma variável, para depois aplicar em um elemento e convert-lo para Fahreinheit


```python
convert_fahrenheit = lambda x : round((x * 1.8)+32, 2)
```


```python
convert_fahrenheit(33.4)
```




    92.12



Criando uma classe com um método e chamando o método


```python
class curso:
    def __init__(self):
        self.instrutores = ['rodrigo', 'thiago']
    
    def imprima_instrutores(self):
        [print(instrutor) for instrutor in self.instrutores]
```


```python
meu_curso = curso()
```


```python
meu_curso.imprima_instrutores()
```

    rodrigo
    thiago
    
