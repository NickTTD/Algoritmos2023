base = 3
exponente = 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente-1)
    
print(potencia(base, exponente))


def fib(num):
    if (num == 0 or num == 1):
        return num
    else:
        fibonacci = fib(num-1) + fib(num-2)
        return fibonacci
    
print(fib(8))