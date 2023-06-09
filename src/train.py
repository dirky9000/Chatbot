from chatterbot import ChatBot

bot = ChatBot('MyChatBot', 
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3')

nlp = spacy.load('en_core_web_sm')
bot.set_trainer(ChatterBotCorpusTrainer, language='en')

from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english')

while True:
    user_input = input('You: ')
    response = bot.get_response(user_input)
    print('ChatBot: ', response)