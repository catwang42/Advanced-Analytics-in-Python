# -*- coding: utf-8 -*-


## test 
list1 = ['physics','chemisty',1997,1982]
list2 = ['physics','chemisty','ss','dsf']

i = 0 
while i < len(list1):
    print(list1[i])
    i+=1 

for i in range(len(list1)):
    print(list1[i])


for i in range(1,len(list1)):
    print(list1[i])    
    
for c in list1: 
    print(c)    
    
for i, v in enumerate(list1, start =1):
    print("index {}, value {}".format(i,v))
 

for i,v in enumerate(list1):
    list22 = list2[i]
    print("list1 {}, list2 {}".format(v,list22))
    
for i,v in zip(list1,list2):
     print("list1 {}, list2 {}".format(i,v))

#split based on condition 
list_split1 = [i for i in list1 if type(i)!=str]
list_split2 = [i for i in list1 if type(i)!=int]


list_split_len1, list_split_len2 = [],[]
for i in list2:
    if len(i)>5:
        list_split_len1.append(i)
    else:
        list_split_len2.append(i)

list_split1 = list1.apply(lambda x: isinstance(x, int))

#geenrate list
[x**2 for x in range(1,11) if x%2 ==0] 
[m+n for m in 'ABC' for n in 'abc']

d = {'x':'A','y':'B','z': 'C'}
[k+'-'+v for k,v in d.items()]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#generator 


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
# Different parameter 
#默认参数一定要用不可变对象
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict
#####################################
#take list/tupe as parameters 
def cal(*number):
    sum = 0 
    for n in number:
        sum = n**2+sum
    return sum 

cal(1,2,3,4)
num =[1,2,3,4]
nums = (1,2,3,4) 
cal(*num)
cal(*nums)

#take dict
def person(name,age,**kw):
    print('name', name, 'Age', age, 'other:', kw)

person('Catherine', 29)
person('Catherine', 29, city='Melbourne')
person('Catheirne',29,city='Melbourne',job='Data Scientist') 
extra= {'city':'Melbrouen','job':'Data Scientist'}

#only take variable with city and job 
def persons(name,age,*,city,job):
    print(name,age,city,job)
persons('Catherine',28,city ='Melbourne',job='Data Scienti')

def persons(name, age, *args, city, job):
    print(name,age,args,city,job)
persons('Catherine',28,(1,2,3),city ='Melbourne',job='Data Scienti')

#conbination 
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2, 3, 'a', 'b', x=99)
f1(1, 2, 3, x=99)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f2(1, 2, d=99, ext=None)



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