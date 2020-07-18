a=int(input("enter the number"))
b=a*2
for x in range(a+1,b,1):
  d=int(x/2)
  for c in range(2,d+1,1):
    if(x%c!=0):
     print("%d is next prime number"%x)
    break