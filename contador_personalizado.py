inicio = int(input('Me fale onde vai começar: '))
fim = int(input('Me fale onde vai acabar: '))
passos = int(input('Me fale quantos passos vai dar: '))

for i in range(inicio, fim, passos):
    print(i)
print('Fim')
