#use functions

def convert_to_base_10(number, base):
    if base == 10:
        return number  # No conversion needed, return the number as-is
    try:
        base_10_number = int(str(number), base)
        return base_10_number
    except ValueError:
        raise ValueError("Invalid input. Make sure the number is valid for the given base.")
def decimal_to_base(number, base):
    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36")

    if number == 0:
        return "0"  # Special case for zero

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""
    negative = False

    if number < 0:
        negative = True
        number = abs(number)

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base

    if negative:
        result = "-" + result

    return result
def sorter(num, order):
    
    count = 0
    for x in num:
        if x == 0:
            count += 1
        sortednum = ''.join(sorted(num, reverse=order))
        znumstr = sortednum.zfill(count)
        final = znumstr
    

    return final
def uniquer(arr):
    if len(arr) == 1:
        return True
    seen = set()
    for item in arr:
        if item in seen:
            return False
        seen.add(item)
    return True




def did(id, base):
    based = str(id)
    k = len(based)
    x = sorter(based, True)
    y = sorter(based, False)
    
    if base != 10:
      z = convert_to_base_10(x, base) - convert_to_base_10(y, base)
      fz = str(decimal_to_base(z, 3))
    elif base == 10:
        z = int(x) - int(y)
        fz = str(z)
    var = len(fz)
    if var < k:
        zval = '0'
        art = k - var
        val = art
        user = zval  * val
        fz = user + fz
    return fz




def already(id, base):
    arr = []
    newN = did(id, base)
    
    arr.append(newN)
    count = 0
    while uniquer(arr) == True:
        contour = did(newN, base)
        newN = contour
        arr.append(newN)
        
        count += 1
        #for case of constant like 1211 in base 10
        if arr[count] == arr[count -1 ]:
            return 1
        
    #breaks out of loop so uniquer(arr) no longer true    
    #for repeating patterns like 210022 in base 3
    
    count2 = 0
    rep = arr.index(arr[count])
    fin = count - rep
    print(fin)

    return fin
    
    
    

con = already(1211, 10)
print("1211 is: ", con)

cont = already(210022, 3)
print(cont)
#print(convert_to_base_10(210022, 3))

#print(already(575, 10))

