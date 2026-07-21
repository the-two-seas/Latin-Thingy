# import necessary modules
import random
import tkinter as tk
import tables, timer_
from tkinter import ttk
from tkinter import messagebox as msg
# nounTab class
class NounTab:
    """the class for the noun's tab in the full program's notebook widget"""
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
        self.components = {
            "nouns": [v for v in tables.NOUNS.keys()],
            "cases": ["NOM", "VOC", "ACC", "GEN", "DAT", "ABL"],
            "numbers": ["SG", "PL"]
        }
        self.allowed = {
            "nouns"   : self.components["nouns"],
            "cases"   : self.components["cases"],
            "numbers" : self.components["numbers"]
        }
    # general funcs
    def selected(self, varDict: dict) -> list[str]:
        """returns all vars in the varDict which are selected"""
        return [name for name, var in varDict.items() if var.get()]
    def possibleParsesOfNoun(self, form: str) -> list[str]:
        """reverse looks through tables.NOUNS and finds all parses for noun"""
        parses = []
        for _, nounData in tables.NOUNS.items():
            for case, caseData in nounData.items():
                for number, declinedForm in caseData.items():
                    if declinedForm == form:
                        parses.append(f"{case} {number}")
        return parses
    def getLatinNoun(self, *, nouns: list[str], cases: list[str], numbers: list[str]) -> tuple[str]:
        """
        gets a latin nouns from tables.NOUNS with the specified constraints\n
        returns ln, nn, cs, nm
        """
        nn = random.choice(nouns)
        cs = random.choice(cases)
        nm = random.choice(numbers)
        ln = tables.NOUNS[nn][cs][nm]
        return ln, nn, cs, nm
    def currentTab(self) -> tk.Frame:
        return self.nounNotebook.nametowidget(self.nounNotebook.select())
    def onTabChanged(self, event) -> None:
        # get the current and previous tabs
        current = self.currentTab()
        previous = self.lastTab
        self.lastTab = current
        if current in [self.parsingFrame, self.typingFrame]:  # the user just entered parsing OR typing mode
            if not all(self.allowed.values()):  # and there is a category in self.allowed which is insufficient
                self.nounNotebook.select(self.setupFrame)  # sends the user back to the setup frame
                msg.showerror("XD", "please pick at least one of everything")  # and displays a message to tell the user
                return
        if current is self.parsingFrame:  # the user just entered parsing mode
            self.nextParse()  # refreshes the noun to avoid cheating ig...?
        if current is self.typingFrame:  # the user just entered typing mode
            self.nextTyping()  # refresh
    def displaySelector(self, *, frame: tk.Frame, thing: str, mode: str, widgetDict: dict, varOrDict, width: int, cols: int = 6, fs: int = 8, command=None, selectColour: str) -> None:
        """displays either the cbs or rbs"""
        for i, abbrev in enumerate(self.components[thing]):
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
        current = self.currentTab()
        if current is self.parsingFrame:
            if self.parsingConfirmButton["state"] == "normal":
                self.confirmParsing()
        elif current is self.typingFrame:
            if self.typingConfirmButton["state"] == "normal":
                self.confirmTyping()
    def spacePressed(self, _) -> None:
        current = self.currentTab()
        if current is self.parsingFrame:
            if self.parsingNextButton.winfo_ismapped():  # if the next button is shown
                self.nextParse()
        elif current is self.typingFrame:
            if self.typingNextButton.winfo_ismapped():  # if the next button is shown
                self.nextTyping()
    # functions for REVIEW
    def renderReviewLatinNoun(self, _) -> None:
        # get all the stats the user entered
        noun = self.reviewNounUserval.get()
        case = self.reviewCaseUserval.get()
        number = self.reviewNumberUserval.get()
        self.reviewLatinNoun = tables.NOUNS[noun][case][number]
        # display
        if self.reviewLatinNoun is not None:
            self.reviewDisplayor.config(text=self.reviewLatinNoun)
        else:
            self.reviewDisplayor.config(text="N/A")
    # functions for SETUP
    def updateAllowance(self):
        print("updating allowance")
        self.allowed["nouns"]  = self.selected(self.setupNounUservals)
        self.allowed["cases"] = self.selected(self.setupCaseUservals)
        self.allowed["numbers"] = self.selected(self.setupNumberUservals)
        self.parsingCorrect = 0
        self.parsingIncorrect = 0
        self.refreshNounRBs()
        self.updateParsingScore()
        if not all(self.allowed.values()):
            self.parsingDisplayor.config(text="INSUFFICIENCY")
            self.parsingConfirmButton.config(state="disabled")
            self.parsingLemma = None
            return
        else:
            self.renderNewLatinNoun()
    def selectAllSetupCBs(self) -> None:
        for CBs in [self.setupNounUservals, self.setupCaseUservals, self.setupNumberUservals]:
            for _, CB in CBs.items():
                CB.set(1)  # checks
        self.updateAllowance()
    def deselectAllSetupCBs(self) -> None:
        for CBs in [self.setupNounUservals, self.setupCaseUservals, self.setupNumberUservals]:
            for _, CB in CBs.items():
                CB.set(0)  # unchecks
        self.updateAllowance()
    # functions for PARSING
    def configParsingRBs(self, state: str) -> None:
        for rbs in [self.parsingCaseRBs, self.parsingNumberRBs]:
            for rb in rbs.values():
                rb.config(state=state)
    def whatDidTheUserParse(self) -> dict[str, str]:
        """empty selections are shown by the EMPTY STRING "" !!!!!!!!!"""
        nn = self.parsingLemma
        cs = self.parsingCaseUserval.get()
        nm = self.parsingNumberUserval.get()
        return {
            "nouns"  : nn,
            "cases"  : cs,
            "numbers": nm
        }
    def refreshNounRBs(self) -> None:
        # deselect all RBs
        for rbVar in [self.parsingCaseUserval, self.parsingNumberUserval]:
            rbVar.set("")
        groups = {"cases": self.parsingCaseRBs, "numbers": self.parsingNumberRBs}
        for thing, RBs in groups.items():
            for component in self.components[thing]:
                rb = RBs[component]
                if component in self.allowed[thing]:
                    rb.config(state="normal")
                else:
                    rb.config(state="disabled")
    def renderNewLatinNoun(self) -> None:
        """user's time to guess STARTS HERE!!!!!"""
        # get the noun
        self.parsingLatinNoun, self.parsingLemma, *_ = self.getLatinNoun(
            nouns=self.allowed["nouns"], cases=self.allowed["cases"], numbers=self.allowed["numbers"]
        )
        self.parsingDisplayor.config(text=self.parsingLatinNoun)  # display the noun      
        self.parsingConfirmButton.config(state="disabled")  # disable the confirm button
        # timer stuff
        self.parsingTimer.start()
    def confirmParsing(self) -> None:
        """checks if the deatils entered by the user are parsingCorrect"""
        if self.parsingLemma is None: msg.showerror("gavin", "self.parsingLemma is None"); return
        # get all user inputs
        lemma, userCase, userNumber = list(self.whatDidTheUserParse().values())
        # timer stuff
        self.parsingTimer.stop()
        # find the user's parse
        userNoun = tables.NOUNS[lemma][userCase][userNumber]
        # DECIDE WHAT TO DO IN (IN)CORRECT SITUATIONS
        self.possibleParsesList = self.possibleParsesOfNoun(self.parsingLatinNoun)
        self.possibleParsesStr = ", ".join(self.possibleParsesList)
        self.parsingStatus = (userNoun == self.parsingLatinNoun)
        if self.parsingStatus:
            self.parsingCorrect += 1
        else:
            self.parsingIncorrect += 1
            msg.showinfo(
                title="you could have had these instead:",
                message=f"possible parses of {self.parsingLatinNoun} ({self.parsingLemma}):\n{',\n'.join(self.possibleParsesList)}.\nyou parsed {userNoun}"
                )
        # general
        self.updateParsingConfirmButton("N2")
        self.updateParsingScore()
        self.updateResults(mode="parsing")
        # disable (radio)buttons to avoid cheating
        self.parsingConfirmButton.config(state="disabled")
        self.configParsingRBs("disabled")
        # show the next button
        self.parsingNextButton.place(x=self.width//2, y=self.height-100, anchor="center")
    def updateParsingConfirmButton(self, _) -> None:
        """does what it says on the tin, and enables/disables the confirmParsing button's state because of this"""
        if self.parsingCaseUserval.get() and self.parsingNumberUserval.get():
            self.parsingConfirmButton.config(state="normal")
        else:
            self.parsingConfirmButton.config(state="disabled")
    def updateParsingScore(self) -> None:
        self.parsingCorrectLabel.config(text=self.parsingCorrect)
        self.parsingIncorrectLabel.config(text=self.parsingIncorrect)
    def nextParse(self) -> None:
        for rb in [self.parsingCaseUserval, self.parsingNumberUserval]:  # reset rbs
            rb.set("")
        self.configParsingRBs("normal")  # enable the parsing rbs
        self.renderNewLatinNoun()  # new round
        self.parsingNextButton.place_forget()  # hide the next button
    # functions for TYPING
    def updateTypingScore(self) -> None:
        self.typingCorrectLabel.config(text=self.typingCorrect)
        self.typingIncorrectLabel.config(text=self.typingIncorrect)
    def confirmTyping(self) -> None:
        self.oldTypingQuestion = self.typingPromptLabel["text"].removeprefix("type this form of ").replace(":\n", " ").upper().strip().replace(" ", "\n")
        self.typingTimer.stop()  # timer stuff
        self.typingUserInput = self.typingUserval.get().lower().strip()  # get the value
        self.typingUserval.set("")  # empty the box
        self.typingEntry.config(state="disabled")  # disable the textbox
        # CHECK IF IT IS (IN)CORRECT
        self.typingStatus = (self.typingUserInput == self.typingLatinNoun)
        if self.typingStatus:  # correct
            self.typingCorrect += 1
        else:
            self.typingIncorrect += 1
            msg.showinfo(
                title="feedback",
                message=f"correct answer: {self.typingLatinNoun}"
            )
        # general
        self.updateTypingScore()
        self.updateResults(mode="typing")
        # show the next button
        self.typingNextButton.place(x=self.width//2, y=self.height-100, anchor="center")
    def nextTyping(self) -> None:
        # get the data
        self.typingLatinNoun, self.typingLemma, self.typingCase, self.typingNumber = self.getLatinNoun(
            nouns=self.allowed["nouns"], cases=self.allowed["cases"], numbers=self.allowed["numbers"]
        )
        # form the message
        message = f"type this form of {self.typingLemma}:\n{self.typingCase} {self.typingNumber}"
        self.typingPromptLabel.config(text=message)  # display
        self.typingTimer.start()
        self.typingNextButton.place_forget()  # hide the next button
        self.typingEntry.config(state="normal")  # enable the textbox
    def updateTypingConfirmButton(self, *args) -> None:
        """if there is nothing (or only whitespace) in the entry box, then the confirm button shall be disabled, else enabled"""
        if self.typingUserval.get().strip():
            self.typingConfirmButton.config(state="normal")
        else:
            self.typingConfirmButton.config(state="disabled")
    # functions for RESULTS
    def updateResults(self, *, mode: str) -> None:
        """adds the previous round to the results"""
        if mode == "parsing":
            # get the user's parse
            userParse = " ".join([x for x in list(self.whatDidTheUserParse().values())[1:] if x])  # to remove the first k:v pair (lemma)
            self.results.append({
                "noun": self.parsingLatinNoun,  # the noun asked
                "status": self.parsingStatus,  # whether it was right or not
                "you put": userParse,  # user parse
                "possible answers": self.possibleParsesOfNoun(self.parsingLatinNoun),  # possible answers
                "time taken": self.parsingTimer.value,  # time taken
            })
            # get/make data to display
            row = len(self.results) - 1
            currentResults = self.results[-1]
            question, status, youPut, possible, timeTaken = currentResults.values()
            colour = "#00ff00" if status else "#ff0000"
            possibleRollover = 3  # this can be changed if needed
            p = ""
            for i, parse in enumerate(possible):
                if not i % possibleRollover:
                    p += "\n"
                p += f"{parse}, "
            p = p[1:-2]  # to remove the ", " or ",\n" at the end and the \n at the start
            possible = p
            round_ = f"{row+1}."
            data = (
f"""you put: {youPut}
possible: {possible}
time taken: {timeTaken}"""
)
        elif mode == "typing":
            # get what the user typed
            self.results.append({
                "question": self.oldTypingQuestion,
                "status": self.typingStatus,
                "you put": self.typingUserInput,
                "answer": self.typingLatinNoun,
                "time taken": self.typingTimer.value
            })
            row = len(self.results) - 1
            currentResults = self.results[-1]
            question, status, youPut, answer, timeTaken = currentResults.values()
            colour = "#00ff00" if status else "#ff0000"
            round_ = f"{row+1}."
            data = (
f"""you put: {youPut}
answer: {answer}
time taken: {timeTaken}
"""
)
        else:
            raise ValueError(f"{mode} is not 'parsing' or 'typing'")
        # create the labels
        font = "Arial", 10
        roundLabel = tk.Label(self.resultsFrame, text=round_, bg=self.bgCol, fg=self.fgCol, font=font)
        questionLabel = tk.Label(self.resultsFrame, text=question, bg=self.bgCol, fg=colour, font=font)
        dataLabel = tk.Label(self.resultsFrame, text=data, bg=self.bgCol, fg=self.fgCol, font=font)
        # grid them in
        roundLabel.grid(row=row, column=0, sticky="w")
        questionLabel.grid(row=row, column=1, sticky="w")
        dataLabel.grid(row=row, column=2, sticky="w")
    # build the subtabs
    def buildReviewSubtab(self, parentNotebook: ttk.Notebook) -> None:
        """this is the subtab for the REVIEW mode, where users can see a "cheat sheet" of noun inflections (tables.NOUNS)"""
        # create the frame
        self.reviewFrame = tk.Frame(parentNotebook, bg=self.bgCol, width=self.width, height=self.height)
        # create displayor
        self.reviewDisplayor = tk.Label(self.reviewFrame, text="puella", font=self.displayFont, bg=self.bgCol, fg=self.fgCol)
        self.reviewDisplayor.grid(row=0, column=0, columnspan=999)
        # create spacer
        tk.Label(self.reviewFrame, bg=self.bgCol, width=6).grid(row=1, column=0)
        # create the frames
        self.reviewNounFrame   = tk.Frame(self.reviewFrame, width=self.width, bg=self.bgCol)
        self.reviewCaseFrame   = tk.Frame(self.reviewFrame, width=self.width, bg=self.bgCol)
        self.reviewNumberFrame = tk.Frame(self.reviewFrame, width=self.width, bg=self.bgCol)
        # grid the frames
        self.reviewNounFrame  .grid(row=1, column=1, sticky="ew")
        self.reviewCaseFrame  .grid(row=2, column=1, sticky="ew")
        self.reviewNumberFrame.grid(row=3, column=1, sticky="ew")
        # create the vars
        self.reviewNounRBs,   self.reviewNounUserval   = {}, tk.StringVar()
        self.reviewCaseRBs,   self.reviewCaseUserval   = {}, tk.StringVar()
        self.reviewNumberRBs, self.reviewNumberUserval = {}, tk.StringVar()
        # select one thing in each frame
        self.reviewNounUserval  .set("PUELLA")
        self.reviewCaseUserval  .set("NOM")
        self.reviewNumberUserval.set("SG")
        # display the noun RBs
        self.displaySelector(frame=self.reviewNounFrame,   mode="rb", thing="nouns",   widgetDict=self.reviewNounRBs,   varOrDict=self.reviewNounUserval,   width=6, command=self.renderReviewLatinNoun,    selectColour=self.selCol, cols=5)
        self.displaySelector(frame=self.reviewCaseFrame,   mode="rb", thing="cases",   widgetDict=self.reviewCaseRBs,   varOrDict=self.reviewCaseUserval,   width=6, command=self.renderReviewLatinNoun,    selectColour=self.selCol)
        self.displaySelector(frame=self.reviewNumberFrame, mode="rb", thing="numbers", widgetDict=self.reviewNumberRBs, varOrDict=self.reviewNumberUserval, width=6, command=self.renderReviewLatinNoun,    selectColour=self.selCol)
        # add the frame to the parent notebook
        parentNotebook.add(self.reviewFrame, text="REVIEW")
    def buildSetupSubtab(self, parentNotebook: ttk.Notebook) -> None:
        """this is the subtab for the SETUP mode, where users can choose what things they wish to be tested on."""
        # create the noun setup frame
        self.setupFrame = tk.Frame(parentNotebook, bg=self.bgCol, width=self.width, height=self.height)
        # create the header
        tk.Label(self.setupFrame, text="choose options:", bg=self.bgCol, fg=self.fgCol, font=("Arial", 25)).grid(row=0, column=0, columnspan=999)
        # create a spacer to avoid leftjustification
        tk.Label(self.setupFrame, bg=self.bgCol, width=6).grid(row=1, column=0)
        # create the noun setup frame for each component
        self.setupNounFrame = tk.Frame(self.setupFrame, width=self.width, bg=self.bgCol)
        self.setupCaseFrame = tk.Frame(self.setupFrame, width=self.width, bg=self.bgCol)
        self.setupNumberFrame = tk.Frame(self.setupFrame, width=self.width, bg=self.bgCol)
        # create the dicts
        self.setupNounCBs,  self.setupNounUservals  = {}, {}
        self.setupCaseCBs, self.setupCaseUservals = {}, {}
        self.setupNumberCBs, self.setupNumberUservals = {}, {}
        # grid the frames inside
        self.setupNounFrame .grid(row=1, column=1, sticky="ew")
        self.setupCaseFrame.grid(row=2, column=1, sticky="ew")
        self.setupNumberFrame.grid(row=3, column=1, sticky="ew")
        # create the display the setup CBs
        self.displaySelector(frame=self.setupNounFrame,   mode="cb", thing="nouns",  widgetDict=self.setupNounCBs,   varOrDict=self.setupNounUservals,   width=6, command=self.updateAllowance, selectColour=self.selCol, cols=5)
        self.displaySelector(frame=self.setupCaseFrame,   mode="cb", thing="cases", widgetDict=self.setupCaseCBs,   varOrDict=self.setupCaseUservals,   width=6, command=self.updateAllowance, selectColour=self.selCol)
        self.displaySelector(frame=self.setupNumberFrame, mode="cb", thing="numbers", widgetDict=self.setupNumberCBs, varOrDict=self.setupNumberUservals, width=6, command=self.updateAllowance, selectColour=self.selCol)
        # other
        self.setupButtonsFrame = tk.Frame(self.setupFrame, width=self.width, bg=self.bgCol)
        self.setupButtonsFrame.grid(row=5, column=1, sticky="ew")
        self.setupSelAll = tk.Button(self.setupButtonsFrame, text="ALL", font=("Arial bold", 7), width=6, command=self.selectAllSetupCBs)
        self.setupSelNone = tk.Button(self.setupButtonsFrame, text="NONE", font=("Arial bold", 7), width=6, command=self.deselectAllSetupCBs)
        self.setupSelAll.grid(row=0, column=0, padx=2, pady=2)
        self.setupSelNone.grid(row=0, column=1, padx=2, pady=2)
        # add the frame to the parent notebook
        parentNotebook.add(self.setupFrame, text="SETUP")
    def buildParsingSubtab(self, parentNotebook: ttk.Notebook) -> None:
        """this is the subtab for the PARSING mode, where users parse latin nouns with the constraints chosen from the SETUP mode."""
        # create the noun parsing frame
        self.parsingFrame = tk.Frame(parentNotebook, bg=self.bgCol, width=self.width, height=self.height)
        self.parsingHeaderFrame = tk.Frame(self.parsingFrame, bg=self.bgCol, width=self.width)
        self.parsingHeaderFrame.grid(row=0, column=0, columnspan=999)
        # create noun displayor
        self.parsingDisplayor = tk.Label(self.parsingHeaderFrame, bg=self.bgCol, fg=self.fgCol, font=self.displayFont)
        self.parsingDisplayor.grid(row=0, column=0, sticky="ew")
        # create noun score labels
        self.parsingCorrectLabel = tk.Label(self.parsingFrame, text=self.parsingCorrect, bg=self.bgCol, fg="#00ff00", font=("Arial bold", 20))
        self.parsingCorrectLabel.place(x=10, y=10)
        self.parsingIncorrectLabel = tk.Label(self.parsingFrame, text=self.parsingIncorrect, bg=self.bgCol, fg="#ff0000", font=("Arial bold", 20))
        self.parsingIncorrectLabel.place(relx=1, x=-10, y=10, anchor="ne")
        # create spacer
        tk.Label(self.parsingFrame, width=6, bg=self.bgCol).grid(row=1, column=0)
        # create the frames for each component
        self.parsingCaseFrame       = tk.Frame(self.parsingFrame, width=self.width, bg=self.bgCol)
        self.parsingNumberFrame     = tk.Frame(self.parsingFrame, width=self.width, bg=self.bgCol)
        # grid them in
        self.parsingCaseFrame  .grid(row=1, column=1, sticky="ew")
        self.parsingNumberFrame.grid(row=2, column=1, sticky="ew")
        # create the dicts and string vars to hold the data
        self.parsingCaseRBs,   self.parsingCaseUserval   = {}, tk.StringVar()
        self.parsingNumberRBs, self.parsingNumberUserval = {}, tk.StringVar()
        # display the noun RBs
        self.displaySelector(frame=self.parsingCaseFrame,   mode="rb", thing="cases",   widgetDict=self.parsingCaseRBs,   varOrDict=self.parsingCaseUserval,   width=6, command=self.updateParsingConfirmButton, selectColour=self.selCol)
        self.displaySelector(frame=self.parsingNumberFrame, mode="rb", thing="numbers", widgetDict=self.parsingNumberRBs, varOrDict=self.parsingNumberUserval, width=6, command=self.updateParsingConfirmButton, selectColour=self.selCol)
        self.parsingConfirmButton = tk.Button(self.parsingFrame, text="CHECK", font=("Arial bold", 8), state="disabled", command=self.confirmParsing)
        self.parsingConfirmButton.grid(row=999, column=1, sticky="ew")
        self.parsingNextButton = tk.Button(self.parsingFrame, text="NEXT", font=("Arial", 10), width=6, command=self.nextParse)
        # add frame to noun notebook
        parentNotebook.add(self.parsingFrame, text="PARSE")       
    def buildTypingSubtab(self, parentNotebook: ttk.Notebook) -> None:
        """this is the subtab for the TYPING mode, where users can type the form that is given as a parse"""
        # create the frame
        self.typingFrame = tk.Frame(parentNotebook, bg=self.bgCol, width=self.width, height=self.height)
        self.typingFrame.grid_columnconfigure(0, weight=1)
        self.typingHeaderFrame = tk.Frame(self.typingFrame, bg=self.bgCol, width=self.width)
        self.typingHeaderFrame.grid(row=0, column=0, columnspan=999)
        # create prompt widget
        self.typingPromptLabel = tk.Label(self.typingHeaderFrame, text="testing testing 123", bg=self.bgCol, fg=self.fgCol, font=("Arial", 15))
        self.typingPromptLabel.grid(row=0, column=0, sticky="ew")
        # create score widgets
        self.typingCorrectLabel = tk.Label(self.typingFrame, text=self.typingCorrect, bg=self.bgCol, fg="#00ff00", font=("Arial bold", 20))
        self.typingCorrectLabel.place(x=10, y=10)
        self.typingIncorrectLabel = tk.Label(self.typingFrame, text=self.typingIncorrect, bg=self.bgCol, fg="#ff0000", font=("Arial bold", 20))
        self.typingIncorrectLabel.place(relx=1, x=-10, y=10, anchor="ne")
        tk.Label(self.typingFrame, bg=self.bgCol, height=1).grid(row=1, column=0)  # spacer
        # create the text box and confirm button
        self.typingUserval = tk.StringVar()
        self.typingEntry = tk.Entry(self.typingFrame, bg=self.bgCol, fg=self.fgCol, font=self.displayFont, width=20, textvariable=self.typingUserval)
        self.typingEntry.grid(row=2, column=0, sticky="ew")
        self.typingUserval.trace_add("write", self.updateTypingConfirmButton)
        self.typingConfirmButton = tk.Button(self.typingFrame, text="CHECK", command=self.confirmTyping)
        self.typingConfirmButton.grid(row=3, column=0)
        # create next button
        self.typingNextButton = tk.Button(self.typingFrame, text="NEXT", command=self.nextTyping)
        self.typingNextButton.grid
        # put it in
        parentNotebook.add(self.typingFrame, text="TYPE")
    def buildResultsSubtab(self, parentNotebook: ttk.Notebook) -> None:
        """this is the subtab for the RESULTS mode, where users can see their results from the PARSING mode"""
        # create the frame
        self.resultsOuterFrame, self.resultsFrame = self.makeScrollableFrame(parentNotebook, bg=self.bgCol)
        # put it in
        parentNotebook.add(self.resultsOuterFrame, text="RESULTS")
    # put everything together
    def BUILD_NOUN_TAB(self, PARENT_NOTEBOOK: ttk.Notebook) -> None:
        # create noun frame
        self.nounFrame = tk.Frame(PARENT_NOTEBOOK, bg=self.bgCol, width=self.width, height=self.height)
        # create noun notebook inside noun frame
        self.nounNotebook = ttk.Notebook(self.nounFrame)
        self.nounNotebook.pack(fill="both", expand=True)
        self.nounNotebook.bind("<<NotebookTabChanged>>", self.onTabChanged)
        self.nounNotebook.bind("<Return>", self.enterPressed)
        self.nounNotebook.bind("<space>", self.spacePressed)
        # add noun subtabs
        self.buildReviewSubtab(self.nounNotebook)
        self.buildSetupSubtab(self.nounNotebook)
        self.buildParsingSubtab(self.nounNotebook)
        self.buildTypingSubtab(self.nounNotebook)
        self.buildResultsSubtab(self.nounNotebook)
        # other
        self.nounNotebook.select(self.resultsOuterFrame)  # this is needed to fix bug where keybinds only work
        self.nounNotebook.select(self.reviewFrame)  # after visiting the results tab
        # add noun frame
        PARENT_NOTEBOOK.add(self.nounFrame, text="NOUNS")
