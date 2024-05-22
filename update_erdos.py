import random as rd

NEW_NODE_RATE = 0.5
P = 0.5

def variable_aleatoire_bernouilli(p):
    tirage  = rd.random()
    if tirage <= p:
        return True
    else :
        return False

def extend_matrice(M, nb_new_nodes, p):
    M.line_count += [0 for _ in range(nb_new_nodes)]
    for i in range(nb_new_nodes):
        for j in range(M.N, M.N + nb_new_nodes):
            if i != j:
                if variable_aleatoire_bernouilli(p):
                    add_arete(M, i+1, j+1)
                    M.line_count[i] += 1
                if variable_aleatoire_bernouilli(p):
                    add_arete(M, j+1, i+1)
                    M.line_count[j] += 1
    M.N += nb_new_nodes
    M.build_f()

def add_arete(M, i, j):
    index_colonne, is_found = find_index(M.P, j)
    if not is_found:
        if M.P[index_colonne][0] > j:
            M.P.insert(index_colonne, (j, [i]))
        else :
            M.P.insert(index_colonne+1, (j, [i]))
    else :
        M.P[index_colonne][1].append(i)

def find_index(P, i):
    a = 0
    b = len(P) - 1
    while a <= b:
        m = (a + b) // 2
        if P[m][0] == i:
            # on a trouvé v
            return m, True
        elif P[m][0] < i:
            a = m + 1
        else:
            b = m - 1
    # on a a > b
    return m, False