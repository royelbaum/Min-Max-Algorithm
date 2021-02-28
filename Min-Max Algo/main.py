
from Graph import *
from Helpful_Function import *
from minmax_algorithm import Minimax_Decision
from maximax_algorithm import Maximax_Decision
from Semi_Cooperative_Maximax import Semi_Maximax_Decision


def getAction(state,graph):
    return {
        ADVERSARIAL: lambda :Minimax_Decision(state, graph),
        SEMI_COOPERATIVE:lambda : Semi_Maximax_Decision(state,graph),
        # SEMI_COOPERATIVE2: lambda: Maximax_Decision(state, graph),
        FULLY_COOPERATIVE: lambda :Maximax_Decision(state,graph)
    }.get(CASE, -1)()  # 9 is default if x not found



def doturn(state,graph,i,j,player1_path,player2_path,scores):
    if state.player1.wait == 0:
        score=graph.nodes[state.player1.node]["P"]
        print("player ", j % 2 + 1)
        if score>0:
            print("collect ",score,"people from node ",state.player1.node)
        graph.nodes[state.player1.node]["P"]=0
        state.update_people(state.player1.node)
        if j % 2 + 1 == 1:
            scores[0] += score
        else:
            scores[1] += score

        if state.isTerminated():
            return state

        action = getAction(state, graph)
        if j % 2 + 1==1:
            player1_path.append(action)
        else:
            player2_path.append(action)
        print ("step ",i,"=",action)
        if DEBAG:
            draw_g(graph)

        player1 = Player(state.player2.node, state.player2.wait, 0)
        player2 = Player(action, graph.edges[state.player1.node, action]["weight"] - 1, 0)
        return Multy_P_state(player1, player2,1, graph=graph)
    player1 = Player(state.player2.node, state.player2.wait, 0)
    player2 = Player(state.player1.node, state.player1.wait-1, 0)
    return Multy_P_state(player1, player2,1, graph=graph)



def simulator(initial_state,graph,max_terms):
    i = 0
    j = 0
    state = initial_state
    player1_path=[initial_state.player1.node]
    player2_path=[initial_state.player2.node]
    player1_score=0
    player2_score=0
    scores=[player1_score,player2_score]

    while len(state.Nodes_W_P) > 0 and max_terms>0:
        if state.player1.wait == 0:
            i += 1
        state = doturn(state, graph, i,j,player1_path,player2_path, scores)
        max_terms -= 1
        j += 1

    print("player1_path= ",player1_path)
    print("player1_score= ", scores[0])

    print("player2_path= ",player2_path)
    print("player2_score= ", scores[1])

    # draw_g(graph)


print({ADVERSARIAL: "ADVERSARIAL",
        SEMI_COOPERATIVE:"SEMI_COOPERATIVE",
        FULLY_COOPERATIVE: "FULLY_COOPERATIVE"}.get(CASE,-1))
g1 = make_graph("input.txt")
g2 = make_graph("input2.txt")
g = g2.copy()
player1 = Player(1, 0, 0)
# player1=Player(2,0,0)
# player2=Player(4,3,0)
player2 = Player(1, 0, 0)
initial_state = Multy_P_state(player1, player2, 1, g2)
# print("Minimax_Decision(initial_state,g)= ",Minimax_Decision(initial_state,g1))
# draw_g(g1)

simulator(initial_state,g2,10)
draw_g(g)
