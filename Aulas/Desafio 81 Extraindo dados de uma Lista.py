lista=[]
while True:
    v=int(input('Digite uma valor: '))
    c=input('Quer continuar[S/N]? ').upper()
    lista.append(v)
    if c in 'N':
        break
lista.sort(reverse=True)
quant=len(lista)
print('=-'*30)
print(f'Você digitou {quant} elementos. ')
print(f'Os valores em ordem decrecente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')