
import random
class numOrdenar:
  def listaAleatorios(self):
    print("Ingrese cuantos numeros aleatorios desea obtener")
    n=int(input())
    n= int(n)
    lista = [0]  * n
    for i in range(n):
      lista[i] = random.randint(0, 100)
    lista.sort()
    print (lista)

aleatorios=numOrdenar()
aleatorios.listaAleatorios()
