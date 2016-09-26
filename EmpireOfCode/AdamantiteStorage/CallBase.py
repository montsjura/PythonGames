from datetime import *
import math

def total_cost(calls):
    dateFormat= '%Y-%m-%d'
    durations = {}
    cost = 0

    for line in calls:
        raw = line.split(' ')
        date = datetime.strptime(raw[0], dateFormat)
        duration = math.ceil(int(raw[2])/60)

        if durations.get(date) != None:
            durations[date] += duration
        else:
            durations[date] = duration

    for duration in list(durations.values()):
        if duration > 100:
            cost += 100 + 2*(duration - 100)
        else:
            cost += duration

    return cost


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

    print("All set? Click 'Check' to review your code and earn rewards!")