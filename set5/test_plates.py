from plates import is_valid


def test_length():
    assert is_valid("AA58572593") == False


def test_starting2letters():
    assert is_valid("A24244") == False


def test_punc():
    assert is_valid("AB!234") == False


def test_nomiddlenum():
    assert is_valid("AA2A22") == False
