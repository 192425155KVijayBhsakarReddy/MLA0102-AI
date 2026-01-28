def alphabeta(depth, node, isMax, values, alpha, beta):
    if depth == 0:
        return values[node]
    if isMax:
        best = -999
        for i in range(2):
            best = max(best, alphabeta(depth-1, node*2+i, False, values, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = 999
        for i in range(2):
            best = min(best, alphabeta(depth-1, node*2+i, True, values, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha: break
        return best

values = [3,5,2,9]
print("Optimal Value =", alphabeta(2, 0, True, values, -999, 999))
