# look in homework_list_work.py for a function that splits a string into words
# haree homework_list_work.py ba funsaun fo fali lista liafuan iha string laran
def get_words(text):
    return text.split()


def filter_words_containing_a(text):
    # return all words in <text> containin the letter a
    # fo fali liafuan iha <text> laran nebee uza letra a
    # Uza filter! Uza lambda!
    #import pudb; pudb.set_trace()
    words = get_words(text)
    #a_words =[word for word in words if 'a' in word]
    a_words = filter(lambda word: 'a' in word, words)
    return a_words


def test_filter_words_containing_a():
    words = filter_words_containing_a("Hello world")
    # check the list has the correct length
    assert len(words) == 0
    # check there are no words that do not contain 'a'
    assert not filter(lambda w: 'a' not in w, words)

    words = filter_words_containing_a("ano mario ony nando niko anders peter")
    # check the list has the correct length
    assert len(words) == 4
    # check there are no words that do not contain 'a'
    assert not filter(lambda w: 'a' not in w, words)

    words = filter_words_containing_a("hau gosta hemu kafe no haan tempe")
    # check the list has the correct length
    assert len(words) == 4
    # check there are no words that do not contain 'a'
    assert not filter(lambda w: 'a' not in w, words)


def get_hello(name):
    # return a string that says hello to <name>
    # fo fali string dehan hello ba <name>
    return "hello" + name


def check_hello(hello, name):
    # checks a hello is valid, contains name, contains hello
    # check <hello> diak, 'Hello' iha <hello> laran no <name> iha <hello> laran
    # Ita la presiza troka funsaun nebee!
    assert name in hello
    assert "Hello".lower() in hello.lower()


def test_get_hello():
    name = "Peter"
    hello = get_hello(name)
    check_hello(hello, name)
    name = "Mario"
    hello = get_hello(name)
    check_hello(hello, name)
    name = "Nando"
    hello = get_hello(name)
    check_hello(hello, name)


def get_all_hellos(names):
    # return a list of hellos, one for each name in <names>
    # fo fali lista hellos, uza hotu name iha <names> laran
    # Uza map, bele uza lambda mos bele uza funsaun get_hello iha leten
    pass


def test_get_all_hellos():
    def check_all_hellos(names, hellos):
        # checks all <hellos> are valid for <names>
        # check hotu <hellos> diak ba <names>
        # Ita la presiza troka funsaun nebee!
        assert len(hellos) == len(names)
        for name, hello in zip(names, hellos):
            check_hello(hello, name)

    names = ['Anders', 'Peter']
    hellos = get_all_hellos(names)
    check_all_hellos(names, hellos)

    names = ['Ony', 'Niko', 'Ano']
    hellos = get_all_hellos(names)
    check_all_hellos(names, hellos)
