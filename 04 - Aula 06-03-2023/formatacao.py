a = "Dieimes"
b = 32
c = "anos"

texto = "a={nome} b={idade}"

texto2 = "O professor {0} possui {1} {2}"

exibir = texto.format(nome=a, idade=b)

exibir2 = texto2.format(a, b, c)

print(exibir)

print(exibir2)