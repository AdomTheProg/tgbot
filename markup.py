from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btn1=KeyboardButton(text='Я лох')
btn2=KeyboardButton(text="Я не лох")
btn3=KeyboardButton(text="Пагода Петрикав")

firstkata= ReplyKeyboardMarkup(resize_keyboard=True).add(btn1,btn2,btn3)