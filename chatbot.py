from chatterbot import ChatBot
from flask import Flask,render_template,request

from chatterbot.trainers import ListTrainer
conversation = open('chats.txt','r').readlines()

chatbot = ChatBot("ChatBot")
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

# flask app
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    msg = request.args.get('msg')
    return str(chatbot.get_response(msg))
 
 
if __name__ == "__main__":
    app.run()

#training
# 

# while True:
#     message = input('You:')
#     msg = message.strip()
#     if msg!='Bye' and msg!='bye':
#         reply = chatbot.get_response(message)
#         print('ChatBot:',reply)
#         continue;
#     if msg=='Bye' or msg=='bye':
#         print('ChatBot:Bye')
#     break



