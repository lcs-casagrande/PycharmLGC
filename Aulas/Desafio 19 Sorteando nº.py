import random
n1=input('1º Sabor de sorvete:')
n2=input('2º Sabor de sorvete:')
n3=input('3º Sabor de sorvete:')
n4=input('4º Sabor de sorvete:')
lista=[n1,n2,n3,n4]
escolhido= random.choice(lista)
print('Escolho o sorvete de {}!'.format(escolhido))
