# secrets...
import tkinter as tk
import webbrowser as web
import os, sys

# logo stuff
def resourcePath(relativePath):
    try:
        basePath = sys._MEIPASS
    except AttributeError:
        basePath = os.path.abspath(".")
    return os.path.join(basePath, relativePath)

class LinkButton:
    """pressing me will go to a link"""
    def __init__(self, window: tk.Tk, *, text: str, link: str, font: tuple[str, int] = ("Arial", 15)) -> None:
        self.window = window
        self.text = text
        self.url = link
        enter = "#aaaaaa"
        leave = "#eeeeee"
        self.button = tk.Button(self.window, text=text, font=font, width=30, bg=leave, command=self.clicked)
        self.button.pack()
        self.button.bind("<Enter>", lambda e: self.button.config(bg=enter))
        self.button.bind("<Leave>", lambda e: self.button.config(bg=leave))
    def clicked(self):
        web.open(self.url)

KONAMI = ["Up", "Up", "Down", "Down", "Left", "Right", "Left", "Right", "b", "a", "Return"]

class Konami:
    """checks if the konami code has been entered, if so then ???"""
    def __init__(self, window: tk.Tk) -> None:
        self.window = window
        self.sequence = []
        self.window.bind("<Key>", self.check)
    def check(self, event) -> None:
        key = event.keysym
        self.sequence.append(key)
        if len(self.sequence) > len(KONAMI):
            self.sequence.pop(0)
        if self.sequence == KONAMI:
            self.unleash()
    def unleash(self) -> None:
        songWindow = tk.Tk()
        songWindow.title("ave imperator/imperatrix")
        songWindow.resizable(False, False)
        songWindow.iconbitmap(resourcePath("logo_rl.ico"))
        tk.Label(songWindow, text="ooh mystery buttons", font=("Arial", 15)).pack()
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=l37cqX2jBhE", text="ET NIL EST")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=3uiea53t1L4", text="TETE NUMQUAM RELINQUAM")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=LEXbnMOscZM", text="NON LOQUENDUM'ST DE BRUNO")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=nL_nb11qeYs", text="EGO VOLO IAM FIERI REX")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=8KabAJhlB8w", text="TRIUMPHUS ALLADINI")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=vpmjHLrj4Z4", text="QUIDNI ME VOCES")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=OfRrazJDARk", text="LIBERO")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=LUhd4GzJvmg", text="IN OTIUM IBIMUS")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=s-jdNS95Rm0", text="DUCE ME")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=cA1Z_9x8v24", text="TU ES MALUS, D. Gr.")
        LinkButton(songWindow, link="https://www.youtube.com/watch?v=9MYGBHD9iSo", text="NUNC EST BIBENDUM")

        # find more if you can!
        
        songWindow.mainloop()
