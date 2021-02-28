
class Multy_P_state(object):
    def __init__(self, player1, player2, turn, graph=None, prev=None):
        self.Nodes_W_P = []
        if prev != None:
            self.Nodes_W_P = prev.Nodes_W_P.copy()
            self.g = prev.g + 1
        else:
            self.g = 0
            for i in graph.nodes:
                if graph.nodes[i]["P"] > 0:
                    self.Nodes_W_P.insert(0, i)
        self.player1 = player1
        self.player2 = player2
        self.prev = prev
        self.turn = turn
        self.terminated = False

    def Terminate(self):
        self.terminated = True

    def isTerminated(self):
        return self.terminated or len(self.Nodes_W_P)==0

    def update_people(self,node):
        if node in self.Nodes_W_P:
            self.Nodes_W_P.remove(node)

class Player(object):
    def __init__(self, node, wait, score):
        self.node = node
        self.wait = wait
        self.score = score

    def copy(self):
        return Player(self.node, self.wait, self.score)

