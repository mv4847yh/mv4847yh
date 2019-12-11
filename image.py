from PIL import Image, ImageDraw, ImageFont

image = Image.open('photo-1552332386-f8dd00dc2f85.jpeg')

image.thumbnail((600, 600))
image.save('taco_thumbnail.jpeg')

img_draw = ImageDraw.Draw(image)

# the list of points are the coordinates of the top left corner X and Y,
# and the bottom right corner X and Y.
