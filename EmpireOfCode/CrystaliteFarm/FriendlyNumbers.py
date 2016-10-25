import math

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    try:
        sign = number / abs(number)
    except ZeroDivisionError:
        sign = 1

    result = ""
    intResult = number
    power = powers[0]

    for i in range(len(powers) - 1, -1, -1):
        if abs(number) // base ** i > 0:
            power = powers[i]
            if decimals > 0:
                intResult = sign * round(abs(number) // base ** i + (abs(number) % base ** i) / base ** i, decimals)
            else:
                intResult = sign * math.floor(abs(number) // base ** i + (abs(number) % base ** i) / base ** i)
            break

    strFormat = '{:.' + str(decimals) + 'f}'
    result += strFormat.format(intResult)
    result += power
    result += suffix

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(12000000, decimals=3) == '12.000M', '12.000M'
    assert friendly_number(-150, powers=['', 'd', 'D'], base=100) == '-1d', '-1d'

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
