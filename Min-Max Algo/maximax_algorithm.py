from Helpful_Function import *

def Max_Value(state, graph):
    if state.terminated or len(state.Nodes_W_P) == 0:
        if DEBAG:
            restore_path_a1_a2(state, 1)
        return utility(state)
    if state.g >= MAX_DEPTH:
        return eval(state)
    v = float('-inf')
    successors = Successor(state, graph)
    for s in successors:
        min_val = Max_Value(s, graph)
        v = max(v, min_val)
    return v


def  Maximax_Decision(state,graph):
    results = []
    val_action = float('-inf')
    for s in Successor(state, graph):
        tmpval = Max_Value(s, graph)
        results.insert(0, (tmpval, s.player2.node))
        if tmpval > val_action:
            val_action = tmpval
    # if DEBAG:
    print("results: ", results)
    filteredresult=list(filter(lambda r: r[0]==val_action ,results))
    print("filtered results: ", filteredresult)
    action=filteredresult[random.randint(0, len(filteredresult)-1)][1]  # choose an action with max value randomly
    return action


