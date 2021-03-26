from PIL import Image
import datetime

# open image to process:
img = Image.open("images/pycharm.png")

# ensure in correct format:
rgb = img.convert('RGB')

# get dimensions:
w = rgb.size[0]
h = rgb.size[1]

# new image to write pixels to:
new_image = Image.new("RGBA", (w, h), "blue")

# go through every pixel
for col in range(w):
    for row in range(h):
        # get pixel object at col, row:
        current_pixel = rgb.getpixel( (col, row))
        
        # get RGB:
        red_amt   = current_pixel[0]
        green_amt = current_pixel[1]
        blue_amt  = current_pixel[2]

        # sest new RGB amounts:
        new_red   = red_amt  # unchanged
        new_green = 0        # No green!
        new_blue  = blue_amt # unchaged
        
        # put new color pixel in new image at same spot:
        new_image.putpixel( (col, row), (new_red, new_green, new_blue) )

# show original and new:
img.show()
new_image.show()

# get date and tiem to guarantee unique file name:
currentDT = datetime.datetime.now()
time_stamp = currentDT.strftime("%Y_%m_%d_%Hh%Mm%Ss")

# save the new image:
new_image.save("new_images/IMG" + time_stamp + ".png")

# always close when done!
new_image.close()
