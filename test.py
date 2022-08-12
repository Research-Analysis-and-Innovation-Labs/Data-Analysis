def checkfunction(x):
    return x**2

def test_checkfunction():
    return checkfunction(2) == 4

def test_checkfunction2():
    return checkfunction(3) == 9

print(test_checkfunction())