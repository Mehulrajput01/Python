#dictonary in python

#dictonary are used in key:value pairs and  it is mutable (changable) don't allow duplicate keys

keys={
    "name":"TONY",
    "age": 45,
    "address":"Mars"
}
print(keys)
print(type(keys))
print(keys["name"])
print(keys["age"])
print(keys["address"])

null_dict={}        #null dictonary create in dictonary
print(null_dict)
print(type(null_dict))
null_dict={"stark"}    #add variable
print(null_dict)

#nested in dictonary
info={
    'name':"Robert",
    "age":21,
    "address":"U.S",
    "area":{
       "city":"Chicago",
       "house No.":3412,
       "Flat":{"as":"sa",
              "fg":"lk"
    
       }
    }
}
print(info["area"])
print((info["area"]["city"]))
print(info)
#methods in dict

print(info.keys())   #return to  all keys

print(info.values())  #return to all values

print(info .items ())  #return to all value in tuple form

print(info.get("age"))   #return to value whatever is asked 

info.update({"surname":"john"})  #updating new key:value in dict
print(info)
      

