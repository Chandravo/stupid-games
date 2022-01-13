import random
l=[0,0,0]
g=[0,1,2]
p=0
t=int(input())
for i in range(t):
    l=[0,0,0]
    g=[0,1,2]
    x=random.randint(0,2)
    
    l[x]=1
    
    c=random.randint(0,2)
    
    k=[0,1,2]
    if c==x:
        k.remove(c)
        o=k[random.randint(0,1)]
        
    else:
        k.remove(c)
        k.remove(x)
        o=k[0]
        
    g.remove(o)
    
    if g.index(c)==0:
        c2=g[1]
    elif g.index(c)==1:
        c2=g[0]
    
    if l[c2]==1:
        p=p+1
print((p/t)*100)
