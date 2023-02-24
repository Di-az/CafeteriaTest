# from main import add_drink
from main import *

def test_names():
    # Incorrect naming
    assert add_drink('Y, 1, 2, 3') == 'Incorrect name: Name too short'
    assert add_drink('Super Coca Cola Ultra, 1, 2, 3') == 'Incorrect name: Name too long'

    # Correct naming
    assert add_drink('xy, 1, 2, 3') == 'Drink has been added'
    assert add_drink('La Mega Coca Cola I, 1, 2, 3') == 'Drink has been added'




def test_sizes():
    # Correct sizing
    assert add_drink('Drink, 1') == 'Drink has been added'
    assert add_drink('Drink, 1, 48') == 'Drink has been added'
    assert add_drink('Drink, 1, 2, 3') == 'Drink has been added'
    assert add_drink('Drink, 1, 2, 3, 4, 5') == 'Drink has been added'
    

    assert add_drink('Coca cola, 0') == 'Incorrect size: Size too small'
    assert add_drink('Coca cola, 10.65') == 'Incorrect size: Decimal number in size'
    assert add_drink('Coca cola, 50') == 'Incorrect size: Size too big'
    assert add_drink('Coca cola, 10, 1, 8') == 'Incorrect size: Not in ascending order'
    assert add_drink('Coca cola, 5, 10, 15, 20, 25, 30') == 'Incorrect size: Too many sizes'


def test_format():
    assert add_drink('') == 'Incorrect format: No name found'
    assert add_drink('Coca cola') == 'Incorrect format: No sizes provided'
    assert add_drink('Coca123, 1, 2, 3') == 'Incorrect format: Non letter in name'
    assert add_drink('Coca-Cola, 1, 2, 3') == 'Incorrect format: Non letter in name'
    assert add_drink('Coca cola 1 2 3') == 'Incorrect format: No sizes provided'
    assert add_drink('Coca cola, 1 0') == 'Incorrect format: Space in size'
    assert add_drink('Coca, cola, 10') == 'Incorrect format: Letters in size'
