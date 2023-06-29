""" Bibliotecas úteis """

import math as m
import datetime as dt
import random as r
import time as t

""" MATH """

""" Raiz quadrada """
print(m.sqrt(10))

""" Seno """
print(m.sin(45))

""" Log """
print(m.log(1000, 10))

""" Número de Euler """
print(m.e)

""" DATETIME """
""" Verificar recursos """
dir(dt)

""" Hoje """
print(dt.date.today())

print(dt.datetime.now())

data = dt.date(2020, 7, 10)
print(data)
print(data.month)
print(data.day)
print(data.year)

""" Definindo hora """
horario = dt.datetime(2023, 2, 26, 18, 13, 0)
print(horario)

print(horario.hour)
print(horario.minute)
print(horario.second)

""" RANDOM """
print(r.random())

""" Com faixa """
print(r.randint(1, 10))

""" Com faixa de 2 em 2 """
print(r.randrange(0, 10, 2))

""" Sorteando """
x = ['K','d', 13, '34-j', 'x' ]

print(r.choice(x))

""" Time """
print(t.time())

antes = t.time()
lista = []

for i in range(0, 1000000):
    lista.append(i)
depois = t.time()

intervalo = depois - antes

print(f'Tempo: {intervalo} segundos')



