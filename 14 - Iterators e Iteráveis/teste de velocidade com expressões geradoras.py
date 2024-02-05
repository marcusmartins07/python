
# Generators (geradores)

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()
print(ge1) # generator

print(next(ge1))
print(next(ge1))

import time
# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1000000))) #100 mihloes
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(1000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')