numbers = []
#i = 0
y = int(input("incremental by ..."))

def adding_list(what):
    i = 0
    while i < what :
        print(f"At the top i is {i}.")
        numbers.append(i)
    #    y = int(input("incremental by..."))
        i += y
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}.")
# bug: Local variable 'i' referenced before assignment.
x = int(input(">"))
adding_list(x)

print ("The numbers: ")

for num in numbers:
    print (num)
