def clock_angle(time):
    diff = 0
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])

    if hour >= 12:
        hour -= 12

    print('Heure : %i' % hour)
    print('Minute : %i' % minute)

    angleHour = 30 * (hour + minute / 60)
    angleMinute = 6 * minute

    print('Heure --> %s / Minute --> %s' % (str(angleHour), str(angleMinute)))

    if angleMinute > angleHour:
        diff = angleMinute - angleHour
    else:
        diff = angleHour - angleMinute

    if diff >= 180:
        diff = 360 - diff

    return diff


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")