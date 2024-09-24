def binomialCoeff(n, k) :
    result = 1
    #for optimisation.
    if (k > n - k) :
        k = n - k
    #It eliminate one term from denominator.
    for i in range(0 , k) :
        result = result * (n - i)
        result = result // (i + 1)
    return result

print(binomialCoeff(7,2))
