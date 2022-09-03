class TestClass:

    value = 0

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x= "hello"
        assert hasattr(x, "hello")

    def test_three(self):
        self.value = 1
        assert self.value == 1

    def test_four(self):
        assert self.value == 1

    