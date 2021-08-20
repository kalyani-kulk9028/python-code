==========Map function============
print
list1 = [10,20,30,40,50]
sqr = map(lambda x :x**2,list1)
type(sqr)
print(list(sqr))

========================================
L = [lambda x : x**2,lambda x :x**3,lambda x : x**4]
for f in L:
    print(f(4))
    
=========================================

a = [1,2,3,4]
b = [3,3,4,5]
p = list(map(lambda x,y : x+y, a,b))
print('p',p)
print(type(p))
=============================

k = [0,1,2,3,4,5,23,56,65]
result = filter(lambda x : x!=1,k)
print(list(result))

==========================================
import reduce
f = lambda a,b : a if(a > b) else b
print(reduce(f,[1,3,4,10,5]))

-===========swap list=======================
def swaplist(newlist):
    size =len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp
    return newlist
newlist = [12,3,14,25,16]
print(swaplist(newlist))

===============swapposition(interchange========================
                            
def swapposition(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
list = [10,30,20,50,60]
pos1,pos2 = 0,1
print(swapposition(list,pos1,pos2))
