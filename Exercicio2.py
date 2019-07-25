"""Exercicio 2:
Faça um programa que receba duas 
notas digitadas pelo usuário. 
Se a nota for maior ou igual a seis, 
escreva aprovado, senão escreva reprovado.   
"""

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
media = int(nota1)+int(nota2)

if media >= 6:
    print("aprovado")
else:
    print("reprovado")
