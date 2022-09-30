from lib import fun, fib


def test_fun_returns_test_string():
    result = fun('Test')
    val = 'Test'
    assert result == val


def test_fun_returns_10_int():
    result = fun(10)
    val = 20
    assert result == val


def test_fib_return_55_when_receive_10():
    result = fib(10)
    val = 55
    assert result == val
