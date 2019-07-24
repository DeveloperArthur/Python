#ler arquivo.txt:

arquivo = open("arquivo.txt")
texto = arquivo.read()
print(texto)

#gravando strings no arquivo.txt

w = open("arquivo.txt", "a")
w.write("Esse eh meu arquivo\n")
w.close()
