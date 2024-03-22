#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
t = tuple((input().split()))

def arbolTrinario(numero):
    return [numero, [], [], []] # Se define un árbol trinario, considerando  los elementos iguales.

def insertaEnArbolTrinario(arbol, numero): # Función que se carga de insertar el número en el árbol trinario.
    if arbol == []: # Si el árbol está vacío, se agrega la estructura básica de un árbol trinario.
        arbol += arbolTrinario(numero)
    elif numero < arbol[0]: # Si es menor se agrega a la izquierda.
        insertaEnArbolTrinario(arbol[1], numero)
    elif numero == arbol[0]: # Si es igual se agrega al centro.
        insertaEnArbolTrinario(arbol[2], numero)
    else: # Si es mayor, se agrega a la derecha.
        insertaEnArbolTrinario(arbol[3], numero)

arbol_trinario = arbolTrinario(int(t[0]))
for i in t:
  insertaEnArbolTrinario(arbol_trinario, int(i))
print(arbol_trinario)
