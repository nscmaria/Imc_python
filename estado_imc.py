    # MODULO IMC

def definir_estado_imc(imc):
    estado = ""

    if imc < 18.5:
        estado = "O peso está a baixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        estado = "O peso está Normal"
    elif imc >= 25 and imc <= 29.9:
        estado = "O peso está levemente a cima do peso"
    elif imc >= 30 and imc <= 34.9:
        estado = "O peso está em Obesidade Grau I"
    elif imc >= 35 and imc <= 39.9:
        estado = "O peso está em Obesidade Grau II"
    elif imc >= 40:
        estado = "O peso está em Obesidade Grau III ou Mórbita"
    else:
        estado = "Inválido."

    print("-------------------------------------------")
    print(f"O IMC do paciente: {imc:.2f}\nO estado do paciente: {estado}")
    print("-------------------------------------------")

def calcular_imc(peso, altura):
    imc = peso / altura ** 2

    definir_estado_imc(imc)

