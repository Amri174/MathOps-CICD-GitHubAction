from pytest import approx
from src.math_operations import addition
from src.math_operations import subtraction
from src.math_operations import multiplication
from src.math_operations import division
from src.math_operations import modulus

def test_addition():
    assert addition(2,6) == 8
    assert addition(1,-9) == -8 
    assert addition(-1,9) == 8
    assert addition(-1,-9) == -10 
    
    assert addition(0,0) == 0 
    assert addition(0,-5) == -5
    assert addition(-5,0) == -5

    assert addition(100000,200000) == 300000
    assert addition(-100000,-200000) == -300000

    assert addition(1.5, 2.3) == approx(3.8)
    assert addition(-1.5, -2.3) == approx(-3.8)
    assert addition(1.5, -2.3) == approx(-0.8)
    assert addition(-1.5, 2.3) == approx(0.8)

    assert addition(10, 2.5) == approx(12.5)
    assert addition(-10, 2.5) == approx(-7.5)
    assert addition(10.5, -2) == approx(8.5)

    assert addition(1e-10, 1e-10) == approx(2e-10)
    assert addition(-1e-10, -1e-10) == approx(-2e-10)
    assert addition(1e15, 1e15) == approx(2e15)
    assert addition(-1e15, -1e15) == approx(-2e15)

    assert addition(1e15, -1e15) == 0


def test_subtraction():
    assert subtraction(6,2) == 4
    assert subtraction(1,-9) == 10
    assert subtraction(-1,9) == -10
    assert subtraction(-1,-9) == 8

    assert subtraction(0,0) == 0
    assert subtraction(0,-5) == 5
    assert subtraction(-5,0) == -5

    assert subtraction(300000,200000) == 100000
    assert subtraction(-300000,-200000) == -100000

    assert subtraction(3.8,2.3) == approx(1.5)
    assert subtraction(1.5,-2.3) == approx(3.8)
    assert subtraction(-1.5,2.3) == approx(-3.8)
    assert subtraction(-3.8,-2.3) == approx(-1.5)

    assert subtraction(1e-10, 1e-10) == approx(0.0)
    assert subtraction(-1e-10, -1e-10) == approx(0.0)
    assert subtraction(2e15, 1e15) == approx(1e15)
    assert subtraction(-2e15, -1e15) == approx(-1e15)

    assert subtraction(1e15, -1e15) == approx(2e15)

def test_multiplication():
    assert multiplication(2,6) == 12
    assert multiplication(1,-9) == -9
    assert multiplication(-1,9) == -9
    assert multiplication(-1,-9) == 9

    assert multiplication(0,0) == 0
    assert multiplication(0,-5) == 0
    assert multiplication(-5,0) == 0

    assert multiplication(100000,200000) == 20000000000
    assert multiplication(-100000,-200000) == 20000000000

    assert multiplication(10,2.5) == approx(25.0)
    assert multiplication(-10,2.5) == approx(-25.0)
    assert multiplication(10.5,-2) == approx(-21.0)
    assert multiplication(-15,-2.3) == approx(34.5)

    assert multiplication(1e-10,1e-10) == approx(1e-20)
    assert multiplication(-1e-10,-1e-10) == approx(1e-20)
    assert multiplication(1e15,1e15) == approx(1e30)
    assert multiplication(-1e15,-1e15) == approx(1e30)

    assert multiplication(1e15, -1e15) == approx(-1e30)
    

def test_division():
    assert division(6,2) == 3
    assert division(9,-3) == -3
    assert division(-9,3) == -3
    assert division(-9,-3) == 3

    assert division(0, 5) == 0
    assert division(0, -5) == 0

    assert division(5,1) == 5
    assert division(-5,1) == -5
    assert division(5,-1) == -5
    assert division(-5,-1) == 5

    assert division(10, 2.5) == approx(4.0)
    assert division(-10, 2.5) == approx(-4.0)
    assert division(10.5, -2) == approx(-5.25)
    assert division(-7.5,-2.5) == approx(3.0)
 
    assert division(4, 0.25) == approx(16.0)
    assert division(-4, 0.25) == approx(-16.0)

    assert division(1e-10, 1e-10) == approx(1.0)
    assert division(-1e-10, -1e-10) == approx(1.0)
    assert division(1e15, 1e15) == approx(1.0)
    assert division(-1e15, -1e15) == approx(1.0)

    assert division(1e15, -1e15) == approx(-1.0)

    try:
        division(10, 0)
        raise AssertionError("ZeroDivisionError")
    except ZeroDivisionError:
        pass


def test_modulus():
    assert modulus(10,3) == 1
    assert modulus(9,-4) == -3
    assert modulus(-9,4) == 3
    assert modulus(-9,-4) == -1

    assert modulus(0,5) == 0
    assert modulus(0,-5) == 0
    assert modulus(5,1) == 0
    assert modulus(-5,1) == 0
    assert modulus(5,-1) == 0
    assert modulus(-5,-1) == 0

    assert modulus(7.5, 2.5) == approx(0.0)
    assert modulus(-7.5, -2.5) == approx(-0.0)
    assert modulus(7.5, -2.5) == approx(0.0)
    assert modulus(-7.5, 2.5) == approx(-0.0)

    assert modulus(10, 2.5) == approx(0.0)
    assert modulus(-10, 2.5) == approx(-0.0)
    assert modulus(10.5, -2) == approx(-1.5)

    assert modulus(1e-10, 1e-10) == approx(0.0)
    assert modulus(-1e-10, -1e-10) == approx(-0.0)
    assert modulus(1e15, 1e15) == approx(0.0)
    assert modulus(-1e15, -1e15) == approx(-0.0)

    assert modulus(1e15, -1e14) == approx(-0.0)
    assert modulus(-1e15, 1e14) == approx(-1e13)

    try:
        modulus(10, 0)
        raise AssertionError("ZeroDivisionError")
    except ZeroDivisionError:
        pass
