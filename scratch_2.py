import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community
with open(r'nodes.csv', 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader][1:]

node_names = []
for n in nodes:
    node_names.append(n[0])

with open('edges.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader][1:]

G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)
print(nx.info(G))

degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')
print(G.nodes['Thomas Bruce, 7th Earl of Elgin'])

nx.write_gexf(G, 'art_dealers.gexf')