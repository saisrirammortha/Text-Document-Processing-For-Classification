
def dist(a,b):
  import math
  n=len(a)
  k=0
  for i in range(0,n):
    k=k+((a[i]-b[i])**2)
  return math.sqrt(k)
def db(X,clusters):
  n=len(X)
  cno=0
  temp=[]
  for i in clusters:
    if i not in temp:
      cno=cno+1
      temp.append(i)
  index=0
  centroid=[]
  for i in range(0,cno):
    cc=[]
    count=0
    k=0
    for j in range(0,n):
      if (clusters[j]==i):
        cc=X[j]
        k=j
        count=count+1
        break
    for j in range(0,n):
      if (clusters[j]==i) and (k!=j):
        cc=cc+X[j]
        count=count+1
    cc=cc/count
    centroid.append(cc)
  cluster=[]
  for i in range(0,cno):
    cluster.append([])
  for i in range(0,cno):
    for j in range(0,n):
      if (clusters[j]==i):
        cluster[i].append(j)
  selfcluster=[]
  for i in range(0,cno):
    k=0
    for j in cluster[i]:
      k=k+dist(X[j],centroid[i])
    k=k/len(cluster[i])
    selfcluster.append(k)
  diff=[]
  for i in range(0,cno):
    a=[]
    for j in range(0,cno):
      a.append(dist(centroid[i],centroid[j]))
    diff.append(a)
  index=[]
  for i in range(0,cno):
    a=[]
    for j in range(0,cno):
      if (i==j):
        a.append(0)
      else:
        k=(selfcluster[i]+selfcluster[j])/diff[i][j]
        a.append(k)
    index.append(a)
  value=[0,0]
  for i in range(0,cno):
    value[0]=value[0]+max(index[i])
  value[0]=value[0]/cno
  den=max(selfcluster)
  new=[]
  for i in range(0,cno):
    for j in diff[i]:
      if (j!=0):
        new.append(j)
  num=min(new)
  value[1]=num/den
  print(value)  
  return value

from igraph import *
g=Graph.Read_GML("Finaldata.gml")
p=g.community_multilevel()
q=g.modularity(p)
print("Louvain Clustering Algorithm")

print(p)
f=open("finalvectors.txt","r")
a=[]
a=[[float(num) for num in line.split(",")] for line in f]
assigned=[]
for i in range(0,100):
  for j in range(0,3):
    if i in p[j]:
      assigned.append(j)
      break
print(assigned)
import numpy as np
myarray = np.asarray(a)
value=db(myarray,assigned)
