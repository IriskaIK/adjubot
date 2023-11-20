import random
from aiogram import types

from aiogram.filters.command import Command

import re
from aiogram.types import FSInputFile


from settings.bot_init import dp, bot




array_of_adjuba = [
    'Аджуба',
    'Аджумамба',
    'Абуба',
    'Абубей',
    'Аджобус',
    'Аджибуда',
    'Абдула',
    'Джу-Джу',
    'Аджубас',
    'Аджисука',
    'Адженга',
    'Аджика',
    'Абобус',
    'Аджесукаблятьзаїбалавже',
    'Аджумогус',
    'Аджубіба',
    'Аджубімба',
    'Аджумен',
    'Аджибумбамбам',
    'Аджусучка',
    'Аджир',
    'Аджимеба',
    'Абдула',
    'Аджела',
    'Аджумба',
    'Аджинджура',
    'Аджибурда',
    'Залупей',
    'Аджумайсимба',
    'Аджамат',
    'Джакарта',
    'Аджага-джага',
    'Аджаз',
    'Марта Аджубей 🍓',
    'Аджміль',
    'Аджурба',
    'Аджмамал',
    'Аджарт',
    'Аджартем',
    'Аджеджалик',
    'Аджинго',
    'Аджиу-дзитсу',
    'Аджакузі',
    'Аджим Керрі ',
    'Аджуліна Джолі',
    'Аджобайден',
    'Аджерело',
    'Раян Аджуослінґ',
    'ЗеДжубей',
    'Борис Аджосонюк',
    'Породжубей',
    'Аджикістан',
    'Аджурка',
    'Марта Трохимівна',
    'Аджаба',
    'Аджопа',
    'Аджигіт',
    'Аджужун',
    'Аджуньджуньчик',
    'Аджоконда',
    'Аджонсіна',
    'Аджубоба',
    'Аджаконда',
    'Аджуділдо',
    'Аджхіджаб',
    'Аджамас',
    'Аджедай',
    'Аджесітх',
    'Аджаллах',
    'Аджепард',
    'Адженчик',
    'Аджифіліс',
    'Аджубейська народна республіка',
    'Аджарктида',
    'Аджибратор',
    'Аджілдо',
    'Аджальна пробка',
    'Аджава сквірт',
    'Північна та Південня Аджерика',
    'Сполучені Штати Аджерики',
    'Аджубське Визвольне Військо',
    'Аджек',
    'Аджулістан',
    'Аджусік',
    'Аджумка',
    'Аджислення',
    'Аджесія',
    'Адженнеді',
    "П'ять ночей у Аджуби",
    'Мшк Аджеббі',
    'Аджуба і смертельні модулі',
    'Аджила',
    'Чорний принц Аджуба',
    'Аджмак 3',
    '11 смертників Аджуби',
    '1000 і 1 Аджуба'
]

@dp.message(Command('adjubus'))
async def start(message: types.Message):
    # await state.set_state(Form.default)
    answer = random.choice(array_of_adjuba)
    await message.reply(answer)
    
@dp.message(Command('img'))
async def start(message: types.Message):
    number = random.randint(1, 4)
    photo=FSInputFile(f'src\static\image{number}.jpg')
    await bot.send_photo(message.chat.id, photo)

@dp.message()
async def findAdjuba(message: types.Message) -> None:
    print(message.text.lower())
    if('аджубей' in message.text.lower()):
        adjuba = random.choice(array_of_adjuba)
        await message.reply(f'Ти мав на увазі: {adjuba}')
    