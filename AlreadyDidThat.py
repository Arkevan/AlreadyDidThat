def convert_to_base_10(number, base):
    if base == 10:
        return number  # No conversion needed, return the number as-is
    try:
        base_10_number = int(str(number), base)
        return base_10_number
    except ValueError:
        raise ValueError("Invalid input. Make sure the number is valid for the given base.")






# print(octal)

def sorter(num, order):
    newnum = str(num)
    count = 0
    for x in newnum:
        if x == 0:
            count += 1
    sortednum = ''.join(sorted(newnum, reverse=order))
    znumstr = sortednum.zfill(count)
    final = int(znumstr)

    return final


def uniquer(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return False
        seen.add(item)
    return True


def did(id, base):
    based = str(convert_to_base_10(id, base))
    k = len(based)
    x = sorter(based, True)
    y = sorter(based, False)
    z = x - y
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
    while len(arr) > 1 and uniquer(arr) == True:
        contour = did(newN, base)
        newN = contour
        arr.append(newN)

    # if algorithm reaches a constant
    if len(arr) == 1:
        return 1

    final = len(arr)


    return final


con = already(1211, 10)
print("1211 is: ", con)

cont = already(210022, 3)
print('210022 is: ', cont)
print(convert_to_base_10(210022, 3))

print(already(575, 10))
