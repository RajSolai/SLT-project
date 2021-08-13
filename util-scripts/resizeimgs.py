import os

path = "/home/solairaj/office/SLT-project/raw_images"

def resize(filename,count):
    os.system ('magick convert '+path
            +'/'
            +filename
            +' -resize 180x180 '+path+'/'
            +str(count)
            +'out.png')

for imagefile in os.listdir(path):
    i = 0
    resize (imagefile,++i)
