"""Exercicio 1: 
Faça um programa que 
receba a idade do usuário 
e diga se ele é maior ou menor de idade.   
"""

idade = input("Digite sua idade: ")

if int(idade) < 18:
    print("voce eh MENOR de idade")
else:
    print("voce eh MAIOR de idade")
