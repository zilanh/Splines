

class Polynomial:
    
    def __init__(self, coefficient_list : list):
        self.degree = len(coefficient_list)
        self.coefficient_list = coefficient_list
    
    def primitive(self):
        coefficients = self.coefficient_list
        degree = self.degree
        primitive_coefficients = [coefficient / (degree-i) for i, coefficient in enumerate(coefficients)] + [0]
        self.primitive = Polynomial(primitive_coefficients)

    def calculate(self, x):
        result = 0
        for i, coefficient in enumerate(self.coefficient_list):
            result += coefficient * x**(self.degree-i-1)
        return result
        
    # integrates a polynomial over [a,b]
    def integrate(self, a, b):
        self.primitive()
        return self.primitive.calculate(b) - self.primitive.calculate(a)
    
P = Polynomial([1,2,1])
print(P.integrate(0,3))

