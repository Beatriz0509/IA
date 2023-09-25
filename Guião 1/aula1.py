#Exercicio 1.1
def comprimento(lista):
    if not lista:
        return 0
    else:
        return (1 + comprimento(lista[1:]))

#Exercicio 1.2
def soma(lista):
	if not lista:
		return 0
	else:
		return (lista[0] + soma(lista[1:]))

#Exercicio 1.3
def existe(lista, elem):
	if not lista:
		return False
	else:
		return (lista[0] == elem or existe(lista[1:], elem))

#Exercicio 1.4
def concat(l1, l2):
	if not l1:
		return l2
	if not l2:
		return l1
	else:
		return [l1[0]] + concat(l1[1:], l2)

#Exercicio 1.5
def inverte(lista):
	if not lista:
		return []
	else:
		return (inverte(lista[1:]) + [lista[0]])

#Exercicio 1.6
def capicua(lista):
	if not lista:
		return True
	else:
		return (lista[0] == lista[-1] and capicua(lista[1:-1]))

#Exercicio 1.7
def concat_listas(lista):
	if not lista:
		return []
	else: 
		return lista[0] + concat_listas(lista[1:])


#Exercicio 1.8
def substitui(lista, original, novo):
	if not lista:
		return []
	else:
		if (lista[0] == original):
			lista[0] = novo
		return [lista[0]] + substitui(lista[1:], original, novo)

#Exercicio 1.9
def fusao_ordenada(lista1, lista2): 
	if not lista1 or not lista2:
		return concat(lista1, lista2)
	else:
		if (lista1[0] <= lista2[0]):
			return [lista1[0]] + fusao_ordenada(lista1[1:], lista2)
		else:
			return [lista2[0]] + fusao_ordenada(lista1, lista2[1:])

#Exercicio 1.10
def lista_subconjuntos(lista):
	if not lista:
		return [[]]
	else:
		elemento = lista[0]
		subconjuntos = lista_subconjuntos(lista[1:])
		return concat(subconjuntos, [[elemento] + subset for subset in subconjuntos])


#Exercicio 2.1
primeiros = []
segundos = []         
def separar(lista):
	if not lista:
		return primeiros, segundos
	else:
		primeiros.append(lista[0][0])
		segundos.append(lista[0][1])
		return separar(lista[1:])
	

#Exercicio 2.2
ocorrencia = 0
def remove_e_conta(lista, elem):
    if not lista:
        return ([], 0)
    if lista[0] == elem:
        sublist, ocorrencia = remove_e_conta(lista[1:], elem)
        return (sublist, ocorrencia + 1)
    else:
        sublist, ocorrencia = remove_e_conta(lista[1:], elem)
        return ([lista[0]] + sublist, ocorrencia)

#Exercicio 3.1
def cabeca(lista):
	if not lista:
		return None
	else:
		return lista[0]

#Exercicio 3.2
def cauda(lista):
	if not lista:
		return None
	else:
		return lista[1:]

#Exercicio 3.3
def juntar(l1, l2):
	if not l1 or not l2:
		return []
	elif len(l1) != len(l2):
		return None
	else:
		return [(l1[0],l2[0])] + juntar(l1[1:], l2[1:])
    

#Exercicio 3.4
def menor(lista):
	if not lista:
		return None
	if len(lista) == 1:
		return lista[0]
	
	menor_da_sublista = menor(lista[1:])

	if lista[0] < menor_da_sublista:
		return lista[0]
	else:
		return menor_da_sublista
	
#Exercicio 3.6
def max_min(lista):
	pass
