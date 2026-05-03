# media dos 3 numeros
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
print("Média: ", media)

# maior dos 2
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a > b:
    print("Maior número:", a)
elif a < b:
    print("Maior número:", b)
else:
    print("Os números são iguais")

# impar ou par
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("É par")
else:
    print("É ímpar")

# maior ou menor de idade
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# positivo e negativo
numero = float(input("Digite um número: "))

if numero >0:
    print("Positivo")
elif numero <0:
    print("Negativo")
else:
    print("Zero")

# desconto
preco = float(input("Digite o preço do produto: "))

if preco > 100:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print("Preço com desconto:", preco_final)
else:
    print("Preço normal:", preco)