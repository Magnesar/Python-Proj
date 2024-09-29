#Dijkstra's algorithm

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}
def shortest_path(graph, start, target =''):
    """unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')"""

    unvisited = list(graph)
    #print(unvisited)
    
    distances = {node: 0 if node == start else float('inf') for node in graph}	#create a dict for distances
    paths = {node: [] for node in graph}	#Make a dict, such that we can save paths 
    paths[start].append(start)			#key start should have start as it's val, since start -> start ends path if target is start
    
    while unvisited:		#while unvisited is not empty
        current = min(unvisited, key=distances.get) #get the node with min distance in distances
        #print(current, distances)     
        for node, distance in graph[current]:		#get distance tuple from the dict for current node
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current] #add the distances for getting to the node from start to current to target/next noe
                
                #Add the node into path if distance is shortest
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]		
                    #print(paths)
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    #print(targets_to_print)
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
    
shortest_path(my_graph, 'D','B')

