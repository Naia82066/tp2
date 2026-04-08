from expression import Expression
from operations import Addition,Multiplication
from polynome import Polynome
import math

class Sin(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def evaluer(self, x: float) -> float:
        return math.sin(self.expr.evaluer(x))

    def deriver(self):
        from fonctions import Cos
        return Multiplication(Cos(self.expr), self.expr.deriver())

    def __str__(self):
        return f"sin({self.expr})"


class Cos(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def evaluer(self, x: float) -> float:
        return math.cos(self.expr.evaluer(x))

    def deriver(self):
        from fonctions import Sin
        return Multiplication(Multiplication(Polynome([-1]), Sin(self.expr)),self.expr.deriver())

    def __str__(self):
        return f"cos({self.expr})" 
class Exp(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def evaluer(self, x: float) -> float:
        return math.exp(self.expr.evaluer(x))

    def deriver(self):
        return Multiplication(self, self.expr.deriver())

    def __str__(self):
        return f"exp({self.expr})"