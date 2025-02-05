file = open("C:\\fidelity\\New FIlee.txt", "r")

print(file.tell())  
file.seek(5) 
data = file.read(10)  

print(data)  

file.close()  

