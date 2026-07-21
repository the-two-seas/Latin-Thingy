# import necessary modules
import tkinter as tk
from tkinter import ttk
import verb, noun
# initialise constants
WIDTH, HEIGHT = 400, 400
DISPLAY_FONT = ("Arial", 30)
BG_COL, FG_COL = "#000000", "#ffffff"
# set the main window up
WINDOW = tk.Tk()
WINDOW.title("latin thingy")
WINDOW.geometry(f"{WIDTH}x{HEIGHT}")
#WINDOW.resizable(False, False)
# set the main notebook up
NOTEBOOK = ttk.Notebook(WINDOW)
NOTEBOOK.pack(fill="both", expand=True)
# add tabs to the notebook
verbs = verb.VerbTab(width=WIDTH, height=HEIGHT, displayFont=DISPLAY_FONT, bgCol=BG_COL, fgCol=FG_COL, selCol="#ff00ff")
verbs.BUILD_VERB_TAB(NOTEBOOK)
nouns = noun.NounTab(width=WIDTH, height=HEIGHT, displayFont=DISPLAY_FONT, bgCol=BG_COL, fgCol=FG_COL, selCol="#0000ff")
nouns.BUILD_NOUN_TAB(NOTEBOOK)
# RUN THE CODE!!!!!!
WINDOW.mainloop()
