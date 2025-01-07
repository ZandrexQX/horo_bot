from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..horo_dict import zodiacs


def get_horo_kb():
    kb = InlineKeyboardBuilder()
    
    for key, value in zodiacs.items():
        kb.button(text=value, callback_data=key)
    
    kb.adjust(2)
    return kb.as_markup()