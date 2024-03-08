from aiogram.types import Message
from keyboards.default.menu import Menu, moon
from loader import dp
from aiogram import types


@dp.message_handler(text="◀️ Orqaga")
async def cancel(message:
    types.Message):
    await message.answer("<b>🏠Bosh Menudasiz✅</b>",reply_markup=Menu)

@dp.message_handler(text="📿 Ramazon taqvimi")
async def main(message:
    types.Message):
    await message.answer("<b>📆 Marhamat, sanani tanlang👇</b>",reply_markup=moon)

@dp.message_handler(text="11 Mart")
async def mart11(message:
    types.Message):
    await message.answer("<b>📆 11-Mart Dushanba\n\n🔺 Saxarlik — 5:33\n🔻 Iftorlik — 18:47\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="12 Mart")
async def mart12(message:
    types.Message):
    await message.answer("<b>📆 12-Mart Seshanba\n\n🔺 Saxarlik — 5:31\n🔻 Iftorlik — 18:48\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="13 Mart")
async def mart13(message:
    types.Message):
    await message.answer("<b>📆 13-Mart Chorshanba\n\n🔺 Saxarlik — 5:30\n🔻 Iftorlik — 18:49\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="14 Mart")
async def mart14(message:
    types.Message):
    await message.answer("<b>📆 14-Mart Payshanba\n\n🔺 Saxarlik — 5:28\n🔻 Iftorlik — 18:51\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="15 Mart")
async def mart15(message:
    types.Message):
    await message.answer("<b>📆 15-Mart Juma\n\n🔺 Saxarlik — 5:26\n🔻 Iftorlik — 18:52\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="16 Mart")
async def mart16(message:
    types.Message):
    await message.answer("<b>📆 16-Mart Shanba\n\n🔺 Saxarlik — 5:24\n🔻 Iftorlik — 18:53\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="17 Mart")
async def mart17(message:
    types.Message):
    await message.answer("<b>📆 17-Mart Yakshanba\n\n🔺 Saxarlik — 5:23\n🔻 Iftorlik — 18:54\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="18 Mart")
async def mart18(message:
    types.Message):
    await message.answer("<b>📆 18-Mart Dushanba\n\n🔺 Saxarlik — 5:21\n🔻 Iftorlik — 18:55\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="19 Mart")
async def mart19(message:
    types.Message):
    await message.answer("<b>📆 19-Mart Seshanba\n\n🔺 Saxarlik — 5:19\n🔻 Iftorlik — 18:56\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="20 Mart")
async def mart20(message:
    types.Message):
    await message.answer("<b>📆 20-Mart Chorshanba\n\n🔺 Saxarlik — 5:17\n🔻 Iftorlik — 18:57\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="21 Mart")
async def mart21(message:
    types.Message):
    await message.answer("<b>📆 21-Mart Payshanba\n\n🔺 Saxarlik — 5:15\n🔻 Iftorlik — 18:58\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="22 Mart")
async def mart22(message:
    types.Message):
    await message.answer("<b>📆 22-Mart Juma\n\n🔺 Saxarlik — 5:14\n🔻 Iftorlik — 18:59\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="23 Mart")
async def mart23(message:
    types.Message):
    await message.answer("<b>📆 23-Mart Shanba\n\n🔺 Saxarlik — 5:12\n🔻 Iftorlik — 19:00\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="24 Mart")
async def mart24(message:
    types.Message):
    await message.answer("<b>📆 24-Mart Yakshanba\n\n🔺 Saxarlik — 5:10\n🔻 Iftorlik — 19:02\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="25 Mart")
async def mart25(message:
    types.Message):
    await message.answer("<b>📆 25-Mart Dushanba\n\n🔺 Saxarlik — 5:08\n🔻 Iftorlik — 19:03\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="26 Mart")
async def mart26(message:
    types.Message):
    await message.answer("<b>📆 26-Mart Seshanba\n\n🔺 Saxarlik — 5:07\n🔻 Iftorlik — 19:04\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="27 Mart")
async def mart27(message:
    types.Message):
    await message.answer("<b>📆 27-Mart Chorshanba\n\n🔺 Saxarlik — 5:05\n🔻 Iftorlik — 19:05\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="28 Mart")
async def mart28(message:
    types.Message):
    await message.answer("<b>📆 28-Mart Payshanba\n\n🔺 Saxarlik — 5:03\n🔻 Iftorlik — 19:06\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="29 Mart")
async def mart29(message:
    types.Message):
    await message.answer("<b>📆 29-Mart Juma\n\n🔺 Saxarlik — 5:01\n🔻 Iftorlik — 19:07\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="30 Mart")
async def mart30(message:
    types.Message):
    await message.answer("<b>📆 30-Mart Shanba\n\n🔺 Saxarlik — 4:59\n🔻 Iftorlik — 19:08\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="31 Mart")
async def mart31(message:
    types.Message):
    await message.answer("<b>📆 31-Mart Yakshanba\n\n🔺 Saxarlik — 4:58\n🔻 Iftorlik — 19:09\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="1 Aprel")
async def aprel1(message:
    types.Message):
    await message.answer("<b>📆 1 Aprel Dushanba\n\n🔺 Saxarlik — 4:56\n🔻 Iftorlik — 19:10\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="2 Aprel")
async def aprel2(message:
    types.Message):
    await message.answer("<b>📆 2 Aprel Seshanba\n\n🔺 Saxarlik — 4:54\n🔻 Iftorlik — 19:11\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="3 Aprel")
async def aprel3(message:
    types.Message):
    await message.answer("<b>📆 3 Aprel Chorshanba\n\n🔺 Saxarlik — 4:52\n🔻 Iftorlik — 19:12\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="4 Aprel")
async def aprel4(message:
    types.Message):
    await message.answer("<b>📆 4 Aprel Payshanba\n\n🔺 Saxarlik — 4:50\n🔻 Iftorlik — 19:13\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="5 Aprel")
async def aprel5(message:
    types.Message):
    await message.answer("<b>📆 5 Aprel Juma\n\n🔺 Saxarlik — 4:48\n🔻 Iftorlik — 19:14\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="6 Aprel")
async def aprel6(message:
    types.Message):
    await message.answer("<b>📆 6 Aprel Shanba\n\n🔺 Saxarlik — 4:46\n🔻 Iftorlik — 19:16\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="7 Aprel")
async def aprel7(message:
    types.Message):
    await message.answer("<b>📆 7 Aprel Yakshanba\n\n🔺 Saxarlik — 4:44\n🔻 Iftorlik — 19:17\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="8 Aprel")
async def aprel8(message:
    types.Message):
    await message.answer("<b>📆 8 Aprel Dushanba\n\n🔺 Saxarlik — 4:42\n🔻 Iftorlik — 19:18\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")

@dp.message_handler(text="9 Aprel")
async def aprel9(message:
    types.Message):
    await message.answer("<b>📆 9 Aprel Seshanba\n\n🔺 Saxarlik — 4:41\n🔻 Iftorlik — 19:19\n\n🕋 2024-yil Ramazon oyini bizning @Termiz_Ramazon_Bot bilan kutib oling</b>")