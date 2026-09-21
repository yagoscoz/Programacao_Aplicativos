#listas Tuplas e Dicionarios


#1 - Listas = vetores, para armazenar varios valores de uma vez

nomes = [12 , 12 , 34 , 54 , 6 , 7 , 7 , 234]
print(nomes)

#Acessando elementos da lista
print(nomes[7])

#Podemos acessar o ultimo elemento
print(nomes[-1])


#4 Adiciona um elemento ao final da lista append()

nomes.append(100)
print(nomes)



#insert() adiciona um elemento em uma posicao

nomes.insert(0,100)
print(nomes)


#remove , remove algo do vetor
nomes.remove(100)
print(nomes)