# Solicitar os dois números
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

# Menu para escolher a operação
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite o número correspondente à operação desejada: "))

# Realizar a operação escolhida
if operacao == 1:
    resultado = number1 + number2
    print("Resultado da soma:", resultado)
elif operacao == 2:
    resultado = number1 - number2
    print("Resultado da subtração:", resultado)
elif operacao == 3:
    resultado = number1 * number2
    print("Resultado da multiplicação:", resultado)
elif operacao == 4:
    if number2 != 0:  # Garantir que não há divisão por zero
        resultado = number1 / number2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida! Tente novamente.")