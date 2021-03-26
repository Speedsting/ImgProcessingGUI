#!/usr/bin/python
# gui.py
'''UI for image processing project'''
__version__ = "1.3"
__author__ = 'beckwith'

import simple_img_processing as sip  # you will write your functions in this module
import advanced_img_processing as aip
import image_open  # for code to open image file with file dialog
import tkinter
from tkinter.font import Font

original_img = ""
new_image = ""

### fill in each of the 3 below for each new function ###
OPTIONS = [
    "Select Process:",  # [0]
    "Inversion",  # [1]
    "Lighten/Darken",  # [2]
    "Greyscale",  # [3]
    "Black and White",  # [4]
    "Filter",   # [5]
    "Reverse",  # [6]
    "Google Search",    # [7]
    "Edge Detection",    # [8]
    "Picture Frame",    # [9]
    "Image Comparison",     # [10]
    "Image Copier",     # [11]
    "Sepia Tone",   # [12]
    "Pixelate",     # [13]
    "Crop",     # [14]
]

# dictionary for instructions:
INSTRUCTIONS = {
    OPTIONS[0]: "nothing yet",
    OPTIONS[1]: "This will invert the colors of your image.  \nSelect an image and " +\
                "hit the START button to begin",
    OPTIONS[2]: "Select an image and drag the 2nd slider to the amount of brightness to change. " +\
                "Then hit the START button.\n" +\
                "This will change the brightness on the image.",
    OPTIONS[3]: "Select an image and this will make a greyscale of the image.",
    OPTIONS[4]: "Select an image and this will generate a black and white version of the image.",
    OPTIONS[5]: "Select an image, type the color filter in the 3rd box (red, green, or blue), and " +\
                "drag the 1st slider to the amount for it to change.",
    OPTIONS[6]: "Select an image and choose whether you want to flip the image over the x axis, y axis, or both. " +\
                "(Type true in the 3rd box for the x axis and/or true in the 4th box for the y axis.)",
    OPTIONS[7]: "Type the name of the image in the 3rd box and this will pull open images of it.",
    OPTIONS[8]: "Select an image and this will return the image with a line around the edge of the image.",
    OPTIONS[9]: "Choose an image and this will create a grey frame around the image.",
    OPTIONS[10]: "Select an image and this will choose a random image to compare it with." +\
                 "The lighter image will be given back.",
    OPTIONS[11]: "Choose an image and you will receive an image with 4 different versions of the original image in " +\
                 "the 4 corners of a single image. One will be the original, one will change its colors randomly, " +\
                 "one will be grey, and one will have a sepia tone.",
    OPTIONS[12]: "Select an image and this will give back the image in a sepia tone.",
    OPTIONS[13]: "Select an image, then type the pixels left to right in the third box and the pixel up to down " +\
                 "in the 4th box (try not to use values greater than the actual width & height).",
    OPTIONS[14]: "Choose your image and this will crop away some of the image.",
}
# dictionary for functions
FUNCTIONS = {
    OPTIONS[0]: None,
    OPTIONS[1]: sip.inversion,
    OPTIONS[2]: sip.lighten_darken,
    OPTIONS[3]: sip.greyscale,
    OPTIONS[4]: sip.black_and_white,
    OPTIONS[5]: sip.filter,
    OPTIONS[6]: sip.reverse,
    OPTIONS[7]: aip.google_search,
    OPTIONS[8]: aip.edge_detection,
    OPTIONS[9]: aip.picture_frame,
    OPTIONS[10]: aip.compare_images,
    OPTIONS[11]: aip.image_copier,
    OPTIONS[12]: aip.sepia_tone,
    OPTIONS[13]: aip.pixelate,
    OPTIONS[14]: aip.crop,

}

root = tkinter.Tk()  # the base window that all tkinter objects go into
root.title("\u2192\u2192\u2192 IMAGE PROCESSING \u27FF\u27FF\u27FF")
root.geometry("1000x400")
root.configure(background='grey')

positive_slider = tkinter.Scale(root, from_=0, to=100, orient="horizontal")
negative_slider = tkinter.Scale(root, from_=-150, to=150, orient="horizontal")

###################################
# FUNCTIONS CALLED BY MENU AND BUTTONS:
###################################
def quitting_time():
    '''called when Quit button is pressed'''
    root.quit()


def large_display(instructions):
    '''sets text in large display'''
    instructions_display.configure(state="normal")  # allow editing of text
    instructions_display.delete(1.0, tkinter.END)  # delete previous text
    instructions_display.insert(tkinter.END, instructions)  # show results in text area
    instructions_display.configure(state="disabled")  # prevent editing of text


def show_instructions(event):
    '''Called when menu item is selected and will show instructions'''

    selection = menu_var.get()  # get which item was selected
    instructions = INSTRUCTIONS[selection]
    #### PUT YOUR INSTRUCTIONS HERE #### 
    large_display(instructions)


def process():
    '''called when the process button is clicked'''

    global menu_var, instructions_display, entry_1, entry_2, entry_3
    global entry_4, input_area, results_label

    global original_img, new_image
    # gets values (as strings) from the entry boxes
    arg_1 = entry_1.get()
    arg_2 = entry_2.get()
    arg_3 = entry_3.get()
    arg_4 = entry_4.get()

    # get selected function and process image!!!!
    fn = None
    selection = menu_var.get()
    fn = FUNCTIONS[selection]

    if fn is not None and original_img != "":
        results_label.config(text="Working...")
        ##### call process function, sending it any agruments it needs #####
        if selection == OPTIONS[2]:
            new_image = fn(original_img, arg_2)
        elif selection == OPTIONS[5]:
            new_image = fn(original_img, arg_1, arg_3)
        elif selection == OPTIONS[6] or selection == OPTIONS[13]:
            new_image = fn(original_img, arg_3, arg_4)
        elif selection == OPTIONS[7]:
            fn(arg_3)
        else:
            new_image = fn(original_img)

        # EXAMPLE OF THOSE NEEDING MORE ARGUMENTS:

        results_label.config(text="Done!")
        # deletes old text and insert results text into the large text area:
        large_display("")

    elif fn is None:
        msg = "No process selected or not ready yet"
        if original_img == "":
            msg += "\nNo image selected!"
        results_label.config(text=msg)


def select_img():
    """calls code to bring up file open dialog and get image path"""
    global original_img
    image_folder = "./images/"

    original_img = image_open.prompt_and_get_file_name(image_folder)

    # show file path in label in gui:
    if original_img == "":
        file_msg = "NO IMAGE FILE SELECTED!"
    else:
        file_msg = "FILE:" + original_img

    results_label.config(text=file_msg)


def show():
    global new_image
    if new_image != "":
        sip.show(new_image)
    else:
        results_label.config(text="Select and process image first!")


def save():
    global new_image
    if new_image != "":
        sip.save(new_image)
    else:
        results_label.config(text="Select and process image first!")


def main():
    global menu_var, instructions_display, entry_1, entry_2, entry_3
    global entry_4, input_area, results_label
    ###################################
    # SET UP ALL THE DISPLAY COMPONENTS:
    ###################################

    # nice font:
    my_font = Font(family="Verdana", size=15, weight="bold")
    my_font2 = Font(family="Verdana", size=11, weight="bold")

    ###################################
    # 1. TEXT AREA THAT DISPLAYS RESULTS, USING THE ABOVE FONT
    ###################################
    instructions_display = tkinter.Text(root,  # display needs the tkinter window to be put in
                                        height=10,
                                        relief="ridge",
                                        bd=6,
                                        width=60,
                                        font=my_font,
                                        foreground='white',
                                        background='black')

    photo = tkinter.PhotoImage(file='python_icon.gif')  # fun photo to display at start
    # (PhotoImages must be .gif)

    instructions_display.configure(state="normal")  # allow editing of text
    instructions_display.image_create(tkinter.END, image=photo)  # inserts fun photo
    instructions_display.insert(tkinter.END, "Welcome to Image Processing using Python!")  # insesrts default text
    instructions_display.configure(state="disabled")

    ###################################
    # 3. TEXT LABEL THAT CAN SHOW RESULTS:
    ###################################
    results_label = tkinter.Label(text="STATUS INFO", foreground="red",
                                  background="black")  # default text is 'other info'

    ###################################
    # 4. BUTTONS
    ###################################

    # will call the select() function when pressed:
    select_img_button = tkinter.Button(text="SELECT IMG", command=select_img,
                                       foreground="green")
    select_img_button.config(font=my_font)
    # will call the process() function when pressed:
    process_button = tkinter.Button(text="===> START", command=process,
                                    foreground="blue")
    process_button.config(font=my_font2)

    show_button = tkinter.Button(text="SHOW", command=show, foreground="purple")
    show_button.config(font=my_font2)

    save_button = tkinter.Button(text="SAVE", command=save, foreground="red")
    save_button.config(font=my_font2)

    # will call quitting_time when pressed:
    quit_button = tkinter.Button(root, text="Quit", command=quitting_time,
                                 foreground="red")
    quit_button.config(font=my_font2)

    ###################################
    # 5. SET UP PULLDOWN MENU OF FUNCTION CHOICES:
    ###################################

    # this variable holds the selected value from the menu
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0])  # default value

    # create the optionmenu (pulldown menu) with the options above:
    option_menu = tkinter.OptionMenu(root, menu_var, *OPTIONS,
                                     command=show_instructions)
    option_menu.config(font=my_font, foreground="brown")

    ###################################
    # 6. PLACE EVERYTHING IN THE TKINTER WINDOW:
    #     a "grid" allows you to turn the tkinter window into a series
    #     of rows and columns and specifcy where to place everything
    ###################################

    select_img_button.grid(row=0, column=0, columnspan=1, padx=10, pady=10,
                           ipadx=5, ipady=5)

    # place the menu in the top left:
    option_menu.grid(row=0, column=1, columnspan=1, padx=10, pady=10,
                     ipadx=5, ipady=5)

    # place the buttons in the top middle:
    process_button.grid(row=0, column=2, columnspan=1, padx=10, pady=10,
                        ipadx=5, ipady=5)
    show_button.grid(row=0, column=3, columnspan=1, padx=10, pady=10,
                     ipadx=5, ipady=5)
    save_button.grid(row=0, column=4, columnspan=1, padx=10, pady=10,
                     ipadx=5, ipady=5)
    quit_button.grid(row=5, column=2, columnspan=3, padx=10, pady=10,
                     ipadx=5, ipady=5)

    # sets up argument input boxes...ADD MORE IF YOU NEED THEM!!!
    entry_1 = positive_slider
    entry_2 = negative_slider  # makes an Entry object
    entry_3 = tkinter.Entry()
    entry_4 = tkinter.Entry()

    # place the entry boxes in the next row, going across...ADD MORE IF NEEDED!!!
    entry_1.grid(row=1, column=0)
    entry_2.grid(row=1, column=1)
    entry_3.grid(row=1, column=2)
    entry_4.grid(row=1, column=3)

    # place the label in the next row (is just one row of text):
    results_label.grid(row=3, column=0, columnspan=5)

    # place the text areas in the next row (is a whole box of text):
    instructions_display.grid(row=4, column=0, columnspan=6)
    # make it so that words won't get broken up when reach end of text box:
    instructions_display.config(wrap=tkinter.WORD)

    # waits for button clicks to take actions:
    root.mainloop()


if __name__ == "__main__":
    main()
