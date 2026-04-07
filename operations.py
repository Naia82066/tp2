from expression import Expression

class Addition(Expression):
    def __init__(self,droite:Expression,gauche:Expression):
        self.droite=droite
        self.gauche=gauche

class Multiplication(Expression):
    def __init__(self,droite:Expression,gauche:Expression):
        self.droite=droite
        self.gauche=gauche