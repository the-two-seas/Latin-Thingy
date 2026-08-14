# secrets...
import tkinter as tk
import webbrowser as web

class LinkButton:
    """pressing me will go to a link"""
    def __init__(self, window: tk.Tk, *, text: str, link: str, font: tuple[str, int]) -> None:
        self.window = window
        self.text = text
        self.url = link
        self.button = tk.Button(self.window, text=text, font=font, width=30, command=self.clicked)
        self.button.pack()
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
        if len(self.sequence) > 12:
            self.sequence.pop(0)
        if self.sequence == KONAMI:
            self.unleash()
    def unleash(self) -> None:
        songWindow = tk.Tk()
        songWindow.title("quo modo me invenisti, o imperator?")
        songWindow.resizable(False, False)
        tk.Label(songWindow, text="ooh mystery buttons", font=("Arial", 15)).pack()
        moana = LinkButton(songWindow, text="ET NIL EST", link="https://www.youtube.com/watch?v=l37cqX2jBhE", font=("Arial", 15))
        never = LinkButton(songWindow, text="TETE NUMQUAM RELINQUAM", link="https://www.youtube.com/watch?v=3uiea53t1L4", font=("Arial", 15))
        bruno = LinkButton(songWindow, text="NON LOQUENDUM'ST DE BRUNO", link="https://www.youtube.com/watch?v=LEXbnMOscZM", font=("Arial", 15))
        simba = LinkButton(songWindow, text="EGO VOLO IAM FIERI REX", link="https://www.youtube.com/watch?v=nL_nb11qeYs", font=("Arial", 15))
        plebs = LinkButton(songWindow, text="TRIUMPHUS ALLADINI", link="https://www.youtube.com/watch?v=8KabAJhlB8w", font=("Arial", 15))
        maybe = LinkButton(songWindow, text="QUIDNI ME VOCES", link="https://www.youtube.com/watch?v=vpmjHLrj4Z4", font=("Arial", 15))
        letgo = LinkButton(songWindow, text="LIBERO", link="https://www.youtube.com/watch?v=OfRrazJDARk", font=("Arial", 15))
        billy = LinkButton(songWindow, text="IN OTIUM IBIMUS", link="https://www.youtube.com/watch?v=LUhd4GzJvmg", font=("Arial", 15))
        ducme = LinkButton(songWindow, text="DUCE ME", link="https://www.youtube.com/watch?v=s-jdNS95Rm0", font=("Arial", 15))


        songWindow.mainloop()
