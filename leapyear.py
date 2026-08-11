a=int(input("Enter a year"))
if a%400==0:
   print(".")
elif a%100==0:
   print(".")
elif a%4==0:
   print("Leap year")
else:
   print("Not Leap year")         