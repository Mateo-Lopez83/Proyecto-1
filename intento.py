from sys import stdin
import time
import queue

def dijkstra(graph, n, diccionario, source,diccionario_inv):
    distances = [float("inf")] * n
    distances[source] = 0
    path = [[] for _ in range(n)]
    visited = [False] * n
    colapq = queue.PriorityQueue()
    colapq.put((0, source))
    while not colapq.empty():
        distancia, nodo = colapq.get()
        if visited[nodo]:
            continue
        visited[nodo] = True
        for vecino, LTP in enumerate(graph[nodo]):
            if not visited[vecino] and LTP != float("inf"):
                distanciaN = distances[nodo] + LTP
                if distanciaN < distances[vecino]:
                    distances[vecino] = distanciaN
                    colapq.put((distanciaN, vecino))
                    path[vecino] = path[nodo] + [diccionario[nodo]]
    opuesto = diccionario_inv[-diccionario[source]]
    camino_opuesto = path[opuesto]+[diccionario[opuesto]]
    costo = distances[opuesto]
    return (camino_opuesto, costo)
            

'''def FloydWarshall(graph, n, index_atom):
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

    return distances, path'''

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

        
def impares(graph):
    impar = None
    a = graph.items()
    for node, neighbors in graph.items():
        if impar is None:
            impar = node
        if len(neighbors) % 2 == 1:
            impar = node
            break
    return impar


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


def fleury(parejas):
    graph = construir(parejas)
    inicial = impares(graph)
    path = []
    for contador in range(len(parejas)):
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
    inicio = time.time() 
    #
    cases = int(stdin.readline().strip())
    
    for _ in range(cases):
        
        free = set()
        lista = []
         
        n, w1, w2 = map(int, stdin.readline().strip().split())
        for _ in range(n):
            a1, a2 = map(int, stdin.readline().strip().split())
            
            free.add(a1)
            free.add(-a1)
            free.add(a2)
            free.add(-a2)
            
            lista.append((a1, a2))
    #n, w1, w2 = 3, 4,5
    #lista=[(1, 2),(1, 3),(1, 37),(1, 5),(1, 30),(3, 37),(5,30)]

        diccionario  ={}
        euler = fleury(lista)
        if euler is not None:
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
            tamano = len(atomos_libres)
            matriz = []
            for i in range(tamano):
                fila = [0] * tamano
                matriz.append(fila)
            matriz = llenar_matriz(matriz,diccionario, w1,w2,tamano) 
            dicc_minimos = {}  
                
            resp = ""
            LTPs = 0
        
            for indice in range(len(euler)):
                pareja = euler[indice]
                conectado = int(pareja[1])
                if conectado not in dicc_minimos.keys():
                    tupla = dijkstra(matriz,len(matriz),diccionario,diccionario_inv[conectado],diccionario_inv) 
                    costo = tupla[1]
                    camino  = tupla[0]
                    dicc_minimos[conectado]= tupla
                else:
                    tupla = dicc_minimos[conectado]
                    costo = dicc_minimos[conectado][1]
                    camino  = dicc_minimos[conectado][0]
                if indice!= len(euler)-1:
                    LTPs += costo
                
                if len(camino)>2:
                    camino.pop(0)
                resp += str(pareja)
                    
                if indice!= len(euler)-1:
                    for n in range(len(camino)):
                        
                        resp+=","+str(camino[n])
                        if n==len(camino)-1:
                            resp+=","
                    
                
            resp+=" "+str(LTPs)
            
        else:
            resp = "NO HAY CAMINO"
        
        print(resp)
    fin = time.time()
    print(fin - inicio)
      
main()


