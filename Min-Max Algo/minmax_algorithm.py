
from Helpful_Function import *




def Min_Value(state, graph,alpha,beta):
    if state.terminated or len(state.Nodes_W_P) == 0:
        if DEBAG:
            restore_path_a1_a2(state, 0, alpha, beta)
        return utility(state)
    if state.g >= MAX_DEPTH:
        return eval(state)
    v = float('inf')
    successors=Successor(state, graph)
    for s in successors:
        max_val=Max_Value(s, graph,alpha,beta)
        v = min(v, max_val)
        if v<= alpha:
            return v
        beta = min(beta,v)

    return v



def Max_Value(state,graph,alpha,beta):
    if state.terminated or len(state.Nodes_W_P) == 0:
        if DEBAG:
            restore_path_a1_a2(state, 1,alpha,beta)
        return utility(state)

    if state.g >= MAX_DEPTH:
        return eval(state)
    v=float('-inf')
    successors = Successor(state, graph)
    for s in successors:
        min_val=Min_Value(s,graph,alpha,beta)
        v=max(v,min_val)
        if v >= beta:
            return v
        alpha = max(alpha, v)

    return v


def  Minimax_Decision(state,graph):
    results = []
    val_action=float('-inf')
    for s in Successor(state,graph):
        tmpval=Min_Value(s,graph,float('-inf'), float('inf'))
        results.insert(0, (tmpval, s.player2.node))
        if tmpval>val_action:
            val_action=tmpval
    # if DEBAG:
    print("results: ", results)

    filteredresult=list(filter(lambda r: r[0]==val_action ,results))
    print("filtered results: ", filteredresult)
    action=filteredresult[random.randint(0, len(filteredresult)-1)][1]
    return action

