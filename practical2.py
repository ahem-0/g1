class Relation:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
    def is_reflexive(self):
        for i in range(self.size):
            if not self.matrix[i][i]:  # Check diagonal elements
                return False
        return True
    def is_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:  # Symmetry condition
                    return False
        return True
    def is_anti_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != j and self.matrix[i][j] and self.matrix[j][i]:  # Anti-symmetry condition
                    return False
        return True
    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j]:
                    for k in range(self.size):
                        # Transitive condition
                        if self.matrix[j][k] and not self.matrix[i][k]:
                            return False
        return True
    def is_equivalence_relation(self):
        return self.is_reflexive() and self.is_symmetric() and self.is_transitive()
    def is_partial_order(self):
        return self.is_reflexive() and self.is_anti_symmetric() and self.is_transitive()
relation_matrix = [  # Example relation as a 3x3 matrix
    [1, 1, 0],  # A relates to A and B, but not C
    [1, 1, 1],  # B relates to A, B, and C
    [0, 1, 1]   # C relates to B and C, but not A
]
relation = Relation(relation_matrix)
# Create a Relation object
print("Reflexive:", relation.is_reflexive())
# Check properties
print("Symmetric:", relation.is_symmetric())
print("Anti-symmetric:", relation.is_anti_symmetric())
print("Transitive:", relation.is_transitive())
print("Equivalence Relation:", relation.is_equivalence_relation())
# Check if it's an equivalence or partial order relation
print("Partial Order Relation:", relation.is_partial_order())
