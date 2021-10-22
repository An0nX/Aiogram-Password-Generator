import random
import logging
from aiogram import Bot, Dispatcher, executor, types
import time
from telegram import ParseMode
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Объект бота
bot = Bot(token="ВАШ ТОКЕН СЮДА")
admin = 
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

button_gen = KeyboardButton('Сгенерировать')
button_sourse = KeyboardButton('Исходный код')
button_help = KeyboardButton('Помощь')

key = ReplyKeyboardMarkup()
key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_gen).row(
    button_help, button_sourse
)

button_stats = KeyboardButton('Статистика')

adm = ReplyKeyboardMarkup()
adm = ReplyKeyboardMarkup(resize_keyboard=True).add(button_stats)

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
sstart = 0
sgenerate = 0
shelp = 0
ssourse = 0

@dp.message_handler(commands="start")
async def start(message: types.Message):
    user_id = message.chat.id
    print(user_id, 'запустил бота')
    global sstart
    sstart += 1
    await bot.send_message(admin, '[LOG] {} запустил бота'.format(user_id))
    await bot.send_message(user_id, "Привет! Я бот для генерации паролей.", reply_markup=key)

@dp.message_handler(commands="adm")
async def admi(message: types.Message):
    user_id = message.chat.id
    admin = 
    if (user_id == admin):
        await bot.send_message(user_id, "Добро пожаловать в админку", reply_markup=adm)
        
@dp.message_handler()
async def buttons(message: types.Message):
    user_id = message.chat.id
    if message.text == 'Сгенерировать':
        print(user_id, 'сгенерировал пароль')
        global sgenerate
        sgenerate += 1
        number = 1
        length = 28
        for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
            try:
                from telegram import ParseMode
                await bot.send_message(user_id, "Твой пароль: <code>{}</code>".format(password), ParseMode.HTML, reply_markup=key)
            except Exception as error:
                await bot.send_message(user_id, "Твой пароль: ", reply_markup=key)
                await bot.send_message(user_id, password, reply_markup=key)
    if message.text == 'Помощь':
        print(user_id, 'открыл раздел помощи')
        global shelp
        shelp += 1
        await bot.send_message(user_id, "Для того чтобы сгенерировать пароль нажми на соответствующую кнопку", reply_markup=key)
    if message.text == 'Исходный код':
        print(user_id, 'открыл раздел сурсов')
        global ssourse
        ssourse += 1
        await bot.send_message(user_id, "Исходники тут: https://github.com/httpshotmaker/Aiogram-Password-Generator", reply_markup=key)
    if message.text == 'Статистика':
        admin = 
        if user_id == admin:
            await bot.send_message(admin, "Количество запусков бота: {}\nКоличество сгенерированных паролей: {}\nКоличество вызовов помощи: {}\nКоличество вызовов сурсов: {}".format(sstart, sgenerate, shelp, ssourse))
        
@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

@dp.message_handler(commands="help")
async def help(message: types.Message):
    user_id = message.chat.id
    print(user_id, 'открыл раздел помощи')
    global shelp
    shelp += 1
    await bot.send_message(user_id, "Для того чтобы сгенерировать пароль нажми на соответствующую кнопку", reply_markup=key)
    
@dp.message_handler(commands="gen")
async def generate_password(message: types.Message):   
    user_id = message.chat.id
    print(user_id, 'сгенерировал пароль')
    global sgenerate
    sgenerate += 1
    number = 1
    length = 28
    for n in range(number):
        password =''
        for i in range(length):
            password += random.choice(chars)
        try:
            from telegram import ParseMode
            await bot.send_message(user_id, "Твой пароль: <code>{}</code>".format(password), ParseMode.HTML, reply_markup=key)
        except Exception as error:
            await bot.send_message(user_id, "Твой пароль: ", reply_markup=key)
            await bot.send_message(user_id, password, reply_markup=key)

@dp.message_handler(commands="sourse")
async def sourse(message: types.Message):
    user_id = message.chat.id
    print(user_id, 'открыл раздел сурсов')
    global ssourse
    ssourse += 1
    await bot.send_message(user_id, "Исходники тут: https://github.com/httpshotmaker/Aiogram-Password-Generator", reply_markup=key)


    
    
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
