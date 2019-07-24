usuarios = ["Arthur", "Leandro"]

usuarios.append("Kevin")

print(usuarios)

#Saber se um elemento existe na lista

if "Arthur" in usuarios:
    print("Arthur esta na lista")
    
del usuarios[2]

print(usuarios)

lista = [44,54656,57,6543,6,673]

lista.reverse()

print(lista)

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)
