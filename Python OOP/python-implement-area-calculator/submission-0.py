import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width = None):
        if width is None:
            area = math.pi * (length ** 2)
            return round(area, 2)
        else:
            area = length * width
            return area
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
