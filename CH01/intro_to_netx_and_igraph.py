""" 
Name:       intro_to_netx_and_igraph.py
Author(s):  Gary Hutson & Matt Jackson on behalf of Packt publishing
Date:       09/12/2022
Usage:      python intro_to_netx_and_igraph.py
"""
# NetworkX basics
import networkx as nx
import igraph
import matplotlib.pyplot as plt

print(f'Current version of NetworkX imported is {nx.__version__}')

# Create NetworkX empty graph object
g = nx.Graph()

# Add node of Jeremy to NetworkX graph
g.add_node("Jeremy")
print(g.nodes)
print(g)

g.add_nodes_from(["Mark", "Jeremy"])
print(f'{g}. Current nodes in network: {g.nodes}')

g.add_nodes_from([(
    "Mark", {"followers": 2100}), 
    ("Jeremy", {"followers": 130}
    )])
    
print(g)

g.add_edge("Jeremy", "Mark")
print(g)
print(g.edges)

# Plot the edges and node connections
nx.draw(g, with_labels=True)
plt.show()

# Igraph basics
import igraph as ig
print(f'Current version of igraph imported is: {ig.__version__}')

g = ig.Graph()
g.add_vertices(2)

# Add attributes
g.vs[0]["name"] = "Jeremy"
g.vs[1]["name"] = "Mark"
g.vs[0]["followers"] = 130
g.vs[1]["followers"] = 2100

# Add followers to Mark and Jeremy in another way 
g.vs["name"] = ["Jeremy", "Mark"]
g.vs["followers"] = [130, 2100]

g.add_edges([(0, 1)])
print(g)
