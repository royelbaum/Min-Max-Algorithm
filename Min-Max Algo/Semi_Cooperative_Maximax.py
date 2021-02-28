from Helpful_Function import *

def Semi_Max_Value(state, graph):
    if state.terminated or len(state.Nodes_W_P) == 0:
        if DEBAG:
            restore_path_a1_a2(state, 1)
        return utility(state)
    if state.g >= MAX_DEPTH:
        return Semi_eval(state)
    v = float('-inf')
    u = float('-inf')
    successors = Successor(state, graph)
    for s in successors:
        my_val, oppenent_val = Semi_Max_Value(s, graph)
        if v == my_val:
            if(oppenent_val > u):
                u = oppenent_val
        elif v < my_val:
            v = my_val
            u = oppenent_val
    return v , u


def  Semi_Maximax_Decision(state,graph):
    results = []
    val_action = float('-inf')
    oppenet_val_score = float('-inf')
    for s in Successor(state, graph):
        myval , oppenentval  = Semi_Max_Value(s, graph)
        results.insert(0, (myval,oppenentval, s.player2.node))
        if myval > val_action:
            val_action = myval
            oppenet_val_score = oppenentval
        elif myval==val_action:
            if oppenentval > oppenet_val_score:
                oppenet_val_score = oppenentval
                action = s.player2.node
    # if DEBAG:
    print("results: ", results)
    filteredresult=list(filter(lambda r: r[0]==val_action and r[1]==oppenet_val_score ,results))
    print("filtered results: ", filteredresult)
    action=filteredresult[random.randint(0, len(filteredresult)-1)][2]
    return action

