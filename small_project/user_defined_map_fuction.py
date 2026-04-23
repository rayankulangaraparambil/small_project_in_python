"""it use the single litreble """
lis=[1,5,4,6,7,9]
def pr(x):
    return x**2

def user_map(fun,intres):
    nels=[]
    for x in intres:
        s=fun(x)  
        nels.append(s)
    return nels
print(lis)    
s=user_map(pr,lis)
print(s)

"""it use the multiple litreble"""

def user_map(fun,*litretes):
    newlst=[]
    for x in zip(*litretes):
        result=fun(*x)
        newlst.append(result)
    return newlst
s=user_map(lambda x:x**2 ,[1,2,3])

print(s)