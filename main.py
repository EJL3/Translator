import pyttsx3
from translate import Translator

#voice
engine = pyttsx3.init()

#translate
while True:
    translator = Translator(from_lang ='English', to_lang = 'Italian')
    result = translator.translate(input('Enter text to translate:-'))
    print(result)
    engine.say(result)
    engine.runAndWait()
