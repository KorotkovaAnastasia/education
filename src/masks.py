def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(card_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    return f"**{card_number[-4:]}"
