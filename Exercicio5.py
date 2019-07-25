"""Exercicio 5:
Escreva um programa que receba 
dois números e um sinal, e faça a 
operação matemática definida pelo sinal.     
"""

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
sinal = input("Digite um sinal para a operacao: ")

if sinal == '+':
    result = n1 + n2
elif sinal == '-':
    result = n1 - n2
elif sinal == '*':
    result = n1 * n2
elif sinal == '/':
    result = n1 / n2
else:
    result = 'erro'
    print("ERRO01: Digite um sinal valido!")
    
if result != 'erro':
    print(result)
