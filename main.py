# commmand to put into terminal to compile it:
# py -m PyInstaller --clean --onefile --windowed --icon="logo_rl.ico" --add-data "logo_rl.ico;." --name="Rescula Latina [VERSION]" main.py
# import necessary modules
import tkinter as tk
from tkinter import ttk
import os, sys
import verb, noun, secrets_
# logo stuff
def resourcePath(relativePath):
    try:
        basePath = sys._MEIPASS
    except AttributeError:
        basePath = os.path.abspath(".")
    return os.path.join(basePath, relativePath)
# initialise constants
WIDTH, HEIGHT = 400, 400
DISPLAY_FONT = ("Arial", 30)
BG_COL, FG_COL = "#000000", "#ffffff"
# set the main window up
WINDOW = tk.Tk()
WINDOW.title("Rescula Latina v1.6.3")
WINDOW.geometry(f"{WIDTH}x{HEIGHT}")
WINDOW.resizable(False, False)
WINDOW.iconbitmap(resourcePath("logo_rl.ico"))
# set the main notebook up
NOTEBOOK = ttk.Notebook(WINDOW)
NOTEBOOK.pack(fill="both", expand=True)
# add tabs to the notebook
verbs = verb.VerbTab(width=WIDTH, height=HEIGHT, displayFont=DISPLAY_FONT, bgCol=BG_COL, fgCol=FG_COL, selCol="#ff00ff")
verbs.BUILD_VERB_TAB(NOTEBOOK)
nouns = noun.NounTab(width=WIDTH, height=HEIGHT, displayFont=DISPLAY_FONT, bgCol=BG_COL, fgCol=FG_COL, selCol="#0000ff")
nouns.BUILD_NOUN_TAB(NOTEBOOK)
# unleash the secrets
detector = secrets_.Konami(WINDOW)
# RUN THE CODE!!!!!!
WINDOW.mainloop()
