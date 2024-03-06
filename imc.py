# modulo imc
# import estado_imc
import estado_imc as calculo

print("************************************")
print("*         Calculadora IMC          *")
print("************************************")
nome = input("Digite o seu nome: ")

erro = True

while erro:
    try:
        peso = int(input("Digite o seu peso: "))
        erro = False

    except:
        print("---Valor do peso inválido. Digite novamente---")

erro = True

while erro:
    try:
        altura = float(input("Digite a sua altura: "))
        erro = False

    except:
        print("---Valor de altura inválido. Digite novamente---")


calculo.calcular_imc(peso, altura)
