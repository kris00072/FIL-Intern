import csv
with open("data.csv","a+") as f:
    w=csv.writer(f)
    w.writerow(["Eno","Ename","Salary"])
    w.writerow([1,"Tom",1000])
    f.seek(0)
    reader=list(csv.reader(f))
    #for reader in f:
        #print(reader)
    print(reader)
    #print(f.read())
    