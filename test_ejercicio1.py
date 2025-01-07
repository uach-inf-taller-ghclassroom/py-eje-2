import pytest
from ejercicio1 import *

'''@pytest.mark.parametrize(argnames, argvalues): 
call a test function multiple times passing in different arguments in turn. 
argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. 
Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.
see https://docs.pytest.org/en/stable/how-to/parametrize.html for more info and examples.
'''

@pytest.mark.parametrize("num1, num2, num3, resultado", [
    (5, 8, 12, 8.333333333333334),
    (0, 0, 0, 0.0),
    (10, 20, 30, 20.0),
    (-5, 5, 15, 5.0)
])
def test_calcular_promedio_correctos(num1, num2, num3, resultado):
    assert calcular_promedio(num1, num2, num3) == resultado

@pytest.mark.parametrize("num1, num2, num3, resultado", [
    (5, 8, "n", ValueError),
    (0, "n", 0,  ValueError),
    ("$", 20, 30,  ValueError),
    ("4", "5", "15", ValueError)
])
def test_calcular_promedio_incorrectos(num1, num2, num3, resultado):
    with pytest.raises(ValueError):
        assert calcular_promedio(num1, num2, num3) == resultado