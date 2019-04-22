from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Training Example')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "./data/traditionalchinese/"
)


message = "告訴我關於美國內戰"
if message.strip() != '再見':
    reply = chatbot.get_response(message)
    print('小帮手 :',reply)
if message.strip() == '再見':
    print('小帮手: 再見')
    # 把語料導出到json文件中

