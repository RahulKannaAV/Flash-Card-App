BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random


window = Tk()
window.title('Flash Card App')
window.config(background=BACKGROUND_COLOR, padx=50, pady=50, height=1000, width=1000)


cross = PhotoImage(file=r"C:\Users\ARJUN RAHUL VIJI\PycharmProjects\100DaysOfCode\Day_31_Flash_Card_App\images\wrong.png")
tick = PhotoImage(file=r"C:\Users\ARJUN RAHUL VIJI\PycharmProjects\100DaysOfCode\Day_31_Flash_Card_App\images\right.png")
back = PhotoImage(file=r"C:\Users\ARJUN RAHUL VIJI\PycharmProjects\100DaysOfCode\Day_31_Flash_Card_App\images\card_back.png")
front = PhotoImage(file=r"C:\Users\ARJUN RAHUL VIJI\PycharmProjects\100DaysOfCode\Day_31_Flash_Card_App\images\card_front.png")

try:
    french = pd.read_csv('words_to_learn.csv')
    if len(french.axes[0]) > 1:
        dict = french.to_dict('records')
    else:
        raise IndexError

except FileNotFoundError:
    french = pd.read_csv('data/french_words.csv')
    dict = french.to_dict(orient='records')
except IndexError:
    french = pd.read_csv('data/french_words.csv')
    dict = french.to_dict(orient='records')

def random_word():
    global pick,engl
    try:
        pick = random.choice(dict)
        button_front.itemconfig(image, image=front)
        button_front.itemconfig(language, text='French', fill='black')
        button_front.itemconfig(french_word, text=pick['French'], fill='black')
        engl = window.after(3000, change)
        fren = [i['French'] for i in dict]
        eng = [i['English'] for i in dict]
        words_to_learn = pd.DataFrame({'French': fren, 'English': eng})
        words_to_learn.to_csv('words_to_learn.csv', index=False)
    except IndexError:
        print('You have understood all the necessary words for Basic Uses')
        quit()



def change():
    button_front.itemconfig(image, image=back)
    button_front.itemconfig(language, text='English', fill='white')
    button_front.itemconfig(french_word, text=pick['English'], fill='white')
    window.after_cancel(engl)
    fren = [i['French'] for i in dict]
    eng = [i['English'] for i in dict]
    words_to_learn = pd.DataFrame({'French': fren, 'English': eng})
    words_to_learn.to_csv('words_to_learn.csv', index=False)


def wrong():
    global pick
    dict.pop(dict.index(pick))
    random_word()



window.after(3000,random_word)

button_cross = Button(image=cross, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
button_tick = Button(image=tick, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
button_back = Canvas(width=830, height=540, bg=BACKGROUND_COLOR, highlightthickness=0)
button_front = Canvas(width=830, height=540, bg=BACKGROUND_COLOR, highlightthickness=0)
image = button_front.create_image(410,270,image=front)
language = button_front.create_text(410,150, text='Welcome', font=('Arial',40,'italic'))
french_word = button_front.create_text(410, 263, text='Flash Card', font=('Arial',60,'bold'))


button_front.grid(row=0, column=0, columnspan=2)
button_cross.grid(row=1, column=0, padx=50)
button_tick.grid(row=1, column=1, padx=50)




window.mainloop()
