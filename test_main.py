import main
def test_add():
    test = main.add(10,5)
    assert test == 12
def test_sub():
    test = main.diff(10,5)
    assert test == 5
def test_mult():
    test = main.mult(10,5)
    assert test == 50
def test_div():
    test = main.div(10,5)
    assert test == 2
def test_mod():
    test = main.mod(10,5)
    assert test == 0