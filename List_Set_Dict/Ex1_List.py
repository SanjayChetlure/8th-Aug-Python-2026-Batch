
s1=["amol",101,65.2,"A",101]


#print type of object/variable
print(type(s1))

#display data
print(s1)

#get size/length of list object
print(len(s1))

#get specific data from List object
print(s1[0])      #amol
# print(s1[5])    #IndexError: list index out of range


#Add data in list append/insert/extend
#Add new element at last position
s1.append("xyz")
print(s1)

#add new element at specific position/ add element in between list -> right shift operation
s1.insert(3,"rahul")
print(s1)

#add multiple new elements at the end
s1.extend([10,"mahesh","ganesh","B"])
print(s1)

#remove data from list -> pop(), pop(index), remove(object/element)
#remove element from last position
s1.pop()
print(s1)

#remove data from specific index -> left shift operation
s1.pop(3)
print(s1)

#remove specific element -> left shift operation
s1.remove("mahesh")
print(s1)



