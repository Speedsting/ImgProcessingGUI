#!/usr/bin/python
#advanced_img_processing.py
__author__ = "Elijah"
__version__ = 1.6
"""Preforms more complex actions with images like edge detection"""

from PIL import Image
import webbrowser
import simple_img_processing as sip
import random

def google_search(name):
    """takes a user response and searches images with that response

    :param name: the choice given by the user
    :return: None
    """
    url = "https://www.google.com/search?tbm=isch&q=" + name
    webbrowser.open(url)


def edge_detection(image_path):
    """finds and puts a line around the edges of the image

    :param image_path: the path of the image
    :return: the image with a line around the edge"""

    img     = sip.black_and_white(image_path)
    width   = img.size[0]
    height  = img.size[1]
    new_img = Image.new("RGBA", (width, height), "white")

    pixel_1 = 766
    pixel_2 = 766
    black = 0
    white = 765
    white_change = False
    black_change = False
    location = 0

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]
            color = red + green + blue

            if color == black:
                if white_change:
                    new_img.putpixel((location, row), (0, 0, 0))
                    black_change = False
                    white_change = False
                    pixel_1 = 766
                    pixel_2 = 766
                    location = 0
                elif pixel_1 != 766:
                    black_change = True
                    location = col
                else:
                    pixel_1 = color

            elif color == white:
                if black_change:
                    new_img.putpixel((location, row), (0, 0, 0))
                    black_change = False
                    white_change = False
                    pixel_1 = 766
                    pixel_2 = 766
                    location = 0
                elif pixel_2 != 766:
                    white_change = True
                    location = col
                else:
                    pixel_2 = color



    black = 0
    white = 765
    pixel_1 = 766
    pixel_2 = 766
    location = 0
    black_change = False
    white_change = False

    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]
            color = red + green + blue

            if color == black:
                if white_change:
                    new_img.putpixel((col, location), (0, 0, 0))
                    black_change = False
                    white_change = False
                    pixel_1 = 766
                    pixel_2 = 766
                    location = 0
                elif pixel_1 != 766:
                    black_change = True
                    location = row
                else:
                    pixel_1 = color

            elif color == white:
                if black_change:
                    new_img.putpixel((col, location), (0, 0, 0))
                    black_change = False
                    white_change = False
                    pixel_1 = 766
                    pixel_2 = 766
                    location = 0
                elif pixel_2 != 766:
                    white_change = True
                    location = row
                else:
                    pixel_2 = color
    return new_img


def picture_frame(image_path):
    """creates a grey frame around the image

    :param image_path: the path of the image
    :return: the image with a grey frame"""

    img     = Image.open(image_path)
    width   = img.size[0]
    height  = img.size[1]
    new_img = Image.open(image_path)

    for col in range(width // 30):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            grey = (red + green + blue) // 3
            new_img.putpixel((col, row), (grey, grey, grey))

    for col in range(width - width // 30, width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            grey = (red + green + blue) // 3
            new_img.putpixel((col, row), (grey, grey, grey))

    for col in range(width):
        for row in range(height // 30):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            grey = (red + green + blue) // 3
            new_img.putpixel((col, row), (grey, grey, grey))

    for col in range(width):
        for row in range(height - height // 30, height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            grey = (red + green + blue) // 3
            new_img.putpixel((col, row), (grey, grey, grey))

    return new_img


def compare_images(image_path):
    """takes two images (one randomly generated) and see which one is lighter

    :param image_path: the path of the image
    :return: the lighter image"""

    path = '/Users/enichols24/Dropbox/PythonNicholsElijah/Projects/ImgProcessingGUI_FNL/images/'
    images = {
        0: 'boston-skyline.jpg',
        1: 'boston.jpg',
        2: 'bostongreyhound.png',
        3: 'Bostonstraight.png',
        4: 'bulldog.jpg',
        5: 'cat_outline.png',
        6: 'owl.jpg',
        7: 'people.jpg',
        8: 'pycharm.png',
        9: 'sky.jpg',
        10: 'test.png',
        11: 'twitter.png'
    }

    img_1 = Image.open(image_path)
    width_1 = img_1.size[0]
    height_1 = img_1.size[1]

    num = random.randint(0, 11)
    choice = images[num]
    image = path + choice
    while image == img_1:
        num = random.randint(0, 11)
        choice = images[num]
        image = path + choice
    print(image)
    img_2 = Image.open(image)
    width_2  = img_2.size[0]
    height_2 = img_2.size[1]

    colors_1 = 0
    colors_2 = 0
    counter  = 0
    for col in range(width_1):
        for row in range(height_1):
            pixel = img_1.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            colors_1 += red + green + blue
            counter += 1

    colors_1 //= counter
    counter = 0

    for col in range(width_2):
        for row in range(height_2):
            pixel = img_2.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            colors_2 += red + green + blue
            counter += 1

    colors_2 //= counter

    if colors_1 > colors_2:
        return img_1
    elif colors_1 < colors_2:
        return img_2
    else:
        return None


def image_copier(image_path):
    """takes the image and duplicates it 4 times as a normal image,
    random color change, grey, and sepia tone

    :param image_path: the path of the image
    :return: the 4 altered images in the four corners of the new image"""

    img = Image.open(image_path)
    width  = img.size[0]
    height = img.size[1]
    new_img = Image.new("RGBA", (width, height), "white")
    new_color = random.randint(0, 255)

    for col in range(width // 2):
        for row in range(height // 2):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            new_img.putpixel((col, row), (red, green, blue))


    for col in range(width // 2):
        for row in range(height // 2):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            if red - new_color < 0:
                red = 0
            else:
                red -= new_color

            if green - new_color < 0:
                green = 0
            else:
                green -= new_color

            if blue - new_color < 0:
                blue = 0
            else:
                blue -= new_color

            new_img.putpixel((col, row + (height // 2)), (red, green, blue))


    for row in range(height // 2):
        for col in range(width // 2):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            color = (red + blue + green)
            color //= 3

            new_img.putpixel((col + (width // 2), row), (color, color, color))

    for col in range(width // 2):
        for row in range(height // 2):
            pixel = img.getpixel((col, row))
            red   = int(pixel[0])
            green = int(pixel[1])
            blue  = int(pixel[2])

            new_red   = int(red * 0.393 + green * 0.769 + blue * 0.189)
            new_green = int(red * 0.349 + green * 0.686 + blue * 0.168)
            new_blue  = int(red * 0.272 + green * 0.534 + blue * 0.131)

            new_img.putpixel((col + (width // 2), row + (height // 2)), (new_red, new_green, new_blue))

    return new_img

def sepia_tone(image_path):
    """creates a sepia tone of the image

    :param image_path: the path of the image
    :return: the image in a sepia tone"""

    img = Image.open(image_path)
    width  = img.size[0]
    height = img.size[1]

    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            new_red   = int(red * 0.393 + green * 0.769 + blue * 0.189)
            new_green = int(red * 0.349 + green * 0.686 + blue * 0.168)
            new_blue  = int(red * 0.272 + green * 0.534 + blue * 0.131)

            img.putpixel((col, row), (new_red, new_green, new_blue))

    return img

def pixelate(image_path, width_amt, height_amt):
    """creates a pixelated version of the image

    :param image_path: the path of the image
    :param width_amt: the amount pixels left to right
    :param height_amt: the amount of pixels up to down
    :return: the image with less pixels than the original"""

    try:
        width_amt  = int(width_amt)
    except ValueError:
        width_amt = 20

    try:
        height_amt = int(height_amt)
    except ValueError:
        height_amt = 20

    img = Image.open(image_path)
    width  = img.size[0]
    height = img.size[1]
    new_img = Image.new("RGBA", (width_amt, height_amt), "white")

    new_col = -1
    new_row = 0
    height_pos = 0
    width_pos  = 0

    if height_amt >= width_amt:
        for j in range(1, height_amt + 1):
            width_pos = 0
            for i in range(1, width_amt + 1):
                red_colors = 0
                green_colors = 0
                blue_colors = 0
                counter = 0
                for col in range(width_pos, (width // width_amt) * i):
                    for row in range(height_pos, (height // width_amt) * j):
                        pixel = img.getpixel((col, row))
                        red = pixel[0]
                        green = pixel[1]
                        blue = pixel[2]

                        red_colors += red
                        green_colors += green
                        blue_colors += blue
                        counter += 1

                new_red   = red_colors   / counter
                new_green = green_colors / counter
                new_blue  = blue_colors  / counter

                new_red   = int(new_red)
                new_green = int(new_green)
                new_blue  = int(new_blue)
                width_pos  = (width // width_amt) * i

                new_col += 1
                if new_col >= width_amt:
                    new_col = 0
                    new_row += 1

                new_img.putpixel((new_col, new_row), (new_red, new_green, new_blue))
            height_pos = (height // height_amt) * j
    else:
        for i in range(1, width_amt + 1):
            height_pos = 0
            for j in range(1, height_amt + 1):
                red_colors = 0
                green_colors = 0
                blue_colors = 0
                counter = 0
                for row in range(height_pos, (height // height_amt) * j):
                    for col in range(width_pos, (width // width_amt) * i):
                        pixel = img.getpixel((col, row))
                        red = pixel[0]
                        green = pixel[1]
                        blue = pixel[2]

                        red_colors += red
                        green_colors += green
                        blue_colors += blue
                        counter += 1

                new_red   = red_colors   / counter
                new_green = green_colors / counter
                new_blue  = blue_colors  / counter

                new_red     = int(new_red)
                new_green   = int(new_green)
                new_blue    = int(new_blue)
                height_pos  = (height // height_amt) * j

                new_row += 1
                if new_row >= height_amt:
                    new_row = 0
                    new_col += 1

                new_img.putpixel((new_col, new_row), (new_red, new_green, new_blue))
            width_pos = (width // width_amt) * i


    return new_img

def crop(image_path):
    """crops the middle of the image (very close at least)

    :param image_path: the path of the image
    :return: the new cropped image"""

    img = edge_detection(image_path)
    width  = img.size[0]
    height = img.size[1]
    new_img = Image.open(image_path)

    pos = []

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            if red + green + blue == 0:
                pos.append(row)
                break
        if len(pos) != 0:
            break

    top = pos[0]
    pos = []

    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            if red + green + blue == 0:
                pos.append(col)
                break
        if len(pos) != 0:
            break
    left = pos[0]
    pos = []

    for row in range(height-1, 0, -1):
        for col in range(width-1, 0, -1):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            if red + green + blue == 0:
                pos.append(row)
                break

        if len(pos) != 0:
            break
    right = pos[0]
    bottom = pos[0]

    new_img = new_img.crop((left, top, right, bottom))
    new_img.resize((400, 400))
    return new_img