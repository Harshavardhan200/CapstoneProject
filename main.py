BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
try:
    data = pd.read_csv('ready_to_learn.csv')
    dict1 = data.to_dict(orient='records')
except FileNotFoundError:
    data = pd.read_csv('french_words.csv')
    dict1 = data.to_dict()
    dataframe = pd.DataFrame(dict1)
    dataframe.to_csv('ready_to_learn.csv')
else:
    random_word = {}
# ---------------------------- FRENCH WORDS ------------------------------- #
def french():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(dict1)
    canvas.itemconfig(image, image=old_image)
    canvas.itemconfig(code_word, text='French')
    canvas.itemconfig(code, text=random_word['French'])
    flip_timer = window.after(1000, func=english)
# ---------------------------- ENGLISH WORDS ------------------------------- #
def english():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(image, image=new_image)
    canvas.itemconfig(code_word, text='English')
    canvas.itemconfig(code, text=random_word['English'])
    flip_timer = window.after(1000, func=french)
# ---------------------------- REMOVED LIST ------------------------------- #
def delete():
    try:
        dict1.remove(random_word)
        dat = pd.DataFrame(dict1)
        print(len(dict1))
        dat.to_csv('ready_to_learn.csv')
        french()
    except:
        french()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Capstone Project')
flip_timer = window.after(1000, func=french)
window.config(padx=40, pady=40, highlightthickness=0, bg=BACKGROUND_COLOR)
old_image = PhotoImage(file='card_back.png')
new_image = PhotoImage(file='card_front.png')
cross_symbol = PhotoImage(file='wrong.png')
correct_symbol = PhotoImage(file='right.png')
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
cross = Button(image=cross_symbol, highlightthickness=0, command=french)
correct = Button(image=correct_symbol, highlightthickness=0, command=delete)
image = canvas.create_image(400, 263, image=old_image)
code_word = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
code = canvas.create_text(400, 263, text='Text', font=('Arial', 65, 'bold'))
french()
canvas.grid(column=0, row=0, columnspan=2)
cross.grid(column=0, row=1)
correct.grid(column=1, row=1)
window.mainloop()