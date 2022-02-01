import aiogram
from aiogram import Dispatcher,types,Bot,executor
import markup as mk

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
import bs

import requests
from bs4 import BeautifulSoup

url = 'https://www.gismeteo.by/weather-petrikov-11014/now/'
HEADERS={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		 }
response = requests.get(url,headers=HEADERS)
soup = BeautifulSoup(response.content, 'lxml')
when=soup.find('div', class_='now-localdate').get_text(strip=True)
temp=soup.find('span',class_="unit unit_temperature_c").get_text(strip=True)
weath_wind=soup.find('div',class_="unit unit_wind_m_s").get_text(strip=True)
waters=soup.find('div',class_="now-info-item humidity").find("div",class_="item-value").get_text(strip=True)

bot=Bot('5150906596:AAHMn3jt3Hh3Y3uSkRogmH0PJ2OMjDhvJGk',parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot,storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])

async def get_started(message:types.Message):
	await bot.send_message(chat_id=message.chat.id,text="Привет лохозаврики.",reply_markup=mk.firstkata)

@dp.message_handler()
async def reply_message(message:types.Message):
	if message.text=="Я лох":
		await bot.send_message(chat_id=message.chat.id,text="Лошарик")
	elif message.text=="Я не лох":
		await bot.send_message(chat_id=message.chat.id,text=("Не пиздел бы ты..."),reply_markup=mk.firstkata)
	elif message.text=="Пагода Петрикав":
		await bot.send_message(chat_id=message.chat.id,text=f'{when} \n {temp}℃ \n Cкорость ветра---> {weath_wind} "Влажность воздуха---> {waters} %')
	else:
		await bot.send_message(chat_id=message.chat.id,text=(f"{message.from_user.first_name},ты чё попутал?Кнопочки для кого поставили?"))




executor.start_polling(dp,skip_updates=True)