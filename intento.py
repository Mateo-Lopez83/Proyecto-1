import sys
import random

def FloydWarshall(graph, n, index_atom):
    distances = [[float("inf") for _ in range(n)] for _ in range(n)]
    path = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 1
            elif graph[i][j] != float('inf'):
                distances[i][j] = graph[i][j]
                path[i][j] = [index_atom[i], index_atom[j]]
            else:
                path[i][j] = []

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    if path[i][k] and path[k][j]:
                        path[i][j] = path[i][k][:-1] + path[k][j]

    return distances, path

def calcular_LTP(m1, m2, w1, w2):
    if (m1>=0) == (m2>=0):
        dato =  1 + (abs(abs(m1) - abs(m2)) % w1)
        return dato
    else:
        return w2 - (abs(abs(m1) - abs(m2)) % w2)
    
    
def llenar_matriz(matriz, diccionario, w1, w2, n):
    for i in range(n):
        for j in range(n):
            
            m1 = diccionario[i]
            m2 = diccionario[j]
            
            if m1 + m2 == 0:
                matriz[i][j] =float("inf")
            else:
                matriz[i][j] =calcular_LTP(m1, m2, w1, w2) 
    return matriz


def crear_matriz(tamano):
    # Crea una matriz nxn donde n es el tamaño del conjunto
    matriz = []
    for i in range(tamano):
        # Crea una nueva fila
        fila = [0] * tamano
        matriz.append(fila)
    return matriz
'''def crearGrafo(lista, matriz, diccionario):
    grafo = {}

    # Primero, construir el diccionario de grafo con listas vacías para cada elemento fundamental
    for elemento in lista:
        if tuple(elemento) not in grafo:
            grafo[tuple(elemento)] = []

    # Buscar conexiones entre elementos con átomos iguales
    for idx1, elemento1 in enumerate(lista):
        atomo1, atomo2 = elemento1

        # Buscar en otros elementos
        for idx2, elemento2 in enumerate(lista):
            if idx1 != idx2:  # Evitar comparar el elemento con sí mismo
                atomo3, atomo4 = elemento2

                # Comparar cada átomo del primer elemento con cada átomo del segundo elemento
                for a1, a2 in [(atomo1, atomo3), (atomo1, atomo4), (atomo2, atomo3), (atomo2, atomo4)]:
                    if a1 == a2:  # Si hay un átomo igual en ambos elementos
                        # Buscar las posiciones en la matriz a través del diccionario
                        pos1 = diccionario.get(a1)
                        pos2 = diccionario.get(a2)

                        if pos1 and pos2:
                            # Agregar conexión al grafo, donde la llave es la tupla del elemento y el valor es un diccionario
                            conexion = {tuple(elemento2): matriz[pos1][pos2]}
                            grafo[tuple(elemento1)].append(conexion)

    return grafo'''
def crearGrafo(lista, matriz, caminos,indice_a_numero, numero_a_indice):
    vertices = []
    lista_ady = [[]]*(2*len(lista))
    diccionario_caminos = {}
    posicion = 0
    for i in range(len(lista)):
        atom1 = lista[i][0]
        atom2 = lista[i][1]
        vertices.append(atom1)
        vertices.append(atom2)
        i = numero_a_indice[atom1]
        j = numero_a_indice[atom2]
        lista_ady[posicion].append((atom1))
    for num1 in range(len(vertices)-1):
        for num2 in range(num1+1,len(vertices)):
            val1 = vertices[num1]
            val2 = vertices[num2]
            if val1 == val2:
                i = numero_a_indice[val1]
                j = numero_a_indice[val2]
                rand = random.randint(0,2000)
                lista_ady[num1].append((num1,num2,matriz[i][j],))
                
                
            
        
        
                
        
    
def main():
  n, w1, w2 = 3, 100, 200
  lista=[(1, 2),(1, 3),(1, 37),(1, 5),(1, 30),(3, 37),(5,30)]
  diccionario  ={}
  diccionario_inv = {}
  contador = 0
  atomos_libres = set()
  for comp in lista:
    atomos_libres.add(comp[0])
    atomos_libres.add(-comp[0])
    atomos_libres.add(comp[1])
    atomos_libres.add(-comp[1])
    if comp[0] not in diccionario.values():
        diccionario[contador] = comp[0]
        diccionario_inv[comp[0]] = contador
        contador+=1
    if comp[1] not in diccionario.values():
        diccionario[contador] = comp[1]
        diccionario_inv[comp[1]] = contador
        contador+=1
    if -comp[0] not in diccionario.values():
        diccionario[contador] = -comp[0]
        diccionario_inv[-comp[0]] = contador
        contador+=1
    if -comp[1] not in diccionario.values():
        diccionario[contador] = -comp[1]
        diccionario_inv[-comp[1]] = contador
        contador+=1

  matriz = crear_matriz(len(atomos_libres))
  matriz = llenar_matriz(matriz,diccionario, w1,w2,len(atomos_libres))
  #print(matriz)
  '''
  print(matriz[diccionario_inv[1]][diccionario_inv[-1]])
  print(matriz[diccionario_inv[30]][diccionario_inv[-37]])
  print(matriz[diccionario_inv[5]][diccionario_inv[-5]])
  print(matriz[diccionario_inv[-1]][diccionario_inv[-3]])
  print(matriz[diccionario_inv[30]][diccionario_inv[30]])
  print(matriz[diccionario_inv[2]][diccionario_inv[-2]])'''
  distancias, caminos = FloydWarshall(matriz, len(matriz),diccionario)
  '''print(distancias[diccionario_inv[1]][diccionario_inv[-1]])
  print(distancias[diccionario_inv[30]][diccionario_inv[-37]])
  print(distancias[diccionario_inv[5]][diccionario_inv[-2]])
  print(distancias[diccionario_inv[-1]][diccionario_inv[-3]])
  print(distancias[diccionario_inv[30]][diccionario_inv[30]])
  print(distancias[diccionario_inv[2]][diccionario_inv[-2]])'''
  grafo = crearGrafo(lista, matriz, caminos,diccionario, diccionario_inv)
  #print(grafo)
  
      
main()