import math
import csv

file = open("data.csv",newline="")
reader = csv.reader(file)
data = list(reader)
newData = data[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data :
        total += int(x)
    mean = total/n
    return mean

sqauredList = []
for number in newData:
    a = int(number) - mean(newData)
    a = a**2
    sqauredList.append(a)
sum = 0
for num in sqauredList:
    sum = sum + num
result = sum/(len(newData)-1)

ans = math.sqrt(result)
print(ans)