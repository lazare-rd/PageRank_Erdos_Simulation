from matrice_creuse_colonne import *

ALPHA = 0.85
ETA = 10**-8
FILE = "matrices/matrice_TD3.mtx"

def norme_1(A):
    result = 0
    for a in A:
        result+=abs(a)
    return result

def iter(M, ALPHA, eta, x):
    i = 0
    result = []
    while True:
        i+=1
        rs = ((1-ALPHA)*(1/M.N)) + (ALPHA*(1/M.N)*matrice_creuse_colonne.multiply_vec_vec(x, M.f, M.N))
        terme_droit = [rs for _ in range(M.N)]
        x_by_P = matrice_creuse_colonne.multiply_by_vector(x, M)
        terme_gauche = [ALPHA*_x for _x in x_by_P]
        x_prime = matrice_creuse_colonne.add_vec_vec(terme_gauche, terme_droit)
        if norme_1(matrice_creuse_colonne.sous_vec_vec(x_prime, x))<=eta:
            result.append((eta, i, x_prime))
            return result
        x = x_prime

def main():
    M = matrice_creuse_colonne(FILE)
    x = [1/M.N for _ in range(M.N)]
    distrib_stat = iter(M, ALPHA, ETA, x)
    for i in distrib_stat:
        print(f"Précision : {i[0]}")
        print(f"nb_iter : {i[1]}")
        print(f"distribution stationnaire : {i[2][:7]} ...")
        print(f"Somme des membres de la proba stat : {sum(i[2])}")

if __name__ == '__main__':
    main()
    