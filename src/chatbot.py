from chatterbot import Chatbot
bot = Chatbot('James')

bot = Chatbot(
    'James',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    database_uri = 'sqlite:///database.sqlite3',
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation'
    ]
)

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break