hora_atual = int(input("Hora atual: "))
espera = int(input("Horas de espera: "))
hora_final = (hora_atual + espera) % 24
print(hora_final)
#
n = int(input("Digite N: "))
nn = n * 11
nnnn = n * 1111
print(n)
print(nn)
print(nnnn)
#
base_maior = float(input("Base maior: "))
base_menor = float(input("Base menor: "))
altura = float(input("Altura: "))
area = ((base_maior + base_menor) * altura) / 2
print(area)
# 
#to achando q esse ta rodando errado
a = float(input("Digite a: "))
b = float(input("Digite b: "))
resultado = (a - b) * (a - b)
print(resultado)
#
km = float(input("Digite a distância em km: "))
metros = km * 1000
centimetros = km * 100000
milhas = km * 0.621371
print("Metros:", metros)
print("Centímetros:", centimetros)
print("Milhas:", milhas)
#
# nao entendi tb
#
numero = int(input("Digite um número de 5 dígitos: "))
soma = 0
while numero > 0:
    soma += numero % 10
    numero = numero // 10
print(soma)
#
n = int(input("Digite um número: "))
if n > 0:
    print("positivo") 
elif n <0:
    print("negativo")
else:
    print("neutro")

#
idade = int(input("Digite a idade: "))
if idade >= 60:
    print("idoso")
elif idade >= 18:
    print("adulto")
elif idade >= 12:
    print("adolescente")
else:
    print("criança")
#
n = int(input("Digite um número: "))
if 50 <= n <= 100:
    print("entre 50 e 100")
elif n < 0 or n > 200:
    print("menor que 0 ou maior que 200")
else:
    print("fora das condições anteriores")
#
a = int(input())
b = int(input())
c = int(input())
soma = a + b + c
if a == b == c:
    print(soma * 3)
else:
    print(soma)
#
n = int(input("Digite um número: "))
if n % 4 == 0:
    print("divisível por 4")
elif n % 5 == 0:
    print("divisível por 5")
else:
    print("não é divisível por 4 ou 5")
#
n = int(input("Digite um número de 4 dígitos: "))
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
if a != b and a != c and a != d and b != c and b != d and c != d:
    print("Todos são diferentes")
else:
    print("Há dígitos iguais")
#
#n tankei