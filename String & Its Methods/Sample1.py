
s1="velocity"
s2="ABCD"
s3="abcd"
s4="my name is abc"

print(len(s1))      #8

# s1=s1.upper()     #Re-initialization
print(s1.upper())
print(s1)

# s2=s2.lower()      #abcd
print(s2.lower())
print(s2)

print("----")
print(s2==s3)                   #compare data & case
print(s2.__eq__(s3))            #Alternate approach

print(s2.lower()==s3.lower())   #compare only data & ignore case

print("----------")
print("abc" in s4)
print(s4.__contains__("abc"))  #Alternative apr

# print("city" in s1)
# print(s1.__contains__("city"))

print(s4.startswith("my "))
# print(s1.startswith("ve"))

print(s4.endswith("abc"))
# print(s1.endswith("ty"))


print("---------")
print(s1[0])
print(s4[3])

print(s1[4:])          #provide start index only
print(s1[4:6])         #starIndex:endIndex+1    (4-5)






