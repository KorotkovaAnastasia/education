import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями"""
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Test USD transaction",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Test EUR transaction",
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Another USD transaction",
        },
        {
            "id": 4,
            "operationAmount": {"amount": "400.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Test RUB transaction",
        },
    ]


@pytest.fixture
def empty_transactions():
    """Фикстура с пустым списком транзакций"""
    return []


@pytest.fixture
def transactions_without_currency():
    """Фикстура с транзакциями без валюты"""
    return [
        {"id": 1, "description": "No operationAmount"},
        {"id": 2, "operationAmount": {"amount": "100.00"}},
        {"id": 3, "operationAmount": {"amount": "200.00", "currency": {}}},
    ]


class TestFilterByCurrency:
    """Тесты для функции filter_by_currency."""

    def test_filter_usd_transactions(self, sample_transactions):
        """Тест фильтрации USD транзакций"""
        usd_transactions = list(filter_by_currency(sample_transactions, "USD"))

        assert len(usd_transactions) == 2
        assert all(txn["operationAmount"]["currency"]["code"] == "USD" for txn in usd_transactions)
        assert {txn["id"] for txn in usd_transactions} == {1, 3}

    def test_filter_eur_transactions(self, sample_transactions):
        """Тест фильтрации EUR транзакций"""
        eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))

        assert len(eur_transactions) == 1
        assert eur_transactions[0]["id"] == 2
        assert eur_transactions[0]["operationAmount"]["currency"]["code"] == "EUR"

    def test_filter_nonexistent_currency(self, sample_transactions):
        """Тест фильтрации несуществующей валюты"""
        gbp_transactions = list(filter_by_currency(sample_transactions, "GBP"))
        assert len(gbp_transactions) == 0

    def test_empty_transactions_list(self, empty_transactions):
        """Тест с пустым списком транзакций"""
        result = list(filter_by_currency(empty_transactions, "USD"))
        assert len(result) == 0

    def test_transactions_without_currency(self, transactions_without_currency):
        """Тест с транзакциями без инф о валюте"""
        result = list(filter_by_currency(transactions_without_currency, "USD"))
        assert len(result) == 0

    def test_generator_behavior(self, sample_transactions):
        """Тест поведения генератора"""
        generator = filter_by_currency(sample_transactions, "USD")

        # Первый вызов
        first = next(generator)
        assert first["id"] == 1

        # Второй
        second = next(generator)
        assert second["id"] == 3

        # Дальше StopIteration
        with pytest.raises(StopIteration):
            next(generator)


class TestTransactionDescriptions:
    """Тесты для функции transaction_descriptions"""

    def test_descriptions_extraction(self, sample_transactions):
        """Тест извлечения описаний транзакций"""
        descriptions = list(transaction_descriptions(sample_transactions))

        expected = ["Test USD transaction", "Test EUR transaction", "Another USD transaction", "Test RUB transaction"]

        assert descriptions == expected

    def test_empty_transactions(self, empty_transactions):
        """Тест с пустым списком транзакций"""
        descriptions = list(transaction_descriptions(empty_transactions))
        assert descriptions == []

    def test_transactions_without_description(self):
        """Тест с транзакциями без описания"""
        transactions = [
            {"id": 1, "operationAmount": {"amount": "100.00"}},
            {"id": 2, "description": "Has description"},
            {"id": 3},  # Нет описания
        ]

        descriptions = list(transaction_descriptions(transactions))
        assert descriptions == ["", "Has description", ""]

    def test_generator_behavior(self, sample_transactions):
        """Тест поведения генератора описаний"""
        generator = transaction_descriptions(sample_transactions)

        assert next(generator) == "Test USD transaction"
        assert next(generator) == "Test EUR transaction"
        assert next(generator) == "Another USD transaction"
        assert next(generator) == "Test RUB transaction"

        with pytest.raises(StopIteration):
            next(generator)


class TestCardNumberGenerator:
    """Тесты для генератора номеров карт"""

    @pytest.mark.parametrize("start,end,expected_count", [(1, 5, 5), (9995, 10000, 6), (1, 1, 1), (123, 123, 1)])
    def test_range_generation(self, start, end, expected_count):
        """Тест генерации в различных диапазонах"""
        numbers = list(card_number_generator(start, end))

        assert len(numbers) == expected_count
        assert all(len(number.replace(" ", "")) == 16 for number in numbers)

    @pytest.mark.parametrize(
        "number,expected_format",
        [
            (1, "0000 0000 0000 0001"),
            (9999, "0000 0000 0000 9999"),
            (1234567890123456, "1234 5678 9012 3456"),
            (9999999999999999, "9999 9999 9999 9999"),
        ],
    )
    def test_number_formatting(self, number, expected_format):
        """Тест форматирования отдельных номеров"""
        result = list(card_number_generator(number, number))
        assert result[0] == expected_format

    def test_small_range(self):
        """Тест небольшого диапазона"""
        numbers = list(card_number_generator(1, 3))

        expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]

        assert numbers == expected

    def test_large_range_first_elements(self):
        """Тест получения первых элементов большого диапазона"""
        generator = card_number_generator(1, 1000000)

        # Проверяем только первые несколько элементов
        assert next(generator) == "0000 0000 0000 0001"
        assert next(generator) == "0000 0000 0000 0002"
        assert next(generator) == "0000 0000 0000 0003"

    def test_edge_cases(self):
        """Тест крайних случаев."""
        # Мин значение
        min_result = list(card_number_generator(1, 1))
        assert min_result == ["0000 0000 0000 0001"]

        # Макс значение
        max_result = list(card_number_generator(9999999999999999, 9999999999999999))
        assert max_result == ["9999 9999 9999 9999"]

    def test_invalid_range(self):
        """Тест обработки неверного диапазона"""
        # start > end
        result = list(card_number_generator(5, 1))
        assert result == []  # Пустой диапазон

    def test_zero_start(self):
        """Тест начала с 0"""
        result = list(card_number_generator(0, 2))
        expected = ["0000 0000 0000 0000", "0000 0000 0000 0001", "0000 0000 0000 0002"]
        assert result == expected
