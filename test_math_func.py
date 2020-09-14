import math_func
import pytest
import sys

# get detail about test case- add -v at the end like this 👉 py.test -v (pytest -v)
# run all test cases 👉 py.test(it will choose files which starts with test)
# command for running particular file from terminal 👉 pytest test_math_func.py
# command for running particular function from terminal 👉 pytest test_math_func.py::test_add
# it will run the testcases which contains add keyword or string 👉  pytest -v -k "add"
# you can use or operator as well here like this 👉 pytest -v -k "add or string"
# you can use end operator as well here like this 👉 pytest -v -k "add and string"
# selectin marker to run the test cases 👉 pytest -v -m number
# Whenever first failure occure after that test execution will stop 👉 pytest -v -x
# it will not print tech brace in terminal 👉 pytest -v -x --tb=no
# whenever failure number will cross limit of maxfail 👉 pytest -v --maxfail=2
# show skip message in terminal 👉 pytest -v -rsx
# show only important info nothing else in terminal 👉 pytest -v -q

@pytest.mark.number
# @pytest.mark.skip(reason="do not run number add test") #👈 for skipping particular function
# @pytest.mark.skipif(sys.version_info > (3, 3), reason="do not run number add test") #👈 for skip for perticular condition

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    # print(math_func.add(7, 3), '--------------------') #log print in terminal as well 👉 pytest -v -s

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result

@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result