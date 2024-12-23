def find_number_of_factors(n):
    factor = 0
    for i in range(1,n+1):
        if n%i == 0:
            factor=factor+1
    return factor


print(find_number_of_factors(100))
