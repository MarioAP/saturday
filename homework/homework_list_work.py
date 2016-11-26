'''
def method_a(arg):
    some_data = method_b(arg)

def method_b(arg):
    return some_data

def method_a(arg):

    def method_b(arg):
        return some_data

    some_data = method_b
'''

# This function returns a list containing all the words in a string
# funsaun nebee fo fali lista. Iha lista laran hout liafuan iha string {text} laran
def get_words(text):
    return text.split()


# Write a function that finds the number of words with less than three letters in a string
# Hakerek funsaun nebee hetan konta liafuan nebee la iha letra liu rua iha string nia laran
def count_words_smaller_than_three(text):
    count = 0
    words = get_words(text)
    for word in words:
        if len(word) < 3:
            count += 1
    return count


def test_count_words_smaller_than_three():
    assert count_words_smaller_than_three("Hau gosta haan tempe ho ai manas no hemu kafe moruk") == 3
    assert count_words_smaller_than_three("Fila fali mai mai haksolok o") == 1
    assert count_words_smaller_than_three("I went to the shops and I bought a large box of biscuits") == 5
    assert count_words_smaller_than_three("Coding python is lots of fun") == 2


# Write a function that finds the number of words that contain the letter 'a'
# Hakerek funsaun nebee hetan konta liafuan nebee uza letra 'a'
def count_words_containing_a(text):
    count = 0
    letter = 'a'
    for char in text:
        if char == letter:
            count += 1
    return count


def test_count_words_containing_a():
    assert count_words_containing_a("Fila fali mai mai haksolok o") == 5
    assert count_words_containing_a("I went to the shops and I bought a large box of biscuits") == 3
    assert count_words_containing_a("Coding python is lots of fun") == 0


# Write a function that finds the number of words that contain the letter 'a' and have three letters or less
# Hakerek funsaun nebee hetan konta liafuan nebee uza letra 'a' no iha letra menus liu ka hanesan tolu
def count_words_containing_a_and_no_more_than_3_letters(text):
    count = 0
    letter = 'a'
    words = get_words(text)
    for word in words:
        if len(word) <= 3:
            for char in word:
                if char == letter:
                    count += 1
    return count


def test_count_words_containing_a_and_no_more_than_3_letters():
    assert count_words_containing_a_and_no_more_than_3_letters("Fila fali mai mai haksolok o") == 2
    assert count_words_containing_a_and_no_more_than_3_letters("I went to the shops and I bought a large box of biscuits") == 2
    assert count_words_containing_a_and_no_more_than_3_letters("Coding python is lots of fun") == 0


# Write a function that finds the number of letters in a string, do not count spaces!
# Hakerek funsaun nebee fo fali konta letra iha text laran, la konta spasi!
def count_total_letters(text):
    # return len(text) - text.count(' ')
    # return len([letter for letter in text if letter != space])
    space = " "
    count = 0
    for letter in text:
        if letter is not space:
            count += 1
    return count


def test_count_total_letters():
    assert count_total_letters("Fila fali mai mai haksolok o") == 23
    assert count_total_letters("I went to the shops and I bought a large box of biscuits") == 44
    assert count_total_letters("Coding python is lots of fun") == 23
