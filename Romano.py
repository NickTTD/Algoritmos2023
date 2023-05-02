# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
#Un símbolo de valor menor a la derecha de un símbolo de valor mayor se resta del valor mayor en lugar de sumarse.
def romano_decimal(NumeroRomano):
    DiccionarioRomano = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    if len(NumeroRomano) == 0:
        return 0
    elif len(NumeroRomano) == 1:
        return DiccionarioRomano[NumeroRomano]
    elif DiccionarioRomano[NumeroRomano[0]] < DiccionarioRomano[NumeroRomano[1]]:
        return DiccionarioRomano[NumeroRomano[1]] - DiccionarioRomano[NumeroRomano[0]] + romano_decimal(NumeroRomano[2:])
    else:
        return DiccionarioRomano[NumeroRomano[0]] + romano_decimal(NumeroRomano[1:])
    

NumeroRomano=str(input("Ingrese el numero romano"))
print(romano_decimal(NumeroRomano))


