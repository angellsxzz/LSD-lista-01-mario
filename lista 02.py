#Verificação simples com and
print("verificação de dois valores)
x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))
if x > 0 and y > 0:
    print("Ambos os valores são positivos")
elif x > 0 or y > 0:
    print("Apenas um dos valores é positivo")
else:
    print("Nenhum dos valores é positivo")

#acesso com or
print("acesso ao sistema")
idade = int(input("Digite a idade: "))
if idade >= 18 or idade >= 65:
    print("Pode acessar o conteúdo")

#bloqueio com not
if not (idade >= 18):
    print("Não pode acessar o conteúdo")
    exit(0)

#condição combinada
print("ap ou rep")
Nota = float(input("Digite a sua nota 0/10: "))
Frequencia = float(input("Digite a sua frequência 0/100: "))
if Nota >= 7 and Frequencia >= 75:
    print("Aprovado")
else:
    print("Reprovado")
    if Nota > 10 or Nota < 0:
        print("Nota inválida")
        if Frequencia > 100 or Frequencia < 0:
            print("Frequência inválida")

#login
print("login no sistema")
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")
