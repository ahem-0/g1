class SET:
    def __init__(self, elements):
        self.elements = list(set(elements))  # ensure uniqueness

    def is_member(self, x):
        return x in self.elements

    def powerset(self):
        result = [[]]
        for elem in self.elements:
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [elem])
            result.extend(new_subsets)
        return result

    def is_subset(self, other):
        for elem in self.elements:
            if elem not in other.elements:
                return False
        return True

    def union(self, other):
        result = self.elements[:]
        for elem in other.elements:
            if elem not in result:
                result.append(elem)
        return result

    def intersection(self, other):
        return [elem for elem in self.elements if elem in other.elements]

    def complement(self, universal):
        return [elem for elem in universal if elem not in self.elements]

    def difference(self, other):
        return [elem for elem in self.elements if elem not in other.elements]

    def symmetric_difference(self, other):
        return self.difference(other) + other.difference(self)

    def cartesian_product(self, other):
        result = []
        for a in self.elements:
            for b in other.elements:
                result.append((a, b))
        return result


# Example usage
if __name__ == "__main__":
    A = SET([1, 2, 3])
    B = SET([3, 4, 5])
    U = [1, 2, 3, 4, 5]

    print("Is 2 a member of A?", A.is_member(2))
    print("Powerset of A:", A.powerset())
    print("A is subset of B?", A.is_subset(B))
    print("Union:", A.union(B))
    print("Intersection:", A.intersection(B))
    print("Complement of A:", A.complement(U))
    print("A - B:", A.difference(B))
    print("Symmetric Difference:", A.symmetric_difference(B))
    print("Cartesian Product:", A.cartesian_product(B))
