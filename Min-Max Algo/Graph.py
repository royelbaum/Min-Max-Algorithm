import networkx as nx
import matplotlib.pyplot as plt 

class Agents_Graph(object):

    def __init__(self, filename):
        self.Number_Of_People_In_Graph = 0
        self.Graph = self.Make_Graph(filename)
    
    def Make_Graph(self,filename):
        Graph = nx.Graph()
        graphfile = open(filename, "r")
        number_of_vertex = 0 
        time = 0
        for line in graphfile.readlines():
            if len(line) > 0 and line[0]=="#":
            #  print(line)
                newline = line.split()
                if line[1] == "N":
                    number_of_vertex = int(newline[1])
                elif line[1] == "D":
                    time = float(newline[1])
                elif line[1] == "V":
                    line = line.split(";")[0]
                    index_of_P = line.find("P")
                    if(index_of_P > 0):
                        Graph.add_node(int(line[2]), P=int(line[index_of_P+1]))
                        self.Number_Of_People_In_Graph += int(line[index_of_P+1])
                    else:
                        Graph.add_node(int(line[2]), P=0)
                elif line[1] == "E":
                    newline[3]= newline[3].replace("W","")
                    Graph.add_edge(int(line[4]), int(line[6]), weight = float(newline[3]), name=line[2], block="false")
        return Graph

    def print_graph(self):
        for i in self.Graph.nodes:
            print("vertex number:" , i , self.Graph.nodes[i],self.Graph.adj[i])




        
    def Get_Vertex(self,index):
        return self.Graph.nodes[index]
    




#------- end class  --------

def make_graph(filename):
    Graph = nx.Graph()
    graphfile = open(filename, "r")
    number_of_vertex = 0
    time = 0
    for line in graphfile.readlines():
          if len(line) > 0 and line[0]=="#":
          #  print(line)
            newline = line.split()
            if line[1] == "N":
                number_of_vertex = int(newline[1])
            elif line[1] == "D":
                time = float(newline[1])
            elif line[1] == "V":
                newline[0]=  newline[0].replace("#V", "")
                line = line.split(";")[0]
                index_of_P = line.find("P")
                if(index_of_P > 0):
                    Graph.add_node(int(newline[0]), P=int(line[index_of_P+1]))
                else:
                    Graph.add_node(int(newline[0]), P=0)
            elif line[1] == "E":
                 newline[3]= newline[3].replace("W","")
                 newline[0] = newline[0].replace("#E", "")
                 Graph.add_edge(int(newline[1]), int(newline[2]), weight = float(newline[3]), name=newline[0], block="false")
    return Graph

def print_graph(graph):
    for i in graph.nodes:
        print("vertex number:" , i , graph.nodes[i],graph.adj[i])


# def drawing_graph(graph):
#     pos = {1: (0, 0), 2: (-1, 0.3), 3: (2, 0.17), 4: (4, 0.255), 5: (5, 0.03),6 :(7,0.35)}
#     pos2 = {1: (-1, 0), 2: (-2, 0.3), 3: (2.5, 0.17), 4: (4.5, 0.255), 5: (5.5, 0.03),6 :(7.5,0.35)}
#     nx.draw_networkx(graph,pos)
#     nods_labels=nx.get_node_attributes(graph,"P")
#     edges_labels = nx.get_edge_attributes(graph,"weight")
#     nx.draw_networkx_labels(graph,pos2 , nods_labels, font_size=12)
#     nx.draw_networkx_edge_labels(graph,pos,edges_labels)
#     # Set margins for the axes so that nodes aren't clipped
#     ax = plt.gca()
#     ax.margins(0.20)
#     plt.axis("off")
#     plt.show()

def draw_g(G):
    plt.subplot(121)
    pos1=nx.shell_layout(G)
    # pos1 = {n: (0, i) for i, n in enumerate(G.nodes[0:len(G.nodes)/3])}
    # pos1.update( {n: (1, i + 0.5) for i, n in enumerate(G.nodes[len(G.nodes)/3 : 2*len(G.nodes)/3]})
    # pos1.update({n: (2, i + 0.5) for i, n in enumerate(G.nodes[2*len(G.nodes)/3 : len(G.nodes)])})

    pos2=pos1.copy()
    for i in pos2:
        pos2[i]=pos2[i]-[-0.1, 0.1]

    nodes_labels=nx.get_node_attributes(G,"P")
    nx.draw_networkx_labels(G,pos2 , nodes_labels, font_size=8,font_color='green')

    edges_labels = nx.get_edge_attributes(G,"weight")
    # pos = nx.spring_layout(G)
    # pos=nx.random_layout(G[, center, dim, seed])
    nx.draw_networkx_edge_labels(G,pos1,edges_labels,font_color='blue',font_size=5)
    # when drawing to an interactive display.  Note that you may need to issue a
    # Matplotlib
    nx.draw(G,pos1, with_labels=True, font_weight='bold',font_size=13)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
    
def Get_Vertex(index, graph):
    return graph.nodes[index]