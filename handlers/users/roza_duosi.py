from aiogram.types import Message
from loader import dp
from aiogram import types

@dp.message_handler(text="🤲 Ro'za duosi")
async def roza_duosi(message:
    types.Message):
    await message.answer("<b>🔺 Saharlik (og‘iz yopish) duosi\n\nNavaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.</b>\n\n<i>Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.</i>\n\n<b>🔻 Iftorlik (og‘iz ochish) duosi\n\nAllohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.</b>\n\n<i>Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.</i>\n\n🕋 @Termiz_Ramazon_Bot")