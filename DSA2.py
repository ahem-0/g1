class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def is_reflexive(self):
        for i in range(self.n):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j]:
                    for k in range(self.n):
                        if self.matrix[j][k] and not self.matrix[i][k]:
                            return False
        return True

    def check_relation_type(self):
        reflexive = self.is_reflexive()
        symmetric = self.is_symmetric()
        antisymmetric = self.is_antisymmetric()
        transitive = self.is_transitive()

        print("Reflexive:", reflexive)
        print("Symmetric:", symmetric)
        print("Anti-symmetric:", antisymmetric)
        print("Transitive:", transitive)

        if reflexive and symmetric and transitive:
            print("=> Equivalence Relation")
        elif reflexive and antisymmetric and transitive:
            print("=> Partial Order Relation")
        else:
            print("=> None of Equivalence or Partial Order")


mat = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
r = RELATION(mat)
r.check_relation_type()
