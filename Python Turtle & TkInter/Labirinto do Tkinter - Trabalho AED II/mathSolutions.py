# Esta função transforma números pares em números ímpares.
def oddInt(n):
    if(n == 0):
        return 1

    if(n % 2 == 0):
        return n - 1
    
    return n
