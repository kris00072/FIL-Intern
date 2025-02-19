from openpyxl import Workbook
wb=Workbook()
data=[[10,29,45],[2,3,4,5,6]]
sh=wb.active
sh['A1']=10
sh['A2']=20
sh['A3']=50
for i in data:
    sh.append(i)
sh['A3']=90

wb.save("C:\\FIL Intern\\numpy_basics\\test1.xlsx")


