import math

def area(r):
    return math.pi * (r**2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma Comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Com Map
areas = map(area, raios)
print(type(areas))
print(list(areas))

# map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))