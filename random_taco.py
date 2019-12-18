import docx  # import this library to create and update a word document
from docx.shared import Inches
from docx.enum.text import WD_BREAK
from docx.enum.text import WD_BREAK # source: stack overFlow
import requests # to get the url
from PIL import Image, ImageDraw, ImageFont

# importing image and font
Image = Image.open('photo-1552332386-f8dd00dc2f85.jpeg')
# opening image
Image.thumbnail((800, 800))
# resizing the thumbnails
Image.save('taco_thumbnails.jpeg')
# saving the image
img_draw = ImageDraw.Draw(Image)

font = ImageFont.truetype('DejaVuSans.ttf', 20)

img_draw.text([200, 80], 'Random Taco Cookbook', fill='purple', font=font)
# drawing text to the taco image
Image.show()
# showing the taco image
Image.save('modified_taco.jpg')
# saving the the taco image and naming it

taco_word = docx.Document()

taco_word.add_paragraoh('Random T..', 'Title')

taco_word.add_picture('modified_taco.jpg')