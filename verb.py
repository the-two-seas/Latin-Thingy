# import necessary modules
import random
import tkinter as tk
import tab, tables, timer_
from tkinter import ttk
from tkinter import messagebox as msg
# verbTab class
class VerbTab(tab.Tab):
    """the class for the verb's tab in the full program's notebook widget"""
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.evenlyChoose = True        
        self.components = {
            "verbs": [v for v in tables.VERBS.keys()],
            "tenses": ["PRES", "IMPF", "PERF", "PLPF", "FUTR", "FTPF"],
            "voices": ["ACT", "PAS"],
            "moods": ["INDC", "SUBJ", "IMPT", "INFN", "PTCP"],
            "people": ["1S", "2S", "3S", "1P", "2P", "3P"],
            "genders": ["MASC", "FEMN", "NEUT"],
            "cases": ["NOM", "VOC", "ACC", "GEN", "DAT", "ABL"],
            "numbers": ["SG", "PL"]
        }
        self.invalidForms = []
        for verb in self.components["verbs"]:
            for tense in self.components["tenses"]:
                for voice in self.components["voices"]:
                    for mood in self.components["moods"]:
                        if tables.VERBS[verb][tense][voice][mood] in tables.EMPTY:
                            self.invalidForms.append((verb, tense, voice, mood))
        self.validForms = [
            (verb, tense, voice, mood)
            for verb  in self.components["verbs"]
            for tense in self.components["tenses"]
            for voice in self.components["voices"]
            for mood  in self.components["moods"]
            if (verb, tense, voice, mood) not in self.invalidForms
        ]
        self.allowed = {
            "verbs" : list(tables.VERBS.keys()),
            "tenses": list(tables.VERBS["AMO"].keys()),
            "voices": list(tables.VERBS["AMO"]["PRES"].keys()),
            "moods" : list(tables.VERBS["AMO"]["PRES"]["ACT"].keys())
        }
    # general funcs
    def verbFormExists(self, verb: str, tense: str, voice: str, mood: str) -> bool:
        return (verb, tense, voice, mood) in self.validForms
    def possibleParsesOfVerb(self, form: str) -> list[str]:
        """
        reverse looks through tables.VERBS and finds all parses for 'vb'
        eg amaverit -> FTPF ACT INDC 3S, PERF ACT SUBJ 3S
        """
        parses = []
        for _, verbData in tables.VERBS.items():
            for tense, tenseData in verbData.items():
                for voice, voiceData in tenseData.items():
                    for mood, moodData in voiceData.items():
                        if mood in ["INDC", "SUBJ", "IMPT"]:
                            for person, inflictedForm in moodData.items():
                                if inflictedForm == form:
                                    parses.append(f"{tense} {voice} {mood} {person}")
                        elif mood == "INFN" and moodData == form:
                            parses.append(f"{tense} {voice} {mood}")
                        elif mood == "PTCP":
                            for gender, genderData in moodData.items():
                                for case, caseData in genderData.items():
                                    for number, inflictedForm in caseData.items():
                                        if inflictedForm == form:
                                            parses.append(f"{tense} {voice} {mood} {gender} {case} {number}")
        return parses
    def getLatinVerb(self, *, verbs: list[str], tenses: list[str], voices: list[str], moods: list[str]) -> tuple[str]:
        """
        gets a latin verb from tables.VERBS with the specified constraints\n
        returns lv, vb, tn, vo, mo, ps, gn, cs, nm
        """
        lv, vb, tn, vo, mo, ps, gn, cs, nm = (None,) * 9
        while lv is None:  # repeat until lv is not None
            # if self.evenlyChoose is True, then there will be no weight towards certain choices unlike
            # in the _else_ clause. eg INFN has a 20% chance to appear, even though there are so
            # few of them as opposed to the other verb elements.
            ps = random.choice(self.components["people"])  #   \
            gn = random.choice(self.components["genders"])  #   \
            cs = random.choice(self.components["cases"])  #      \
            nm = random.choice(self.components["numbers"])  #     \
            if self.evenlyChoose:  # <----------------------------'
                _, tn, vo, mo = random.choice(self.validForms)
                validAndAllowed = [
                    (verb, tense, voice, mood)
                    for verb, tense, voice, mood in self.validForms
                    if verb in verbs and tense in tenses and voice in voices and mood in moods
                ]
                vb, tn, vo, mo = random.choice(validAndAllowed)
            else:
                vb = random.choice(verbs)
                tn = random.choice(tenses)
                vo = random.choice(voices)
                mo = random.choice(moods)
            match mo:
                case "INFN":
                    lv = tables.VERBS[vb][tn][vo][mo]
                case "PTCP":
                    lv = tables.VERBS[vb][tn][vo][mo][gn][cs][nm]
                case "INDC" | "SUBJ" | "IMPT":
                    lv = tables.VERBS[vb][tn][vo][mo][ps]
                case _:
                    raise ValueError(f"{mo} is an invalid mood. (getLatinVerb)")
        return lv, vb, tn, vo, mo, ps, gn, cs, nm
    def onTabChanged(self, event) -> None:
        # get the current and previous tabs
        current = self.currentTab(self.verbNotebook)
        previous = self.lastTab
        self.lastTab = current
        if current in [self.parsingFrame, self.typingFrame]:  # the user just entered parsing OR typing mode
            if not all(self.allowed.values()):  # and there is a category in self.allowed which is insufficient
                self.verbNotebook.select(self.setupFrame)  # sends the user back to the setup frame
                msg.showerror("XD", "please pick at least one of everything")  # and displays a message to tell the user
                return
            if not self.doesValidVTVMComboExist():  # if  all vtvm combos are invalid
                self.verbNotebook.select(self.setupFrame)  # tell the user and send them back to setup mode
                msg.showerror("XD", "all combos are invalid")
                return
        if current is self.parsingFrame:  # the user just entered parsing mode
            self.nextParse()  # refreshes the verb to avoid cheating ig...?
        if current is self.typingFrame:  # the user just entered typing mode
            self.nextTyping()  # refresh
    def enterPressed(self, _) -> None:
        current = self.currentTab(self.verbNotebook)
        if current is self.parsingFrame:
            if self.parsingConfirmButton["state"] == "normal":
                self.confirmParsing()
        elif current is self.typingFrame:
            if self.typingConfirmButton["state"] == "normal":
                self.confirmTyping()
    def spacePressed(self, _) -> None:
        current = self.currentTab(self.verbNotebook)
        if current is self.parsingFrame:
            if self.parsingNextButton.winfo_ismapped():  # if the next button is shown
                self.nextParse()
        elif current is self.typingFrame:
            if self.typingNextButton.winfo_ismapped():  # if the next button is shown
                self.nextTyping()
    # functions for REVIEW
    def displayReviewBeyondMoods(self, mood) -> None:
        """when the mood (review) is selected, the choices beyond wil alter to suit it."""
        match mood:
            case "INDC" | "SUBJ" | "IMPT":
                self.reviewPersonFrame.grid()
                self.reviewParticipleFrame.grid_remove()
            case "INFN":
                self.reviewPersonFrame.grid_remove()
                self.reviewParticipleFrame.grid_remove()
            case "PTCP":
                self.reviewPersonFrame.grid_remove()
                self.reviewParticipleFrame.grid()
        self.renderReviewLatinVerb("gavin")
    def renderReviewLatinVerb(self, _) -> None:
        # get all the stats the user entered
        verb = self.reviewVerbUserval.get()
        tense = self.reviewTenseUserval.get()
        voice = self.reviewVoiceUserval.get()
        mood = self.reviewMoodUserval.get()
        match mood:
            case "INDC" | "SUBJ" | "IMPT":
                person = self.reviewPersonUserval.get()
                self.reviewLatinVerb = tables.VERBS[verb][tense][voice][mood][person]
            case "INFN":
                self.reviewLatinVerb = tables.VERBS[verb][tense][voice][mood]
            case "PTCP":
                gender = self.reviewGenderUserval.get()
                case = self.reviewCaseUserval.get()
                number = self.reviewNumberUserval.get()
                self.reviewLatinVerb = tables.VERBS[verb][tense][voice][mood][gender][case][number]
        # display
        if self.reviewLatinVerb is not None:
            self.reviewDisplayor.config(text=self.reviewLatinVerb)
        else:
            self.reviewDisplayor.config(text="N/A")
    # functions for SETUP
    def doesValidVTVMComboExist(self) -> bool:
        combos = []
        for verb, verbVal in self.setupVerbUservals.items():
            verbVal: bool = verbVal.get()
            for tense, tenseVal in self.setupTenseUservals.items():
                tenseVal: bool = tenseVal.get()
                for voice, voiceVal in self.setupVoiceUservals.items():
                    voiceVal: bool = voiceVal.get()
                    for mood, moodVal in self.setupMoodUservals.items():
                        moodVal: bool = moodVal.get()
                        if verbVal and tenseVal and voiceVal and moodVal:
                            combos.append(self.verbFormExists(verb, tense, voice, mood))
        return any(combos)
    def updateAllowance(self):
        print("updating allowance")
        self.allowed["verbs"]  = self.selected(self.setupVerbUservals)
        self.allowed["tenses"] = self.selected(self.setupTenseUservals)
        self.allowed["voices"] = self.selected(self.setupVoiceUservals)
        self.allowed["moods"]  = self.selected(self.setupMoodUservals)
        self.parsingCorrect = 0
        self.parsingIncorrect = 0
        self.refreshVerbRBs()
        self.updateParsingScore()
        if not all(self.allowed.values()):
            self.parsingDisplayor.config(text="INSUFFICIENCY")
            self.parsingConfirmButton.config(state="disabled")
            self.parsingLVUninflected = None
            return
    def selectAllSetupCBs(self) -> None:
        for CBs in [self.setupTenseUservals, self.setupVoiceUservals, self.setupMoodUservals, self.setupVerbUservals]:
            for _, CB in CBs.items():
                CB.set(1)  # checks
        self.updateAllowance()
    def deselectAllSetupCBs(self) -> None:
        for CBs in [self.setupTenseUservals, self.setupVoiceUservals, self.setupMoodUservals, self.setupVerbUservals]:
            for _, CB in CBs.items():
                CB.set(0)  # unchecks
        self.updateAllowance()
    # functions for PARSING
    def configParsingRBs(self, state: str) -> None:
        for rbs in [self.parsingTenseRBs, self.parsingVoiceRBs, self.parsingMoodRBs, self.parsingPersonRBs, self.parsingGenderRBs, self.parsingNumberRBs, self.parsingCaseRBs]:
            for rb in rbs.values():
                rb.config(state=state)
    def whatDidTheUserParse(self) -> dict[str, str]:
        """empty selections are shown by the EMPTY STRING "" !!!!!!!!!"""
        vb = self.parsingLVUninflected
        tn = self.parsingTenseUserval.get()
        vo = self.parsingVoiceUserval.get()
        mo = self.parsingMoodUserval.get()
        ps = self.parsingPersonUserval.get()
        gn = self.parsingGenderUserval.get()
        cs = self.parsingCaseUserval.get()
        nm = self.parsingNumberUserval.get()
        return {
            "verbs"  : vb,
            "tenses" : tn,
            "voices" : vo,
            "moods"  : mo,
            "people" : ps,
            "genders": gn,
            "cases"  : cs,
            "numbers": nm
        }
    def refreshVerbRBs(self) -> None:
        # deselect all RBs
        for rbVar in [self.parsingTenseUserval, self.parsingVoiceUserval, self.parsingMoodUserval, self.parsingPersonUserval, self.parsingGenderUserval, self.parsingCaseUserval, self.parsingNumberUserval]:
            rbVar.set("")
        groups = {"tenses": self.parsingTenseRBs, "voices": self.parsingVoiceRBs, "moods": self.parsingMoodRBs}
        for thing, RBs in groups.items():
            for component in self.components[thing]:
                rb = RBs[component]
                if component in self.allowed[thing]:
                    rb.config(state="normal")
                else:
                    rb.config(state="disabled")
    def renderNewLatinVerb(self) -> None:
        """user's time to guess STARTS HERE!!!!!"""
        # get the verb
        self.parsingLatinVerb, self.parsingLVUninflected, *_ = self.getLatinVerb(
            verbs=self.allowed["verbs"], tenses=self.allowed["tenses"], voices=self.allowed["voices"], moods=self.allowed["moods"]
        )
        self.parsingDisplayor.config(text=self.parsingLatinVerb)  # display the verb      
        self.parsingConfirmButton.config(state="disabled")  # disable the confirm button
        # timer stuff
        self.parsingTimer.start()
    def displayParsingBeyondMoods(self, mood) -> None:
        """when the mood (parsing) is selected, the choices beyond will alter to suit it."""
        match mood:
            case "INDC" | "SUBJ" | "IMPT":
                self.parsingPersonFrame.grid()
                self.parsingParticipleFrame.grid_remove()
                for component in [self.parsingGenderUserval, self.parsingCaseUserval, self.parsingNumberUserval]: component.set("")
            case "INFN":
                self.parsingPersonFrame.grid_remove()
                self.parsingParticipleFrame.grid_remove()
                for component in [self.parsingGenderUserval, self.parsingCaseUserval, self.parsingNumberUserval, self.parsingPersonUserval]: component.set("")
            case "PTCP":
                self.parsingPersonFrame.grid_remove()
                self.parsingParticipleFrame.grid()
                self.parsingPersonUserval.set("")
        self.updateParsingConfirmButton("???")
    def confirmParsing(self) -> None:
        """checks if the deatils entered by the user are parsingCorrect"""
        if self.parsingLVUninflected is None: msg.showerror("gavin", "self.parsingLVUninflected is None"); return
        # get all user inputs
        userVerb, userTense, userVoice, userMood, userPerson, userGender, userCase, userNumber = list(self.whatDidTheUserParse().values())
        # timer stuff
        self.parsingTimer.stop()
        # find the user's parse
        match userMood:
            case "INDC" | "SUBJ" | "IMPT":
                self.userLatinVerb = tables.VERBS[userVerb][userTense][userVoice][userMood][userPerson]
            case "INFN":
                self.userLatinVerb = tables.VERBS[userVerb][userTense][userVoice][userMood]
            case "PTCP":
                self.userLatinVerb = tables.VERBS[userVerb][userTense][userVoice][userMood][userGender][userCase][userNumber]
            case _:
                raise ValueError(f"invalid user mood {userMood} (confirmParsing function)")
        # DECIDE WHAT TO DO IN (IN)CORRECT SITUATIONS
        self.possibleParsesList = self.possibleParsesOfVerb(self.parsingLatinVerb)
        self.possibleParsesStr = ", ".join(self.possibleParsesList)
        self.parsingStatus = self.userLatinVerb == self.parsingLatinVerb
        if self.parsingStatus:
            self.parsingCorrect += 1
        else:
            self.parsingIncorrect += 1
            msg.showinfo(
                title="you could have had these instead:",
                message=f"possible parses of {self.parsingLatinVerb} ({self.parsingLVUninflected}):\n{',\n'.join(self.possibleParsesList)}.\nyou parsed {self.userLatinVerb}"
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
        match self.parsingMoodUserval.get():
            case "INDC" | "SUBJ" | "IMPT":
                if self.parsingTenseUserval.get() and self.parsingVoiceUserval.get() and self.parsingPersonUserval.get():
                    self.parsingConfirmButton.config(state="normal")
                else:
                    self.parsingConfirmButton.config(state="disabled")
            case "INFN":
                if self.parsingTenseUserval.get() and self.parsingVoiceUserval.get():
                    self.parsingConfirmButton.config(state="normal")
                else:
                    self.parsingConfirmButton.config(state="disabled")
            case "PTCP":
                if self.parsingTenseUserval.get() and self.parsingVoiceUserval.get() and self.parsingGenderUserval.get() and self.parsingCaseUserval.get() and self.parsingNumberUserval.get():
                    self.parsingConfirmButton.config(state="normal")
                else:
                    self.parsingConfirmButton.config(state="disabled")
            case _:  # mood is not selected
                self.parsingConfirmButton.config(state="disabled")
    def updateParsingScore(self) -> None:
        self.parsingCorrectLabel.config(text=self.parsingCorrect)
        self.parsingIncorrectLabel.config(text=self.parsingIncorrect)
    def nextParse(self) -> None:
        for rb in [
            self.parsingTenseUserval, self.parsingVoiceUserval, self.parsingMoodUserval, self.parsingPersonUserval,
            self.parsingGenderUserval, self.parsingCaseUserval, self.parsingNumberUserval
            ]:  # reset rbs
            rb.set("")
        self.configParsingRBs("normal")  # enable the parsing rbs
        self.renderNewLatinVerb()  # new round
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
        self.typingStatus = self.typingUserInput == self.typingLatinVerb
        if self.typingStatus:  # correct
            self.typingCorrect += 1
        else:
            self.typingIncorrect += 1
            msg.showinfo(
                title="feedback",
                message=f"correct answer: {self.typingLatinVerb}"
            )
        # general
        self.updateTypingScore()
        self.updateResults(mode="typing")
        # show the next button
        self.typingNextButton.place(x=self.width//2, y=self.height-100, anchor="center")
    def nextTyping(self) -> None:
        # get the data
        self.typingLatinVerb, self.typingVerbUninflected, self.typingTense, self.typingVoice, self.typingMood, self.typingPerson, self.typingGender, self.typingCase, self.typingNumber = self.getLatinVerb(
            verbs=self.allowed["verbs"], tenses=self.allowed["tenses"], voices=self.allowed["voices"], moods=self.allowed["moods"]
        )
        # form the message
        match self.typingMood:
            case "INDC" | "SUBJ" | "IMPT":
                message = " ".join([x for x in (self.typingTense, self.typingVoice, self.typingMood, self.typingPerson) if x])
            case "INFN":
                message = " ".join([x for x in (self.typingTense, self.typingVoice, self.typingMood) if x])
            case "PTCP":
                if (self.typingTense, self.typingVoice) != ("FUTR", "PAS"):
                    message = " ".join([x for x in (self.typingTense, self.typingVoice, self.typingMood, self.typingGender, self.typingCase, self.typingNumber) if x])
                else:
                    message = " ".join([x for x in ("GERUNDIVE", self.typingGender, self.typingCase, self.typingNumber) if x])
            case _:
                raise ValueError("typing mood is not in INDC SUBJ IMPT INFN PTCP")
        message = f"type this form of {self.typingVerbUninflected}:\n{message}"
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
            userParse = " ".join([x for x in list(self.whatDidTheUserParse().values())[1:] if x])  # to remove the first k:v pair (the verb eg "verb": "amo")
            self.results.append({
                "verb": self.parsingLatinVerb,  # the verb asked
                "status": self.parsingStatus,  # whether it was right or not
                "you put": userParse,  # user parse
                "possible answers": self.possibleParsesOfVerb(self.parsingLatinVerb),  # possible answers
                "time taken": self.parsingTimer.value,  # time taken
            })
            # get/make data to display
            row = len(self.results) - 1
            currentResults = self.results[-1]
            question, status, youPut, possible, timeTaken = currentResults.values()
            colour = "#00ff00" if status else "#ff0000"
            possibleRollover = 1  # this can be changed if needed
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
                "answer": self.typingLatinVerb,
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
        """this is the subtab for the REVIEW mode, where users can see a "cheat sheet" of verb inflections (tables.VERBS)"""
        # create the frame
        self.reviewFrame = tk.Frame(parentNotebook, bg=self.bgCol, width=self.width, height=self.height)
        # create displayor
        self.reviewDisplayor = tk.Label(self.reviewFrame, text="amo", font=self.displayFont, bg=self.bgCol, fg=self.fgCol)
        self.reviewDisplayor.grid(row=0, column=0, columnspan=999)
        # create spacer
        tk.Label(self.reviewFrame, bg=self.bgCol, width=6).grid(row=1, column=0)
        # create the ptcp frame
        self.reviewParticipleFrame = tk.Frame(self.reviewFrame, width=self.width, bg=self.bgCol)
        self.reviewParticipleFrame.grid(row=5, column=1, sticky="ew")
        self.reviewParticipleFrame.grid_remove()  # this is to ensure that the ptcp frame knows where it is before being shown for the first time
        # other frames and things...
        self.reviewVerbFrame,  self.reviewVerbRBs,    self.reviewVerbUserval   = self.makeSelectors(mode="rb", thing="verbs",   parentFrame=self.reviewFrame, coords=(1, 1), command=self.renderReviewLatinVerb,    setting="AMO", cols=5)
        self.reviewTenseFrame,  self.reviewTenseRBs,  self.reviewTenseUserval  = self.makeSelectors(mode="rb", thing="tenses",  parentFrame=self.reviewFrame, coords=(2, 1), command=self.renderReviewLatinVerb,    setting="PRES")
        self.reviewVoiceFrame,  self.reviewVoiceRBs,  self.reviewVoiceUserval  = self.makeSelectors(mode="rb", thing="voices",  parentFrame=self.reviewFrame, coords=(3, 1), command=self.renderReviewLatinVerb,    setting="ACT")
        self.reviewMoodFrame,   self.reviewMoodRBs,   self.reviewMoodUserval   = self.makeSelectors(mode="rb", thing="moods",   parentFrame=self.reviewFrame, coords=(4, 1), command=self.displayReviewBeyondMoods, setting="INDC")
        self.reviewPersonFrame, self.reviewPersonRBs, self.reviewPersonUserval = self.makeSelectors(mode="rb", thing="people",  parentFrame=self.reviewFrame, coords=(5, 1), command=self.renderReviewLatinVerb,    setting="1S")
        self.reviewGenderFrame, self.reviewGenderRBs, self.reviewGenderUserval = self.makeSelectors(mode="rb", thing="genders", parentFrame=self.reviewParticipleFrame, coords=(1, 1), command=self.renderReviewLatinVerb, setting="MASC")
        self.reviewCaseFrame,   self.reviewCaseRBs,   self.reviewCaseUserval   = self.makeSelectors(mode="rb", thing="cases",   parentFrame=self.reviewParticipleFrame, coords=(2, 1), command=self.renderReviewLatinVerb, setting="NOM")
        self.reviewNumberFrame, self.reviewNumberRBs, self.reviewNumberUserval = self.makeSelectors(mode="rb", thing="numbers", parentFrame=self.reviewParticipleFrame, coords=(3, 1), command=self.renderReviewLatinVerb, setting="SG")
        # add the frame to the parent notebook
        parentNotebook.add(self.reviewFrame, text="REVIEW")
    def buildSetupSubtab(self, parentNotebook: ttk.Notebook) -> None:
        """this is the subtab for the SETUP mode, where users can choose what things they wish to be tested on."""
        # create the verb setup frame
        self.setupFrame = tk.Frame(parentNotebook, bg=self.bgCol, width=self.width, height=self.height)
        # create the header
        tk.Label(self.setupFrame, text="choose options:", bg=self.bgCol, fg=self.fgCol, font=("Arial", 25)).grid(row=0, column=0, columnspan=999)
        # create a spacer to avoid leftjustification
        tk.Label(self.setupFrame, bg=self.bgCol, width=6).grid(row=1, column=0)
        # create the widgets
        self.setupVerbFrame,  self.setupVerbCBs,  self.setupVerbUservals  = self.makeSelectors(mode="cb", thing="verbs",  parentFrame=self.setupFrame, coords=(1, 1), command=self.updateAllowance, cols=5)
        self.setupTenseFrame, self.setupTenseCBs, self.setupTenseUservals = self.makeSelectors(mode="cb", thing="tenses", parentFrame=self.setupFrame, coords=(2, 1), command=self.updateAllowance)
        self.setupVoiceFrame, self.setupVoiceCBs, self.setupVoiceUservals = self.makeSelectors(mode="cb", thing="voices", parentFrame=self.setupFrame, coords=(3, 1), command=self.updateAllowance)
        self.setupMoodFrame,  self.setupMoodCBs,  self.setupMoodUservals  = self.makeSelectors(mode="cb", thing="moods",  parentFrame=self.setupFrame, coords=(4, 1), command=self.updateAllowance)
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
        """this is the subtab for the PARSING mode, where users parse latin verbs with the constraints chosen from the SETUP mode."""
        # create the verb parsing frame
        self.parsingFrame = tk.Frame(parentNotebook, bg=self.bgCol, width=self.width, height=self.height)
        self.parsingHeaderFrame = tk.Frame(self.parsingFrame, bg=self.bgCol, width=self.width)
        self.parsingHeaderFrame.grid(row=0, column=0, columnspan=999)
        # create verb displayor
        self.parsingDisplayor = tk.Label(self.parsingHeaderFrame, bg=self.bgCol, fg=self.fgCol, font=self.displayFont)
        self.parsingDisplayor.grid(row=0, column=0, sticky="ew")
        # create verb score labels
        self.parsingCorrectLabel = tk.Label(self.parsingFrame, text=self.parsingCorrect, bg=self.bgCol, fg="#00ff00", font=("Arial bold", 20))
        self.parsingCorrectLabel.place(x=10, y=10)
        self.parsingIncorrectLabel = tk.Label(self.parsingFrame, text=self.parsingIncorrect, bg=self.bgCol, fg="#ff0000", font=("Arial bold", 20))
        self.parsingIncorrectLabel.place(relx=1, x=-10, y=10, anchor="ne")
        # create spacer
        tk.Label(self.parsingFrame, width=6, bg=self.bgCol).grid(row=1, column=0)
        # create the ptcp frame
        self.parsingParticipleFrame = tk.Frame(self.parsingFrame, width=self.width, bg=self.bgCol)
        self.parsingParticipleFrame.grid(row=5, column=1, sticky="ew")
        self.parsingParticipleFrame.grid_remove()  # this is to ensure that the ptcp frame knows where it is before being shown for the first time
        # create the other widgets
        self.parsingTenseFrame,  self.parsingTenseRBs,  self.parsingTenseUserval  = self.makeSelectors(mode="rb", thing="tenses",  parentFrame=self.parsingFrame, coords=(1, 1), command=self.updateParsingConfirmButton)
        self.parsingVoiceFrame,  self.parsingVoiceRBs,  self.parsingVoiceUserval  = self.makeSelectors(mode="rb", thing="voices",  parentFrame=self.parsingFrame, coords=(2, 1), command=self.updateParsingConfirmButton)
        self.parsingMoodFrame,   self.parsingMoodRBs,   self.parsingMoodUserval   = self.makeSelectors(mode="rb", thing="moods",   parentFrame=self.parsingFrame, coords=(3, 1), command=self.displayParsingBeyondMoods)
        self.parsingPersonFrame, self.parsingPersonRBs, self.parsingPersonUserval = self.makeSelectors(mode="rb", thing="people",  parentFrame=self.parsingFrame, coords=(4, 1), command=self.updateParsingConfirmButton)
        self.parsingGenderFrame, self.parsingGenderRBs, self.parsingGenderUserval = self.makeSelectors(mode="rb", thing="genders", parentFrame=self.parsingParticipleFrame, coords=(0, 1), command=self.updateParsingConfirmButton)
        self.parsingCaseFrame,   self.parsingCaseRBs,   self.parsingCaseUserval   = self.makeSelectors(mode="rb", thing="cases",   parentFrame=self.parsingParticipleFrame, coords=(1, 1), command=self.updateParsingConfirmButton)
        self.parsingNumberFrame, self.parsingNumberRBs, self.parsingNumberUserval = self.makeSelectors(mode="rb", thing="numbers", parentFrame=self.parsingParticipleFrame, coords=(2, 1), command=self.updateParsingConfirmButton)
        # other stuff
        self.parsingConfirmButton = tk.Button(self.parsingFrame, text="CHECK", font=("Arial bold", 8), state="disabled", command=self.confirmParsing)
        self.parsingConfirmButton.grid(row=999, column=1, sticky="ew")
        self.parsingNextButton = tk.Button(self.parsingFrame, text="NEXT", font=("Arial", 10), width=6, command=self.nextParse)
        # add frame to verb notebook
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
    def BUILD_VERB_TAB(self, PARENT_NOTEBOOK: ttk.Notebook) -> None:
        # create verb frame
        self.verbFrame = tk.Frame(PARENT_NOTEBOOK, bg=self.bgCol, width=self.width, height=self.height)
        # create verb notebook inside verb frame
        self.verbNotebook = ttk.Notebook(self.verbFrame)
        self.verbNotebook.pack(fill="both", expand=True)
        self.verbNotebook.bind("<<NotebookTabChanged>>", self.onTabChanged)
        self.verbNotebook.bind("<Return>", self.enterPressed)
        self.verbNotebook.bind("<space>", self.spacePressed)
        # add verb subtabs
        self.buildReviewSubtab(self.verbNotebook)
        self.buildSetupSubtab(self.verbNotebook)
        self.buildParsingSubtab(self.verbNotebook)
        self.buildTypingSubtab(self.verbNotebook)
        self.buildResultsSubtab(self.verbNotebook)
        # other
        self.verbNotebook.select(self.resultsOuterFrame)  # this is needed to fix bug where keybinds only work
        self.verbNotebook.select(self.reviewFrame)  # after visiting the results tab
        # add verb frame
        PARENT_NOTEBOOK.add(self.verbFrame, text="VERBS")
