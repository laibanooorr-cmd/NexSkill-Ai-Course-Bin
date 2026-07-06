MobileiinfoList = [1, 2, 3, 4, 5]
print(list)
print(type(MobileiinfoList))
print(len(MobileiinfoList))
for i in MobileiinfoList:
    print(i)
    

print(MobileiinfoList[2])

Mobilelength = float(input("please enter your length"))
MobileiinfoList.append(Mobilelength)
print(MobileiinfoList)


MobileiinfoList.insert(5 , 8)
print(MobileiinfoList)

MobileiinfoList.remove(5)
print(MobileiinfoList)

MobileiinfoList.pop(1)
print(MobileiinfoList)