
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

#update data
s1[0]="AMOL"
print(s1)

#check specific element present or not
print(s1.__contains__("A"))


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

#copy list object
s2=s1.copy()
print(s2)

print("--print all data using for loop---")
#             1<8
for i in range(0,8):
    print(s1[i])      #s1[0]

print("----")

#             1<8
for i in range(0,len(s1)):
    print(s1[i])      #s1[0]


print("--print all data using for each loop---")
for i in s1:
    print(i)



#Sorting operation
s3=[20,50,10,40,30]
print("------Before sorting-------")
print(s3)

print("-----After sorting-> Ascending order------")
s3.sort()       #[10,20,30,40,50]
print(s3)


print("-----sort data in reverse order (descending order)------")
s3.reverse()     #[50,40,30,20,10]
print(s3)


print("----Count occurrence of specific element in list object------")
s4=[20,50,10,40,30,50,10,50]
print(s4.count(15))


print("---delete all data from list object---")
s4.clear()
print(s4)


print("-----delete list object-----")
del s4
# print(s4)






