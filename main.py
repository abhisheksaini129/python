num=int(input("enter the number of prime no. for list"))
mylist=[]
count=num;
i=1
while(count>0):
 i=i+1
 z=0
 flag=0
 for d in range(2,int(i/2)+1):
     if(i%d==0):
       flag=0
     else:
       flag=1
     if(flag==1):
       mylist.insert(i,z)
       z=z+1
       count=count-1
print("your list is",mylist)
