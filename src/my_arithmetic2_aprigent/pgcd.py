def pgcd(a, b):
    #comment
    while b:
        a, b = b, a % b
    return a

