import pyttsx3
from translate import Translator

#voice
engine = pyttsx3.init()
v = engine.getProperty('voices')
engine.setProperty('voice', v[1].id)

#translate
while True:
    translator = Translator(from_lang ='English', to_lang = 'Italian')
    result = translator.translate(input('Enter text to translate:-'))
    print(result)
    engine.say(result)
    engine.runAndWait()
