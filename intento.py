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
    # Matriz tiene que ser nxn y simetrica
    matriz = []
    for i in range(tamano):
        # Crea una nueva fila
        fila = [0] * tamano
        matriz.append(fila)
    return matriz

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
                
                
            
        
def impares(graph):
    odd_vertex = None
    for node, neighbors in graph.items():
        if odd_vertex is None:
            odd_vertex = node
        if len(neighbors) % 2 == 1:
            odd_vertex = node
            break
    return odd_vertex


def hay_dfs(v, u, graph):
    if len(graph[v]) > 0:
        visited = set()
        cola = []
        cola.append(v)
        visited.add(v)
        while len(cola)>0:
            current_node = cola.pop(0)
            for next_node in graph[current_node]:
                if next_node == u:
                    return True
                if next_node not in visited:
                    cola.append(next_node)
                    visited.add(next_node)
        return False
    else:
        return True


def construir(parejas):
    graph = {}
    for elemento in parejas:
        a = elemento[0]
        b = elemento[1]
        if a not in graph.keys():
            graph[a] = []
        graph[a].append(b)
        if b not in graph.keys():
            graph[b] = []
        graph[b].append(a)
    return graph


def solve(parejas):
    graph = construir(parejas)
    num = len(parejas)
    inicial = impares(graph)
    path = []
    for contador in range(num):
        neighbors = graph[inicial]
        for u in neighbors:
            graph[inicial].remove(u)
            graph[u].remove(inicial)
            if hay_dfs(inicial, u, graph):
                path.append((inicial, u))
                inicial = u
                break
            else:
                graph[inicial].append(u)
                graph[u].append(inicial)
    if len(path)!= len(parejas):
        return None
    return path
                
        
    
def main():
    n, w1, w2 = 3, 4,5
    lista=[(1, 2),(1, 3),(1, 37),(1, 5),(1, 30),(3, 37),(5,30),(15,7)]
    euler = solve(lista)
    if euler is not None:
    #lista = [(1,3),(-6,3),(1,7)]
    #lista = [(1,2),(2,3),(4,4)]
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

        distancias, caminos = FloydWarshall(matriz, len(matriz),diccionario)
        resp = ""
        LTPs = 0
    
        for indice in range(len(euler)):
            pareja = euler[indice]
            conectado = int(pareja[1])
            
            costo = distancias[diccionario_inv[conectado]][diccionario_inv[-conectado]]
            if indice!= len(euler)-1:
                LTPs += costo
            camino  = caminos[diccionario_inv[conectado]][diccionario_inv[-conectado]]
            if len(camino)>2:
                camino.pop(0)
            resp += str(pareja)
                
            if indice!= len(euler)-1:
                for numero in camino:
                    
                    resp+=","+str(numero)
                
            
        resp+=" "+str(LTPs)
        
    else:
        resp = "NO HAY CAMINO"
    
    print(resp)
      
main()


