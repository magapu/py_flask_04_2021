from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from werkzeug.exceptions import BadRequest

bot = ChatBot("Srinivas ChatBot")
trainer = ListTrainer(bot)
trainer.train(["Hey",
               "Hi there, How are you?",
               "Hi",
               "Hi!",
               "How are you doing?",
               "I'm doing great.",
               "That is good to hear",
               "Thank you.",
               "You're welcome.",
               "What is your name?", "My name is Resume ChatBot",
               "Who created you?", "Srinivas",
               "Tell me about yourself",
               "My name is Sunanda Somwase. I am a third year computer engineering student at PVGCOET",
               "Contact",
               "Email : sunandasomwase@gmail.com, Mobile number : +91 9021393816 Location : Pune, Maharashtra",
               "Education",
               "Bachelor of Engineering (B.E), Computer Science & Engineering\n Pune Vidyarthi Grihas College Of Engineering And Technology Pune '\n'2018 - 2022 '\n'CGPA: 8.84/10 '\n'Senior Secondary (XII), Science Sir Parashurambhau College Pune Maharashtra (MAHARASHTRA STATE BOARD board) Year of completion: 2018 Percentage: 88.40% Secondary (X) Sant Meera School Aurangabad (MAHARASHTRA STATE BOARF board) Year of completion: 2016 Percentage: 96.20%",
               "Projects",
               ])


def return_bot_res(user_input):
    if user_input is not None:
        return str(bot.get_response(user_input))
    else:
        raise BadRequest('Invalid Input')
