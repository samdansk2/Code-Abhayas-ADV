# program to return all the elements which are n/3 times greater than where n is length of array

arr=[1,4,3,4,3,3,3,4,4]
b=len(arr)/3
lis=set()
for i in range(len(arr)):
    if arr[i] not in lis:
        temp=arr.count(arr[i])
    if(temp>b):
        lis.add(arr[i])
print(lis)
