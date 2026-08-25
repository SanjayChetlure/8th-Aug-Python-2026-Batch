

print("--------Ex3: elif-----------")

marks=61.4
#   48>=65
if marks>=65:
    print("Distinction")
    #48>=60 and 62<65

elif marks>=60 and marks<65:
    print("1st class")
    #48>=50 and 54<60
elif marks>=50 and marks<60:
    print("2nd class")
    #48>=35 and 48<50
elif marks>=35 and marks<50:
    print("2nd class")
elif marks<35:
    print("Fail")


print("----")

marks=22
#   48>=65
if marks>=65:
    print("Distinction")
    #48>=60 and 62<65
elif marks>=60 and marks<65:
    print("1st class")
    #48>=50 and 54<60
elif marks>=50 and marks<60:
    print("2nd class")
    #48>=35 and 48<50
elif marks>=35 and marks<50:
    print("2nd class")
else:
    print("Fail")





# true and true -> true
# true and false -> false
# false and true -> false
# false and false -> false