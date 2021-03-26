#!/usr/bin/python
#simple_img_processing.py
__author__ = "Elijah"
__version__ = 1.9
"""Preforms special actions with images
such as flipping them or changing certain pixels."""

from PIL import Image
import date_time_file_name as dt

def inversion(image_path):
    """inverts the color of every pixel in the image

    :param image_path: the path that leads to the image file
    :return: the inverted image"""

    img = Image.open(image_path)
    width  = img.size[0]
    height = img.size[1]
    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = 255 - pixel[0]
            green = 255 - pixel[1]
            blue  = 255 - pixel[2]

            img.putpixel((col, row), (red, green, blue))

    return img



def lighten_darken(image_path, brightness):
    """changes the brightness of the image based on the input

    :param image_path: the path of the image
    :param brightness: level of brightness
    :return: the image with a new level of brightness"""

    try:
        brightness = int(brightness)
    except ValueError:
        brightness = 0
    img = Image.open(image_path)
    width  = img.size[0]
    height = img.size[1]

    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]
            colors = [red, green, blue]

            for i in range(len(colors)):
                if brightness < 0:
                    if colors[i] + brightness < 0:
                        colors[i] = 0
                    else:
                        colors[i] += brightness
                else:
                    if colors[i] + brightness > 255:
                        colors[i] = 255
                    else:
                        colors[i] += brightness
                        
            img.putpixel((col, row), (colors[0], colors[1], colors[2]))

    return img


def greyscale(image_path):
    """changes the color of the image to a grey version

    :param image_path: the path of the image
    :return: the grey version of the image"""

    img = Image.open(image_path)
    new_img = img
    width  = img.size[0]
    height = img.size[1]
    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]
            color = int(red / 3 + green / 3 + blue / 3)
            new_img.putpixel((col, row), (color, color, color))

    return new_img


def black_and_white(image_path):
    """changes an image into a black and white version

    :param image_path: the path of the image
    :return: the image in a black/white format"""

    img    = greyscale(image_path)
    width  = img.size[0]
    height = img.size[1]

    colors_list = []
    min_colors  = 0
    max_colors  = 0
    count       = 0

    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]
            color = red + green + blue

            colors_list.append(color)
    colors_list.sort()

    for i in range(len(colors_list) // 2):
        min_colors += colors_list[i]
        count += 1

    min_colors //= count
    count = 0
    del[colors_list[0:len(colors_list) // 2]]

    for i in colors_list:
        max_colors += i
        count += 1

    max_colors //= count
    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            color = pixel[0] + pixel[1] + pixel[2]
            if color > min_colors:
                color = 0
            elif color < max_colors:
                color = 255

            img.putpixel((col, row), (color, color, color))

    return img


def filter(image_path, amt, color_choice):
    """uses a color filter on the image with the user's input

    :param image_path: path of the image
    :param amt: the amount of brightness
    :param color_choice: the color (red, green, or blue)
    :return: the image with the color filter"""

    try:
        amt = int(amt)
    except ValueError:
        amt = 0
    img = Image.open(image_path)
    width  = img.size[0]
    height = img.size[1]
    color = 0
    choice = 0
    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            if color_choice == "red":
                color = red
                choice = 0
            elif color_choice == "green":
                color = green
                choice = 1
            elif color_choice == "blue":
                color = blue
                choice = 2
            else:
                return img

            if color > amt:
                color = 255
            else:
                color = 0

            if choice == 0:
                img.putpixel((col, row), (color, green, blue))
            elif choice == 1:
                img.putpixel((col, row), (red, color, blue))
            else:
                img.putpixel((col, row), (red, green, color))

    return img


def reverse(image_path, x_axis, y_axis):
    """reverses or flips the image with the axis that the user chooses

    :param image_path: the path of the image
    :param x_axis: determines if the image is flipped horizontally
    :param y_axis: determines if the image is flipped vertically
    :return: the reversed image"""

    img = Image.open(image_path)
    new_img = Image.open(image_path)
    width  = img.size[0]
    height = img.size[1]

    if x_axis.lower() == "true":
        x_axis = True
    else:
        x_axis = False

    if y_axis.lower() == "true":
        y_axis = True
    else:
        y_axis = False

    for col in range(width):
        for row in range(height):
            pixel = img.getpixel((col, row))
            red   = pixel[0]
            green = pixel[1]
            blue  = pixel[2]

            if y_axis:
                if col < width:
                    new_col = width - col - 1
                elif col == width // 2:
                    new_col = col

            if x_axis:
                if row < height:
                    new_row = height - row - 1
                elif row == height:
                    new_row = row

            if x_axis and y_axis:
                new_img.putpixel((new_col, new_row), (red, green, blue))
            elif x_axis:
                new_img.putpixel((col, new_row), (red, green, blue))
            elif y_axis:
                new_img.putpixel((new_col, row), (red, green, blue))
            else:
                new_img.putpixel((col, row), (red, green, blue))

    return new_img


def save(image):
    """saves the image with the date and time in the title

    :param image: the path of the image
    :return: None"""

    name = dt.save_image()
    image.save(name)


def show(image):
    """shows the image that was most recently generated

    :param image: the path of the image
    :return: None"""

    image.show()