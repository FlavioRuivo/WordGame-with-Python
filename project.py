import random
import sys
from tkinter import *

from PIL import Image, ImageTk

# global language
# global level
selected_list_words = []


def main():
    global window
    global help_control
    help_control = 0
    window = Tk()
    window.title("Find Words v2")
    window.geometry("1400x900+250+50")
    window.resizable(False, False)

    # Load the image
    global photo_letter_bg
    global photo_think
    global photo_ok
    global photo_not_ok
    image_ok = Image.open("data\ok.png")
    photo_ok = ImageTk.PhotoImage(image_ok)
    image_not_ok = Image.open("data\ok_not.png")
    photo_not_ok = ImageTk.PhotoImage(image_not_ok)
    image_think = Image.open("data\my_think.png")
    photo_think = ImageTk.PhotoImage(image_think)
    image_magic = Image.open("data\magic_wand.png")
    photo_magic = ImageTk.PhotoImage(image_magic)
    image_mixer = Image.open("data\mixer.png")
    photo_mixer = ImageTk.PhotoImage(image_mixer)
    image_header = Image.open("data\header.png")
    photo_header = ImageTk.PhotoImage(image_header)
    image_body = Image.open("data\my_body.png")
    photo_body = ImageTk.PhotoImage(image_body)
    image_letter_bg = Image.open("data\letter_bg.png")
    photo_letter_bg = ImageTk.PhotoImage(image_letter_bg)
    image_help = Image.open("data\help.png")
    photo_help = ImageTk.PhotoImage(image_help)

    # header background
    label_header = Label(window, image=photo_header, height=250)
    label_header.place(x=0, y=0)
    # body background
    label_body = Label(window, image=photo_body, height=650)
    label_body.place(x=0, y=250)

    # label language
    global lbl_lang
    lbl_lang = Label(window, text=translate(" ", 0), bg="#47475f",
                     fg='red', font=("Helvetica", 14))
    lbl_lang.place(x=40, y=17)

    # label level
    global lbl_level
    lbl_level = Label(window, text=translate(" ", 1), bg="#47475f",
                      fg='red', font=("Helvetica", 14))
    lbl_level.place(x=40, y=87)

    # label high score
    global lbl_high_score
    lbl_high_score = Label(window, text=translate(" ", 5), bg="#47475f",
                           fg='green', font=("Helvetica", 18, "bold"))
    lbl_high_score.place(x=1170, y=20)

    # label high score number
    global var_new_high_score_n
    var_new_high_score_n = IntVar(value=0)
    lbl_high_score_n = Label(window, text=high_score(0), bg="#47475f", textvariable=var_new_high_score_n,
                             fg='white', font=("Helvetica", 16, "bold"))
    lbl_high_score_n.place(x=1170, y=53)

    # label my score
    global lbl_score
    lbl_score = Label(window, text=translate(" ", 6), bg="#47475f",
                      fg='green', font=("Helvetica", 16, "bold"))
    lbl_score.place(x=1170, y=90)

    # label my score number
    global var_my_score_n
    var_my_score_n = IntVar(value=0)
    lbl_score_n = Label(window, text="03", bg="#47475f", textvariable=var_my_score_n,
                        fg='white', font=("Helvetica", 14, "bold"))
    lbl_score_n.place(x=1170, y=120)

    # get high score
    var_new_high_score_n.set(high_score(0))

    # radiobutton language
    global var_lang
    var_lang = StringVar(value="EN")
    # var_lang.set(0)
    global r1
    global r2
    r1 = Radiobutton(window, text="PT", variable=var_lang, value="PT", bg="#47475f", font=("Helvetica", 12),
                     command=check_if_radiobutton_lang_selected)
    r2 = Radiobutton(window, text="EN", variable=var_lang, value="EN", bg="#47475f", font=("Helvetica", 12),
                     command=check_if_radiobutton_lang_selected)
    r1.place(x=40, y=40)
    r2.place(x=40, y=60)

    # radiobutton level
    global var_level
    var_level = IntVar(value=4)
    # var_level.set(0)
    global r3
    global r4
    global r5
    r3 = Radiobutton(window, text="Easy", variable=var_level, bg="#47475f", font=("Helvetica", 12),
                     value=4, command=check_if_radiobutton_level_selected)
    r4 = Radiobutton(window, text="Medium", variable=var_level, bg="#47475f", font=("Helvetica", 12),
                     value=6, command=check_if_radiobutton_level_selected)
    r5 = Radiobutton(window, text="Advanced", variable=var_level, bg="#47475f", font=("Helvetica", 12),
                     value=8, command=check_if_radiobutton_level_selected)
    r3.place(x=40, y=110)
    r4.place(x=40, y=133)
    r5.place(x=40, y=156)

    # button get random word Mixed word
    btn_mixed = Button(window, image=photo_mixer, height=150, width=150, fg='blue',
                       font=('Arial', 16), bd=15, command=myClick_random)
    btn_mixed.place(x=600, y=50)

    # words
    global txtfld
    txtfld = Entry(window, width=15, font=('Arial 90'),
                   text="Give here your solution", bd=15)
    txtfld.place(x=70, y=550)

    # button check Result
    btn_result = Button(window, text="Result", image=photo_magic, height=145, width=145, fg='blue',
                        font=('Arial', 16), bd=15, command=myClick_check)
    btn_result.place(x=1160, y=545)

    # button get help
    btn_help = Button(window, image=photo_help, height=50, width=50, fg='blue',
                      font=('Arial', 16), bd=10, command=myClick_help)
    btn_help.place(x=1300, y=170)

    # label help
    global lbl_help
    lbl_help = Label(window, text=translate(" ", 7), bg="#47475f",
                     fg='yellow', font=("Helvetica", 8, "italic"))
    lbl_help.place(x=40, y=190)

    window.bind("<Return>", (lambda event: myClick_check()))
    window.bind("<space>", (lambda event: myClick_random()))
    window.bind("<F1>", (lambda event: myClick_help()))

    window.mainloop()


def check_if_radiobutton_lang_selected():
    # function language
    selected_option_lang = var_lang.get()
    if selected_option_lang == "":
        print("No option selected.")
    else:
        print(f"Selected option : {selected_option_lang }")
        lbl_lang.config(text=translate(selected_option_lang, 0))
        lbl_level.config(text=translate(selected_option_lang, 1))
        r3.config(text=translate(selected_option_lang, 2))
        r4.config(text=translate(selected_option_lang, 3))
        r5.config(text=translate(selected_option_lang, 4))
        lbl_high_score.config(text=translate(selected_option_lang, 5))
        lbl_score.config(text=translate(selected_option_lang, 6))
        lbl_help.config(text=translate(selected_option_lang, 7))
        return selected_option_lang


# function level
def check_if_radiobutton_level_selected():
    selected_option_level = var_level.get()
    if selected_option_level == "":
        print("No option selected.")
    else:
        print(f"Selected option : {selected_option_level}")
        return selected_option_level


# Function to clear the Entry field
def clear_entry():
    txtfld.delete(0, 'end')


def myClick_random():
    # function set ramdom word
    global score_control
    score_control = 1
    # clean entry
    clear_entry()
    global my_word
    my_word = choice_word(
        check_if_radiobutton_lang_selected(), check_if_radiobutton_level_selected())
    # space to mixed word
    x = 0
    for n in "liteight":
        label_l = Label(window, image=photo_letter_bg, bd=0)
        label_l.place(x=70+x, y=300)
        x += 160
    k = 0
    global my_word_mixed
    my_word_mixed = random.sample(
        my_word, check_if_radiobutton_level_selected())
    for n in my_word_mixed:
        label_l = Label(window, text=n, fg='black',
                        bg="white", font=("Helvetica", 70))
        label_l.place(x=110+k, y=320)
        k += 160
    # waiting answers
    label_think = Label(window, image=photo_think, bd=0)
    label_think.place(x=650, y=750)
    print("random: ", my_word)
    print("random: ", my_word_mixed)


def help_entry(txt):
    # Define a function to change the value
    txtfld.delete(0, 'end')
    txtfld.insert(0, txt)


def myClick_help():
    # function help
    global help_control
    help_control = 1
    txt_help = my_word[0:int(len(my_word)/2)]
    help_entry(txt_help)


def my_score_help_half(add_score, level):
    add_score_half = add_score-level/2
    return int(add_score_half)


def my_score():
    global help_control
    add_score = int(var_my_score_n.get())
    if var_level.get() == 4:
        add_score = add_score+4
        if help_control == 1:
            add_score = my_score_help_half(add_score, var_level.get())
            help_control = 0
    elif var_level.get() == 6:
        add_score = add_score+6
        if help_control == 1:
            add_score = my_score_help_half(add_score, var_level.get())
            help_control = 0
    elif var_level.get() == 8:
        add_score = add_score+8
        if help_control == 1:
            add_score = my_score_help_half(add_score, var_level.get())
            help_control = 0

    var_my_score_n.set(add_score)
    # set new high score
    var_new_high_score_n.set(high_score(add_score))


def myClick_check():
    # function check right/wrong
    if my_word == txtfld.get().strip():
        # Label widget to display the image
        label_ok = Label(window, image=photo_ok, bd=0)
        label_ok.place(x=650, y=750)
        # get/set score
        global score_control
        if score_control == 1:
            my_score()
            score_control = 0
    else:
        label_not_ok = Label(window, image=photo_not_ok, bd=0)
        label_not_ok.place(x=650, y=750)



def translate(l, p):
    if l == "PT":
        pt = ["Escolher Lingua: ", "Escolher Nivel: ",
              "Fácil (4p)", "Médio (6p)", "Dificil (8p)", "Pontuação Máxima:", "Pontuação:", "Metade dos pontos se usar ajuda"]
        return pt[p]
        print("pt_t")
    elif l == "EN":
        en = ["Choose Language: ", "Choose Level: ",
              "Easy (4p)", "Medium (6p)", "Advanced (8p)", "High Score:", "Score:", "Half the points if you use help"]
        return en[p]
        print("en-t")
    else:
        en = ["Choose Language: ", "Choose Level: ",
              "Easy (4p)", "Medium (6p)", "Advanced (8p)", "High Score:", "Score:", "Half the points if you use help"]
        return en[p]
        print("en-t")


def choice_word(lang, level):
    try:
        if lang == "PT":
            language = "data\words_PT.txt"
        else:
            language = "data\words_EN.txt"
        # clear list
        selected_list_words.clear()
        with open(language, "r") as file:
            lines = file.readlines()
            for n in lines:
                if len(n.strip()) == level:
                    selected_list_words.append(n)

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        # print(selected_list_words, end="\n")
        selected_word = random.choice(selected_list_words).strip()

        # print("random: " + selected_word)
        # print("random: ", random.sample(selected_word, level))
        return(selected_word)


def high_score(hs):
    score_file = "data\score.txt"
    with open(score_file, "r") as file:
        line = file.readlines()
        if hs > int(line[0]):
            with open(score_file, 'w') as file:
                file.write(str(hs))
                print("new winner")
            return hs
        else:
            return int(line[0])




if __name__ == "__main__":
    main()
