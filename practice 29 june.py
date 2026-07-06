print("welcome to practice 29 june 2026")
MobileName = input("please enter your mobile name:") # Enter name
print("MobleName:", MobileName)
print(type(MobileName))
print(len(MobileName))

for i in MobileName:
    print(i)
    # My first code ende here

MobilePrice = float(input("please enter your MobilePrice"))
print(type(MobilePrice))

if MobilePrice > 5:
    print(" Greater 5")
elif MobilePrice < 5:
    print("less then 5")
elif MobilePrice < 3:
    print("less 3")
else:
    print("what ever.....")
    
