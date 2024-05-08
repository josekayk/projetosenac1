'''
def fatorial (a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i
        return fat
    
x = int(input("Digitde = int(inpue um numero inteiro: "))
print("O fatorial de ", x, "é: ", fatorial(x))
'''
'''
#nome, altura, idade, tem_carro

nome = input("Digite seu nome: ")
idade("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
tem_carro = input("você possui algum carro? (sim/não): ")

tem_carro = tem_carro.lower() == "sim"

print("informações digitadas: ")
print("Nome: ", nome)
print("Altura: ", altura)
print("Tem carro? ", "sim" if tem_carro else "não")
'''
'''
def contagem_regressiva():
    numero i= int(input("Digite um numero inteiro construtivo: "))
    if numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
        contagem_regressiva()

    else:
         while numero >= 0:
            print(numero)
            numero -= 1

contagem_regressiva()
'''

def soma (a, b):
    return a+ b
def subtração(a, b):
    return a - b
def multiplicação (a, b):
    return a * b
def divisão (a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão invalida"
    

def calculadora(:)
    print("Bem vindo a calculadora em python!")
    print("Selecione a operação desejada: ")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação ")
    print("4: Divisão ")
    
    escolha = input("Digite sua escolha 1/2/3/4: ")
    if escolha in ('1', '2', '3', '4'):
        num1 = float (input("Digite o primeiro número: "))
        mum2 = float (input("Digite o segundo número: "))




