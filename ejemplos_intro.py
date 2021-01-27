#Introducción a Python
print("Abre este archivo con editor para revisar comentarios y entender las salidas")
'''Tres comillas simples o dobles nos permiten colocar
comentarios multilínea en Python, el # solo comentario por línea'''

#Operadores básicos
"""
Asignación =
Comparación ==
División /
División Entera //

Números imaginarios
a=3+5j

Parte Real a.real
Parte Imaginaria a.imag

Tipo de datos type(dato_variable)
"""
#Asignación múltiple
numero, decimal, nombre = 17, 0.33, "Alex"
#Asigna por posición el valor de las variables y los elementos
#Cadenas

"""
Se pueden multiplicar (*) y concatenar (+)
En los operadores se aplican jerarquías
"""
nombre = "Alex"
'<'+nombre*5+'>'
3*'do'+'mi'

#Impresion
print("Hola")
print(nombre)
print(nombre + "\n" * 5)
print("Hola", "Como estas")

#Agregar algo al final de una cadena: end=""
print("Hola", "Como estas", end="==")

#Agregar algo entre dos textos: sep=""
print("Hola", "Como estas", sep="---")

#cadenas
cadena = "bienvenido a mi aplicación" 

#Primera letra con mayuscula
print(cadena.capitalize())

#Todas con mayusculas
print(cadena.swapcase())

#Declarando una cadena y haciendo la primer letra mayuscula
cadena = "bienvenido a mi aplicación".capitalize()
#Cadena centrada con signos iguales
print(cadena.center(50, "="))

#count: cuenta las veces que aparece un objeto de una lista o en un elemento
print(cadena.count("a"))
cadena="123"

#isdigit: detecta numeros en una cadena, si hay numeros devuelve 'True', en caso contrario 'False'
print(cadena.isdigit())

#islower: detecta si la cadena esta compuesta de solo letras minuscular, si hay devuelve un 'True', en caso contrario 'False'
print(cadena.islower())
cadena = "pepe grillo"
print(cadena.islower())

#Formatos
cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}" 
print(cadena.format(100, 21, 121))

cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}" 
print(cadena.format(bruto=100, iva=21, neto=121))
print(cadena.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100))

cadena = "--www.eugeniabahit.com---"
print(cadena)
#Devuelve una copia de la cadena con los caracteres iniciales y finales en blanco
cadena.strip()
print(cadena)

#INPUT - Leer de teclado
n = int(input("Ingresa un número: "))
print(n >= 100)

#LISTAS - similares a arreglos, solo un tipo de dato

lista1=["gato","perro","araña"]
lista2=["delfin","ballena","pulpo"]
print(lista1)
print(lista2)

lista1[0]
lista1[0:3]
lista1[-2]

#append agrega una objeto a una lista
lista1.append("tigre")

#remove: quita un objeto de una lista
lista1.remove("gato")

#sort: acomoda los objetos de una lista
lista2.sort()
print(lista2)

#count cuentas las veces que aparece un objeto en una lista
lista1.count("araña")
lista1.count("perro")
lista1.count("delfin")

print(lista1)

'''
reverse es otro método 

Diferencias (analizar)
lista1=lista2
lista2=lista1[:]
'''

#TUPLAS - pueden contener distintos tipos de datos
#Una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo
#range, genera una lista de los numero del primero al ultimo, sin contar el ultimo
tupla = tuple(range(4, 9))
print(tupla)
tup=() #tupla vacia
tup1 = ('hola', 'mundo', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

a = 1,2,5,7,8 #enpaqueta todos los numeros en una tupla
print(a[3]) #puede ser indexada
#a[0] = 3 es inmutable (descomentar esta linea provoca un error)
u,v,w,x,y = a #desempaqueta
#u,v,w = a  #debe coincidir el numero de variables y de elementos en la tupla
            #(descomentar la linea anterior marca error)
print(u,v,w,x,y)
b = (4,) #tupla de un solo elemento
c = (1,3),"Hola" #puede haber tuplas dentro de tuplas
x,y = c 
u,v = x

thistuple = ("apple",)
#type: devuelve el tipo de variable que es
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Constructor
thistuple = tuple(("apple", "banana", "cherry"))

#MÉTODOS Y FUNCIONES
'''
Un MÉTODO es propiedad de los datos para los que trabaja, mientras que una FUNCIÓN
es propiedad de todo el código.

Método: Tipo específico de una función, puede cambiar el estado de una entidad
Función: Generalmente devuelve un resultado
'''