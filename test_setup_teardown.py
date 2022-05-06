def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")


def test_case1():
    print("case1")


def test_case2():
    print("case2")


def setup_function():
    print("setup function")


def teardown_function():
    print("teardown function")


class TestDemo:

    def setup_class(self):
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")
