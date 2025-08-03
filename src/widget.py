from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    if "счет" in account_card.lower():
        if account_card[-20:].isdigit():
            return f"счет {get_mask_account(account_card[-20:])}"
    else:
        if account_card[-16:].isdigit():
            return f"{account_card[:-16]} {get_mask_card_number(account_card[-16:])}"


def get_date(time_card: str) -> str:
    return time_card[8:10] + "." + time_card[5:7] + "." + time_card[:4]
