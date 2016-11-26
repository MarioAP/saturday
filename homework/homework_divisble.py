
def divisible_by_2(number):
    # Write a function that returns true if a number is exactly divisible by 2
    # Hakerek funsaun fo fali loos se numero bele fahe ba rua ezactamente
    if number % 2 == 0:
        return True
    return False


def test_divisible_by_2():
    assert(divisible_by_2(0) is True)
    assert(divisible_by_2(3) is False)
    assert(divisible_by_2(8) is True)
    assert(divisible_by_2(31) is False)
    assert(divisible_by_2(235232) is True)


def divisible_by_3(number):
    # Write a function that returns true if a number is exactly divisible by 3
    # Hakerek funsaun fo fali loos se numero bele fahe ba 3 ezactamente
    if number % 3 == 0:
        return True
    return False


def test_divisible_by_3():
    assert(divisible_by_3(0) is True)
    assert(divisible_by_3(3) is True)
    assert(divisible_by_3(9) is True)
    assert(divisible_by_3(31) is False)
    assert(divisible_by_3(235233) is True)


def divisible_by(number, divisor):
    # Write a function that returns true if a number is exactly divisible by a divisor
    # Hakerek funsaun fo fali loos se numero bele fahe ba divisor ezactamente
        if number % divisor == 0:
            return True
        return False


def test_divisible_by():
    assert(divisible_by(0, 4) is True)
    assert(divisible_by(3, 1) is True)
    assert(divisible_by(9, 3) is True)
    assert(divisible_by(30, 4) is False)
    assert(divisible_by(24, 6) is True)


def get_multiples(number, count):
    # Write a function that return a list of <count> multiples of <number>
    # Hakerek funsaun nebee fo fali lista konta <count> ho multiples husi <numero>
    '''lista = []
    for item in range(0, count*number, number):
        lista.append(item)
    return lista'''


def test_get_multiples():
    multiples = get_multiples(1, 2)
    # check we have <count> elements
    assert len(multiples) == 2
    # check none of those elements are not multiples of <number>
    assert not filter(lambda m: m % 1 != 0, multiples)
    # check all the elements are different
    assert len(multiples) == len(set(multiples))

    multiples = get_multiples(3, 3)
    assert len(multiples) == 3
    assert not filter(lambda m: m % 3 != 0, multiples)
    assert len(multiples) == len(set(multiples))

    multiples = get_multiples(222, 3)
    assert len(multiples) == 3
    assert not filter(lambda m: m % 222 != 0, multiples)
    assert len(multiples) == len(set(multiples))
