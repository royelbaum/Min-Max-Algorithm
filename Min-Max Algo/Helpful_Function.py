from objects import *
import random
MAX_DEPTH= 15
DEBAG=False
ADVERSARIAL=1
SEMI_COOPERATIVE=2
FULLY_COOPERATIVE=3
# SEMI_COOPERATIVE2 = 4
CASE=3


def Successor(state, graph):
    if state.player1.wait > 0:
        # when creating new state we create a new level in the search tree and swapping between player1 and player2
        return [
            Multy_P_state(state.player2.copy(), Player(state.player1.node, state.player1.wait - 1, state.player1.score),
                          -1 * state.turn, prev=state)]
    getpeople(state, graph)
    successors = []
    for i in list(graph.adj[state.player1.node]):
        successors.insert(0, Multy_P_state(state.player2.copy(),
                                          Player(i, graph.edges[state.player1.node, i]["weight"] - 1,
                                                 state.player1.score), -1 * state.turn, prev=state))

    return successors


def getpeople(state, graph):
    score = 0
    node = state.player1.node
    if node in state.Nodes_W_P:
        score = graph.nodes[node]["P"]
        state.Nodes_W_P.remove(node)
    state.player1.score += score
    # if  (state.player1.score + state.player2.score > 6):
    #     print("more then 6 p in g scores=", [state.player1.score, state.player2.score])
    if len(state.Nodes_W_P) == 0:
        state.Terminate()

# a function that restore the path and scores along the way fo debag

def restore_path_a1_a2(state, minmax, alpha, beta):
    if state.turn == -1:
        path_a1 = [state.player2.node]
        scors1 = [state.player2.score]
        scors2 = [state.player1.score]
        path_a2 = [state.player1.node]

    else:

        path_a1 = [state.player1.node]
        scors1 = [state.player1.score]
        scors2 = [state.player2.score]
        path_a2 = [state.player2.node]
    tmp = state
    while (tmp.prev != None):
        tmp = tmp.prev
        if tmp.turn == 1:
            if path_a1[0] != tmp.player1.node:
                path_a1.insert(0, tmp.player1.node)
                scors1.insert(0, tmp.player1.score)

            if path_a2[0] != tmp.player2.node:
                path_a2.insert(0, tmp.player2.node)
                scors2.insert(0, tmp.player2.score)
        else:
            if path_a1[0] != tmp.player2.node:
                path_a1.insert(0, tmp.player2.node)
                scors1.insert(0, tmp.player2.score)
            if path_a2[0] != tmp.player1.node:
                path_a2.insert(0, tmp.player1.node)
                scors2.insert(0, tmp.player1.score)
    if path_a1[1] == 2:
        if state.turn == -1:
            v = state.player2.score - state.player1.score
        else:
            v = state.player1.score - state.player2.score
        if minmax == 1:
            print("max_utility")
        else:
            print("min_utility")

        print("path_a1: ", path_a1, "\tpath_a2 : ", path_a2)
        print("a1_score= ", scors1, "\ta_2.score= ", scors2)
        print("score game= ", v)
        print("alpha=", alpha, "\tbeta=", beta)
# if turn==-1 player2= player1 in the initial state

def Adversarial_utility(state):
    if state.turn==-1:
        v= state.player2.score - state.player1.score
    else:
        v=state.player1.score - state.player2.score
    return v

# def Adversarial_utility2(state):
#     if state.turn==-1:
#         v= state.player2.score - state.player1.score -0.05*state.g
#     else:
#         v=state.player1.score - state.player2.score -0.05*state.g
#     return v
#

# if turn==-1 player2= player1 in the initial state
# def Semi_cooperative_utility(state):
#     if state.turn==-1:
#         v= state.player2.score
#     else:
#         v=state.player1.score
#     return v

# def Semi_cooperative_utility2(state):
#     if state.turn==-1:
#         v= 6*(state.player2.score) + state.player1.score -0.05*state.g
#     else:
#         v= 6*(state.player1.score) + state.player2.score -0.05*state.g
#     return v

def Semi_cooperative_utility(state):
    if state.turn==-1:
        v= state.player2.score
        u = state.player1.score
    else:
        v=state.player1.score
        u = state.player2.score
    return v,u

# if turn==-1 player2= player1 in the initial state
def Fooly_cooperative_utility(state):
    v= state.player2.score + state.player1.score
    return v

# def Fooly_cooperative_utility2(state):
#     v= state.player2.score + state.player1.score - 0.05*state.g
#     return v
# in our case eval=utility
def eval(state):
    return utility(state)   #- 0.05*state.g

def Semi_eval(state):
     v, u = utility(state)
     # v=v- 0.05*state.g
     # u=u- 0.05*state.g
     return v, u

# if turn==-1 player2= player1 in the initial state
def utility(state):
        return {
            ADVERSARIAL: lambda :Adversarial_utility(state),
            SEMI_COOPERATIVE: lambda :Semi_cooperative_utility(state),
            # SEMI_COOPERATIVE2: lambda: Semi_cooperative_utility2(state),
            FULLY_COOPERATIVE:lambda :Fooly_cooperative_utility(state)
        }.get(CASE, -1)() # -1 is default if x not found

