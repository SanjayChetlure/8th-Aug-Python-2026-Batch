
print("--")
s5="abcabca"
print(s5.find("c"))    #get index of 1st occurrence of char from left side
print(s5.index('c'))    #Alternative
print(s5.rfind('c'))   #get index of last occurrence of char from left side

print("---")

s6="abc"
s7="xyz"
s8=" Hi "
s9="my name is abc"
print(s6+s7)     #abc+xyz

print(s8)
print(s8.strip())   #remove space from left & right side of string
print(s8.lstrip())  #remove space only from left side of string
print(s8.rstrip())  #remove space only from right side of string
print(s9.replace("abc","xyz"))

ls=s9.split(" ")      #break/split statement    ['my', 'name', 'is', 'abc']
print(ls)

print("--------additional methods---------")

str1="velocity"
str2="my name is abc"
str3="Abcd"
print(str1.capitalize())        #Capitalizes the first letter of the string.
print(str2.title())             #Converts the first character of each word to uppercase.
print(str3.swapcase())


print("-------")

str4="122"
str5="abc123"
str6="     "
str7="my name is abc my"
print(str1.isalpha())    #expect only alpha
print(str4.isdigit())     #expect only digit
print(str5.isalnum())    #expect only alpha or digit or both
print(str6.isspace())    #expect only space
print(str7.count("my"))
print(str5.count('b'))

