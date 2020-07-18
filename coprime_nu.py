a=int(input("enter first number"))
b=int(input("enter second number"))
hcf=0
for num in range(1,a):
  if(a%num==0 & b%num==0):
   hcf=num
if(hcf==1):
  print("they are not co-prime numbers")
else:
  print("they are co-prime numbers")