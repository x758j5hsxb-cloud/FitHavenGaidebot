import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.exceptions import TelegramUnauthorizedError

# ====== Токен бота ======
API_TOKEN = os.environ.get('FITHAVEN_TOKEN') or "8516507191:AAFpxuyiTIDSutVN7Uzp_QehB9hGnpyAyDE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ====== Словарь с упражнениями ======
exercises = {
    "Спина": [
        {"name": "Тяга вертикального блока", "link": "https://t.me/trraningg/65"},
        {"name": "Подтягивания в гравитроне", "link": "https://t.me/trraningg/76"},
        {"name": "Австралийские подтягивания", "link": "https://t.me/trraningg/21"},
        {"name": "Тяга Горизонтального блока", "link": "https://t.me/trraningg/24"},
        {"name": "Пуловер в кроссовере", "link": "https://t.me/trraningg/66"},
        {"name": "Гиперэкстензия", "link": "https://t.me/trraningg/52"},
        {"name": "Тяга гантели одной рукой", "link": "https://t.me/trraningg/47"},
        {"name": "Классические подтягивания", "link": "https://t.me/trraningg/55"},
        {"name": "Тяга штанги в наклоне", "link": "https://t.me/trraningg/62"}
    ],
    "Грудь": [
        {"name": "Жим лежа на горизонтальной скамье", "link": "https://t.me/trraningg/71"},
        {"name": "Сведение рук в Пек-деке", "link": "https://t.me/trraningg/67"},
        {"name": "Жим штанги на наклонной скамье", "link": "https://t.me/trraningg/34"},
        {"name": "Разведение гантелей на наклонной скамье", "link": "https://t.me/trraningg/53"},
        {"name": "Жим гантелей на наклонной скамье", "link": "https://t.me/trraningg/54"},
        {"name": "Отжимания от смита", "link": "https://t.me/trraningg/20"},
        {"name": "Отжимания на брусьях", "link": "https://t.me/trraningg/77"},
        {"name": "Отжимания классические", "link": "https://t.me/trraningg/49"}
    ],
    "Ноги": [
        {"name": "Выпады по залу", "link": "https://t.me/trraningg/45"},
        {"name": "Приседания плие", "link": "https://t.me/trraningg/41"},
        {"name": "Приседания в Смите", "link": "https://t.me/trraningg/30"},
        {"name": "Выпады с прямым корпусом", "link": "https://t.me/trraningg/75"},
        {"name": "Жим ногами узкой постановкой ног", "link": "https://t.me/trraningg/74"},
        {"name": "Сведение ног в тренажере сидя", "link": "https://t.me/trraningg/73"},
        {"name": "Разгибание ног сидя", "link": "https://t.me/trraningg/70"},
        {"name": "Сгибание ног сидя", "link": "https://t.me/trraningg/69"},
        {"name": "Жим платформы ногами средней постановкой ног", "link": "https://t.me/trraningg/68"}
    ],
    "Ягодицы": [
        {"name": "Ягодичный мостик со штангой", "link": "https://t.me/trraningg/46"},
        {"name": "Болгарские выпады", "link": "https://t.me/trraningg/32"},
        {"name": "Румынская тяга с гантелями", "link": "https://t.me/trraningg/43"},
        {"name": "Отведение ноги в сторону в кроссовере", "link": "https://t.me/trraningg/15"}
    ],
    "Плечи": [
        {"name": "Подъем блина перед собой", "link": "https://t.me/trraningg/35"},
        {"name": "Махи гантелей в стороны", "link": "https://t.me/trraningg/31"},
        {"name": "Махи гантелей сидя", "link": "https://t.me/trraningg/50"},
        {"name": "Жим гантелей на плечи", "link": "https://t.me/trraningg/57"},
        {"name": "Жим штанги на плечи", "link": "https://t.me/trraningg/56"},
        {"name": "Разведение рук в стороны в пэк деке", "link": "https://t.me/trraningg/68"},

        
    ],
    "Руки": [
        {"name": "Сгибание рук со штангой EZ", "link": "https://t.me/trraningg/72"},
        {"name": "Сгибание рук с гантелями", "link": "https://t.me/trraningg/37"},
        {"name": "Сгибание рук нейтральным хватом", "link": "https://t.me/trraningg/63"},
        {"name": "Сгибание рук в блоке с прямой рукояткой", "link": "https://t.me/trraningg/58"},
        {"name": "Разгибание рук с гантелью", "link": "https://t.me/trraningg/39"},
        {"name": "Разгибание рук с гантелью одной рукой", "link": ""},
        {"name": "Разгибание рук в блоке с прямой рукояткой", "link": "https://t.me/trraningg/5"},
        {"name": "Разгибание рук в блоке с кривой рукояткой", "link": "https://t.me/trraningg/59"},
        {"name": "Разгибание рук в блоке с канатом", "link": "https://t.me/trraningg/60"},
        {"name": "Разгибание рук из-за головы с канатом", "link": "https://t.me/trraningg/61"}
    ],
    "Пресс": [
        {"name": "Скручивания", "link": "https://t.me/trraningg/19"},
        {"name": "Прямой подъем ног в упоре на брусьях", "link": "https://t.me/trraningg/40"},
        {"name": "Скручивания сидя", "link": "https://t.me/trraningg/22"},
        {"name": "Подъем ног лежа на скамье", "link": "https://t.me/trraningg/18"}
    ]
}

# ====== Главное меню ======
def main_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=group, callback_data=f"group_{group}")]
            for group in exercises.keys()
        ] + [[InlineKeyboardButton(text="Хочу план под себя 🔥", callback_data="custom_plan")]]
    )
    return keyboard

# ====== Старт ======
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! Выбери целевую мышцу и посмотри, какие упражнения ты можешь сделать 💪",
        reply_markup=main_menu()
    )

# ====== Обработка кнопок ======
@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    data = callback.data

    if data == "custom_plan":
        await callback.message.answer(
            """🔥 Индивидуальный тренировочный план под тебя

Хочешь тренироваться результативно, а не наугад?
Я помогу собрать персональный тренировочный план с учётом твоей цели, уровня подготовки и возможностей зала.

💪 Что ты получишь:
• Индивидуальный тренировочный план
• Упражнения с гиперссылками на технику выполнения
• Подбор нагрузки под твой уровень
• 🎁 Одна персональная тренировка в подарок

📘 В дополнение ты получишь 3 полезных гайда:
• Как повышать тренировочную нагрузку
• Как правильно прогрессировать и не стоять на месте
• Как вести отчёт по тренировкам и отслеживать результат

📩 Напиши: @kagane_07
Сделаем твой прогресс понятным, безопасным и быстрым 🔥"""
        )
        return

    if data.startswith("group_"):
        group = data[6:]
        if exercises.get(group):
            buttons = []
            for i, ex in enumerate(exercises[group]):
                link = ex.get("link")
                if link:
                    buttons.append([InlineKeyboardButton(text=ex["name"], url=link)])
                else:
                    buttons.append([InlineKeyboardButton(text=ex["name"], callback_data=f"no_link_{group}_{i}")])

            buttons.append([InlineKeyboardButton(text="⬅ Главное меню", callback_data="back")])
            keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
            await callback.message.answer(f"Выберите упражнение для {group}:", reply_markup=keyboard)
        else:
            await callback.message.answer(f"Упражнения для {group} пока не добавлены 😎")
        return

    if data == "back":
        await callback.message.answer("Главное меню:", reply_markup=main_menu())

    if data.startswith("no_link_"):
        await callback.message.answer("Ссылка на это упражнение пока не добавлена 😅")
        return

# ====== Запуск бота ======
async def main():
    print("Бот готов к работе! 🟢")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except TelegramUnauthorizedError:
        print("Ошибка: неавторизованный токен Telegram (Unauthorized).")
        raise SystemExit(1)
    except KeyboardInterrupt:
        print("Бот остановлен вручную.")

