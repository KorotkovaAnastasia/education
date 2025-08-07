def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    принимает список словарей и опционально значение для ключа state.

    :param data: Список словарей с данными.
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [item for item in data if item.get("state") == state]

