import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import random


# ------------ VARIABLES ----------------/

BG1 = "SkyBlue2"
BG2 = 'green'
BG3 = 'grey'
BG4 = 'black'
BG5 = '#E8E4C9'  # kind of pale yellow
BG6 = '#336B7D'
FONT1 = ("Courier New", 18, "bold")
FONT2 = ("Courier New", 14, "bold")
FONT3 = ("Helvetica", 16, "bold")
FONT4 = "TkDefaultFont", 24, "bold"

start_time = 0
end_time = 0
number_of_char = 0
highlight_word_index = 0

# -----------Word lists -----------/

phrase1 = "The sun is shining, the birds are singing, and the flowers are in full bloom. " \
          "The sound of children laughing can be heard in the distance. A gentle breeze blows through the trees, " \
          "rustling the leaves. The world seems at peace, and all is right. A dog barks in the distance, " \
          "breaking the tranquility. But even that sound adds to the beauty of the moment. " \
          "Life is good, and there is much to be grateful for. We should take the time to appreciate " \
          "these simple pleasures that make life so wonderful."

phrase2 = "The stars twinkle in the night sky like diamonds on black velvet. " \
          "Each one seems to have a personality of its own, shining brightly and beckoning to us. " \
          "Looking up at them, we can't help but feel small and insignificant, " \
          "yet at the same time awestruck by their beauty and majesty. " \
          "Stars have captivated humans for centuries, inspiring countless stories and myths. " \
          "They remind us of our place in the universe and our endless curiosity about the unknown."

phrase3 = "Noah was a righteous man who followed God's commands to build an ark. " \
          "He gathered two of every kind of animal and saved them from the flood. " \
          "His faith in God saved him and his family. Noah's story is a testament to " \
          "the power of faith and obedience."

list_of_phrases = [phrase1, phrase2, phrase3]
random_phase_list = random.choice(list_of_phrases)
words = random_phase_list.split()

# ------------- Define Functions --------------------/

def evaluate(value):
    global start_time
    # typing what the user has entered
    write_char = tp.get('1.0', 'end-1c')            # end-1c removes the line break
    breaks = write_char.count('\n')
    global number_of_char
    number_of_char = len(write_char)-breaks         # total nro char written removing each break created by char
    counter_label.config(text=str(number_of_char))
    progressbar1['value'] = number_of_char/3        # reduce bar progress by 3
    if number_of_char == 1:
        global start_time
        start_time = time.time()
        progressbar1.config(style='green.Horizontal.TProgressbar')
    elif number_of_char < 200:
        progressbar1.config(style='green.Horizontal.TProgressbar')
    elif number_of_char >= 300:
        progressbar1.config(style='red.Horizontal.TProgressbar')
        # t1.delete('end-2c')
        global end_time
        end_time = time.time()
        total_time = (end_time - start_time)
        speed_tracker.config(text=str('{0:.2f}'.format(total_time)))
        print(total_time)
        print(number_of_char)
        print(total_time/number_of_char)
        typing_speed.config(text=str(f'Your total typing speed is {number_of_char/(total_time/60)} chars per minute'))
    else:
        progressbar1.config(style='yellow.Horizontal.TProgressbar')


def highlight_current_word():
    # Remove the highlight from the previous word
    global words
    if highlight_word_index > 0:
        start_index = "1.%d" % sum(len(w) + 1 for w in words[:highlight_word_index - 1])
        end_index = "1.%d" % (sum(len(w) + 1 for w in words[:highlight_word_index]) - 1)
        text_widget.tag_remove("highlight", start_index, end_index)

    # Get the start and end index of the current word and highlight it in yellow
    start_index = "1.%d" % sum(len(w) + 1 for w in words[:highlight_word_index])
    end_index = "1.%d" % (sum(len(w) + 1 for w in words[:highlight_word_index + 1]) - 1)
    print(start_index, end_index)
    text_widget.tag_add("highlight", start_index, end_index)
    text_widget.tag_config("highlight", background=BG3, font=FONT4)
    text_widget.tag_config("highlight", background=BG3)


def on_key_press(event):
    global highlight_word_index
    # Check if the pressed key is a space
    print("Space bar pressed!")
    if event.keysym == "space":
        # Increment the word index and highlight the next word
        highlight_word_index += 1
        print(highlight_word_index)
        highlight_current_word()


# ----- WINDOW WIDGET AREA ------------------- /

window = tk.Tk()
window.geometry('800x800')
window.configure(bg=BG1)
window.iconbitmap('assets/photo.ico')
window.title('Typing Speed App')

# ------ Create the frames -------------

# creating Read_From frame
frame1 = tk.LabelFrame(window, width=600, height=200, bg=BG3, text='Read Frame')
frame1.configure(background=BG3, font=FONT1)
frame1.grid(row=0, column=0, padx=30, pady=10)
frame1.grid_propagate(False)

# Insert the text to the Text widget and highlight the first word in yellow
text = words
text_widget = tk.Text(frame1)
text_widget.grid(row=0, column=0, padx=10, pady=10)
text_widget.focus_set()
text_widget.bind("<space>", on_key_press)
text_widget.insert("1.0", text)
highlight_current_word()


# typewriter window 'tp'
tp = Text(window, height=10, width=75, bg=BG3)
tp.configure(font=FONT2)
tp.grid(row=1, column=0, padx=30, pady=10)
window.bind("<space>", on_key_press)

# Counter Label widgets
counter_label_title = Label(window, text="Character Counter", bg=BG1, font=FONT3)
counter_label_title.grid(row=2, column=0, padx=30, pady=30, sticky=W)

counter_label = Label(window, text=0, width=3, bg=BG6)
counter_label.grid(row=2, column=0, padx=30, pady=30)

#Speed Tracker Widgets
speed_tracker_label = Label(window, text="Elapsed Time in seconds", bg=BG1, font=FONT3)
speed_tracker_label.grid(row=3, column=0, padx=30, pady=10, sticky=W)

speed_tracker = Label(window, text="", width=20, bg=BG6)
speed_tracker.grid(row=3, column=0, padx=30, pady=10)

# typing speed Label
typing_speed = Label(window, text="Your Typing Speed is", font=FONT3, bg=BG1)
typing_speed.grid(row=4, column=0, padx=30, pady=30, sticky=W)

# key binder
tp.bind('<KeyPress>', evaluate)

# Progress bar configuration
s = ttk.Style()
s.theme_use('alt')
s.configure("red.Horizontal.TProgressbar", background='red')
s.configure("yellow.Horizontal.TProgressbar", background='yellow')
s.configure("green.Horizontal.TProgressbar", background='green')

# progressbar label 'pbar'
pbar = Label(window, text='Your Progress', width=15, bg=BG1)
pbar.configure(font=FONT3)
pbar.grid(row=5, column=0, pady=20)
#
progressbar1 = ttk.Progressbar(window, length=390, mode='determinate', value=0, style='green.Horizontal.TProgressbar')
progressbar1.grid(row=6, column=0, columnspan=2, pady=10)

window.mainloop()
