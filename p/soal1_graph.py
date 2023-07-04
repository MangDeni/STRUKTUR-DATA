def semua_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if not node in path:
            newpaths = semua_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
def path_terpendek(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    pendek = None
    for node in graph[start]:
        if node not in path:
            newpath = path_terpendek(graph, node, end, path)
            if newpath:
                if not pendek or len(newpath) < len(pendek):
                    pendek = newpath
    return pendek
def Cari_ListPathTerpendek(Allpaths,ShortestPath):
    List_pendek = [];
    for path in Allpaths:
        if len(path) == len(ShortPath):
            List_pendek.append(path)
    return List_pendek

def displayBlock(Paths):
    for i in range(len(Paths)):
        print('Path',i+1,'=',Paths[i])
        
def Cari_semuaEdge(graphs):
    List_Edge = []
    for keys in graphs.keys():
        if graphs[keys] != []:
            for value in graphs[keys]:
                temp = keys+' => '+value,
                List_Edge.append(temp)
    return List_Edge


gasgraph = {
 'A': ['B','C','D'],
 'B': ['E','C','F'],
 'C': ['F'],
 'D': ['C','T','G'],
 'E': ['T'],
 'F': ['T'],
 'G': ['T'],
 'T': []
 }
SemuaEdge = Cari_semuaEdge(gasgraph)
print('\nBanyaknya Edge : ')
displayBlock(SemuaEdge)
Listsemua_path = semua_path(gasgraph,'A','T')
print('\nBanyaknya Path : ')
displayBlock(Listsemua_path)
ShortPath = path_terpendek(gasgraph,'A','T')
ListPathTerpendek = Cari_ListPathTerpendek(Listsemua_path,ShortPath)
print('\nPath Terpendek : ')
displayBlock(ListPathTerpendek)