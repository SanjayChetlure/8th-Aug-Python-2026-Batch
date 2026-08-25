
print("------Ex2: nested if -----")

shoppingAmt=8000

#          8000>=500
if shoppingAmt>=500:
    print("Free Delivery")
    #          8000>=5000
    if shoppingAmt>=5000:
        print("Additional 10% Discount")
    else:
        print("No Additional Discount")
else:
    print("RS 50 Delivery charges")



