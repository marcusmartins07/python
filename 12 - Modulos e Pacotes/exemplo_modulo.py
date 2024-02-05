def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total+=num
    return total