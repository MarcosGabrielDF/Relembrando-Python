import string

def Criptografia(senha):
    if senha.isalpha():  # Verifica se é composta apenas por letras
        alfabeto = string.ascii_lowercase
        conversao_alfabeto = [alfabeto.index(letra.lower()) + 1 for letra in senha if letra.isalpha()]  # Transforma as letras em números referentes à sua posição no alfabeto.
        modificar_conversao = [n ** 7 / 4.22 for n in conversao_alfabeto]
        return modificar_conversao
    else:
        print("Só é válido letras.")

def Descriptografar(senha):
    inverter_modificador_conversor = [round((n * 4.22) ** (1 / 7)) for n in senha]
    alfabeto = string.ascii_lowercase
    senha_recuperada = "".join([alfabeto[numero - 1] for numero in inverter_modificador_conversor])
    return senha_recuperada

senha = input('Qual é sua senha? ')  # Pergunta qual é a senha

senha = Criptografia(senha)
print(senha)

senha_quebrada = Descriptografar(senha)
print(senha_quebrada)