# Домашняя работа № 11.1

## Описание проекта

Создание удобного инструмента для:
- эффективной работы с большими объемами данных транзакций, 
используя возможности Python для обработки данных через генераторы.
- Фильтрации транзакций по статусу и валюте
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

## Использование:

### Основные модули

1. **Импорт функций из существующих модулей:**
```
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
```
2. Импорт функций из нового модуля generators:
```
from generators import filter_by_currency, transaction_descriptions, 
card_number_generator
```
3. Примеры использования:
```
# Маскирование номера карты
masked_card = get_mask_card_number("1234567812345678")
print(masked_card)  # "1234 56** **** 5678"

# Маскирование номера счета
masked_account = get_mask_account("1234567890")
print(masked_account)  # "**7890"
```

## Тестирование:
Запуск тестов:
```
# Все тесты
pytest -v

# С HTML отчетом о покрытии
pytest --cov=src --cov-report=html
```
Покрытие тестами - 100%

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

## Документация


### Основные материалы
- [API Reference](docs/API.md) - полное описание всех функций и их параметров
- [Data Format Standard](docs/DATA_FORMAT.md) - требования к формату входных и выходных данных
- [Quick Start Guide](examples/quickstart.md) - быстрое начало работы за 5 минут
- [Примеры использования](examples/) - готовые примеры кода для разных сценариев