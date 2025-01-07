from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from functools import partial

from ..utils.api_horo import get_horo
from ..horo_dict import zodiacs


router_horo = Router()

async def get_answer_horo(call: CallbackQuery, key: str):
    horo_text = get_horo(key)
    photo = FSInputFile(f'./core/images/{key}.jpg')
    await call.message.answer_photo(photo=photo, caption=horo_text)
    await call.answer()


for key, _ in zodiacs.items():
    # Создаем частичную функцию с фиксированным значением key
    callback_function = partial(get_answer_horo, key=key)
    
    # Привязываем обработчик к конкретному ключу
    router_horo.callback_query(F.data == key)(callback_function)