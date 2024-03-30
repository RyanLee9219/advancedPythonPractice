from PIL import Image, ImageFilter

# Open the image
img = Image.open('./images/astro.jpg.')
img.thumbnail((400,400))
img.save('./thumbnail.jpg')

print(img.size)