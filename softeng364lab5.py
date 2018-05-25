# -*- coding: utf-8 -*-
"""
Created on Mon May 21 22:29:03 2018

@author: William Ning
"""
import json
import os
from pprint import pprint  # "pretty print"
filename = os.path.join('.', 'KuroseRoss5-15.json')  # modify as required
netjson = json.load(open(filename))
pprint(netjson)


import networkx as nx  # saves typing later on
graph = nx.Graph()
graph.add_nodes_from((
    (node['id'], node['properties'])  # node-attributes
        for node in netjson['nodes']))
graph.add_edges_from((
    (link['source'], link['target'], {'cost': link['cost']})  # source-target-attributes
        for link in netjson['links']))


"""
for node, data in graph.nodes(data=True):
    pprint((node, data))

for source, target, data in graph.edges(data=True):
    pprint((source, target, data))  # edges & attributes

for node in graph:
    pprint((node, dict(graph[node])))  # neighbours
    """
    
    
node_positions = nx.get_node_attributes(graph, name='pos')
edge_label_positions = nx.draw_networkx_edge_labels(
        graph,
        pos=node_positions,
        node_labels=nx.get_node_attributes(graph, name='name'),
        edge_labels=nx.get_edge_attributes(graph, name='cost'))
nx.draw_networkx(graph, pos=node_positions)

import routing as ass


path = ass.dijkstra_generalized(graph,"u", plus=True)
pprint(path)




#pprint(ass.forwarding(path[0]))


