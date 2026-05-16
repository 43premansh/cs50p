import set2.twttr.twttr as twttr


def test_strs():
    assert twttr.shorten("vowel") == "vwl"
    assert twttr.shorten("bigger") == "bggr"


def test_numbers():
    assert twttr.shorten("big hero 6") == "bg hr 6"
    assert twttr.shorten("sam gal on 7") == "sm gl n 7"
