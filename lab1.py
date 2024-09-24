import math

city = "Striy"
print(city)


is_voter = False
is_citizen = True
print(is_citizen and is_voter)
print(is_citizen or is_voter)
print(not is_voter)
print(is_citizen)


is_raining = True
is_snowing = False
print(not is_raining)
print(not is_snowing)


y = 7.315
z = 3.127
res = 16 * y**2 + math.exp(y * z) + z**(1/3) + 1.51 + math.log(y * z)
rounded_res = round(res, 2)
print(rounded_res)