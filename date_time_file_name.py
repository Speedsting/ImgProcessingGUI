import datetime

# get date and time to guarantee unique file name:
currentDT = datetime.datetime.now()
# formatted date and time:
time_stamp = currentDT.strftime("%Y_%m_%d_%Hh%Mm%Ss")

# new image name:
new_image_name = "new_images/IMG" + time_stamp + ".png"

# now save image

def save_image():
    """creates a new save file name using the date and time

    param: None
    return: the file with a date/time generated name"""

    currentDT = datetime.datetime.now()
    time_stamp = currentDT.strftime("%Y_%m_%d_%Hh%Mm%Ss")
    new_image_name = "new_images/IMG" + time_stamp + ".png"

    return new_image_name