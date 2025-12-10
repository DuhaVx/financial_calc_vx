"""
Тесты для финансового калькулятора.
"""
import pytest
from financial_calc.calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax,
)


class TestCalculateSimpleInterest:
    """Тесты для функции calculate_simple_interest"""
    
    def test_correct_calculation_1(self):
        """Проверка правильности расчёта (пример 1)"""
        result = calculate_simple_interest(1000, 5, 2)
        expected = 100.0  # 1000 * 5 * 2 / 100 = 100
        assert result == expected
    
    def test_correct_calculation_2(self):
        """Проверка правильности расчёта (пример 2)"""
        result = calculate_simple_interest(500, 10, 3)
        expected = 150.0  # 500 * 10 * 3 / 100 = 150
        assert result == expected
    
    def test_zero_principal(self):
        """Проверка работы с нулевой основной суммой"""
        result = calculate_simple_interest(0, 5, 2)
        assert result == 0.0
    
    def test_zero_rate(self):
        """Проверка работы с нулевой процентной ставкой"""
        result = calculate_simple_interest(1000, 0, 2)
        assert result == 0.0
    
    def test_zero_time(self):
        """Проверка работы с нулевым временем"""
        result = calculate_simple_interest(1000, 5, 0)
        assert result == 0.0
    
    def test_negative_principal(self):
        """Проверка вызова ValueError при отрицательной основной сумме"""
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(-1000, 5, 2)
    
    def test_negative_rate(self):
        """Проверка вызова ValueError при отрицательной процентной ставке"""
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, -5, 2)
    
    def test_negative_time(self):
        """Проверка вызова ValueError при отрицательном времени"""
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, 5, -2)


class TestCalculateCompoundInterest:
    """Тесты для функции calculate_compound_interest"""
    
    def test_correct_calculation_annual(self):
        """Проверка правильности расчёта (ежегодное начисление)"""
        result = calculate_compound_interest(1000, 5, 2, n=1)
        expected = 102.5  # 1000 * (1 + 0.05)^2 - 1000 = 102.5
        assert abs(result - expected) < 0.01
    
    def test_correct_calculation_monthly(self):
        """Проверка правильности расчёта (ежемесячное начисление)"""
        result = calculate_compound_interest(1000, 12, 1, n=12)
        expected = 126.83  # 1000 * (1 + 0.12/12)^(12*1) - 1000 ≈ 126.83
        assert abs(result - expected) < 0.01
    
    def test_zero_principal(self):
        """Проверка работы с нулевой основной суммой"""
        result = calculate_compound_interest(0, 5, 2)
        assert result == 0.0
    
    def test_zero_rate(self):
        """Проверка работы с нулевой процентной ставкой"""
        result = calculate_compound_interest(1000, 0, 2)
        assert result == 0.0
    
    def test_zero_time(self):
        """Проверка работы с нулевым временем"""
        result = calculate_compound_interest(1000, 5, 0)
        assert result == 0.0
    
    def test_negative_principal(self):
        """Проверка вызова ValueError при отрицательной основной сумме"""
        with pytest.raises(ValueError, match="должны быть неотрицательными"):
            calculate_compound_interest(-1000, 5, 2)
    
    def test_negative_rate(self):
        """Проверка вызова ValueError при отрицательной процентной ставке"""
        with pytest.raises(ValueError, match="должны быть неотрицательными"):
            calculate_compound_interest(1000, -5, 2)
    
    def test_negative_time(self):
        """Проверка вызова ValueError при отрицательном времени"""
        with pytest.raises(ValueError, match="должны быть неотрицательными"):
            calculate_compound_interest(1000, 5, -2)
    
    def test_invalid_n_zero(self):
        """Проверка вызова ValueError при n=0"""
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 2, n=0)
    
    def test_invalid_n_negative(self):
        """Проверка вызова ValueError при отрицательном n"""
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 2, n=-1)
    
    def test_invalid_n_float(self):
        """Проверка вызова ValueError при нецелом n"""
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 2, n=1.5)


class TestCalculateTax:
    """Тесты для функции calculate_tax"""
    
    def test_correct_calculation_1(self):
        """Проверка правильности расчёта (пример 1)"""
        result = calculate_tax(1000, 20)
        expected = 200.0  # 1000 * 20 / 100 = 200
        assert result == expected
    
    def test_correct_calculation_2(self):
        """Проверка правильности расчёта (пример 2)"""
        result = calculate_tax(500, 13)
        expected = 65.0  # 500 * 13 / 100 = 65
        assert result == expected
    
    def test_zero_amount(self):
        """Проверка работы с нулевой суммой"""
        result = calculate_tax(0, 20)
        assert result == 0.0
    
    def test_zero_tax_rate(self):
        """Проверка работы с нулевой налоговой ставкой"""
        result = calculate_tax(1000, 0)
        assert result == 0.0
    
    def test_100_tax_rate(self):
        """Проверка работы со 100% налоговой ставкой"""
        result = calculate_tax(1000, 100)
        assert result == 1000.0
    
    def test_negative_amount(self):
        """Проверка вызова ValueError при отрицательной сумме"""
        with pytest.raises(ValueError, match="Сумма amount должна быть неотрицательной"):
            calculate_tax(-1000, 20)
    
    def test_negative_tax_rate(self):
        """Проверка вызова ValueError при отрицательной налоговой ставке"""
        with pytest.raises(ValueError, match="tax_rate должен быть между 0 и 100"):
            calculate_tax(1000, -5)
    
    def test_tax_rate_above_100(self):
        """Проверка вызова ValueError при налоговой ставке выше 100%"""
        with pytest.raises(ValueError, match="tax_rate должен быть между 0 и 100"):
            calculate_tax(1000, 150)