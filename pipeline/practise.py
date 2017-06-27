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

#split based on condition , using list generator 
list_split1 = [i for i in list1 if type(i)!=str]
list_split2 = [i for i in list1 if type(i)!=int]


list_split_len1, list_split_len2 = [],[]
for i in list2:
    if len(i)>5:
        list_split_len1.append(i)
    else:
        list_split_len2.append(i)

list_split1 = list1.apply(lambda x: isinstance(x, int))


#list geenrate method
[x**2 for x in range(1,11) if x%2 ==0] 
[m+n for m in 'ABC' for n in 'abc']

d = {'x':'A','y':'B','z': 'C'}
[k+'-'+v for k,v in d.items()]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)


#generator 
L = [x*x for x in range(10)]   
g = (x*x for x in range(10))    #generator 
#next(g) , never use next() to iterate generator, use for 
for i in g:
    print(i)
    

##iterator 
from collections import Iterable 
from collections import Iterator
isinstance([],Iterable)
isinstance((x for x in range(1,10)),Iterable)
isinstance((x for x in range(1,10)),Iterator)



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
# Functional Programming 
#####################################
def f(x):
    return x**2

r = map(f,[1,2,3,4,5,6,7,8,9])
list(r) #r is iterator
list(map(str,[1,2,3,4,5,6,7,8,9]))



