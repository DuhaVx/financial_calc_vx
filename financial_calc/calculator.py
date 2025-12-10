"""
Финансовый калькулятор с функциями для расчёта:
- простых процентов
- сложных процентов
- налога
"""


def calculate_simple_interest(principal: float, rate: float, time: float) -> float:

    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    
    return principal * rate * time / 100


def calculate_compound_interest(
    principal: float, 
    rate: float, 
    time: float, 
    n: int = 1
) -> float:
    
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы principal, rate и time должны быть неотрицательными")

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть целым положительным числом")
    

    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    return amount - principal  


def calculate_tax(amount: float, tax_rate: float) -> float:

    if amount < 0:
        raise ValueError("Сумма amount должна быть неотрицательной")
    
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("tax_rate должен быть между 0 и 100")
    
    return amount * tax_rate / 100
