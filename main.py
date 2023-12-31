import openai
import logging
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler

BOT_TOKEN = '5924509650:AAH_AEkHZKp4jl8AzvSyFxufDe5ICzj5y8Y'
openai.api_key = "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"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
reply_keyboard = [['/help', '/start']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def ask(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0]['text']


async def start_command(update, context):
    """Отправляет сообщение когда получена команда /start"""
    # user = update.effective_user
    # await update.message.reply_html(
    #     f"Привет {user.mention_html()}! Я ангел-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    #     reply_markup=markup
    # )
    await context.bot.send_message(update.message.chat.id, "Получил координаты")


async def echo(update, context):
    if update.message.text.lower().startswith('толян'):
        prompt = update.message.text[7:]
        print(prompt)

        await context.bot.send_message(update.message.chat.id, ask(prompt))

    if update.message.text.lower().startswith('оооо'):
        await update.get_bot().send_video(update.message.chat.id, open('oborona.mp4', 'rb'))


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler('start', start_command))
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
