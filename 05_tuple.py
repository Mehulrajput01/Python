05_tuple
# [tuples in python] 
   # A built in data type that lets us create immutable sequence of values.
tup=(1,2,3,4.5,)
print(type(tup))          
print(tup[2])       #finding element with indexing
print(tup[3])
#tup[0]=5         #error not allowed in tuple 
tup=()        # this allowed in tuple this is called empty tuple
print (tup)
print(type (tup))
tup=(1 ,)           # single element
print(tup)
print(type(tup))
# slicing in tuple
tup=(1,2,3,4,5,)
print(tup[1:])
print(tup[:])
#tuple method
#index method
tup=(1,2,3,4,5,)
print(tup.index(2)) #find the element in tuple
#count method
tup=(1,2,3,4,5,)
print(tup.count(2))   #counts total occurences