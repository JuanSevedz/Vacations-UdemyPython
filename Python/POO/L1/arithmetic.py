class Arithmetic:
    """
    This is a class to definy an arithmetic operation
    """
    def __init__(self, OperA, OperB):
        self.OperA = OperA
        self.OperB = OperB

    def sum(self):
        return self.OperA + self.OperB

    def mult(self):
        return self.OperA * self.OperB

    def res(self):
        return self.OperA - self.OperB

    def div(self):
        return self.OperA / self.OperB
arithmetic1 = Arithmetic(5,3)
print(f'La suma es: {arithmetic1.sum()}')
print(f'La resta es: {arithmetic1.res()}')
print(f'La multiplicacion es: {arithmetic1.mult()}')
print(f'La división es: {arithmetic1.div(): .2f}')