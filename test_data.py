from math_func import StudentDB
import pytest

#################################### fixture ####################################


@pytest.fixture(scope='module')
def db():
    print('---------- setup ----------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('---------- teardown ----------')
    db.close()


def test_himanshu_data(db):
    himanshu_data = db.get_data('Himanshu')
    assert himanshu_data['id'] == 1
    assert himanshu_data['name'] == "Himanshu"
    assert himanshu_data['result'] == "pass"


def test_sushil_data(db):
    sushil_data = db.get_data('Sushil')
    assert sushil_data['id'] == 2
    assert sushil_data['name'] == "Sushil"
    assert sushil_data['result'] == "fail"


#################################### setup,teardown ####################################


# db = None

# Setup method
# def setup_module(module):
#     print('---------- setup ----------')
#     global db
#     db = StudentDB()
#     db.connect('data.json')

# Teardown method
# def teardown_module(module):
#     print('---------- teardown ----------')
#     db.close()


# def test_himanshu_data():
#     himanshu_data = db.get_data('Himanshu')
#     assert himanshu_data['id'] == 1
#     assert himanshu_data['name'] == "Himanshu"
#     assert himanshu_data['result'] == "pass"


# def test_sushil_data():
#     sushil_data = db.get_data('Sushil')
#     assert sushil_data['id'] == 2
#     assert sushil_data['name'] == "Sushil"
#     assert sushil_data['result'] == "fail"
