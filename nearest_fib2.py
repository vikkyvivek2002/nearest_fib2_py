n=int(input())
a,b=0,1
#print(a,b,end=' ')
while b<n:
c=a+b
a=b
b=c
#print(a,end=' ')
print('answer',a,b)
