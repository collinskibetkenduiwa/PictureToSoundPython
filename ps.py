# The libararies used are gtts,pikkow and pytesseract
from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string

def image_to_sound(path_to_image):
    try:
        loaded_image = Image.open(path_to_image)

        decoded_text = image_to_string(loaded_image)

        cleaned_text = ' '.join(decoded_text.split('\n'))

        print(cleaned_text)
         
        sound = gTTS(cleaned_text, lang = 'en')

        sound.save('sound.mp3')      

        return True

    except Exception as bug:

        print('The bug thrown while excuting the code\n', bug)

        return
        
image_to_sound('image.jpg')
input()
