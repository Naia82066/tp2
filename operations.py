from expression import Expression

class Addition(Expression):
    def __init__(self,droite:Expression,gauche:Expression):
        self.droite=droite
        self.gauche=gauche
    def evaluer(self,x:float)->float:
        return self.droite.evaluer(x)+self.gauche.evaluer(x)
    def deriver(self):
        return Addition(self.droite.deriver(),self.gauche.deriver())
    def __str__(self):
        return f"({self.droite} + {self.gauche})"

class Multiplication(Expression):
    
    def __init__(self,droite:Expression,gauche:Expression):
        self.droite=droite
        self.gauche=gauche
    def evaluer(self, x: float) -> float:
        return self.gauche.evaluer(x) * self.droite.evaluer(x)
    def deriver(self):
        return Addition(Multiplication(self.gauche.deriver(), self.droite),Multiplication(self.gauche, self.droite.deriver()))
    def __str__(self):
        return f"({self.gauche} * {self.droite})"