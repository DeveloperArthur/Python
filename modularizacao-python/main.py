import aleatorio as a
import media as m

lista = a.gerarListaInteiro(4)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("Minha lista: ")
print(lista)
print("A media da minha lista eh "+str(media))
print("A mediana da minha lista eh "+str(mediana))
print("A moda da minha lista eh "+str(moda)) 