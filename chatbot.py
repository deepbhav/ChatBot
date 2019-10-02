from chatterbot import ChatBot

bot = ChatBot('Simple ChatBot App')

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

conversation= ["Hi","Hello",
"How are you ?","I am Fine. What about you?",
"I am Cool","Where do you live?",
"I live in an Endorence",
"Everything is fine ?","All Good"]

# with open ('imp.txt',"r" ,encoding="utf8") as c :
#     conversation = c.readlines()

trainer.train(conversation)


while True :
    query=input("User : ")
    if query == 'Exit' :
        break
    bot_input=bot.get_response(query)
    print('Bot : ',bot_input)

