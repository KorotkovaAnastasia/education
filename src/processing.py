from datetime import datetime


def filter_by_state(transaction: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    принимает список словарей и опционально значение для ключа state.
    """
    return [item for item in transaction if item.get("state") == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки.
    """
    return sorted(transactions, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S"), reverse=reverse)
