import sys
import os
from PIL import Image

#grab fisrt and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


#check is new / exists, if not create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png','png')
    print('All Done!')




#loop through Images,
#Convert images to PNG

#save to the new folder