import csv 
with open("data.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
weight_data=[]
for i in range(len(file_data)):
    weight=file_data[i][2]
    weight_data.append(float(weight))
n=len(weight_data)
total=0    
for k in weight_data:
    total=total+k
mean=total/n
print("mean is:"+str(mean))    