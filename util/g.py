class Computation():
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            return self.value + other

        def __sub__(self, other):
            return self.value - other


c = Computation(5)
c + 5

c - 3
