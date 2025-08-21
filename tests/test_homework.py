import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processering import filter_by_state, sort_by_date


# Фикстуры для тестовых данных
@pytest.fixture
def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2023-01-15T12:30:45", "amount": "100.00"},
        {"state": "PENDING", "date": "2023-01-14T11:20:30", "amount": "200.00"},
        {"state": "EXECUTED", "date": "2023-01-16T10:10:15", "amount": "300.00"},
        {"state": "CANCELED", "date": "2023-01-13T09:05:00", "amount": "400.00"},
    ]


@pytest.fixture
def transactions_with_same_date():
    return [
        {"date": "2023-01-15T12:30:45"},
        {"date": "2023-01-15T12:30:45"},
        {"date": "2023-01-10T10:00:00"},
    ]


# Тесты для get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "1234",
        "",
        "abc",
    ],
)
def test_get_mask_card_number_short_or_invalid(card_number):
    result = get_mask_card_number(card_number)
    assert isinstance(result, str)


# Тесты для get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567890", "**7890"),
        ("12345678", "**5678"),
    ],
)
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number",
    [
        "1234",
        "",
    ],
)
def test_get_mask_account_short_or_empty(account_number):
    result = get_mask_account(account_number)
    assert isinstance(result, str)


# Тесты для filter_by_state
@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("PENDING", 1),
        ("CANCELED", 1),
        ("INVALID", 0),
    ],
)
def test_filter_by_state(sample_transactions, state, expected_count):
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected_count


# Тесты для sort_by_date
@pytest.mark.parametrize(
    "reverse, expected_dates",
    [
        (True, ["2023-01-16T10:10:15", "2023-01-15T12:30:45", "2023-01-14T11:20:30", "2023-01-13T09:05:00"]),
        (False, ["2023-01-13T09:05:00", "2023-01-14T11:20:30", "2023-01-15T12:30:45", "2023-01-16T10:10:15"]),
    ],
)
def test_sort_by_date(sample_transactions, reverse, expected_dates):
    result = sort_by_date(sample_transactions, reverse=reverse)
    assert [item["date"] for item in result] == expected_dates


# Тесты для mask_account_card
def test_mask_account_card_returns_string():
    # Проверяем, что функция возвращает строку (а не None)
    result = mask_account_card("Счет 12345678901234567890")
    assert isinstance(result, str)
    result = mask_account_card("Visa 1234567812345678")
    assert isinstance(result, str)


# Тесты для get_date
@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2023-01-15T12:30:45", "15.01.2023"),
        ("2022-12-31T23:59:59", "31.12.2022"),
    ],
)
def test_get_date_valid(input_date, expected):
    result = get_date(input_date)
    assert result == expected


@pytest.mark.parametrize(
    "short_date",
    [
        "2023-01",
        "2023",
        "",
    ],
)
def test_get_date_short_or_empty(short_date):
    result = get_date(short_date)
    assert isinstance(result, str)


# Тесты на обработку исключений
def test_functions_do_not_crash():
    """Проверяем, что функции не падают с исключениями"""
    test_data = [
        ("get_mask_card_number", "1234"),
        ("get_mask_account", "1234"),
        ("get_date", "2023-01-15"),
    ]

    for func_name, data in test_data:
        try:
            if func_name == "get_mask_card_number":
                get_mask_card_number(data)
            elif func_name == "get_mask_account":
                get_mask_account(data)
            elif func_name == "get_date":
                get_date(data)
        except Exception as e:
            pytest.fail(f"Функция {func_name} вызвала исключение: {e}")
