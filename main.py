from tkinter import *
import pandas as pd
import random as r
import time


BACKGROUND_COLOR = "#B1DDC6"


try: 
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/polske_ord.csv")


polsk_norsk_dict = data.to_dict(orient="records")
current_card = {}


words_to_learn = polsk_norsk_dict 

def word_known():
  words_to_learn.remove(current_card)
  update_word()
  new_data = pd.DataFrame(words_to_learn)
  new_data.to_csv("./data/words_to_learn.csv", index=False)
  

def next_card():
  global current_card
  new_word = r.choice(words_to_learn)
  current_card = new_word
  return (new_word["Polsk"], new_word["Norsk"])

def update_word():
  global flip_timer
  screen.after_cancel(flip_timer)
  new_word = next_card()
  canvas.itemconfig(canvas_image, image=canvas_front_image)
  canvas.itemconfig(tittel, text='Polsk', fill="black")
  canvas.itemconfig(polsk_glose, text=new_word[0], fill="black")
  flip_timer = screen.after(3000, flip)





def flip():
  global current_card
  canvas.itemconfig(tittel, text="Norsk", fill="white")
  canvas.itemconfig(polsk_glose, text=current_card["Norsk"], fill="white")
  canvas.itemconfig(canvas_image, image=canvas_back_image)

screen = Tk()
screen.title("Pugger")
screen.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = screen.after(3000, flip)

canvas_front_image = PhotoImage(file="./images/card_front.png")
canvas_back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,)
canvas.grid(row=0, column=0, columnspan=2)
canvas_image = canvas.create_image((400,263), 
image=canvas_front_image)

tittel = canvas.create_text((400, 150), text="", font=("Ariel", 40, "italic"), fill="black")
polsk_glose = canvas.create_text((400, 263), text="", font=("Ariel", 60, "bold"), fill='black')


    
  


wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, highlightbackground=BACKGROUND_COLOR, command=update_word)
wrong_button.grid(row=1, column=0)


right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, borderwidth=0, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=word_known)
right_button.grid(row=1, column=1)

update_word()

screen.mainloop()