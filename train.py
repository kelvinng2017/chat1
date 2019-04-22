from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Training Example')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "./data/traditionalchinese/"
)

while True:
    message = input('你:')
    if message.strip() != '再見':
        reply = chatbot.get_response(message)
        print('小帮手 :',reply)
    if message.strip() == '再見':
        print('小帮手: 再見')
        # 把語料導出到json文件中

        break
