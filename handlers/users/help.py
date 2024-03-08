from aiogram.types import Message
from loader import dp, db, bot
from aiogram import types
import datetime
import pytz

@dp.message_handler(text="📇 Qo'llanma")
async def help(message:
    types.Message):
    await message.answer("<b>📃 @Termiz_Ramazon_Bot qo'llanmasi:\n\n🤖 Bizning bot orqali Muqaddas Ramazon oyining 30 kunlik ro'zasini o'z vaqtida bajaring.\n\n📜 Botimiz taqvimi Termiz shahar vaqtiga moslashgan va faqatgina 2024 yilning Ramazon taqvimi bor\n\n🕋 2024-yil Muqaddas Ramazon oyini biz bilan kutib oling\n\n☪️ @Termiz_Ramazon_Bot</b>")

@dp.message_handler(text="📊 Statistika")
async def statistika(message:
    types.Message):
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
    yil = pst_now.strftime("%d-%m-%Y")
    soat = pst_now.strftime("%H:%M:%S")
    count = db.count_users()[0]
    msg = f"<b>🤖 BOT STATISTIKASI 📊\n\n📆 Bugun:</b> <i>{yil}</i>\n<b>⏰ Soat:</b> {soat}\n👥 <b>Barcha Obunachilar =</b> <i>{count} ta</i>\n\n<b>✅ @Termiz_Ramazon_Bot</b>"
    photo_id = "AgACAgIAAxkBAAOrZesAAXsbK-eDaHSi_7e7pXyLJM-oAAJR1jEbnwNYS5dZlcsTbsAkAQADAgADeAADNAQ"
    await message.answer_photo(photo_id,caption=msg)

@dp.message_handler(text="👨‍💻 Dasturchi")
async def dev(message:
    types.Message):
    photo_id = "AgACAgIAAxkBAAOkZesAASGDd2tp7NI05CPeUEyRjCVcAAJP1jEbnwNYSwABklLoJwhkEAEAAwIAA3gAAzQE"
    await message.answer_photo(photo_id,caption="<b>👨‍💻 Dasturchi haqida malumot 📇\n\n👤 Dasturchi: Jasur Kenjayev\n💬 Telegram: @Python_Koders\n🪪 Instagram: <code>1.we_wolf</code>\n☎️ Telefon: +998333009888\n\n✅ @Termiz_Ramazon_Bot</b>")