"""
Финансовый калькулятор с функциями для расчёта:
- простых процентов
- сложных процентов
- налога
"""


def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Рассчитывает простые проценты.

    Args:
        principal: основная сумма (неотрицательная)
        rate: процентная ставка (неотрицательная)
        time: время в годах (неотрицательное)

    Returns:
        Сумма простых процентов

    Raises:
        ValueError: если любой из аргументов отрицательный
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    
    return principal * rate * time / 100


def calculate_compound_interest(
    principal: float, 
    rate: float, 
    time: float, 
    n: int = 1
) -> float:
    """
    Рассчитывает сложные проценты.

    Args:
        principal: основная сумма (неотрицательная)
        rate: процентная ставка (неотрицательная)
        time: время в годах (неотрицательное)
        n: количество начислений процентов в год (целое положительное)

    Returns:
        Сумма сложных процентов

    Raises:
        ValueError: при некорректных аргументах
    """
    # Проверка на отрицательные значения
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы principal, rate и time должны быть неотрицательными")
    
    # Проверка, что n - целое положительное число
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть целым положительным числом")
    
    # Рассчитываем сложные проценты
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    return amount - principal  # Возвращаем только проценты


def calculate_tax(amount: float, tax_rate: float) -> float:
    """
    Рассчитывает сумму налога.

    Args:
        amount: сумма, с которой начисляется налог (неотрицательная)
        tax_rate: процентная ставка налога (от 0 до 100)

    Returns:
        Сумма налога

    Raises:
        ValueError: если tax_rate не между 0 и 100 или amount отрицательный
    """
    if amount < 0:
        raise ValueError("Сумма amount должна быть неотрицательной")
    
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("tax_rate должен быть между 0 и 100")
    
    return amount * tax_rate / 100