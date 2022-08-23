from googletrans import Translator
from client import lang


translator = Translator()

text = 'Como andas!'

translated_text = translator.translate(text, src=lang, dest='en')

print(translated_text.text)