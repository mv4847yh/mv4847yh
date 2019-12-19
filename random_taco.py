import docx  # import this library to create and update a word document

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
# showing the taco image
Image.save('modified_taco.jpg')
# saving the the taco image and naming it

taco_book = []

for i in range(3):
    taco_url = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
    taco_book.append(taco_url)
    print(taco_book)

taco_word = docx.Document()

taco_word.add_paragraph('Random Taco Cookbook', 'Title')

taco_word.add_picture('modified_taco.jpg')

taco_word.add_paragraph("Tai's Captures")

taco_word.add_paragraph('https://taco-1150.herokuapp.com/random/?full_taco=true')

taco_word.add_paragraph('Mohamed Hussein')

taco_word.add_page_break()

for item in range(len(taco_book)):
    taco_word.add_paragraph(taco_book[item]["seasoning"]["name"], 'heading 1')
    taco_word.add_paragraph(taco_book[item]["seasoning"]["recipe"])
    taco_word.add_paragraph(taco_book[item]["condiment"]["recipe"])
    taco_word.add_paragraph(taco_book[item]["mixin"]["recipe"])
    taco_word.add_paragraph(taco_book[item]["base_layer"]["recipe"])

taco_word.save('Lo.docx')


taco_word.add_page_break()

taco_word.save('docx')