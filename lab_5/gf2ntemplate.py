# 50.042 FCS Lab 5 Modular Arithmetic
# Year 2024

import copy
class Polynomial2:
    def __init__(self,coeffs):
        self.coeffs = coeffs

    def add(self,p2):
        p1len = len(self.coeffs)
        p2len = len(p2.coeffs)
        
        if p1len > p2len:
            pad = p1len - p2len
            return Polynomial2([a ^ b for a, b in zip(self.coeffs, p2.coeffs + [0] * pad)])
        else:
            pad = p2len - p1len
            return Polynomial2([a ^ b for a, b in zip(self.coeffs + [0] * pad, p2.coeffs)])

    def sub(self,p2):
        return self.add(p2)

    def mul(self,p2,modp=None):
        if modp != None:
            mod = Polynomial2(modp.coeffs.copy())
            x_max = len(mod.coeffs) - 1
            _ = mod.coeffs.pop()
        n = len(self.coeffs)
        result = Polynomial2([0] * n)

        # generating partial results
        for i in range(n):
            if i == 0:
                working = Polynomial2(p2.coeffs)    # initial polynomial
            else:
                working.coeffs.insert(0, 0)
                if modp != None:
                    # handling multiplying out of range (modulus required)
                    if working.coeffs[x_max] == 1:
                        workingPoly = Polynomial2(working.coeffs[0:x_max])
                        working = workingPoly.add(mod)  # subtracting modulus
            
            if self.coeffs[i] == 1:
                result = working.add(result)

        highest = len(result.coeffs) - 1
        while highest:
            if result.coeffs[highest] == 0:
                result.coeffs.pop()
                highest -= 1
            else:
                break

        return result


    def div(self,p2):
        q = Polynomial2([0])
        r = Polynomial2(self.coeffs.copy())
        d = self.deg(p2.coeffs)
        c = p2.coeffs[d]
        while self.deg(r.coeffs) >= d:
            s = int((r.coeffs[self.deg(r.coeffs)] / c))
            s2 = Polynomial2([0] * (self.deg(r.coeffs) - d) + [1])
            q = q.add(s2)
            sb = p2.mul(s2)
            r = r.sub(sb)

        return q, r
    
    def deg(self, r):
        for i in range(len(r) - 1, -1, -1):
            if r[i] != 0:
                return i
        return -1

    def __str__(self):
        poly = ""
        for i in range(len(self.coeffs) - 1, -1, -1):
            if self.coeffs[i] == 1:
                poly += f"x^{i}+"
        if poly == "":
            return "0"
        else:
            return poly[:-1]

    def getInt(p):
        result = 0

        for i in range(len(p)):
            if p[i] == 1:
                result += 2** i

        return result


class GF2N:
    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        self.x = x
        self.n = n
        self.ip = ip
        self.p = self.getPolynomial2()



    def add(self,g2):
        poly2 = self.p.add(g2.getPolynomial2())

        return GF2N(Polynomial2.getInt(poly2.coeffs), self.n, self.ip)
    
    def sub(self,g2):
        return self.add(g2)
    
    def mul(self,g2):
        poly2 = self.p.mul(g2.getPolynomial2(), self.ip)
        return GF2N(Polynomial2.getInt(poly2.coeffs), self.n, self.ip)

    def div(self,g2):
        q, r = self.p.div(g2.getPolynomial2())
        return GF2N(Polynomial2.getInt(q.coeffs), self.n, self.ip), GF2N(Polynomial2.getInt(r.coeffs), self.n, self.ip)

    def getPolynomial2(self):
        poly = [0] * (self.n)
        number = self.x

        for i in range(len(poly) - 1, -1, -1):
            if number//2**i == 1:
                poly[i] = 1
                number -= 2**i
        return Polynomial2(poly)

    def __str__(self):
        return str(self.getInt())

    def getInt(self):
        return self.x

print("\nTest 1")
print("======")
print("p1=x^5+x^2+x")
print("p2=x^3+x^2+1")
p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)
print("p3= p1+p2 = ", p3)

print("\nTest 2")
print("======")
print("p4=x^7+x^4+x^3+x^2+x")
print("modp=x^8+x^7+x^5+x^4+1")
p4=Polynomial2([0,1,1,1,1,0,0,1])
# modp=Polynomial2([1,1,0,1,1,0,0,0,1])
modp=Polynomial2([1,0,0,0,1,1,0,1,1])
p5=p1.mul(p4,modp)
print("p5=p1*p4 mod (modp)=", p5)

print("\nTest 3")
print("======")
print("p6=x^12+x^7+x^2")
print("p7=x^8+x^4+x^3+x+1")
p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])    
p7=Polynomial2([1,1,0,1,1,0,0,0,1])
p8q,p8r=p6.div(p7)
print("q for p6/p7=", p8q)
print("r for p6/p7=", p8r)

####
print("\nTest 4")
print("======")
g1=GF2N(100)
g2=GF2N(5)
print("g1 = ", g1.getPolynomial2())
print("g2 = ", g2.getPolynomial2())
g3=g1.add(g2)
print("g1+g2 = ", g3)

print("\nTest 5")
print("======")
ip=Polynomial2([1,1,0,0,1])
print("irreducible polynomial", ip)
g4=GF2N(0b1101,4,ip)
g5=GF2N(0b110,4,ip)
print("g4 = ", g4.getPolynomial2())
print("g5 = ", g5.getPolynomial2())
g6=g4.mul(g5)
print("g4 x g5 = ", g6.p)

print("\nTest 6")
print("======")
g7=GF2N(0b1000010000100,13,None)
g8=GF2N(0b100011011,13,None)
print("g7 = ",g7.getPolynomial2())
print("g8 = ",g8.getPolynomial2())
q,r=g7.div(g8)
print("g7/g8 =")
print("q = ", q.getPolynomial2())
print("r = ", r.getPolynomial2())