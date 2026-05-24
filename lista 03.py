#numeros 1 a 20
print("Números de 1 a 20:")
numero = 1
while numero <= 20:
    print(numero)
    numero += 1
    
#numeros pares de acordo com o numero digitado
print("Números pares a partir do número digitado até 20:")
num = int(input("Digite um numero: "))
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1
#programa para calcular a média de números até inserir -1
print("Calculadora de média. Digite números inteiros:")

soma = 0
quantidade = 0

print("Digite números inteiros (digite -1 para parar):")

while True:
        numero = int(input("Digite um número: "))
        
        if numero == -1:
            break
        else:
            soma += numero
            quantidade += 1
if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma total: {soma}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhum número foi digitado.")
    
#pedir um numero e calcular a tabuada ate 100 com while
print("Tabuada do número digitado até o resultado ser maior que 100:")
numb = int(input("Digite um número para calcular a tabuada: "))
resultado = 0
contador = 1
while True:
    resultado = numb * contador
    if resultado > 100:
        break
    print(f"{numb} x {contador} = {resultado}")
    contador += 1

#fatorial
print("Calculadora de fatorial:")

n = int(input("Digite um número: "))
fatorial = 1
while n > 0:
    fatorial *= n
    n -= 1
print(fatorial)

#adivinhação de números entre 10 e 50
import random
numero_secreto = random.randint(10, 50)
print("Tente adivinhar o número entre 10 e 50:")
while True:
    palpite = int(input("Digite seu palpite: "))
      #passar para o prox cod 
    if palpite == 1:
        break
  
    if palpite < 10 or palpite > 50:
        print("Por favor, digite um número entre 10 e 50.")
        continue
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
        
#quadhex
print("Números de 1 a 50 com QuadHex:")
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
    
#numero binario de acordo com o numero digitado
numdecimal = int(input("Digite um número decimal para converter para binário: "))
num_binario = ""
if numdecimal == 0:
    num_binario = "0"
while numdecimal > 0:
    resto = numdecimal % 2
    num_binario = str(resto) + num_binario
    numdecimal //= 2
print(f"O número binário é: {num_binario}")

#numero perfeito
a = int(input("Digite um número para verificar se é perfeito: "))
somadivisores = 0
cont = 1
while cont < a:
    if a % cont == 0:
        somadivisores += cont
    cont += 1
if somadivisores == a:
    print(f"{a} é um número perfeito.")
else:
    print(f"{a} não é um número perfeito.")
    
#numero perfeito dentro de um intervalo
print("Números perfeitos dentro de um intervalo:")
começo = int(input("Digite o começo do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
while começo <= fim:
    somadivisores = 0
    contt = 1
    while contt < começo:
        if começo % contt == 0:
            somadivisores += contt
        contt += 1
    if somadivisores == começo:
        print(f"{começo} é um número perfeito.")
    começo += 1
    continue
#ngc dos raio la
print("Cálculo do volume de um cilindro:")
raio = float(input("Digite o raio do círculo: "))
altura = float(input("Digite a altura do cilindro: "))
r = 3.14
vlm = r * raio ** 2 * altura
print("O volume do cilindro é:", vlm)

#livros livros livros
print("Cálculo do custo total de livros com desconto e frete:")
print("livros")
quantidade = 74
livros = 32.90
desconto = 35/100
freteexemplar1 = 4
freteresto = 0.80
descontoaplicado = livros * desconto
totaldesconto = livros - descontoaplicado
totaldescontofrete = totaldesconto + freteexemplar1+ (75 *freteresto)
print(totaldescontofrete)

#quando o relogio bate as 9 todas as caveiras se sacodem
print("Cálculo do horário do alarme:")
oshorario = 9
alarmecaveira = (37 + oshorario) % 24      
print(f"Seu alarme irá tocar às: {alarmecaveira} horas meu patrão!")

#codigo la das horas p2
print("Cálculo do horário do alarme com base no horário atual e horas para esperar:")
horarioatual = int(input("Digite o horário atual (0-23): "))
horasesperar = int(input("Digite o número de horas pra esperar: "))
horariotocara = (horarioatual + horasesperar) % 24
print(f"O horário em que o alarme irá tocar é: {horariotocara} horas.")
#nnnn
print("Transformando um número em nn e nnnn")
n = int(input("Digite um número para transformar-lo: "))
nn = n * 11
nnnn = n * 1111
print(f"os valores são: {n} {nn} {nnnn}")

#trapezio
print("Cálculo da área do trapézio")
bsma = float(input("Digite o valor da base maior: "))
bsmn = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))
af = ((bsma + bsmn) * altura) / 2
print(f"A área do trapézio é: {af:.2f}")
f1 = float(input("Digite o valor a: "))
f2 = float(input("Digite o valor b: "))
fr = (f1 - f2) * (f1 - f2)
print(f"O resultado é: {fr:.2f}")

#milha metro e centimetros
print("Conversão de quilômetros para milhas, metros e centímetros:")
km = float(input("Digite a distância em quilômetros: "))
milhas = km * 0.621371
metros = km * 1000
centimetros = km * 100000
print(f"{km} km é igual a {milhas:.2f} milhas, {metros:.2f} metros e {centimetros:.2f} centímetros.")

#distancia entre dois pontos(q porra é essa meu fi)
print("Cálculo da distância entre dois pontos no plano cartesiano:")
print("Digite as coordenadas do Ponto 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Digite as coordenadas do Ponto 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"A distância entre os pontos é: {distancia:.2f}")

#5 digitos em 1
print("Soma dos dígitos de um número de 5 dígitos:")
n = int(input("Digite um número de 5 dígitos: "))
s = 0
while n > 0:
    digito = n % 10
    s += digito
    n //= 10
print(f"A soma dos dígitos é: {s}")

# verificação dos numeros e armazenamento em variavel
print("Verificação se um número é positivo, negativo ou neutro:")
v1 = float(input("digite um valor para verificar: "))
if v1 > 0:
    print("O número é positivo.")  
elif v1 < 0:
        print("O número é negativo.")
else:
        print("O número é neutro.") 
#classificar idade
idade = int(input("Digite a idade: "))
if idade < 0:
    print("desiste mano.")
elif idade <= 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
    
#intervalo de numeros
print("Classificação de um número em intervalos:")

i1 = int(input("Digite um numero: "))
if i1 < 0 or i1 > 200:
  print("Número fora do intervalo.")
elif i1 >= 50 and i1 < 100:
    print("entre 50 e 100")
else:
    print("fora das condições")

#calculo de 3 numeros
print("Cálculo de três números com condição de igualdade:")
a1 = float(input("Digite o primeiro número: "))
a2 = float(input("Digite o segundo número: "))
a3 = float(input("Digite o terceiro número: "))
if a1 == a2 == a3:
    resultado = (a1 + a2 + a3) * 3
    print(f"O resultado é: {resultado}")
else:
    resultado = a1 + a2 + a3
    print(f"O resultado é: {resultado}")
    
#divisivel por 4 5 ou nenhum
print("Verificação de divisibilidade por 4 e 5:")
d1 = int(input("Digite um número: "))
if d1 % 4 == 0:
    print("O número é divisível por 4.")
elif d1 % 5 == 0:
    print("O número é divisível por 5.")
else:
    print("O número não é divisível por 4 nem por 5.")  

#numeros de um valor diferente ou iguais
print("Verificação de igualdade dos dígitos:")
r1 = float(input("Digite o número: "))
v = r1 % 10
c = r1 // 10 % 10
d = r1 // 100 % 10
u = r1 // 1000 % 10
if v == c == d == u:
    print("Todos os dígitos são iguais.")
else:
    print("nenhum dos/nem todos os dígitos são iguais.")
    
#numero espelhado 1221
por = input("Digite um número de 4 dígitos: ")
d1 = por[0]
d2 = por[1]
d3 = por[2]
d4 = por[3]
if d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4:
    print("Todos os dígitos são diferentes entre si.")
else:
    print("Existem dígitos repetidos no número.")
