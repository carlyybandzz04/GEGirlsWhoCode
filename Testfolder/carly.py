from PIL import Image

def load_img (filename):
    im = Image.open(filename)
    return im

def show_img(im):
    im.show()

def save_img(im, filename):
    im.save(filename,"jpeg")
    show_img(im)

def carly(im):
    pixels = im.getdata()

    newPixels=[]
    purple=(600,51,76)
    orange=(530,200,450)
    green=(112,510,158)
    yellow=(400,0,166)

    for p in pixels:
        intensity = p[0] + p[1] +p[2]

        if intensity < 182:
            newPixels.append(purple)
        elif intensity>=100 and intensity < 364:
            newPixels.append(orange)
        elif intensity in range (364,546):
            newPixels.append(green)
        else:
            newPixels.append(yellow)


    newImage = Image.new("RGB",im.size)
    newImage.putdata(newPixels)
    return newImage
