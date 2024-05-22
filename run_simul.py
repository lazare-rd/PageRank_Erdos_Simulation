from implementation_PageRank import *
from update_erdos import *
from matrice_creuse_colonne import *
import json
from tqdm import tqdm

ETA = 10**-8
FILE = "matrices.nosync/soc-Slashdot0902.mtx"
NEW_NODE_RATE = [0.01, 0.005, 0.0005]
PROBA_BERNOUILLI = [0.1, 0.3, 0.5, 0.8]
ALPHA = [0.85, 0.7, 0.6, 0.5]
NEW_NODE_RATE_FIXE = 0.005
PROBA_BERNOUILLI_FIXE = 0.5
ALPHA_FIXE = 0.85
NB_EXTEND = 5

def run_simul(alpha, p, new_node_rate, nb_extend):
    M = matrice_creuse_colonne(FILE)
    x = [1/M.N for _ in range(M.N)]
    x_bis = iter(M, alpha, ETA, x)[0][2]
    result = [[], []]
    for _ in tqdm(range(nb_extend)):
        nb_new_nodes = int(M.N*new_node_rate)
        extend_matrice(M, nb_new_nodes, p)
        x = [1/M.N for _ in range(M.N)]
        x_bis += [0 for _ in range(nb_new_nodes)]
        distrib_stat = iter(M, alpha, ETA, x)
        distrib_stat_bis = iter(M, alpha, ETA, x_bis)
        x_bis = distrib_stat_bis[0][2]
        result[0].append(distrib_stat[0][1])
        result[1].append(distrib_stat_bis[0][1])
    return result

def exe():
    result_dico = {
                    "new_node_rate" : ({}, (PROBA_BERNOUILLI_FIXE, ALPHA_FIXE)),
                    "proba_ber" : ({}, (NEW_NODE_RATE_FIXE, ALPHA_FIXE)),
                    "alpha" : ({}, (NEW_NODE_RATE_FIXE, PROBA_BERNOUILLI_FIXE))
                   }
    for rate in tqdm(NEW_NODE_RATE):
        result = run_simul(ALPHA_FIXE, PROBA_BERNOUILLI_FIXE, rate, NB_EXTEND)
        result_dico["new_node_rate"][0][rate] = result
    for proba in tqdm(PROBA_BERNOUILLI):
        result = run_simul(ALPHA_FIXE, proba, NEW_NODE_RATE_FIXE, NB_EXTEND)
        result_dico["proba_ber"][0][proba] = result
    for alpha in tqdm(ALPHA):
        result = run_simul(alpha, PROBA_BERNOUILLI_FIXE, NEW_NODE_RATE_FIXE, NB_EXTEND)
        result_dico["alpha"][0][alpha] = result
    return result_dico

def main():
    data_dico = exe()
    file = open("data.json", "w")
    data_json = json.dumps(data_dico, indent=2)
    file.write(data_json)
    file.close()

if __name__ == '__main__':
    main()
    