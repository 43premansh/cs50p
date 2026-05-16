from bank import value


def test_1() :
    assert value("hello, how are you ?") == 0

def test_2() :
    assert value("hey, how are you ?") == 20

def test_3() :
    assert value("OLA, how are you ?") == 100