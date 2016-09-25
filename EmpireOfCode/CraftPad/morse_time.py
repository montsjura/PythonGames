def morse_time(time_string):

    digitLength = [2, 4]
    code = {'0':'.', '1':'-'}
    result = ''
    lock = False

    times = time_string.split(":")

    for time in times:
        if times.index(time) > 0 and lock == False:
            digitLength[0] += 1
            lock = True

        if len(time) < 2:
            time = '0' + time

        for i in range(2):
            digit = bin(int(time[i]))[2:]

            if len(digit) < digitLength[i]:
                for j in range(digitLength[i]-len(digit)):
                    digit = '0' + digit

            for k in range(len(digit)):
                result += code.get(digit[k])

            result += ' '

        result += ': '

    print("'%s'" % result[:-3])

    return result[:-3]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")