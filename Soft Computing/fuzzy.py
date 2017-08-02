class FuzzyException(RuntimeError):
    
    def __init__(self, args):
        self.args = args


class FuzzySet(object):

    def __init__(self, elements, membership):
        self.elements = elements
        self.membership = membership

    def __repr__(self):
        reprtn = '[ '
        for element, value in zip(self.elements, self.membership):
            reprtn += '('+str(element)+', '+str(value)+') '
        reprtn += ']'
        return reprtn

    def complement(self):
        for i in range(len(self.elements)):
            self.membership[i] = round(1 - self.membership[i], 2)

    def is_subset(self, set_b):
        if len(self.elements) != len(set_b.elements):
            raise FuzzyException("Unequal Sets")

        for value_a, value_b in zip(self.membership, set_b.membership):
            if not value_b < value_a:
                return False
        return True

    def union(self, set_b):
        res = []

        for value_a, value_b in zip(self.membership, set_b.membership):
            res.append(max(value_a, value_b))

        return FuzzySet(self.elements, res)

    def intersection(self, set_b):
        res = []

        for value_a, value_b in zip(self.membership, set_b.membership):
            res.append(min(value_a, value_b))

        return FuzzySet(self.elements, res)

    def alg_sum(self, set_b):
        res = []

        for value_a, value_b in zip(self.membership, set_b.membership):
            res.append(value_a + value_b - value_a*value_b)

        return FuzzySet(self.elements, res)

    def alg_product(self, set_b):
        res = []

        for value_a, value_b in zip(self.membership, set_b.membership):
            res.append(value_a * value_b)

        return FuzzySet(self.elements, res)

    def bound_sum(self, set_b):
        res = []

        for value_a, value_b in zip(self.membership, set_b.membership):
            res.append(min(1, value_a+value_b))

        return FuzzySet(self.elements, res)

    def bound_diff(self, set_b):
        res = []

        for value_a, value_b in zip(self.membership, set_b.membership):
            res.append(max(0, value_a-value_b))

        return FuzzySet(self.elements, res)
