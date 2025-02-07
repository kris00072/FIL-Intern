#lambda parameters : exp
        #(n1 ; n2)
#add=lambda x,y: x+y
#print(add(10,20))

#map function
#map(f1,iterable):
#newValue=map(addValue,price)
#price=[10,20,30,40,50,60]
#add=2
#newValue=map(lambda x:x+add,price)
#print(list[newValue])

#FILTER FUNCTION

#ageList=[10,40,50,60,15]

#def getAge(x):
    #if x>18#:
        #return True

#age = filter(getAge,ageList)
#print(list(age))
   
from collections import defaultdict

def dv():
    return "Key Is Not Present"

d1=defaultdict(dv)
d1['a']=10
d1['b']=20
print(d1['c'])