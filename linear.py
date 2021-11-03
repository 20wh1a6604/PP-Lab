def linear_search(arr,x):
   for i in  range(len(arr)):
     if arr[i] == x:
          return i
     return -1
arr = [1 ,2 ,3 ,4, 15]
x = 12
r = linear_search(arr,x)
if(r == -1):
    print("element is not found")
else:
    print("element is found")
