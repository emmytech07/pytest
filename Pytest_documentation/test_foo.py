class Foo:
    def __init__(self, val):
        self.val = val

    def __eg__ (self, other):
        return self.val == other.val
def test_comapare():
    f1 =Foo(1)
    f2 = Foo(2)
    assert f1 == f2