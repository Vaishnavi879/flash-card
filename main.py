from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
row_number=0
prev_word=None
current_word=None

def right_next_word():
    global row_number
    global prev_word
    prev_word=row_number
    print(len(df.index))
    df.drop([prev_word],inplace=True)
    df.to_csv("data/words_to_learn.csv", index=False)
    wrong_next_word()

def wrong_next_word():
    global row_number
    global current_word
    row_number=random.randint(1,number_of_words-1)
    current_word=df["french"].values[row_number]
    canvas.itemconfig(card_image, image=image1)
    canvas.itemconfig(text1, text="French",fill="black")
    canvas.itemconfig(text2,text=current_word,fill="black")
    windows.after(3000,func=change_to_english)

def change_to_english():
    global row_number
    canvas.itemconfig(card_image,image=image2)
    canvas.itemconfig(text1,text="English",fill="white")
    english_word=df["english"].values[row_number]
    canvas.itemconfig(text2,text=english_word,fill="white")


# *********************************USER INTERFACE*********************************************

# df=pd.read_csv("data/french_words.csv")
# number_of_words=len(df.index)

try:
    with open("data/words_to_learn.csv","r") as file:
        df=pd.read_csv(file)
        number_of_words=len(df.index)
except FileNotFoundError:
    with open("data/words_to_learn.csv", "w") as file:
        df = pd.read_csv("data/french_words.csv")
        number_of_words = len(df.index)
        # file.write(df.to_csv(index=False))
        df.to_csv("data/words_to_learn.csv",index=False)

windows=Tk()
windows.title("Flashy")
windows.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
image1=PhotoImage(file="images/card_front.png")
image2=PhotoImage(file="images/card_back.png")
card_image=canvas.create_image(400,263,image=image1)
text1=canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
text2=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

image_wrong=PhotoImage(file="images/wrong.png")
button1=Button(image=image_wrong,highlightthickness=0,command=wrong_next_word)
button1.grid(row=1,column=0)

image_right=PhotoImage(file="images/right.png")
button2=Button(image=image_right,highlightthickness=0,command=right_next_word)
button2.grid(row=1,column=1)

windows.mainloop()