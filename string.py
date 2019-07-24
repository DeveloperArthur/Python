a = "ola"
b = "mundo"
string = "eu to morrendo de fome"
lista = string.split(" ")
busca = string.find("fome")

concatenar = a+" "+b 
print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(a[0])
print(b[1:4])

print(concatenar.lower())
print(concatenar.upper())

print(lista)
print(busca)

string = string.replace("fome","sono")
print(string)
