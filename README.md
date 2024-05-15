[Uploading quesa2.py…]()def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
numero = 5
print("O fatorial de", numero, "é", fatorial(numero))

def fatorial(numero):
    if not isinstance(numero, int) or numero < 0:
        return "Por favor, forneça um número inteiro não negativo."
    elif numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

numero = [5]
print("O fatorial de", numero, "é", fatorial(numero))
def validar_senha(func):
    def decorador(*args, **kwargs):
         args = [str(arg) for arg in args]
         kwargs = {key: str(value) for key, value in kwargs.items()}
         return func(*args, **kwargs)
    return decorador

import re

print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
senha = input("Digite sua senha : ")

while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r'[!@#$%¨&*]', senha)):  
    senha = input("Use como base os critérios informado : ")

print("Senha cadastrada com sucesso!")

while senha.islower():
        senha = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")

while len(senha) < 7 :
    senha = input("A senha deve ter pelo menos 8 caracteres: ")

while senha.isalpha() :
    senha = input("Necessita de um numero: ")

while senha.isalnum() :
    senha = input("Necessita de um Caractere especial: ")

'''def calcular_estatisticas(notas):
    total = sum(notas)
    media = total / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    return media, nota_maxima, nota_minima

# Solicitar ao usuário quantos alunos e notas deseja inserir
num_alunos = int(input("Quantos alunos você deseja inserir? "))
num_notas_por_aluno = int(input("Quantas notas cada aluno tem? "))

# Listas para armazenar as notas de cada aluno
notas_alunos = []

# Solicitar e armazenar as notas de cada aluno
for i in range(num_alunos):
    notas = []
    print(f"Notas do aluno {i + 1}:")
    for j in range(num_notas_por_aluno):
        nota = float(input(f"Insira a nota {j + 1} do aluno {i + 1}: "))
        notas.append(nota)
    notas_alunos.append(notas)

# Calcular as estatísticas
medias = []
notas_maximas = []
notas_minimas = []

for notas in notas_alunos:
    media, nota_maxima, nota_minima = calcular_estatisticas(notas)
    medias.append(media)
    notas_maximas.append(nota_maxima)
    notas_minimas.append(nota_minima)

# Calcular a média geral
media_geral = sum(medias) / len(medias)

# Exibir os resultados
print("Média geral dos alunos:", media_geral)
print("Nota mais alta:", max(notas_maximas))
print("Nota mais baixa:", min(notas_minimas))
'''
'''

import re

print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
senha = input("Digite sua senha : ")

while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r'[!@#$%¨&*]', senha)):  
    senha = input("Use como base os critérios informado : ")

print("Senha cadastrada com sucesso!")





while senha.islower():
        senha = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")

while len(senha) < 7 :
    senha = input("A senha deve ter pelo menos 8 caracteres: ")

while senha.isalpha() :
    senha = input("Necessita de um numero: ")

while senha.isalnum() :
    senha = input("Necessita de um Caractere especial: ")
'''
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

# Teste da função
numero = 5
print("O fatorial de", numero, "é", fatorial(numero))
 
 def fatorial(numero):
    if not isinstance(numero, int) or numero < 0:
        return "Por favor, forneça um número inteiro não negativo."
    elif numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

# Teste da função
numero = [5]
print("O fatorial de", numero, "é", fatorial(numero))

