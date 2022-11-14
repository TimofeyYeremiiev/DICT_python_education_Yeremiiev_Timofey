import random
from tkinter import *

lives = 8
entered_letters = []
current_word = ""
WORDS_FOR_GAME = ["python",
                  "java",
                  "javascript",
                  "php",
                  "html",
                  "hai",
                  "potato",
                  "futuristic",
                  "cache",
                  "list",
                  "hash",
                  "pycharm",
                  "discord"]


def close_game() -> None:
    window.destroy()


def start_game() -> None:
    global lives
    global entered_letters
    entered_letters = []
    lives = 8
    lbl_2.configure(text="Угадай слово!")
    btn_start.grid_forget()
    entry_field.grid(column=0, row=4)
    lbl_2.grid(column=0, row=2)
    lbl_word.grid(row=3)
    button_try_letter.grid(column=0, row=5)
    global current_word
    current_word = random.choice(WORDS_FOR_GAME)
    fill_label()


def fill_label() -> None:
    to_fill = ""
    for b in list(current_word):
        if b in entered_letters:
            to_fill += b
        else:
            to_fill += "-"
    lbl_word.configure(text=str(to_fill))


def check_is_word_done() -> bool:
    entered_letters2 = entered_letters.copy()
    entered_letters2.append(list(entry_field.get())[0])
    is_all_done = True
    for b in list(current_word):
        if b in entered_letters2:
            pass
        else:
            is_all_done = False
    return is_all_done


def try_letter() -> None:
    global lives
    if check_is_word_done():
        entry_field.grid_forget()
        lbl_2.configure(text="Вы выиграли! Было загадано слово: ")
        lbl_word.configure(text=current_word)
        button_try_letter.grid_forget()
        btn_start.grid(column=0, row=4)
        btn_start.configure(text="Начать заново")
        return
    if (not (list(entry_field.get())[0] in entered_letters)) and (list(entry_field.get())[0] in list(current_word)):
        pass
    else:
        lives -= 1
        if lives < 0:
            entry_field.grid_forget()
            lbl_2.configure(text="Вы проиграли! Было загадано слово: ")
            lbl_word.configure(text=current_word)
            button_try_letter.grid_forget()
            btn_start.grid(column=0, row=4)
            btn_start.configure(text="Начать заново")
            return
    entered_letters.append(list(entry_field.get())[0])
    lbl_2.configure(text="Осталось попыток: " + str(lives))
    fill_label()
    pass


window = Tk()
window.title("Hangman")

entry_field = Entry(window, width=10, font=("Arial Bold", 30))
lbl_2 = Label(window, text="Угадай слово!", font=("Arial Bold", 20))
button_try_letter = Button(window, text="Предположить букву", font=("Arial Bold", 20), command=try_letter)
lbl_word = Label(window, text="-", font=("Arial Bold", 20))

lbl = Label(window, text="HANGMAN GAME", font=("Arial Bold", 30))
lbl.grid(column=0, row=0)

btn_start = Button(window, text="Начать игру!", font=("Arial Bold", 30), command=start_game)
btn_start.grid(column=0, row=2)
btn_exit = Button(window, text="Выйти", font=("Arial Bold", 30), command=close_game)
btn_exit.grid(column=0, row=10)

window.mainloop()
