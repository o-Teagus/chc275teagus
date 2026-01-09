mylist = [5,10,15,20]
print(mylist)
print(mylist[0])
print(mylist[0]*mylist[3])
sum=(mylist[1]+mylist[2])
print(sum)
i=0
while i <=3:
    print(mylist[i])
    i=i+1
mylist = [5,10,15,20]
print("with forloop")
for num in mylist:
    print(num)
    
i=0
while i <=3:
    mylist[i]=mylist[i]+5
    i=i+1
    print(mylist)