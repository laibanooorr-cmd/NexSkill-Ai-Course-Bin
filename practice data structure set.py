BoookSet = {"Price", 232, "Title", 54.2}
print(BoookSet)
print(type(BoookSet))
print(len(BoookSet))
for i in (BoookSet):
    print(i)
BoookSet.add(23.4)
print(BoookSet)
BoookSet.discard(54.2)
print(BoookSet)
