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

#ano, bissexto, 4 anos

ano = input("Digite seu nome: ")