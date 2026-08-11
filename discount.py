q=int(input("Enter quantity of iteam"))
p=int(input("Enter price of iteam"))
total_bill=q*p
if total_bill>=1000:
    total_bill*=1.8  
    print("20% discount applied!")
    print(total_bill)
elif total_bill>=500:
    total_bill*=0.9
    print("10% discount applied!")
    print(total_bill)    
else:
    print("No discount applied sorry!")     
