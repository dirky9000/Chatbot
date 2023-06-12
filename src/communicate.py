from chatterbot.trainers import ListTrainer

conversation = [
    'Hello',
    'Hi there',
    'How are you doing',
    'I''m doing great',
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

response = chatbot.get_response('Good morning!')
print(response)