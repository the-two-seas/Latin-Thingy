# import necessary modules
import random
import tkinter as tk
import tables, timer_
from tkinter import ttk
from tkinter import messagebox as msg
# create the class
class Tab:
    """the generic parent Tab class from which all others in main.NOTEBOOK will be inherited"""
    def __init__(self, *, width: int, height: int, displayFont: tuple[str, int], bgCol: str, fgCol: str, selCol: str):
        self.parsingCorrect, self.parsingIncorrect = 0, 0
        self.typingCorrect, self.typingIncorrect = 0, 0
        self.width, self.height = width, height
        self.displayFont = displayFont
        self.bgCol, self.fgCol = bgCol, fgCol
        self.selCol = selCol
        self.parsingTimer = timer_.Timer(dp=2)
        self.typingTimer = timer_.Timer(dp=2)
        self.lastTab = None
        self.results = []
    def selected(self, varDict: dict) -> list[str]:
        """returns all vars in the varDict which are selected"""
        return [name for name, var in varDict.items() if var.get()]
    def currentTab(self, ntbk: ttk.Notebook) -> tk.Frame:
        return ntbk.nametowidget(ntbk.select())
    def displaySelector(self, *, frame: tk.Frame, options: list[str], mode: str, widgetDict: dict, varOrDict, width: int, cols: int = 6, fs: int = 8, command=None, selectColour: str) -> None:
        """displays either the cbs or rbs"""
        for i, abbrev in enumerate(options):
            row = i // cols
            col = i % cols
            match mode:
                case "rb":
                    widget = tk.Radiobutton(frame, text=abbrev, value=abbrev, variable=varOrDict, indicatoron=False, width=width, font=("Arial", fs), selectcolor=selectColour, command=(lambda a=abbrev: command(a)) if command else None)
                case "cb":
                    v = tk.BooleanVar()
                    widget = tk.Checkbutton(frame, text=abbrev, variable=v, indicatoron=False, width=width, selectcolor=selectColour, command=command, font=("Arial", fs))
                    varOrDict[abbrev] = v
                    v.set(1)  # checks it
                case _:
                    raise ValueError(f"'{mode}' is not 'rb' or 'cb'")
            widget.grid(row=row, column=col, padx=2, pady=2)
            widgetDict[abbrev] = widget
    def makeScrollableFrame(self, parent, *, bg) -> tuple[tk.Frame]:
        """since frames cant use scrollwheels, it must be placed inside a canvas. returns "outer" (put this in the notebook), and "frame" (put widgets in here)"""
        # create widgets
        outer = tk.Frame(parent, bg=bg)  # stuff created in this method goes in here
        canvas = tk.Canvas(outer, bg=bg, highlightthickness=0)
        scrollbar = tk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)  # bind scroller to the CANVAS
        frame = tk.Frame(canvas, bg=bg)  # here we go
        window = canvas.create_window((0, 0), window=frame, anchor="nw")
        # no idea what this does!
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfigure(window, width=e.width))
        def mousewheel(event): canvas.yview_scroll(-event.delta // 120, "units")  # function to scroll with mousewheel
        frame.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", mousewheel))  # can only scroll with mousewheel if mouse is inside frame
        frame.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))  # else, disable scrolling
        canvas.pack(side="left", fill="both", expand=True)  # put it in!
        scrollbar.pack(side="right", fill="y")  # put it in!
        return outer, frame
    def enterPressed(self, _) -> None:
        self.confirm()
    def spacePressed(self, _) -> None:
        self.next() 
    def confirm(self): pass
    def next(self): pass
