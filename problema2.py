#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t = tuple(input().split())
t_reversa = tuple(reversed(t))
output = []
for i in t_reversa:
  try:
    output.append(int(i))
  except ValueError: 
    output.append(i)
    continue
print(tuple(output))
