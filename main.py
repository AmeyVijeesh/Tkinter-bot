from tkinter import *
import webbrowser
import pyttsx3
from datetime import datetime
import time
from PIL import Image, ImageTk
import random
import Dialogs

root = Tk()
root.title("bot")
root.geometry("750x600")
root.resizable(False, False)

bot_name = "Bot"
user_name = open("UserData/name.txt")
name = user_name.readline()

image = open("UserData/Background.txt")
img = image.readline()

user_name.close()
image.close()


def settings():
    window = Toplevel()
    window.geometry("650x500")

    bg1 = ImageTk.PhotoImage(file="Images/BackgroundImage1.jpeg")
    bg2 = ImageTk.PhotoImage(file="Images/BackgroundImage3.jpeg")
    bg3 = ImageTk.PhotoImage(file="Images/BackgroundImage2.jpeg")

    def preview_img():
        preview = Toplevel()
        preview.geometry("750x650")
        preview.resizable(False, False)

        def add_image1():
            img_label['image'] = bg1

        def add_image2():
            img_label['image'] = bg2

        def add_image3():
            img_label['image'] = bg3

        img_label = Label(preview, image=bg1)
        img_label.place(x=0, y=0)

        img1_btn = Button(preview, text='Image 1', highlightbackground="black", command=add_image1)
        img1_btn.place(x=50, y=10)

        img2_btn = Button(preview, text='Image 2', highlightbackground="black", command=add_image2)
        img2_btn.place(x=350, y=10)

        img3_btn = Button(preview, text='Image 3', highlightbackground="black", command=add_image3)
        img3_btn.place(x=650, y=10)

        pre_text = Text(preview, highlightbackground='black', highlightthickness=4, state="disabled")
        pre_text.place(x=100, y=100)

        pre_entry = Entry(preview, state="readonly")
        pre_entry.place(x=280, y=450)

    def change():
        new_name = entry.get()

        with open("UserData/name.txt", "w") as file:
            file.write(new_name)
    user_details = f"UserName: {name} \n Account created: False \n"
    details_label = Label(window, text=user_details)
    details_label.pack()

    def img1():
        label1['image'] = bg1

    def img2():
        label1['image'] = bg2

    def img3():
        label1['image'] = bg3

    entry = Entry(window)
    entry.pack()

    btn = Button(window, text='Change your name', command=change)
    btn.pack()

    btn1 = Button(window, text='Image 1', command=img1)
    btn1.pack()

    btn2 = Button(window, text='Image 2', command=img2)
    btn2.pack()

    btn3 = Button(window, text='Image 3', command=img3)
    btn3.pack()

    button3 = Button(window, text='Preview', command=preview_img)
    button3.pack()


def insert(result):
    text.insert("1.0", f'{bot_name}: {result}\n')


def enter_clicked(argument=None):
    user_command = (user_input.get()).lower()
    print(user_command)
    text.insert("1.0", f"{name}: {user_command}\n")

    if "open" in user_command:
        if "google" in user_command:
            insert("Opening Google")
            webbrowser.open_new_tab("https://google.com")

        elif "mail" in user_command:
            if "google mail" in user_command:
                insert("Opening Google mail")
                webbrowser.open_new_tab("https://mail.google.com")

            elif "outlook" in user_command:
                insert("Opening Outlook")
                webbrowser.open_new_tab("https://outlook.com")

        elif "bing" in user_command:
            text.insert("1.0", f'Bot: Opening https://bing.com \n')

        # Other websites

    elif "https://" in user_command:
        insert(f"Opening {user_command}")
        webbrowser.open_new_tab(user_command)

    elif "hi" in user_command or "hello" in user_command:
        greetings = random.choice(Dialogs.greetings)
        insert(f'{greetings} \n ')

    elif "how are you" in user_command:
        hru_response = random.choice(Dialogs.hru_response)
        insert(f'{hru_response}')

    elif "time" in user_command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        insert(f'The time is - {current_time}')

    else:
        insert("I am not sure what to do")


bg1 = ImageTk.PhotoImage(file=img)
label1 = Label(root, image=bg1)
label1.place(x=0, y=0)

settings_photo = (Image.open("Images/Settings.png"))
settings_resize = settings_photo.resize((40, 40))
settings_img = ImageTk.PhotoImage(settings_resize)

settings_button = Button(root, image=settings_img, highlightbackground='white', relief='flat', command=settings)
settings_button.place(x=680, y=50)

user_input = Entry(root)
user_input.focus_set()
user_input.place(x=280, y=450)

btn = Button(root, text='Enter', command=enter_clicked)
btn.place(x=100, y=50)
text = Text(root, highlightbackground='black', highlightthickness=4)
text.place(x=100, y=100)

root.bind('<Return>', enter_clicked)

root.mainloop()
