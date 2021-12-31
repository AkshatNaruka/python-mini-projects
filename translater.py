from googletrans import Translator
text = input("Enter the text to translate")
translator=Translator()
Detect=translator.detect(text)
translated=translator.translate(text)
print(translated.text)