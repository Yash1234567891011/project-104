import csv
from statistics import median
with open("data.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
weight_data=[]
for i in  range(len(file_data)):
    weight= file_data[i][2]
    weight_data.append(float(weight))
n=len(weight_data)
weight_data.sort()
if n % 2==0:
    median1=float(weight_data[n//2])
    median2=float(weight_data[n//2 - 1])
    median=(median1+median2)/2
else:
    median=float(weight_data[n//2]) 
print("median is:"+str(median))       