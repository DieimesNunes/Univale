# if / elif / else
#se / se não se /  senão 

teste = True
resultado = input('Deseja entrar no sistema? "Sim" ou "Não": ')

if resultado == "Sim":
    print("Você entrou no sistema ")
elif resultado == "Não":
    print("Você saiu no sistema ")
else:
    print("Você não digitou nem Sim e nem Não ")