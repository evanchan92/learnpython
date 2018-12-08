def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(200,2)

print(f"Age: {age}, Height: {height}, weight: {weight},IQ:{iq}")

print("There's a puzzle.")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print("that becomes",what, "Can you do it by hand?")
