def f1():
    yield 'a';
    yield 'b';
    yield 'c';

p=f1();
print(next(p));
print(next(p));

#memory efficiency lod
#ye fidelity wale achhe