lista=[]
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado. Não adicionado. ')
    else:
        lista.append(n)
        print('Adicionado com sucesso!')
    con = input('Quer continuar [S/N]? ').upper()
    if con in 'N':
        break
lista.sort()
print(lista)

