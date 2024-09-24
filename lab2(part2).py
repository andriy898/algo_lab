import math

def calculator(x, error=10**-6):
    result = 0
    n = 1
    term = 1  
    while abs(term) > error:
        chiselnuk = (x - 1) ** (2 * n + 1)
        znamennuk = (2 * n + 1) * (x + 1) ** (2 * n + 1)
        term = chiselnuk / znamennuk
        result += term
        n += 1
    return 2 * result

h = 0.02  
x_values = [1 + i * h for i in range(int((1.2 - 1) / h) + 1)]

for x in x_values:
    series_sum = calculator(x)
    print(f"x = {x}, Сума ряду = {series_sum}")