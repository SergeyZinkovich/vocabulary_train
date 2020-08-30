from tkinter import *
from engine import *

window = Tk()
window.title("Учим английский, или че то там делаем")
window.geometry('1000x1000')

selectedThem = IntVar()
selectedThem.set(-1)
selectedType = IntVar()
selectedType.set(0)


def clear_window():
    for i in window.grid_slaves():
        i.destroy()


def start_lesson():
    Engine.start_lesson(selectedThem.get(), selectedType.get())
    show_word_question()


def show_word_question():
    clear_window()
    word = Engine.get_word()
    lbl = Label(window, text=word[0], font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)

    inpt = Entry()
    inpt.grid(column=1, row=0)

    btn = Button(window, text="Проверить", font=("Arial Bold", 16), command=check_answer)
    btn.grid(column=1, row=3)


def check_answer():
    window.winfo_children()[-1].destroy()

    if Engine.get_word()[1] == window.winfo_children()[-1].get():
        Engine.pass_word(True)
        lbl = Label(window, text='Верно', font=("Arial Bold", 20))
        lbl.grid(column=2, row=0)
    else:
        Engine.pass_word(False)
        lbl = Label(window, text='Неверно', font=("Arial Bold", 20))
        lbl.grid(column=2, row=0)

    if Engine.has_next_word():
        btn = Button(window, text="Далее", font=("Arial Bold", 16), command=show_word_question)
        btn.grid(column=1, row=3)
    else:
        btn = Button(window, text="В меню", font=("Arial Bold", 16), command=show_menu)
        btn.grid(column=1, row=3)


def show_menu():
    clear_window()

    lbl = Label(window, text="Урок", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)

    rad1 = Radiobutton(window, text='Все', value=-1, variable=selectedThem)
    rad1.grid(column=0, row=1, sticky=W)
    for i, them in enumerate(Engine.get_themes()):
        rad = Radiobutton(window, text=them, value=i, variable=selectedThem)
        rad.grid(column=0, row=2 + i, sticky=W)

    lbl = Label(window, text="Тип", font=("Arial Bold", 20))
    lbl.grid(column=1, row=0, padx=50, pady=10)

    rad2 = Radiobutton(window, text='С русского на английский', value=0, variable=selectedType)
    rad2.grid(column=1, row=1, sticky=W, padx=50, pady=10)
    rad2 = Radiobutton(window, text='С английского на русский', value=1, variable=selectedType)
    rad2.grid(column=1, row=2, sticky=W, padx=50, pady=10)
    # rad2 = Radiobutton(window, text='Случайно для каждого слова', value=2, variable=selectedType)
    # rad2.grid(column=1, row=3, sticky=W, padx=50, pady=10)

    btn = Button(window, text="Начать", font=("Arial Bold", 20), command=start_lesson)

    btn.grid(column=2, row=0, padx=50, pady=10)


show_menu()
window.mainloop()
