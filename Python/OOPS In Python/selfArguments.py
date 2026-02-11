class ChaiCup :
    size = 100
    
    def makechai (self) :
        return f"A {self.size} ml Chai Cup"
    
    
cup = ChaiCup()
print(cup.makechai())
# @ If I call Direcly With Classs - > TypeError: ChaiCup.makechai() missing 1 required positional argument: 'self'
print(ChaiCup.makechai(cup))