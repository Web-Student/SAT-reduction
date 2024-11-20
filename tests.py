from Verify import *
from SAT import *
 
def test_canvas_test_1():
    testinput = ['a;b;c', '-a;b;-c', '-d;-b', '-a;c', '-b;a']
    expected = {'a':1.0,'b':1.0,'c':1.0,'d':0.0}
    actual = FindSat(testinput)
    assert expected == actual

def test_tautology():
    testinput = ['a;b;c;d;e', 'a','b','c','d','e']
    expected = {'a':1.0,'b':1.0,'c':1.0,'d':1.0, 'e':1.0}
    actual = FindSat(testinput)
    assert expected == actual
 
def test_contradiction():
    try:
        testinput = ['a;b;c;d;e', '-a;-b;-c;-d;-e']
        expected = {'a':0.0,'b':0.0,'c':0.0,'d':0.0, 'e':0.0}
        actual = FindSat(testinput)
        assert expected == actual
    except:
        assert True