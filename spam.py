import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot("5932611213:AAH5UEnej4KjWg3UpofCAfz8oKjKucQtT8w")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обработчик команды /spam
@dp.message_handler(commands=['spam'])
async def start_spam(message: types.Message):
    args = message.get_args().split()
    
    if len(args) < 3:
        await message.reply("Использование: /spam <id пользователя> <количество> <текст>")
        return
    
    try:
        user_id = int(args[0])
        count = int(args[1])
    except ValueError:
        await message.reply("Проверьте правильность введенных данных.")
        return
    
    text = ' '.join(args[2:])
    
    for _ in range(count):
        await bot.send_message(user_id, text)
        await asyncio.sleep(0.1)  # Отправляем сообщения с интервалом 0.01 секунды
    
    await message.reply(f"Отправлено {count} сообщений пользователю с ID {user_id}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
