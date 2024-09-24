import math

a = 2
b = 5
h = 0.2
x = a 

while x <=b:
    if x < 3:
        print("| x = ", x, " | F(x) =", math.cos(x**0.3), "|")
    elif 3<=x<4:
        print("| x = ", x, " | F(x) =", math.sqrt(x**3+math.log10(x)), "|")
    else:
        "| x = ", x, " | F(x) =", ((math.cos(x)/math.sin(x))**2), "|"
    x += h