# -*- coding: utf-8 -*-


#bisection 
## guess converges on log2N steps 

cube = int(input("Enter cube number for x: "))
epsilon = 0.01 
num_guess = 0 
low = 0 
high = cube 
guess = (low+high)/2
while abs(guess**3 -cube) >= epsilon:
    if guess **3 < cube:
        low = guess 
    else: 
        high = guess 
    guess = (low+high)/2
    num_guess +=1
print ('Number of guess', num_guess)
print (guess , 'is close to the cube root of', cube)

#bisection 
## guess converges on log2N steps 

cube = int(input("Enter cube number for x: "))
epsilon = 0.01 
num_guess = 0 
low = 0 
high = cube 
guess = (low+high)/2
while abs(guess**3 -cube) >= epsilon:
    if guess **3 < cube:
        low = guess 
    else: 
        high = guess 
    guess = (low+high)/2
    num_guess +=1
print ('Number of guess', num_guess)
print (guess , 'is close to the cube root of', cube)

#####################################
#tovers of HANOI
# slove a smaller problem and think of a base case 
#####################################
def printMove (fr,to):
    print ('item move from '+ str(fr) + ' to ' + str(to))
    
def Towers(n,fr,to,spare):
    """
    think of a basic case, for the last step, we move n-1 items to spare tower
    move 1 last item to to tower
    move n-1 items back to the to tower
    """
    if n ==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
              
#####################################
# EXAMPLE:  fibonacci



def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        print(fib(x-1) , fib(x-2))
        return fib(x-1) + fib(x-2)

fib(5)

#keep track of already calculated items 
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}
argToUse = 34
print(fib_efficient(argToUse, d))

#tail recursive , avoid outbount 
def fact(n):
    return fib_tail(n,1)

def fib_tail(num,product):
    if num ==1:
        return product 
    else:
        return fib_tail(num-1,num*product)

#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
##c = Fraction(3.14, 2.7)