def roman(number):
    roman = ''
    translate = {1: 'I', 4:'IV', 5: 'V', 9:'IX', 10: 'X', 40:'XL', 50: 'L', 90:'XC', 100: 'C', 400:'CD', 500: 'D', 900:'CM', 1000: 'M'}
    bases = sorted(translate.keys(), reverse=True)

    for i in range(len(bases)):
        base = number // bases[i]
        mod = number % bases[i]
        if base > 0 and base <= 3:
            for k in range(base):
                roman += translate.get(bases[i])
            number = mod

    # replace this for solution
    return roman

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == 'VI', '6'
    assert roman(76) == 'LXXVI', '76'
    assert roman(499) == 'CDXCIX', '499'
    assert roman(3888) == 'MMMDCCCLXXXVIII', '3888'