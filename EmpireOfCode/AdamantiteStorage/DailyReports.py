from datetime import *


def count_reports(full_report, from_date, to_date):
    dateFormat = '%Y-%m-%d'
    total = 0
    dateMin = datetime.strptime(from_date, dateFormat)
    dateMax = datetime.strptime(to_date, dateFormat)

    for w in full_report.split('\n'):
        date = datetime.strptime(w.split(' ')[0], dateFormat)
        contents = w.split(' ')[1].split(',')

        if date >= dateMin and date <= dateMax:
            for i in range(len(contents)):
                total += (ord(contents[i][0]) - 65) * 9 + int(contents[i][1])

    return total


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_reports("2015-01-01 A1,B2\n"
                         "2015-01-05 C3,C2,C1\n"
                         "2015-02-01 B4\n"
                         "2015-01-03 Z9,Z9",
                         "2015-01-01", "2015-01-31") == 540, "Normal"
    assert count_reports("2000-02-02 Z2,Z1\n"
                         "2000-02-01 Z2,Z1\n"
                         "2000-02-03 Z2,Z1",
                         "2000-02-04", "2000-02-28") == 0, "Zero"
    assert count_reports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31") == 235, "Millenium"

    print("Earn cool rewards by using the 'Check' button!")
