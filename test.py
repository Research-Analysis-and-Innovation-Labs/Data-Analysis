def checkfunction(x):
    return x**2

def test_checkfunction():
    return checkfunction(2) == 4

def test_checkfunction2():
    return checkfunction(3) == 9

def test_checkfunction3():
    return checkfunction(4) == 16

def test_checkfunction4():
    return checkfunction(5) == 25

print(test_checkfunction())
print(test_checkfunction2())
print(test_checkfunction3())
print(test_checkfunction4())
