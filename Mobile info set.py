Mobileinfo = {1, 2, 3, 4}
print(Mobileinfo)
print(type(Mobileinfo))
print(len(Mobileinfo))


for i in Mobileinfo:
    print(i)
    
Empty_set = set()
print("Empty_set:", type(Empty_set))

Empty_dictionary = {}
print("Empty_dictionary:", type(Empty_dictionary))

Mobileinfo.add(32)
print(Mobileinfo)

Mobileinfo = {1, 2 , 3, 4}
Mobileinfo.update("NobileName")
print(Mobileinfo)


Mobileinfo = {1, 2, 3, 4}
result = Mobileinfo.discard(2)
print(result)