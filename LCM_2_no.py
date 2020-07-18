a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
flag=1
if(a>b):
 num=a
else:
     num=b
while(flag==1):
  if(num%a==0 and num%b==0):
     result=num
     flag=0
     break
  else:
    num+=1
    
   
print("there lcm is %d"%result)