##
#This function should receive two integer (postive or not) number and then white au string of factional reduced expression
##
SignTable = {-1: '-', 1: '+'}
class TypeErrore(Exception): pass
class DivisionBy0(Exception): pass

class fractions:
    def __init__(self,numerator, denominator):
        self.num=numerator
        self.den=denominator
        self.check()
        self.num_red=abs(numerator)
        self.den_red=abs(denominator)
        pro=numerator*denominator
        signvalue=pro/abs(pro)
        self.sign=SignTable[signvalue]
        self.ToFraction()
    
    def ToFraction(self):
        div=self.PGCD(self.num_red,self.den_red)
        while div!=1:
            self.num_red=self.num_red/div
            self.den_red=self.den_red/div
            div=self.PGCD(self.num_red,self.den_red)
        self.Fraction=self.sign+str(int(self.num_red))+"/"+str(int(self.den_red))

    def check(self):
        if type(self.num)!=int or type(self.den)!=int:
            raise TypeErrore
        if self.den==0:
            raise DivisionBy0
        return
        
    def PrimaryNumbers(self, number):
        primaryNumList=[]
        divisor=1
        while divisor<=number:
            quo=number//divisor
            rest=number-quo*divisor
            if rest==0:
                primaryNumList.append(divisor)
                number=quo
            divisor+=1
        return(primaryNumList)
    
    def PGCD(self, a, b):
        primary_a=self.PrimaryNumbers(a)
        primary_b=self.PrimaryNumbers(b)
        for i in range(len(primary_a)-1,0,-1):
            for j in range(len(primary_b)-1,0,-1):
                if primary_a[i]==primary_b[j]:
                    return(primary_a[i])
        return(1)