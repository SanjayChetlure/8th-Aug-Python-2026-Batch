print("------Ex1: nested if -----")

# if condition1:       //outer if
# 	print()
# 	if condition2        //inner/nested if
# 		inner if body


PEM=251

# 251>=250
if PEM>=250:            #Outer if
    print("Selected in Prelim exam")
    print("Preparing for main exam")
    MEM=450
    #  450>=500
    if MEM>=500:         #Inner/Nested if
        print("Selected in Mains exam")
    else:
        print("Rejected from mains exam")
else:
    print("Rejected from Prelim exam")

