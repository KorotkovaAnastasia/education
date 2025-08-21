# Домашняя работа № 10.2

## Описание проекта

Создание удобного инструмента для:
- Фильтрации транзакций по статусу
- Сортировки транзакций по дате
- Подготовки данных для дальнейшего анализа

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/KorotkovaAnastasia/education.git
```

2. Установите зависимости:
```
poetry install
```

## Использование:

1. Импорт функций:
```
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
```
2. Примеры использования:
```
# Маскирование номера карты
masked_card = get_mask_card_number("1234567812345678")
print(masked_card)  # "1234 56** **** 5678"

# Маскирование номера счета
masked_account = get_mask_account("1234567890")
print(masked_account)  # "**7890"

# Фильтрация транзакций по статусу
transactions = [...]
executed_transactions = filter_by_state(transactions, "EXECUTED")

# Сортировка транзакций по дате
sorted_transactions = sort_by_date(transactions, reverse=True)
```

## Тестирование:
Запуск тестов:
```
# Все тесты
pytest -v

# С HTML отчетом о покрытии
pytest --cov=src --cov-report=html
```
Покрытие тестами:

- Общее покрытие: 92%
- Модуль masks.py: 100%
- Модуль widget.py: 95%
- Модуль processing.py: 88%

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

## Документация


### Основные материалы
- [API Reference](docs/API.md) - полное описание всех функций и их параметров
- [Data Format Standard](docs/DATA_FORMAT.md) - требования к формату входных и выходных данных
- [Quick Start Guide](examples/quickstart.md) - быстрое начало работы за 5 минут
- [Примеры использования](examples/) - готовые примеры кода для разных сценариев