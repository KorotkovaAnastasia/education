from src.masks import get_mask_card_number, get_mask_account


card_number = "1234567890123456"

print(get_mask_card_number(card_number))
print(get_mask_account(card_number))
