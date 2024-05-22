from mtx_management import *

class matrice_creuse_colonne:

    """
    P est une représentation de la matrice creuse M de taille N**2
    P est une liste de tuples
    Soit P[i] un tuple de P : 
    - P[i][0] est l'indice d'une colonne c_i
    - P[i][1] est une liste de tuples, chaque tuple contenant l'indice d'une ligne l_i et la
      valeur non nulle (l_i, c_i) de la  matrice creuse
    -----------------------------------------------------------------------------------------
    line_count est une liste telle que line_count[i-1] est la somme des valeurs de la ligne i de M
    """
    def __init__(self, file) :
        data = read_file(file)
        self.P, self.line_count, self.N = build_matrix(data) 
        self.build_f()

    def build_f(self):
        self.f = [0 for _ in range(self.N)]
        for i, x in enumerate(self.line_count):
            if x == 0 :
                self.f[i] = 1 
    
    def get_val(self, line):
        return 1/self.line_count[line-1]
        
    # Multiplication vec*M
    # vec est un vecteur de la forme 1xN
    # M est une matrice de la forme  NxN
    # -----------------------------------
    # M est stockée en matrice creuse groupée par colonnes
    def multiply_by_vector(vec, M):
        result = [0 for _ in range(M.N)]
        for colonne in M.P:
            for ligne in colonne[1]:
                result[colonne[0]-1] += vec[ligne-1]*M.get_val(ligne)
        return result
    
    def sous_vec_vec(A, B):
        result = []
        for i, a in enumerate(A) :
            result.append(a - B[i])
        return result
    
    def add_vec_vec(A, B):
        for i, a in enumerate(A) :
            A[i] = a + B[i]
        return A
    
    def multiply_vec_vec(A, B, N):
        r = [A[i]*B[i] for i in range(N)]
        return sum(r)
    
"""
M = matrice_creuse_colonne("matrices/wb-cs-stanford.mtx")
x = [1/M.N for x in range(M.N)]

A = [1, 2, 3]
B = [1, 2, 3]

print(M.P[0][1])
print(M.line_count[250])

def main():
    pass

if __name__ == '__main__':
    main()
"""