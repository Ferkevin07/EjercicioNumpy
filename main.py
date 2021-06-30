#Colocar el num de ejercicio para no repetirse!
#Kevin num ejercicio: 15, 56, 60
#Daniel num ejercicio: 85, 83, 80, 64
#Jeremy num ejercicio:44,78,61,59
#Cindy num ejercicio: 53, 63, 32, 58
import numpy as np
from numpy import random
import random
import time

def menu():
  while True:
    try:
      print("\nMenu de opciones para ejercicios")
      print("1. Ejercicio 15")
      print("2. Ejercicio 32")
      print("3. Ejercicio 44")
      print("4. Ejercicio 53")
      print("5. Ejercicio 56")
      print("6. Ejercicio 58")
      print("7. Ejercicio 59")
      print("8. Ejercicio 60")
      print("9. Ejercicio 61")
      print("10. Ejercicio 63")
      print("11. Ejercicio 64")
      print("12. Ejercicio 78")
      print("13. Ejercicio 80")
      print("14. Ejercicio 83")
      print("15. Ejercicio 85")
      print("Ingrese una opción: ")
      op = input()
      
      return op
    except ValueError:
      print("Ingrese un numero entero!")

def ejercicio64():
  print("Instruccion: Considere un conjunto de 10 tripletes que describen 10 triángulos (con vértices compartidos), encuentre el conjunto de segmentos de línea únicos que componen todos los triángulos")
  faces = np.random.randint(0,100,(10,3))
  F = np.roll(faces.repeat(2,axis=1),-1,axis=1)
  F = F.reshape(len(F)*3,2)
  F = np.sort(F,axis=1)
  G = F.view( dtype=[('p0',F.dtype),('p1',F.dtype)] )
  G = np.unique(G)
  print(G)

def ejercicio80():
  print("Instruccion: Cómo obtener los n valores más grandes de una matriz")
  Z = np.arange(10000)
  np.random.shuffle(Z)
  n = 5
  # Slow
  print (Z[np.argsort(Z)[-n:]])
  # Fast
  print (Z[np.argpartition(-Z,n)[:n]])

def ejercicio83():
  print("Instruccion: Considere un vector grande Z, calcule Z elevado a 3 usando 3 métodos diferentes")
  z = np.random.rand(5e7)
  primerInit = time.time()
  np.power(z,3)
  print(round(time.time()-primerInit,5))
  segundoInit = time.time()
  z*z*z
  print(round(time.time()-segundoInit,5))
  tercerInit = time.time()
  np.einsum('i,i,i->i',z,z,z)
  print(round(time.time()-tercerInit,5))

def ejercicio85():
  print("Instruccion: Considerando una matriz de 10x3, extraiga filas con valores desiguales")
  Z = np.random.randint(0,5,(10,3))
  E = np.logical_and.reduce(Z[:,1:] == Z[:,:-1], axis=1)
  U = Z[~E]
  print(Z)
  print(U)

def ejercicio32():
  print("\nCrear un vector aleatorio de tamaño 10 y ordenarlo")
  Z = np.random.random(10)
  print("Vector sin ordenar: ", Z)
  Z.sort()
  print("Vector ordenado: ", Z)

def ejercicio53():
  print("\nEncontrar el valor más cercano de un valor dado en una matriz")
  Z = np.random.uniform(0,1,10)
  z = 0.5
  m = Z.flat[np.abs(Z-z).argmin()]
  print("Mantriz:", Z)
  print(m)

def ejercicio58():
  print("\nConsidere una matriz de cuatro dimensiones ¿Cómo se puede obtener la suma de los dos últimos ejees de una sola vez?")
  A = np.random.randint(0,10, (3,4,3,4))
  print("Matriz: ", A)
  sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
  print("Resultado: ", sum)

def ejercicio63():
  print("\nIntercamviar dos filas de una matriz")
  A = np.arange(25).reshape(5,5)
  print("Matriz inicial: \n", A)
  A[[0,1]] = A[[1,0]]
  print("Matriz intercambiada las dos primeras filas: \n", A)
def ejercicio44():
  print("Considere un vector aleatorio con forma (100,2) que representa coordenadas, encuentre distancias punto por punto")
  Z=np.random.random((100,2))
  X,Y = np.atleast_2d(Z[:,0]), np.atleast_2d(Z[:,1])
  D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
  print(D)
  print(D.shape)

def ejercicio78():
  print("Considere una matriz de 16x16, ¿cómo obtener la suma de bloques (el tamaño del bloque es 4x4)?")
  Z = np.ones((16,16))
  print("primera matriz")
  print(Z)
  k = 4
  S = np.add.reduceat(np.add.reduceat(Z, np.arange(0,Z.shape[0], k), axis=0),np.arange(0, Z.shape[1], k), axis=1)
  print("resultado")
  print(S)

def ejercicio61():
  print("Considere el vector [1, 2, 3, 4, 5], ¿cómo construir un nuevo vector con 3 ceros consecutivos intercalados entre cada valor?")
  Z = np.array([1,2,3,4,5])
  nz = 3
  Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
  Z0[::nz+1] = Z
  print(Z0)
def ejercicio59():
  print("Considerando un vector D unidimensional, ¿cómo calcular las medias de los subconjuntos de D utilizando un vector S del mismo tamaño que describe índices de subconjuntos?")
  D = np.random.uniform(0,1,100)
  S = np.random.randint(0,10,100)
  D_sums = np.bincount(S, weights=D)
  D_counts = np.bincount(S)
  D_means = D_sums / D_counts
  print(D_means)
def ejercicio56():
  print("¿Cómo acumular elementos de un vector (X) en una matriz (F) basada en una lista de índice?")
  print("(X)= [1,2,3,4,5,6] \n")
  print("(I)= [1,3,9,3,4,1] \n")
  print("(F)=?")
  X = [1,2,3,4,5,6]
  I = [1,3,9,3,4,1]
  F = np.bincount(I,X)
  print(F)
def ejercicio60():
  print("¿Cómo obtener la diagonal de un producto escalar?")
  print("(A)= [1,2,3],[2,5,9] \n")
  print("(B)= [1,3,9],[8,6,9] \n")
  A = [1,2,3,4,5]
  B = [1,2,3,4,5]
  print(np.diag(np.dot(A, B)))

print("***Trabajo grupal***")
opcion = int(menu())
if opcion == 1:
  print(1)
elif opcion == 2:
  ejercicio32()
elif opcion == 3:
  ejercicio44()
elif opcion == 4:
  ejercicio53()
elif opcion == 5:
  ejercicio56()
elif opcion == 6:
  ejercicio58()
elif opcion == 7:
  ejercicio59()
elif opcion == 8:
  ejercicio60()
elif opcion == 9:
  ejercicio61()
elif opcion == 10:
  ejercicio63()
elif opcion == 11:
  ejercicio64()
elif opcion == 12:
  ejercicio78()
elif opcion == 13:
  ejercicio80()
elif opcion == 14:
  ejercicio83()
elif opcion == 15:
  ejercicio85()
else:
  print("Ingrese un valor valido!")

print("\nElaborado por: Benavides Kevin, Guachamin Daniel, Leon Jeremy, Yazán Cindy")