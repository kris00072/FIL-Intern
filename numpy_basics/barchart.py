from collections import namedtuple
Student=namedtuple("Student",['name','age'])
s=(Student('Steve',41))
print(s)
#s=('rahul',89)
print(s.age)
