
print("--------Ex3: elif-----------")

# Syntax:

# if condition1:
#     condition1 body
# elif condition2:
#     body
# elif condition3:
#     body
# elif condition4:
#     body
# elif condition5:
#     body

shoppingAmt=500

#         500>=20000
if shoppingAmt>=20000:
    print("20% discount")
    #     500>=10000
elif shoppingAmt>=10000:
    print("10% discount")
    # 500 >= 5000
elif shoppingAmt>=5000:
    print("5% discount")
    #500<5000
elif shoppingAmt<5000:
    print("no discount")



print("----------")


shoppingAmt=500

if shoppingAmt>=20000:
    print("20% discount")
elif shoppingAmt>=10000:
    print("10% discount")
elif shoppingAmt>=5000:
    print("5% discount")
else:
    print("no discount")

print("--------")

shoppingAmt=5000

if shoppingAmt>=20000:
    print("20% discount")
elif shoppingAmt>=10000 and shoppingAmt<20000:
    print("10% discount")
elif shoppingAmt>=5000 and shoppingAmt<10000:
    print("5% discount")
else:
    print("no discount")



