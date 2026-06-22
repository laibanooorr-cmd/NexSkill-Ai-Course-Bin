n = 1
if n == 1:
    pass  # Do nothing
for n in range(1, 3):
    if n == 1:
        print("n is 1")
    elif n == 2:
        print("n is 2")
else:
    print("n is neither 1 nor 2")
    n = 3
    if n == 3:
        print("n is 3")

    for n in range(6):
        if n == 4:
            break
        print(n)
    print("Next run")


    for n in range(6):
         if n == 4:
            continue
         print(n)
    print("Nesxt run")