n=int(input())
l=[]
for i in range(n):
    m=int(input(F"ENTER THE 1ST  {n} FIBONACCI NUMBERS :  "))
    l.append(m)

# print(list)    

res=map(lambda x:x**3,l)
print(list(res))