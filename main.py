# commmand to put into terminal to compile it (remember to update the version!!!):
# py -m PyInstaller --clean --onefile --windowed --icon="logo_rl.ico" --add-data "logo_rl.ico;." --name="Rēscula Latīna [VERSION]" main.py
# import necessary modules
import tkinter as tk
from tkinter import ttk
import os, sys
import verb, noun, secrets_, tab
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
VERSION = "v1.6.4"
NAME = f"Rēscula Latīna {VERSION}"
# set the main window up
WINDOW = tk.Tk()
WINDOW.title(NAME)
WINDOW.geometry(f"{WIDTH}x{HEIGHT}")
WINDOW.resizable(False, False)
WINDOW.iconbitmap(resourcePath("logo_rl.ico"))
# set the main notebook up
NOTEBOOK = ttk.Notebook(WINDOW)
NOTEBOOK.pack(fill="both", expand=True)
# add the info tab to the notebook
infoFrameOuter, infoFrameInner = tab.Tab.makeScrollableFrame(tab.Tab, NOTEBOOK, bg=BG_COL)
infoText = f"""
Thank you for messing around with {NAME}.
Choose a category (verbs or nouns) and a subcategory (review, setup, parse, type, results).
Review allows you to enter in a parse to see the Latin word.
Setup allows you to choose what to and not to be tested on in Parse and Type.
Parse gives you a Latin word to parse.
Type allows you to type in the Latin word of a given parse.
Results allows you to see your results from Parse and Type.

Abbreviations:
- PRES = present
- IMPF = imperfect
- PERF = perfect
- PLPF = pluperfect
- FUTR = future
- FTPF = future perfect
- ACT = active (also used for forms such as conor, loquī, patiēns, etc)
- PAS = passive (FUTR PAS PTCP = gerundive)
- INDC = indicative
- SUBJ = subjunctive
- INFN = infinitive
- IMPT = imperative
- PTCP = participle
- 1S/2S/3S = 1st/2nd/3rd person singular
- 1P/2P/3P = 1st/2nd/3rd person plural
- MASC = masculine
- FEMN = feminine
- NEUT = neuter
- NOM = nominative
- VOC = vocative
- ACC = accusative
- GEN = genitive
- DAT = dative
- ABL = ablative
- SG = singluar
- PL = plural

Notes:
- the verb fīō is (stored as) the passive of faciō
- gerundives are stored as future passive participles
- enter the konami code (followed by Enter) to !%@$ %&!*@£\"#?=
- if you find any bugs, or would like to give suggestions for updates, please let T.A. U5R know (:
"""
infoLabel = tk.Label(infoFrameInner, text=infoText, bg=BG_COL, fg=FG_COL, width=WIDTH, anchor="w", justify="left", wraplength=WIDTH-20)
infoLabel.pack()
NOTEBOOK.add(infoFrameOuter, text="INFO")
# add other tabs to the notebook
verbs = verb.VerbTab(width=WIDTH, height=HEIGHT, displayFont=DISPLAY_FONT, bgCol=BG_COL, fgCol=FG_COL, selCol="#ff00ff")
verbs.BUILD_VERB_TAB(NOTEBOOK)
nouns = noun.NounTab(width=WIDTH, height=HEIGHT, displayFont=DISPLAY_FONT, bgCol=BG_COL, fgCol=FG_COL, selCol="#0000ff")
nouns.BUILD_NOUN_TAB(NOTEBOOK)
# unleash the secrets
detector = secrets_.Konami(WINDOW)
# RUN THE CODE!!!!!!
WINDOW.mainloop()
