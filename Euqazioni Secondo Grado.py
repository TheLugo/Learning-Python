import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    print(f"x1 = {x1}")

    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    print(f"x2 = {x2}")
elif delta == 0:
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    print(f"x = {x}")
else:
    print("Impossible!")
    