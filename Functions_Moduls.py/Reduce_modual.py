from functools import reduce
l1=[5,8,9,5]
result=reduce(lambda x,y:x+y,l1)
print(result)