
def total_price(price):
    """Функция для расчёта финальной стоимости с учётом комиссий"""

    tax = price * 0.06
    bank_comission = price * 0.02
    author_comission = price * 0.02
    my_comission = price * 0.2

    final_price = price + tax + bank_comission + author_comission + my_comission

    return final_price
