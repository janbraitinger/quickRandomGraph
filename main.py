from random import randrange

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()

def getRandValue():
    return randrange(0, 2)


def generateMatrix(nodes):
    array = []
    for x in range(nodes):
        row = []
        for y in range(nodes):
            row.append(getRandValue())
        array.append(row)
        #print(row)
    normalizeMatrix(array)
    return array


def normalizeMatrix(matrix):
    print("\n")
    matrix[0][0] = 0
    for i in range(0, len(matrix)):
        for j in range(0, i + 1):
            matrix[i][j] = 0
        print(matrix[i])

    return matrix


def drawNodes(nodes):
    for x in range(1, nodes + 1):
        G.add_node(x)


matrix = generateMatrix(15)
V = len(matrix)


def isEuler(matrix):
    checkList = []
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix[i])):
            count += matrix[i][j]
        if(count%2==0):
            checkList.append("g")
        else:
            checkList.append("n")

    if(checkList.count("n")>2):

        return False

    return True


drawNodes(V)
array = np.array(matrix)
E = np.where(array == 1)
listofIndices = list(zip(E[0], E[1]))

for indice in listofIndices:
    G.add_edge(indice[0]+1,indice[1]+1)


print(isEuler(matrix))


d = dict(G.degree)
pos = nx.spring_layout(G)
colors = [i / len(G.nodes) for i in range(len(G.nodes))]
nx.draw(G, pos, node_color=colors, with_labels=True, nodelist=d.keys(), node_size=[v * 200 for v in d.values()])
nx.draw_networkx_edges(G, pos=pos, alpha=0.5, width=.1)
plt.savefig('123.png')
plt.show()

