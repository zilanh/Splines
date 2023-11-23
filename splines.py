

class Polynomial:
    
    def __init__(self, coefficient_list : list):
        self.degree = len(coefficient_list)
        self.coefficient_list = coefficient_list
    
    def primitive(self):
        coefficients = self.coefficient_list
        degree = self.degree
        primitive_coefficients = [coefficient / (degree+1-i) for i, coefficient in coefficients]
        self.primitive = Polynomial(primitive_coefficients)

    def calculate(self, x):
        result = 0
        for i, coefficient in enumerate(self.coefficient_list):
            result += coefficient * x**(self.degree-i-1)
        return result
        

    # integrates a polynomial over [a,b]
    def integrate(self, a, b):
        self.primitive(self)
        return self.primitive.calculate(b) - self.primitive.calculate(a)
    
P = Polynomial([1,2,1])
print(P.calculate(-1), P.calculate(3))

