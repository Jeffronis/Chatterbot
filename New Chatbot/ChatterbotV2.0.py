from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "Smater Jhon",
    logic_adapters=[
        #allows the chat bot to do basic math and give the user the current time
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
        
        
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    #training data for converstations humor and greetings
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.humor"
)
while True:
    
    #user input
    inputText = input("Talk to bot V2.0...")


    #Get response to the input text

    response = bot.get_response(inputText)

    print(response)

#differnt resoponses will happen however for jokes it only dose the first joke, and will tell
#you the time if key words are used even when not aksing time.
