contador = 2
while contador <= 20:
    print(contador)
    contador += 1
#
num= int(input("Digite um número: "))
cont= 0        
while cont <= num:
    if cont % 2 == 0:
        print(cont)
    cont += 1
soma = 0
quantidade = 0
#
num= int(input("Digite um número: "))
while num != -1:
    soma += num
    quantidade += 1
    num = int(input("Digite outro número (ou -1 para parar): "))
media = soma / quantidade
print("Média:", media)
#
numero = int(input("Digite um número: "))
while numero != 0:
    contador = 1
    while numero * contador < 100:
        print(numero * contador)
        contador += 1
    numero = int(input("Digite outro número (0 para sair): "))
#
n = int(input("Digite um número: "))
fatorial = 1
while n > 0:
    fatorial *= n
    n -= 1
print(fatorial)
#
import random
num = random.randint(10, 50)
palpite = int(input("Adivinhe o número: "))
while palpite != num:
    if palpite < num:
        print("O número é maior!")
    else:
        print("O número é menor!")
    palpite = int(input("Tente novamente: "))
print("Acertou!")
#
contador = 1
while contador <= 50:
    if contador % 4 == 0 and contador % 6 == 0:
        print("QuadHex")
    elif contador % 4 == 0:
        print("Quad")
    elif contador % 6 == 0:
        print("Hex")
    else:
        print(contador)
    contador += 1
#
# nao entendi essa de binário sorry
#
numero = int(input("Digite um número: "))
soma = 0
contador = 1
while contador < numero:
    if numero % contador == 0:
        soma += contador
    contador += 1
if soma == numero:
    print("Número perfeito")
else:
    print("Não é perfeito")
#
inicio = int(input("Início: "))
fim = int(input("Fim: "))
numero = inicio
while numero <= fim:
    soma = 0
    divisor = 1
    while divisor < numero:
        if numero % divisor == 0:
            soma += divisor
        divisor += 1
    if soma == numero:
        print(numero)
    numero += 1
#
r = float(input("Raio: "))
h = float(input("Altura: "))
v = 3.14 * r**2 * h
print("Volume =", v)
#
print("Livros")
preco = 32.90
desconto = 0.35
livro = preco - preco * desconto
total_livros = livro * 75
frete = 4 + (74 * 0.80)
total = total_livros + frete
print("Total =", total)
#
hora = 9
alarme = (hora + 37) % 24
print("O alarme tocará às", alarme, "horas")