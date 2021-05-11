from prettynum import __version__
from prettynum.prettynum import comma, dollar


def test_version():
    assert __version__ == '0.1.0'
    
    
def test_comma():
    assert comma(1000) == "1,000"
    assert comma(1000, 3) == "1,000.000"
    assert comma(1000.0) == "1,000.0"
    assert comma(1000.89, 1) == "1,000.9"
    

def test_dollar():
    assert dollar(1000) == "$1,000"
    assert dollar(1000, 3) == "$1,000.000"
    assert dollar(1000.0) == "$1,000.0"
    assert dollar(1000.89, 1) == "$1,000.9"
