from matrice_creuse_colonne import *


def iter(file, nb_iter, pi_0):
    M = matrice_creuse_colonne(file)
    for _ in range(nb_iter):
        pi_0 = matrice_creuse_colonne.multiply_by_vector(pi_0, M)
    return pi_0

print(iter("matrices/matrice_test.mtx", 10, [0.8, 0.2]))