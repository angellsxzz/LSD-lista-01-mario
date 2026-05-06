# Média de 3 numeros
print("Média de 3 numeros")
numero1 = float(input("insira o primeiro número:"))
numero2 = float(input("insira o segundo número:"))
numero3 = float(input("insira o terceiro número:"))
media = (numero1+numero2+numero3) / 3
print('Média:', media)

# Maior dos dois números
print("qual numero é maior...")
n1 = float(input("digite o primeiro número:"))
n2 = float(input("digite o segundo numero:"))
if n1>n2:
    print('o número 1 é maior que o numero 2')
elif n1<n2:
    print('o número 2 é maior que o numero 1')
else:
    print('os numeros são iguais.')

# Impar ou par
print("impar ou par")
numip=float(input("digite um número para saber se é impar ou par:"))
if  numip % 2 == 0:
    print('o numero é par')
else:
    print('o numero é impar')

# Idade
print("Maior ou menor de idade")
idade = int(input("digite a sua idade:"))
if idade >= 18:
    print('você é maior de idade')
else:     
    print('você é menor de idade!')

# + ou -
print("Número positivo ou negativo")
numL = float(input("digite um numero para saber se é positivo ou negativo:"))
if numL > 0:
    print('o valor é positivo')
else:
    print('o valor é negativo')

print("desconto")
produto = float(input("digite o valor do produto:"))
if produto >= 100:
    desconto = produto*0.10
    aposdesconto = produto - desconto
    print("você pagará:", aposdesconto)
else:
    print(produto)
    


