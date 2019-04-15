from igraph import *
g=Graph.Read("Finaldata.gml")
d=g.community_infomap()
print("Infomap Clustering Algorithm")
print (d)
