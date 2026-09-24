

#key-String, value-float
dict1={"mahesh":75.2,"ramesh":61.8,"suresh":90.0,"ganesh":77.4}
print(dict1)

#key-Int, value-string
dict2={1:"suresh",2:"ganesh", 3:"mahesh",4:"ramesh"}
print(dict2)

#key-Int, value-string/float
dict3={1:"suresh",2:"ganesh", 3:75.5, 4:98.4}
print(dict3)


#length of dictionary
print(len(dict1))

#get value of any specific key
print(dict1["ramesh"])   #61.8
print(dict2[3])          #mahesh

#update/modify value of any specific key
dict2[1]="SURESH"
print(dict2)

#check any specific key available or not
print(dict1.__contains__("ramesh"))
print("ramesh" in dict1)

#Add new key-value pair
dict1["Amol"]=75.1
print(dict1)


#remove key-value pair
dict1.pop("ramesh")      #pop(key)
print(dict1)

#Remove last inserted item(k-v)
dict1.popitem()
print(dict1)

print("----get all keys-----")
allKeys=dict1.keys()
for singleKey in allKeys:
    print(singleKey)

print("---")

for singleKey in dict1.keys():
    print(singleKey)


print("----get all values-----")
allValues=dict1.values()
for singleValue in allValues:
    print(singleValue)

print("---")

for singleValue in dict1.values():
    print(singleValue)


print("------get all key-value pairs -------")
allkeyValues=dict1.items()
for k,v in allkeyValues:
    print(k, v)

print("---")
for k,v in dict1.items():
    print(k, v)

print("----")

for key in allKeys:
    print(key, dict1[key])


print("---clear all data in dict---")
dict1.clear()
print(len(dict1))

print("---delete dict---")
del dict1
# print(dict1)









