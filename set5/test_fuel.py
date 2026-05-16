from fuel import gauge, convert
import pytest

def test_int() :
    with pytest.raises(ValueError) :
        convert("cat/dog")

def test_ynotgreater() :
    with pytest.raises(ValueError) :
        convert("5/4")

def test_conzeroerror() :
    with pytest.raises(ValueError) :
        convert("5/0")

def test_gauge() :
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(10) == "10%"