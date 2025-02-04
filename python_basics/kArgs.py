def functionName(*ar):
    return ar;

s=functionName(10,20,30);
print(type(s));

ti=();
print(type(ti));

def func1(a,b):
    return (a+b);

p=func1;
print(p(10,20));

def f12():
    def f2():
        return "Hello";
    return f2();

f1();

data=10;
def f1():
    data+=10;
    return data;
print(f1());