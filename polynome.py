from expression import Expression

class  Polynome(Expression):
    def __init__(self,coeffs):
        self.coeffs = coeffs

    def evaluer(self, x:float)->float:
        valeur=0
        for puissance, coeff in enumerate(self.coeffs):
            valeur += coeff*(x**puissance)
        return valeur
    def deriver(self):
        if len(self.coeffs)<=1:
            return Polynome([0])
        
        liste=[]
        for i in range(1,len(self.coeffs)):
            liste.appepend(i*self.coeffs[i])
        return Polynome(liste)
    def __str__(self):
        termes=[]
        for i, coef in enumerate(self.coeffs):
            if coef==0:
                continue
            if i==0:
                termes.append(str(coef))
            elif i==1:
                if coef==1:
                    termes.append("x")
                else:
                    termes.append(f"{coef}x")
            else:
                if coef==1:
                    termes.append(f"x^{i}")
                else:
                    termes.append(f"{coef}x^{i}")
        return " + ".join(reversed(termes)) if termes else "0"
    
