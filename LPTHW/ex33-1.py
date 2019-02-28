numbers  = []

y = int(input("incrementor is..."))
x = range(1,int(input("total is...")))
c = 0

for i in x:
#    c = 0
    print(f"At the top c is {c}.")
    numbers.append(c)
    c += y
    print("Numbers now: ", numbers)
    print(f"At the bottom c is {c}.")
# Error
