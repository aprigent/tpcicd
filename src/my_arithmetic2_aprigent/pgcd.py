def pgcd(a, b):
    #comment
    if b>1024:
        print("ok")
    while b:
        a, b = b, a % b
    return a

