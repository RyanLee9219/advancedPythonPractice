from PIL import Image, ImageFilter

# Open the image
img = Image.open('./images/pikachu.jpg')

# Apply the blur filter
filtered_img = img.convert('L')
box=(100,100,400,400)
region = filtered_img.crop(box)

# resize = filtered_img.resize((300,300))
region.save("./grey.png")
