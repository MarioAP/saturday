# Write a function that addPs up every item in a list
# Hakerek funsaun nebee hatama hamutuk sasan hoto-hotu iha lista laran
def list_sum(input_list):
    list_sum = 0
    for i in input_list:
        list_sum += i
    return list_sum


def test_list_sum():
    assert list_sum([]) is 0
    assert list_sum([1]) == 1
    assert list_sum([1, 2]) == 3
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([10, 20, 30]) == 60
    # chosse a random length from 0 to 10
    import random
    list_length = random.randint(0, 10)
    test_list = []
    test_total = 0
    for i in range(0, list_length):
        # get a random integer
        test_integer = random.randint(0, 100)
        # add the integer into the list
        test_list.append(test_integer)
        # add the integer to the test total
        test_total = test_total + test_integer

    # test the random list
    assert list_sum(test_list) == test_total


# Write a function that returns True if a list contains the number 42
# Hakerek funsaun nebee fo fali Loos se numero 42 iha lista laran
def contains_42(input_list):
    if 42 in input_list:
        return True
    else:
        return False


def test_contains_42():
    assert contains_42([]) is False
    assert contains_42([42]) is True
    assert contains_42([4, 2]) is False
    assert contains_42([42, 2]) is True


# Write a function that returns True if a list contains a value
# Hakerek funsaun nebee fo fali Loos se valor ( input_value ) iha lista laran
def contains_value(input_list, input_value):
    if input_value in input_list:
        return True
    else:
        return False


def test_contains_value():
    assert contains_value([], 42) is False
    assert contains_value([42], 42) is True
    assert contains_value([4, 2], 12) is False
    assert contains_value([42, 2], 2) is True


# Write a function that returns True if a list contains a value EXACTLY twice
# Hakerek funsaun nebee fo fali Loos se valor ( input_value ) iha lista laran dala rua ezatamente
def contains_value_twice(input_list, input_value):
    # return input_list.count(input_value) == 2
    count = 0  # FO VARIABEL COUNT HANESAN MAMUK
    for item in input_list:  # ITA HALO LOOP BA KADA LISTA (input_list) IDA NIA LARAN
        if item == input_value:  # CEK SE ITEM HANESAN HO VALOR (input_value) NEBE IHA
            count = count + 1  # AUMENTA VALOR IDA BA VARIABEL COUNT SE VALOR NEE HANESAN (input_value)
    if count == 2:  # CEK VALOR (input_value) HANESAN RUA ENTAUN
        return True  # FO FALI LOS
    else:  # SELAE
        return False  # FO FALI SALA


def test_contains_value_twice():
    assert contains_value_twice([], 42) is False
    assert contains_value_twice([42, 42], 42) is True
    assert contains_value_twice([4, 2, 12], 12) is False
    assert contains_value_twice([2, 42, 2], 2) is True
    assert contains_value_twice([2, 2, 2], 2) is False


# Write a function that returns True if a list contains a value EXACTLY count times
# Hakerek funsaun nebee fo fali Loos se valor ( input_value ) iha lista ( input_list ) laran ezatamente konta ( count )
def contains_value_count_times(input_list, input_value, count):
    hetan = 0
    for item in input_list:
        if item == input_value:
            hetan = hetan + 1
    if hetan == count:
        return True
    else:
        return False


def test_contains_value_count_times():
    assert contains_value_count_times([], 42, 1) is False
    assert contains_value_count_times([], 42, 0) is True
    assert contains_value_count_times([42, 42], 42, 2) is True
    assert contains_value_count_times([4, 2, 12], 12, 3) is False
    assert contains_value_count_times([2, 42, 2], 2, 2) is True
    assert contains_value_count_times([2, 2, 2], 2, 5) is False
    assert contains_value_count_times([2, 2, 2], 2, 3) is True


# Write a function that returns True if a list contains a value more than count times
# Hakerek funsaun nebee fo fali Loos se valor ( input_value ) iha lista ( input_list ) laran barak liu tan duke konta ( count )
def contains_value_more_than_count_times(input_list, input_value, count):
    hetan = 0
    for item in input_list:
        if item == input_value:
            hetan = hetan + 1
    if hetan > count:
        return True
    else:
        return False


def test_contains_value_more_than_count_times():
    assert contains_value_more_than_count_times([], 42, 1) is False
    assert contains_value_more_than_count_times([], 42, 0) is False
    assert contains_value_more_than_count_times([42], 42, 0) is True
    assert contains_value_more_than_count_times([43, 42], 42, 2) is False
    assert contains_value_more_than_count_times([4, 2, 12], 12, 1) is False
    assert contains_value_more_than_count_times([2, 42, 2], 2, 1) is True
    assert contains_value_more_than_count_times([2, 2, 2], 2, 3) is False
    assert contains_value_more_than_count_times([2, 2, 2], 2, 2) is True


# This function takes a list as input.
# Return a list with each of the integers in the list doubled
# Iha funsaun ida ne'e foti lista ida hanesan input
# Fo fali lista ho  integer sira double fali
def double_integers_in_list(input_list):
    '''
    lista = []
    for item in input_list:
        if type(item) == int:
            lista.append(item * 2)
        else:
            lista.append(item)
    return lista
    '''
    lista_foun = []
    for valor in input_list:
        if type(valor) == int:
            lista_foun += [2 * valor]  # aumenta ba lista hanesan 'append'
        else:
            lista_foun += [valor]
    return lista_foun


def test_double_integers_in_list():
    assert double_integers_in_list([1, 1, 3]) == [2, 2, 6]
    assert double_integers_in_list([2, 4, 8, 16, 32]) == [4, 8, 16, 32, 64]
    assert double_integers_in_list([2, 4, 'blah']) == [4, 8, 'blah']
