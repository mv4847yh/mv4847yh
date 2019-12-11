from PIL import Image, ImageDraw, ImageFont

Image = Image.open('photo-1552332386-f8dd00dc2f85.jpeg')

Image.thumbnail((800, 800))
Image.save('taco_thumbnails.jpeg')

img_draw = ImageDraw.Draw(Image)
font = ImageFont.truetype('DejaVuSans.ttf', 20)

img_draw.text([200, 200], 'Random Taco Cookbook', fill='purple', font=font)

Image.show()

