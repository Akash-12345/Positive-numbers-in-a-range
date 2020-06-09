list1=[1,-7,5,64,-14]
list2=[12,11,-65,3]
temp=[]
for num in list1:
    if num>=0:
        print(num,"\t",end="")

for y in list2:
    if y>=0:
        temp.append(y)
print("\n",temp)
