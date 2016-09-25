import collections


def non_unique(data):
    # Identify duplicates
    duplicates = [x for x, y in collections.Counter(data).items() if y > 1]

    print(duplicates)

    for item in data:
        if type(item) is str:
            if item.isupper() and item.lower() in data:
                duplicates.append(item)
                duplicates.append(item.lower())
            if item.islower() and item.upper() in data:
                duplicates.append(item)
                duplicates.append(item.upper())

    result = []

    for item in data:
        if item in duplicates or str(item).upper() in duplicates or str(item).lower() in duplicates:
            result.append(item)

    return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

    # Rank 2
    assert non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                       'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                       'p', 'r', 7, 'b']) == ['P', 7, 'j', 'A', 'P', 'A', 'j', 'p', 7], "Letters"

    print("All done? Earn rewards by using the 'Check' button!")
