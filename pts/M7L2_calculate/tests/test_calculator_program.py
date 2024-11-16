import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2
    assert calculate(-1, -1, '+') == -2  # Тест на сложение отрицательных чисел
    assert calculate(0, 5, '+') == 5      # Тест на сложение с нулем

def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2
    assert calculate(-1, -1, '-') == 0   # Тест на вычитание отрицательных чисел
    assert calculate(0, 5, '-') == -5     # Тест на вычитание с нулем

def test_calculate_multiplication():
    assert calculate(3, 4, '*') == 12
    assert calculate(-2, 3, '*') == -6    # Тест на умножение с отрицательным числом
    assert calculate(0, 5, '*') == 0       # Тест на умножение с нулем
    assert calculate(1000000, 1000000, '*') == 1000000000000  # Тест на умножение больших чисел

def test_calculate_division():
    assert calculate(8, 2, '/') == 4
    assert calculate(5, 0, '/') == "Ошибка: деление на ноль."  # Тест на деление на ноль
    assert calculate(-6, -2, '/') == 3   # Тест на деление отрицательных чисел
    assert calculate(1000000000, 1000000000, '/') == 1  # Тест на деление больших чисел

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."
