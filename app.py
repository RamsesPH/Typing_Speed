import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import random

# ------------ / VARIABLES / ----------------/

BG1 = "SkyBlue2"
BG2 = 'green'
BG3 = '#6C3483'
BG4 = '#1B2631'
BG5 = '#E8E4C9'  # kind of pale yellow
BG6 = '#336B7D'
FONT1 = ("Courier New", 18, "bold")
FONT2 = ("Courier New", 14, "bold")
FONT3 = ("Helvetica", 16, "bold")
FONT4 = "TkDefaultFont", 24, "bold"

start_time = 0
end_time = 0
elapsed_time = 0
highlight_word_index = 0
total_words_number = 0
total_words_written = 0
portion = 0
typing_speed = 0

# ----------- / Word lists to choose from /-----------/

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

# -----/ Variables derived from the phrases / ----

list_of_phrases = [phrase1, phrase2, phrase3]
random_phrase_list = random.choice(list_of_phrases)
words = random_phrase_list.split()

# ---------------/  NOTE / ---------------

# NOTE ALL PRINTING STATEMENT CAN BE DELETES, ONLY ADDED FOR DEBUGGING PURPOSES


# -------------/ Define thr various Functions / --------------------/

def evaluate(event=None):
    global start_time, words, progressbar1, highlight_word_index, \
        total_words_number, portion, total_words_written, typing_speed
    # Get the text that the user has entered
    written_text = text_widget.get("1.0", "end-1c")
    total_words_number = len(words)
    total_words_written = highlight_word_index + 1
    print(f"total number of words = {total_words_number}")
    print(f"written_words = { total_words_written }")
    portion = round((total_words_written / total_words_number) * 100)
    print(f"portion = {portion}")

    #update the progress of the bar
    progressbar1['value'] = portion
    # update the counter label
    counter_label.config(text=str(total_words_written))
    global start_time, elapsed_time
    if total_words_written == 1:     # starts time counter on typing the first word.
        start_time = time.time()

    if portion == 100:
        print('is green ?')
        progressbar1.config(style='green.Horizontal.TProgressbar')
        elapsed_time = time.time() - start_time
        tp.unbind("<space>")     # stop recording variables
        typing_speed = total_words_written / (elapsed_time/60)
        typing_speed_label.config(text="Typing speed: {} WPM".format(round(typing_speed)))

    elif portion < 60:
        print('is yellow?')
        progressbar1.config(style='yellow.Horizontal.TProgressbar')
        elapsed_time = time.time() - start_time
    elif portion >= 60:
        print('is red? ')
        progressbar1.config(style='red.Horizontal.TProgressbar')
        elapsed_time = time.time() - start_time

    #update the typing time
    time_tracker.config(text=str(round(elapsed_time, 2)))

    return portion, total_words_written, elapsed_time, time_tracker, typing_speed


def highlight_current_word():
    # Remove the highlight from the previous word
    global words
    # highlighting the word ( in text_widget ) that will be written on ( tp window )
    if highlight_word_index > 0:
        start_index = "1.%d" % sum(len(w) + 1 for w in words[:highlight_word_index - 1])
        end_index = "1.%d" % (sum(len(w) + 1 for w in words[:highlight_word_index]) - 1)
        text_widget.tag_remove("highlight", start_index, end_index)

    # Get the start and end index of the current word and highlight it in yellow
    start_index = "1.%d" % sum(len(w) + 1 for w in words[:highlight_word_index])
    end_index = "1.%d" % (sum(len(w) + 1 for w in words[:highlight_word_index + 1]) - 1)

    text_widget.tag_add("highlight", start_index, end_index)
    text_widget.tag_config("highlight", background=BG4, font=FONT4)


def on_key_press(event):
    global highlight_word_index
    # Check if the pressed key is a space
    print("Space bar pressed!")
    if event.keysym == "space":
        # Increment the word index and highlight the next word
        highlight_word_index += 1
        # highlight_word_index is equivalent to the number of words printed
        print(highlight_word_index)
        # Call the function highlight_word_index
        highlight_current_word()


# ------- / WINDOW WIDGET AREA /------------------- /

window = tk.Tk()
window.geometry('800x800')
window.configure(bg=BG1)
window.iconbitmap('assets/writer.ico')
window.title('Typing Speed App')

# ------/ Create the Text Frames / ------------

# Insert the text to the Text widget and highlight the first word in yellow
text = words
text_widget = Text(window, height=12, width=85, bg=BG3, wrap="word")
text_widget.grid(row=0, column=0, padx=10, pady=20)
text_widget.focus_set()
text_widget.bind("<space>", on_key_press)
text_widget.insert("1.0", text)
highlight_current_word()

# typewriter window 'tp'
tp = Text(window, height=10, width=75, bg=BG6)
tp.configure(font=FONT2)
tp.grid(row=1, column=0, padx=30, pady=10)
window.bind("<space>", on_key_press)

# -------- / widget config / -----------/

# ___ / progressbar label 'pbar' / --
pbar = Label(window, text='Your Progress', width=15, bg=BG1)
pbar.configure(font=FONT3)
pbar.grid(row=5, column=0, pady=20)

# --- / Progress bar configuration

s = ttk.Style()
s.theme_use('alt')
s.configure(style='green.Horizontal.TProgressbar')
s.configure(style='red.Horizontal.TProgressbar')
s.configure(style='yellow.Horizontal.TProgressbar')

#---/ Progress bar widget
progressbar1 = ttk.Progressbar(window, length=390, mode='determinate', style='green.Horizontal.TProgressbar', value=0)
progressbar1.grid(row=6, column=0, columnspan=2, pady=10)

# Counter Label widgets
counter_label_title = Label(window, text="Word Counter", bg=BG1, font=FONT3)
counter_label_title.grid(row=2, column=0, padx=30, pady=30, sticky=W)

counter_label = Label(window, text=str(total_words_written), width=3, bg=BG6)
counter_label.grid(row=2, column=0, padx=30, pady=30)

#time Tracker Widgets
time_tracker_label = Label(window, text="Elapsed Time in seconds", bg=BG1, font=FONT3)
time_tracker_label.grid(row=3, column=0, padx=30, pady=10, sticky=W)

time_tracker = Label(window, text=str(round(elapsed_time, 2)), width=20, bg=BG6)
time_tracker.grid(row=3, column=0, padx=30, pady=10)

# typing speed Label
typing_speed_label = Label(window, text="Typing speed: 0 WPM", font=FONT3, bg=BG1)
typing_speed_label.grid(row=7, column=0, pady=20)

# key binder
tp.bind('<space>', evaluate)

window.mainloop()
