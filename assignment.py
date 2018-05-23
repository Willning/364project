def dijkstra_5_14(graph, source, weight='cost'):
    """
    Shortest paths via Dijkstra's algorithm,
    consistent with pseudocode on Slide 5-14.
    """
    import math
    #TODO make predecessors work properly

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



def forwarding(pred):
    """
    This function will provide a forwarding table from a predecessor map.
    Output will be a dictionary of lists
    Give the first jump form the source to the destination
    """  
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


def hextet_complement(x):   
    mask = 0xffff #8 bitmask        
    out = bin(~x&mask)
    return out

    


      
                            