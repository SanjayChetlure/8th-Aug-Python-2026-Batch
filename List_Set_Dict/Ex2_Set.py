
s1={"amol",101,65.5,"A+",101,101}

print(s1)

print(len(s1))
print(type(s1))

#Check for presence of element
print(s1.__contains__(102))
print(102 in s1)  # Output: True ()


# ------Adding Elements (add/update)----------
#Add Single Element
s1.add(105)
print(s1)

# Add multiple elements
s1.update(["mahesh","suresh"])
print(s1)


# ------Removing Elements(remove/discard)----------
s1.remove("A+")
print(s1)

s1.discard(200)
print(s1)

s2=s1.pop()
print(s2)
print(s1)      #remove any random element from set


#copy set
s3=s1.copy()
print(s3)

#sorting
s4={50,20,10,40,20,20}
print(s4)
print(sorted(s4))

s4=sorted(s4)    #reinitialization
print(s4)


#delete/clear all data from set obj
s1.clear()
print(len(s1))

#delete set object
del s1

print("------Print all data using for each loop-----")
for i in s4:
    print(i)


#Convert Set object to list
s5={50,20,10,40,20,20,30}
print(type(s5))
print(s5)

s6=list(s5)          #convert set object into list
print(type(s6))
print(s6)

#print smallest number
s6.sort()
print(s6)
print(s6[0])


#convert list object into set
s7=[10,20,50,40,40,20]
print(s7)

s8=set(s7)       #convert list object into set
print(s8)





