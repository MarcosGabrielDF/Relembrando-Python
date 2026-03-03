# Uma calculadora
valor1 = float(input('Informe o primeiro valor: '))

operacao = input("""
Informe qual operação você quer fazer:

    [ + ] somar
    [ - ] Subtrair
    [ * ] multiplicar
    [ / ] Dividir
    
Informe: """)

valor2 = float(input('Informe o segundo valor: '))

if operacao == '+':
    resultado = valor1 + valor2
elif operacao == '-':
    resultado = valor1 - valor2
elif operacao == '*':
    resultado = valor1 * valor2
elif operacao == '/':
    resultado = valor1 / valor2

print(f'Resultado de {valor1:g} {operacao} {valor2:g} é {resultado:g}')

