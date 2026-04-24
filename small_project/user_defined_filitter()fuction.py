
# s=list(map(lambda x:x**2,filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))
# print(s)
'''i will  create in filiter()'''
#its create a user defined map()
def user_defined_map(fun,*itreters):
    lis=[]
    if len(itreters)==1:
        for x in itreters[0]:
            if isinstance(x,(list,tuple)):
                result=fun(*x)
                lis.append(result)
            else:
                result=fun(x)
                lis.append(result)
    else:
        for x in zip(*itreters):
            result=fun(*x)
            lis.append(result)
    return lis
#its create a user defined filiter()
def user_defined_filiter(con,*itr):
    newfllis=[]
    for x in zip(*itr):
        result=con(*x)
        if result==True:
            newfllis.append(x)
    return newfllis

print(user_defined_map(
    lambda x,y: x+y,
    user_defined_filiter(
        lambda x,y: x+y > 6,
        [1,2,3],
        [4,5,6]
    )
))
    
s=user_defined_map(lambda x:x**2,user_defined_filiter(lambda x:x %2==0,[1,2,3,4,5,6,7,8,9,10]))
print(s)
v=user_defined_map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,10])
print(v)