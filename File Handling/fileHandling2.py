file = open("C:\\fidelity\\New FIlee.txt", "r")
ccount=0
for l in file:
    print(file.readline())
    print(file.tell)