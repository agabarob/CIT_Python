# A simple temperature converter
print("To convert from celsius to farhnheit, type 1 and To convert from farhnheit to celsius type 2")
user_input= int(input())
if user_input == 1:
   T_1 = float(input("Enter the temperature in degrees Celsius:"))
   C =((9/5)*T_1) + 32
   print (C)
elif user_input == 2:
   print("To convert from  farhnheit to celsius,")
   T_2 = float(input("Enter the temperature in degrees Farhnheit:"))
   F =(T_2 -32)*(5/9)
   print(F)
else:
    print("Your input is invalid. Please Enter 1 or 2")
