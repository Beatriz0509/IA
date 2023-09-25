from math import sqrt, atan2

#Exercicio 4.1
impar = lambda number : number % 2 != 0

#Exercicio 4.2
positivo = lambda number : number > 0

#Exercicio 4.3
comparar_modulo = lambda number1, number2 : abs(number1) < abs(number2)

#Exercicio 4.4
cart2pol = lambda x, y : (sqrt(x*x + y*y), atan2(y,x))

#Exercicio 4.5
ex5 = lambda f, g, h : lambda x, y, z : h(f(x, y), g(y, z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    if not lista:
        return True
    else:
        return quantificador_universal(lista[1:], f) and f(lista[0])


#Exercicio 4.8
def subconjunto(lista1, lista2):
    if not lista1:
        return True
    elif not lista2:
        return False
    else:
        if lista1[0] == lista2[0]:
            return True and subconjunto(lista1[1:], lista2[1:])
        else:
            return subconjunto(lista1, lista2[1:])

#Exercicio 4.9
def menor_ordem(lista, f):
    if not lista:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] if f(lista[0], menor_ordem(lista[1:], f)) else menor_ordem(lista[1:], f)

#Exercicio 4.10
def menor_e_resto_ordem(lista, f):
    if not lista:
        return None
    elif len(lista) == 1:
        return lista[0], []
    else:
        menor, resto = menor_e_resto_ordem(lista[1:], f)
        if f(lista[0], menor):
            return lista[0], lista[1:]
        else:
            return menor, [lista[0]] + resto

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass
