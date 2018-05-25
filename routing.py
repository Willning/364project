# -*- coding: utf-8 -*-

def dijkstra_predecessor_and_distance(graph, source, weight='cost'):
    """
    Least-cost paths via Dijkstra's algorithm.
    """
    import math
    

    # Definitions consistent with Kurose & Ross
    u = source
    def c(x, y):
        return graph[x][y][weight]
    N = frozenset(graph.nodes())
    NPrime = {u}  # i.e. "set([u])"
    
    D = dict.fromkeys(N, math.inf)
    #Dictionary for all the weights
    
    pred = {source: []} 
    #Dictionary of predecessors

    # Initialization
    for v in N:
        pred[v] = [] #no predecessors at first
        if graph.has_edge(u, v):
            D[v] = c(u, v)
    D[u] = 0  # over-write inf entry for source
    

    # Loop
    while NPrime != N:  #while all nodes not run through
        candidates = {w: D[w] for w in N if w not in NPrime} #for the nodes left
        w, Dw = min(candidates.items(), key=lambda item: item[1])#grab the closest node
        NPrime.add(w) #this node is now used
        for v in graph[w]: 
                       
            if v not in NPrime:
                DvNew = D[w] + c(w, v)                
                               
                if DvNew < D[v]: #if new path is better
                    D[v] = DvNew #update distance                     
                    pred[v].append(w) #add new node that is better
                    
     #Once algorithm is done, we go over those without any predecessors and not
     #the source and just add the source for notation purposes
    for v in graph:        
        if not pred[v] and v!=u:           
            pred[v].append(u)                                                     
                                        
    return (pred, D)


def predecessor_to_forwarding(predecessor, source):
    """ 
    Compute a forwarding table from a predecessor list. 
    """
    pred = predecessor
    #fish out the source
    for key in pred:        
        if not pred[key]:
            source = key
        else:
            notsource = key #dummmy variable so that the table is initialized properly
     
    #using the source to generate a forwarding table dictionary
    table = {notsource:[]}
    
    for key in pred:
        if (pred[key]):            
            table[key] = [source]
            if pred[key]==[source]:                               
                table[key].append(key)
            else:              
                table[key].append(pred[key][-1]) #add the last element on the path, this will be the node just before dest            
    return table
	
	
def dijkstra_generalized(graph, source, weight='cost', 
                         infinity=None, 
                         plus=None,
                         less=None,
                         min=min):    
    """
    Least-cost or widest paths via Dijkstra's algorithm.
    """
    import math    

    # Definitions consistent with Kurose & Ross
    u = source
    def c(x, y):
        return graph[x][y][weight]
    N = frozenset(graph.nodes())
    NPrime = {u}  # i.e. "set([u])"
    
    D = dict.fromkeys(N, math.inf)
    #All bandwidth of zero at start
    
    pred = {source: []} 
    #Dictionary of predecessors

    # Initialization
    for v in N:
        pred[v] = [] #no predecessors at first
        if graph.has_edge(u, v):
            D[v] = c(u, v)
    D[u] = 0  # over-write inf entry for source
    
    if plus == True:
        # Loop
        while NPrime != N:  #while all nodes not run through 
            print(D)            
            candidates = {w: D[w] for w in N if w not in NPrime} #for the nodes left
            w, Dw = min(candidates.items(), key=lambda item: item[1])
            NPrime.add(w) #this node is now used
                    
            
            for v in graph[w]:                        
                if v not in NPrime:                                                       
                    DvNew = max(D[min(D)],  c(w, v))
                    print(w)
                    print(v)
                    print(DvNew)
                                   
                    if DvNew < D[v]: #if new path is better
                        D[v] = DvNew #update distance                     
        return D
    
           # Loop
    while NPrime != N:  #while all nodes not run through
        candidates = {w: D[w] for w in N if w not in NPrime} #for the nodes left
        w, Dw = min(candidates.items(), key=lambda item: item[1])#grab the closest node
        NPrime.add(w) #this node is now used
        for v in graph[w]: 
                       
            if v not in NPrime:
                DvNew = D[w] + c(w, v)                
                               
                if DvNew < D[v]: #if new path is better
                    D[v] = DvNew #update distance                     
                    pred[v].append(w) #add new node that is better             
     #Once algorithm is done, we go over those without any predecessors and not
     #the source and just add the source for notation purposes
    for v in graph:        
        if not pred[v] and v!=u:           
            pred[v].append(u)                                                     
                                        
    return (pred, D)


