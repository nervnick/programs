import eel
from translate import Translator

eel.init('www')

@eel.expose
def translate_text(text):
    translator = Translator(from_lang="ru", to_lang="en")
    end_text = translator.translate(text)
    eel.set_text(end_text)

eel.start('index.html', size = (600, 800)) 