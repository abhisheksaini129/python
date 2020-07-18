x=int(input("enter the number"))
y=int(x/2)
for a in range(2,y+1):
 if (x%a==0) :
   print("%d is not a prime number"%x)
   break
if (x <=1) :
  print("%d is not a prime number"%x)

else:
 print("%d is a prime number"%x)