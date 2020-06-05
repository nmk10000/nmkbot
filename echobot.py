from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)



TOKEN = "1285306305:AAHuPNLroWn6JU4ocZegsQQ7pTooyegB1eI"

def start_tcb(self, bot, update, args):

        """
        start_tcb - callback triggered on /start command

        :param bot: bot object comes from telegram API
        :param update: update object comes from telegram API
        :param args: our custom args

        """

        user_data = bot.get_chat(update.message.chat_id)

        bot.sendMessage(
            chat_id=update.message.chat_id, text="Hello {}, I'm HMSU Radio Bot.".format(user_data.username)
        )

        # keyboard = [[InlineKeyboardButton("Get radiokey", callback_data='1'), InlineKeyboardButton("Help", callback_data='2')]]

        # reply_markup = InlineKeyboardMarkup(keyboard)

        # update.message.reply_text('Please choose:', reply_markup=reply_markup)


        bot.sendMessage(chat_id=update.message.chat_id, text="Type /help for full list of commands") 
