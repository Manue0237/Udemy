texto=input("Ingrese un texto: ")
letra=input("Ingrese una letra: ")
texto=texto.lower()
letra=letra.lower()

lista=list(texto)
Sol1=lista.count(letra)
print("La letra",letra,"aparece",Sol1,"veces en el texto")


Sol2=len(texto.split())
print("El texto tiene",Sol2,"palabras")

##Sol3
print("La primera letra del texto es: ",lista[0]," y la ultima letra es:", lista[-1])

##Sol4
print("El texto al reves",texto[::-1])


##Sol5
if ('python' in texto):
    print("La palabra python esta en el texto")
else:
    print("La palabra python no esta en el texto")

