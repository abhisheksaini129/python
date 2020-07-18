for num in range(1,1000):
 copy=num
 n=0
 result=0
 while(copy!=0):
   n=n+1
   copy=int(copy/10)
 copy=num
 while(copy!=0):
   rem=copy%10
   d=rem**n
   result=result+d
   copy=int(copy/10)
 if(result==num):
  print("%d is armstrong number"%result)
