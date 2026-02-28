import random

numero = random.randint(1, 10)

print('''======Jogo da advinha======
    
   Você tem 5 tentativas
''')

contador = 0

while contador < 5:
    Entrada_do_jogador = input('Digite um número: ') # Entrada de número.
    try:# Tratamento de erro caso não sejá um número.
        Entrada_do_jogador = int(Entrada_do_jogador) # Converte para inteiro

        if Entrada_do_jogador <= 10 and Entrada_do_jogador >= 1: #Verifica se a entrada é menor ou igual a 10 e maior ou igual a 1.
            if numero == Entrada_do_jogador:
                print('Você acertou!')
                break
            elif numero > Entrada_do_jogador:
                print('O número é maior, Tente novamente' if contador  < 4 else 'Número errado, suas chances acabaram')
                contador += 1
            else:
                print('O número é menor, Tente novamente' if contador < 4 else 'Número errado, suas chances acabaram')
                contador += 1
        else:
            print('Esse valor é invalido, só é permitido números entre 1 e 10')

    except ValueError:
        print('Tem que ser um número.')