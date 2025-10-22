from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по валюте операции.

    Args:
        transactions: список словарей с транзакциями
        currency_code: код валюты для фильтрации (например, "USD")

    Returns:
        итератор, который выдает транзакции с заданной валютой
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор описаний операций из списка транзакций.

    Args:
        transactions: список словарей с транзакциями

    Returns:
        итератор, который выдает описания операций
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: начальный номер карты (целое число от 1 до 9999999999999999)
        end: конечный номер карты (целое число от start до 9999999999999999)

    Returns:
        итератор, который выдает номера карт в заданном диапазоне
    """
    for number in range(start, end + 1):
        # Преобразуем число в строку и дополняем нулями до 16 цифр
        card_str = str(number).zfill(16)

        # Форматируем в группы по 4 цифры
        formatted_card = " ".join([card_str[i : i + 4] for i in range(0, 16, 4)])

        yield formatted_card
