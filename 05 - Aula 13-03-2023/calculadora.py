sair = "sair"
while True:
    numero1 = input ("Escreva o primeiro número: ")
    numero2 = input ("Escreva o segundo número: ")
    operador = input ("Digite o operador (+-*/): ")
    numero1_float = 0
    numero2_float = 0 

    numero_valido= None   
    try: # Tentar executar o código
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numero_valido= True

    except: # Caso tenha executar o código
      numero_valido = False

    if numero_valido == False:
        print("Número inválido. ")
        continue

    operador_aceito= ("+-*/")
    
    if operador not in operador_aceito:
        print("Operador não aceito")

    if len(operador) > 1:
        print("Operador inválido ")     


    if operador == "+":
        print(f"{numero1_float} + {numero2} = ", numero1_float + numero2_float )
    elif operador == "-":
        print(f"{numero1_float} - {numero2} = ", numero1_float - numero2_float )
    elif operador == "*":
        print(f"{numero1_float} * {numero2} = ", numero1_float * numero2_float )
    elif operador == "/":
        print(f"{numero1_float} / {numero2} = ", numero1_float / numero2_float )
    else:
        print("Error")

    sair = input ("Deseja sair? ").lower().startswith("s")
    if sair is True:
        break