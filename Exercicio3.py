"""Exercicio 3:
Escreva um programa que resolva 
uma equação de segundo grau.   
"""

a = input("Digite o coeficiente quadrático: ")
b = input("Digite o coeficiente linear: ")
c = input("Digite o coeficiente constante: ")

b_negado = int(b)*-1
delta = ((int(b)**2) - (4*int(a)*int(c)))
raizDelta = delta ** (1/2)
x1 = ((int(b_negado)+int(raizDelta))/(2*int(a)))
x2 = ((int(b_negado)-int(raizDelta))/(2*int(a)))

if delta < 0:
    print("\nDelta menor que 0\nNao possui raizes reais")
elif delta > 0:
    print("\nDelta maior que 0\nPossui 2 raizes\nResultados:")
    print(x1)
    print(x2)
else:
    print("\nDelta igual a 0\nPossui uma raiz real\nResultado (não simplificado):")
    print(x1)
