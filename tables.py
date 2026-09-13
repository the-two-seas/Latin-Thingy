# functions
def decline212(word: str) -> dict[str, dict[str, dict[str, str]]]:
    stem = word[:-2]
    return {
        "MASC": {
            "NOM": {
                "SG": stem + "us",
                "PL": stem + "ī"
            },
            "VOC": {
                "SG": stem + "e",
                "PL": stem + "ī"
            },
            "ACC": {
                "SG": stem + "um",
                "PL": stem + "ōs"
            },
            "GEN": {
                "SG": stem + "ī",
                "PL": stem + "ōrum"
            },
            "DAT": {
                "SG": stem + "ō",
                "PL": stem + "īs"
            },
            "ABL": {
                "SG": stem + "ō",
                "PL": stem + "īs"
            }
        },
        "FEMN": {
            "NOM": {
                "SG": stem + "a",
                "PL": stem + "ae"
            },
            "VOC": {
                "SG": stem + "a",
                "PL": stem + "ae"
            },
            "ACC": {
                "SG": stem + "am",
                "PL": stem + "ās"
            },
            "GEN": {
                "SG": stem + "ae",
                "PL": stem + "ārum"
            },
            "DAT": {
                "SG": stem + "ae",
                "PL": stem + "īs"
            },
            "ABL": {
                "SG": stem + "ā",
                "PL": stem + "īs"
            }
        },
        "NEUT": {
            "NOM": {
                "SG": stem + "um",
                "PL": stem + "a"
            },
            "VOC": {
                "SG": stem + "um",
                "PL": stem + "a"
            },
            "ACC": {
                "SG": stem + "um",
                "PL": stem + "a"
            },
            "GEN": {
                "SG": stem + "ī",
                "PL": stem + "ōrum"
            },
            "DAT": {
                "SG": stem + "ō",
                "PL": stem + "īs"
            },
            "ABL": {
                "SG": stem + "ō",
                "PL": stem + "īs"
            }
        }
    }
def decline33_i(word: str, gen: str) -> dict[str, dict[str, dict[str, str]]]:
    stem = gen[:-2]
    return {
        "MASC": {
            "NOM": {
                "SG": word,
                "PL": stem + "ēs"
            },
            "VOC": {
                "SG": word,
                "PL": stem + "ēs"
            },
            "ACC": {
                "SG": stem + "em",
                "PL": stem + "ēs"
            },
            "GEN": {
                "SG": stem + "is",
                "PL": stem + "ium"
            },
            "DAT": {
                "SG": stem + "ī",
                "PL": stem + "ibus"
            },
            "ABL": {
                "SG": stem + "e",
                "PL": stem + "ibus"
            }
        },
        "FEMN": {
            "NOM": {
                "SG": word,
                "PL": stem + "ēs"
            },
            "VOC": {
                "SG": word,
                "PL": stem + "ēs"
            },
            "ACC": {
                "SG": stem + "em",
                "PL": stem + "ēs"
            },
            "GEN": {
                "SG": stem + "is",
                "PL": stem + "ium"
            },
            "DAT": {
                "SG": stem + "ī",
                "PL": stem + "ibus"
            },
            "ABL": {
                "SG": stem + "e",
                "PL": stem + "ibus"
            }
        },
        "NEUT": {
            "NOM": {
                "SG": word,
                "PL": stem + "ia"
            },
            "VOC": {
                "SG": word,
                "PL": stem + "ia"
            },
            "ACC": {
                "SG": word,
                "PL": stem + "ia"
            },
            "GEN": {
                "SG": stem + "is",
                "PL": stem + "ium"
            },
            "DAT": {
                "SG": stem + "ī",
                "PL": stem + "ibus"
            },
            "ABL": {
                "SG": stem + "e",
                "PL": stem + "ibus"
            }
        } 
    }
def inflection(s1, s2, s3, p1, p2, p3) -> dict[str, str]:
    return {
        "1S": s1,
        "2S": s2,
        "3S": s3,
        "1P": p1,
        "2P": p2,
        "3P": p3
    }
def constantInflection(s) -> dict[str, str]:
    return inflection(s, s, s, s, s, s)
def unmacron(s: str) -> str:
    if s is None: return None
    return s.translate(str.maketrans({
        "ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u", "ȳ": "y",
        "Ā": "A", "Ē": "E", "Ī": "I", "Ō": "O", "Ū": "U", "Ȳ": "Y",
    }))
def addNounEndings(q, w, e, r, t, y, a, s, d, f, g, h, *, stem) -> dict:
    return {
        "NOM": {"SG": stem + q, "PL": stem + a},
        "VOC": {"SG": stem + w, "PL": stem + s},
        "ACC": {"SG": stem + e, "PL": stem + d},
        "GEN": {"SG": stem + r, "PL": stem + f},
        "DAT": {"SG": stem + t, "PL": stem + g},
        "ABL": {"SG": stem + y, "PL": stem + h}
    }
def noun(nom: str, gen: str, isNeut: bool = False, i: bool = False, **overrides) -> dict:
    # analyse (1f, 2m, 2n, 3mf, 3n, 4m, 4n, 5fa, 5fb)
    def ends(x, y): return nom.endswith(x) and gen.endswith(y)
    if ends("a", "ae"):      kind, stem = "1f", nom.removesuffix("a")  # nauta
    elif ends("us", "ī"):    kind, stem = "2m", nom.removesuffix("us")  # fagus
    elif ends("um", "ī"):    kind, stem = "2n", nom.removesuffix("um")  # ?!
    elif gen.endswith("is"): kind, stem = "3"+("n" if isNeut else "mf")+("i" if i else ""), gen.removesuffix("is")
    elif ends("us", "ūs"):   kind, stem = "4m", nom.removesuffix("us")  # manus
    elif ends("ū", "ūs"):    kind, stem = "4n", nom.removesuffix("ū")  # cornu genu pecu veru
    elif ends("iēs", "iēī"): kind, stem = "5fi",nom.removesuffix("ēs")  # dies
    elif ends("ēs", "eī"):   kind, stem = "5f", nom.removesuffix("ēs")
    # create endings dict
    endings = {
        "1f": ("a", "a", "am", "ae", "ae", "ā", "ae", "ae", "ās", "ārum", "īs", "īs"),
        "2m": ("us", "e", "um", "ī", "ō", "ō", "ī", "ī", "ōs", "ōrum", "īs", "īs"),
        "2n": ("um", "um", "um", "ī", "ō", "ō", "a", "a", "a", "ōrum", "īs", "īs"),
        "3mf":  ("", "", "em", "is", "ī", "e", "ēs", "ēs", "ēs", "um", "ibus", "ibus"), 
        "3n":   ("", "", "", "is", "ī", "e", "a", "a", "a", "um", "ibus", "ibus"), 
        "3mfi": ("", "", "em", "is", "ī", "e", "ēs", "ēs", "ēs", "ium", "ibus", "ibus"), 
        "3ni":  ("", "", "", "is", "ī", "e", "ia", "ia", "ia", "ium", "ibus", "ibus"), 
        "4m": ("us", "us", "um", "ūs", "uī", "ū", "ūs", "ūs", "ūs", "uum", "ibus", "ibus"),
        "4n": ("ū", "ū", "ū", "ūs", "ū", "ū", "ua", "ua", "ua", "uum", "ibus", "ibus"),
        "5f": ("ēs", "ēs", "em", "eī", "eī", "ē", "ēs", "ēs", "ēs", "ērum", "ēbus", "ēbus"),
        "5fi": ("ēs", "ēs", "em", "ēī", "ēī", "ē", "ēs", "ēs", "ēs", "ērum", "ēbus", "ēbus")
    }
    # create noun
    table = addNounEndings(*(endings[kind]), stem=stem)
    table["NOM"]["SG"] = nom
    table["GEN"]["SG"] = gen
    if kind in ("3mf", "3mfi"):
        table["VOC"]["SG"] = nom
    elif kind in ("3n", "3ni"):
        table["VOC"]["SG"] = nom
        table["ACC"]["SG"] = nom
    # do any overrides
    for location, override in overrides.items():
        location = f"""table{"".join([f"['{l.upper()}']" for l in location.split("_")])}"""
        if isinstance(override, str):
            exec(f"{location} = '{override}'")
        elif isinstance(override, dict):
            exec(f"{location} = {override}")
        else: raise ValueError
    return table

# empty stuff
def emptyParticiple() -> dict:
    return {
        gender: {
            case: {"SG": None, "PL": None}
            for case in ["NOM", "VOC", "ACC", "GEN", "DAT", "ABL"]
        }
        for gender in ["MASC", "FEMN", "NEUT"]
    }
def emptyInflection() -> dict:
    return {
        person: None
        for person in ["1S", "2S", "3S", "1P", "2P", "3P"]
    }
def emptyVoice() -> dict:
    return {
        "INDC": emptyInflection(),
        "SUBJ": emptyInflection(),
        "IMPT": emptyInflection(),
        "INFN": None,
        "PTCP": emptyParticiple()
    }
def emptyTense() -> dict:
    return {"ACT": emptyVoice(), "PAS": emptyVoice()}
def emptyVerb() -> dict:
    return {t: emptyTense() for t in ("PRES", "IMPF", "PERF", "PLPF", "FUTR", "FTPF")}
EMPTY_PARTICIPLE = emptyParticiple()
EMPTY_INFLECTION = emptyInflection()
EMPTY_VOICE = emptyVoice()
EMPTY_TENSE = emptyTense()
EMPTY_VERB = emptyVerb()
EMPTY = [EMPTY_VERB, EMPTY_TENSE, EMPTY_PARTICIPLE, EMPTY_INFLECTION, EMPTY_VOICE, None]

# verbs
PRESENT_SYSTEM = ("PRES", "IMPF", "FUTR")
PERFECT_SYSTEM = ("PERF", "PLPF", "FTPF")

def analyse(parts: tuple[str, str, str, str]) -> dict:
    pres, infn, perf, ppp = (*parts, None, None, None, None)[:4]
    transitivity = bool(ppp)  # ~= "passivity"
    # find kind and conj
    # regular and semideponent
    if   pres.endswith("ō")  and infn.endswith("āre"): kind, conj = "semideponent" if (perf.endswith("us sum") and (not ppp)) else "regular", 1
    elif pres.endswith("eō") and infn.endswith("ēre"): kind, conj = "semideponent" if (perf.endswith("us sum") and (not ppp)) else "regular", 2
    elif pres.endswith("iō") and infn.endswith("ere"): kind, conj = "semideponent" if (perf.endswith("us sum") and (not ppp)) else "regular", 3.5
    elif pres.endswith("ō")  and infn.endswith("ere"): kind, conj = "semideponent" if (perf.endswith("us sum") and (not ppp)) else "regular", 3
    elif pres.endswith("iō") and infn.endswith("īre"): kind, conj = "semideponent" if (perf.endswith("us sum") and (not ppp)) else "regular", 4
    # deponent
    elif pres.endswith("or")  and infn.endswith("ārī") and perf.endswith("us sum") and not ppp: kind, conj, regInf = "deponent", 1,   f"{infn[:-1]}e"
    elif pres.endswith("eor") and infn.endswith("ērī") and perf.endswith("us sum") and not ppp: kind, conj, regInf = "deponent", 2,   f"{infn[:-1]}e"
    elif pres.endswith("ior") and infn.endswith("īrī") and perf.endswith("us sum") and not ppp: kind, conj, regInf = "deponent", 4,   f"{infn[:-1]}e"
    elif pres.endswith("ior") and infn.endswith("ī")   and perf.endswith("us sum") and not ppp: kind, conj, regInf = "deponent", 3.5, f"{infn[:-3]}ere"
    elif pres.endswith("or")  and infn.endswith("ī")   and perf.endswith("us sum") and not ppp: kind, conj, regInf = "deponent", 3,   f"{infn[:-3]}ere"
    # defective
    elif pres.endswith("ī") and infn.endswith("isse") and not perf and not ppp: kind, conj = "defective", 1  # conj doesnt matter
    else: kind, conj, regInf = "regular", 3, infn
    # get stems
    match kind:
        case "regular":
            # get stems
            presStem = pres[:-2] if conj in [2, 3.5, 4] else pres[:-1]
            perfStem = perf.removesuffix("ī")
            ptcpStem = ppp.removesuffix("us")
            ptcpInflection = (ppp,)*3 + (f"{ptcpStem}ī",)*3
            regInf = infn
        case "semideponent":
            presStem = pres[:-2] if conj in [2, 3.5, 4] else pres[:-1]
            perfStem = None
            pap = perf.removesuffix(" sum")
            ptcpStem = pap.removesuffix("us")
            ptcpInflection = (pap,)*3 + (f"{ptcpStem}ī",)*3
            regInf = infn
        case "deponent":
            presStem = pres[:-3] if conj in [2, 3.5, 4] else pres[:-2]
            perfStem = None
            pap = perf.removesuffix(" sum")
            ptcpStem = pap.removesuffix("us")
            ptcpInflection = (pap,)*3 + (f"{ptcpStem}ī",)*3
        case "defective":
            presStem = pres.removesuffix("ī")
            perfStem, ptcpStem, ptcpInflection, regInf = None, None, None, None
    return {
        "kind": kind,
        "conj": conj,
        "transitivity": transitivity,
        "presStem": presStem,
        "perfStem": perfStem,
        "ptcpStem": ptcpStem,
        "ptcpInflection": ptcpInflection,
        "regularInfinitive": regInf
    }
def stitchConcise(stem: str | None, connection: str | None, ending: str | None) -> str | None:
    try:
        result = stem + connection + ending
    except TypeError:
        result = None
    return result
def stitchPeriphrastic(ptcp: str, word2: str) -> str:
    # ptcp may be PERF or FUTR, word2 may come from sum or is 'īrī'
    if word2 in ("īrī", "esse"):
        return f"{ptcp} {word2}"  # all INFNs go here
    elif word2 in ("sum", "es", "est", "eram", "erās", "erat", "erō", "eris", "erit", "sim", "sīs", "sit", "essem", "essēs", "esset"):
        return f"{ptcp} {word2}"  # all singular forms
    elif word2 in ("sumus", "estis", "sunt", "erāmus", "erātis", "erant", "erimus", "eritis", "erunt", "sīmus", "sītis", "sint", "essēmus", "essētis", "essent"):
        return f"{ptcp.removesuffix("us")}ī {word2}"  # all plural forms
    else:
        raise ValueError
def conjugate(parts: tuple[str], *, tense: str, voice: str, mood: str, person: str = None, gender: str = None, case: str = None, number: str = None, **analysisOverrides) -> str:
    """conjugates verb"""
    pres, infn, perf, ppp = (parts + (None,)*4)[:4]
    analysis = analyse(parts)  # analyse verb
    analysis |= analysisOverrides
    # create endings
    endings = {
        "ost": inflection("ō", "s", "t", "mus", "tis", "nt"),
        "mst": inflection("m", "s", "t", "mus", "tis", "nt"),
        "PAS": inflection("r", "ris", "tur", "mur", "minī", "ntur"),
        "PERF": inflection("ī", "istī", "it", "imus", "istis", "ērunt"),
        "sum PRES INDC": inflection("sum", "es", "est", "sumus", "estis", "sunt"),
        "sum PRES SUBJ": inflection("sim", "sīs", "sit", "sīmus", "sītis", "sint"),
        "sum IMPF INDC": inflection("eram", "erās", "erat", "erāmus", "erātis", "erant"),
        "sum IMPF SUBJ": inflection("essem", "essēs", "esset", "essēmus", "essētis", "essent"),
        "sum FUTR": inflection("erō", "eris", "erit", "erimus", "eritis", "erunt"),
        "vowel": {1: "ā", 2: "ē", 3: "ē", 3.5: "iē", 4: "iē"},
        "PRES ACT IMPT": inflection(None, "", None, None, "te", None),
        "PRES PAS IMPT": inflection(None, "re", None, None, "minī", None),
        "FUTR ACT IMPT": inflection(None, "tō", "tō", None, "tōte", "ntō"),
        "FUTR PAS IMPT": inflection(None, "tor", "tor", None, None, "ntor"),
        "mst with e": inflection("em", "ēs", "et", "ēmus", "ētis", "ent"),
        "PAS with e": inflection("er", "ēris", "ētur", "ēmur", "ēminī", "entur"),
        "IMPF ACT": inflection("bam", "bās", "bat", "bāmus", "bātis", "bant"),
        "IMPF PAS": inflection("bar", "bāris", "bātur", "bāmur", "bāminī", "bantur"),
        "FTPF": inflection("erō", "eris", "erit", "erimus", "eritis", "erint"),
        "PERF SUBJ": inflection("erim", "erīs", "erit", "erīmus", "erītis", "erint")
    }
    # create connectors
    connectors = {
        1: {
            "PRES": {
                "ACT": {
                    "INDC": inflection("", "ā", "a", "ā", "ā", "a"),
                    "SUBJ": inflection("e", "ē", "e", "ē", "ē", "e"),
                    "IMPT": inflection(None, "ā", None, None, "ā", None)
                },
                "PAS": {
                    "INDC": inflection("o", "ā", "ā", "ā", "ā", "a"),
                    "SUBJ": inflection("e", "ē", "ē", "ē", "ē", "e"),
                    "IMPT": inflection(None, "ā", None, None, "ā", None)
                }
            },
            "FUTR": {
                "ACT": {
                    "INDC": inflection("āb", "ābi", "ābi", "ābi", "ābi", "ābu"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "ā", "ā", None, "ā", "a")
                },
                "PAS": {
                    "INDC": inflection("ābo", "ābe", "ābi", "ābi", "ābi", "ābu"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "ā", "ā", None, None, "a")
                }
            }
        },
        2: {
            "PRES": {
                "ACT": {
                    "INDC": inflection("e", "ē", "e", "ē", "ē", "e"),
                    "SUBJ": inflection("ea", "eā", "ea", "eā", "eā", "ea"),
                    "IMPT": inflection(None, "ē", None, None, "ē", None)
                },
                "PAS": {
                    "INDC": inflection("eo", "ē", "ē", "ē", "ē", "e"),
                    "SUBJ": inflection("ea", "eā", "eā", "eā", "eā", "ea"),
                    "IMPT": inflection(None, "ē", None, None, "ē", None)
                }
            },
            "FUTR": {
                "ACT": {
                    "INDC": inflection("ēb", "ēbi", "ēbi", "ēbi", "ēbi", "ēbu"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "ē", "ē", None, "ē", "e")
                },
                "PAS": {
                    "INDC": inflection("ēbo", "ēbe", "ēbi", "ēbi", "ēbi", "ēbu"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "ē", "ē", None, None, "e")
                }
            }
        },
        3: {
            "PRES": {
                "ACT": {
                    "INDC": inflection("", "i", "i", "i", "i", "u"),
                    "SUBJ": inflection("a", "ā", "a", "ā", "ā", "a"),
                    "IMPT": inflection(None, "e", None, None, "i", None)
                },
                "PAS": {
                    "INDC": inflection("o", "e", "i", "i", "i", "u"),
                    "SUBJ": inflection("a", "ā", "ā", "ā", "ā", "a"),
                    "IMPT": inflection(None, "e", None, None, "i", None)
                }
            },
            "FUTR": {
                "ACT": {
                    "INDC": inflection("a", "ē", "e", "ē", "ē", "e"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "i", "i", None, "i", "u")
                },
                "PAS": {
                    "INDC": inflection("a", "ē", "ē", "ē", "ē", "e"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "i", "i", None, None, "u")
                }
            }
        },
        3.5: {
            "PRES": {
                "ACT": {
                    "INDC": inflection("i", "i", "i", "i", "i", "iu"),
                    "SUBJ": inflection("ia", "iā", "ia", "iā", "iā", "ia"),
                    "IMPT": inflection(None, "e", None, None, "i", None)
                },
                "PAS": {
                    "INDC": inflection("io", "e", "i", "i", "i", "iu"),
                    "SUBJ": inflection("ia", "iā", "iā", "iā", "iā", "ia"),
                    "IMPT": inflection(None, "e", None, None, "i", None)
                }
            },
            "FUTR": {
                "ACT": {
                    "INDC": inflection("ia", "iē", "ie", "iē", "iē", "ie"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "i", "i", None, "i", "u")
                },
                "PAS": {
                    "INDC": inflection("ia", "iē", "iē", "iē", "iē", "ie"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "i", "i", None, None, "iu")
                }
            }
        },
        4: {
            "PRES": {
                "ACT": {
                    "INDC": inflection("i", "ī", "i", "ī", "ī", "iu"),
                    "SUBJ": inflection("ia", "iā", "ia", "iā", "iā", "ia"),
                    "IMPT": inflection(None, "ī", None, None, "ī", None)
                },
                "PAS": {
                    "INDC": inflection("io", "ī", "ī", "ī", "ī", "iu"),
                    "SUBJ": inflection("ia", "iā", "iā", "iā", "iā", "ia"),
                    "IMPT": inflection(None, "ī", None, None, "ī", None)
                }
            },
            "FUTR": {
                "ACT": {
                    "INDC": inflection("ia", "iē", "ie", "iē", "iē", "ie"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "ī", "ī", None, "ī", "iu")
                },
                "PAS": {
                    "INDC": inflection("ia", "iē", "iē", "iē", "iē", "ie"),
                    "SUBJ": constantInflection(None),
                    "IMPT": inflection(None, "ī", "ī", None, None, "iu")
                }
            }
        }
    }
    # create vars
    kind, conj, transitive, presStem, perfStem, ptcpStem, ptcpInflection, regInf = analysis.values()
    try: connector = connectors[conj][tense][voice][mood][person]
    except KeyError: connector = None
    vowel = endings["vowel"][conj]
    # make the verb
    match kind:
        case "regular":
            match (tense, voice, mood):  # 6 * 2 * 5 = 60
                case ("PRES", "ACT", "INDC"): form = stitchConcise(presStem, connector, endings["ost"][person])
                case ("PRES", "ACT", "SUBJ"): form = stitchConcise(presStem, connector, endings["mst"][person])
                case ("PRES", "ACT", "IMPT"): form = stitchConcise(presStem, connector, endings["PRES ACT IMPT"][person])
                case ("PRES", "ACT", "INFN"): form = infn
                case ("PRES", "ACT", "PTCP"): form = decline33_i((presStem+vowel+"ns"), (presStem+unmacron(vowel)+"ntis"))
                case ("PRES", "PAS", "INDC"): form = stitchConcise(presStem, connector, endings["PAS"][person])
                case ("PRES", "PAS", "SUBJ"): form = stitchConcise(presStem, connector, endings["PAS"][person])
                case ("PRES", "PAS", "IMPT"): form = stitchConcise(presStem, connector, endings["PRES PAS IMPT"][person])
                case ("PRES", "PAS", "INFN"): form = f"{infn[:-1]}ī" if conj not in [3, 3.5] else f"{infn.removesuffix("ere")}ī"
                case ("PRES", "PAS", "PTCP"): form = None
                
                case ("IMPF", "ACT", "INDC"): form = stitchConcise(presStem, vowel, endings["IMPF ACT"][person])
                case ("IMPF", "ACT", "SUBJ"): form = stitchConcise(regInf[:-1], "", endings["mst with e"][person])
                case ("IMPF", "ACT", "IMPT"): form = None
                case ("IMPF", "ACT", "INFN"): form = None
                case ("IMPF", "ACT", "PTCP"): form = None
                case ("IMPF", "PAS", "INDC"): form = stitchConcise(presStem, vowel, endings["IMPF PAS"][person])
                case ("IMPF", "PAS", "SUBJ"): form = stitchConcise(regInf[:-1], "", endings["PAS with e"][person])
                case ("IMPF", "PAS", "IMPT"): form = None
                case ("IMPF", "PAS", "INFN"): form = None
                case ("IMPF", "PAS", "PTCP"): form = None

                case ("PERF", "ACT", "INDC"): form = stitchConcise(perfStem, "", endings["PERF"][person])
                case ("PERF", "ACT", "SUBJ"): form = stitchConcise(perfStem, "", endings["PERF SUBJ"][person])
                case ("PERF", "ACT", "IMPT"): form = None
                case ("PERF", "ACT", "INFN"): form = f"{perfStem}isse"
                case ("PERF", "ACT", "PTCP"): form = None
                case ("PERF", "PAS", "INDC"): form = stitchPeriphrastic(ppp, endings["sum PRES INDC"][person])
                case ("PERF", "PAS", "SUBJ"): form = stitchPeriphrastic(ppp, endings["sum PRES SUBJ"][person])
                case ("PERF", "PAS", "IMPT"): form = None
                case ("PERF", "PAS", "INFN"): form = f"{ppp} esse"
                case ("PERF", "PAS", "PTCP"): form = decline212(ppp)

                case ("PLPF", "ACT", "INDC"): form = stitchConcise(perfStem, "", endings["sum IMPF INDC"][person])
                case ("PLPF", "ACT", "SUBJ"): form = stitchConcise(perfStem, "iss", endings["mst with e"][person])
                case ("PLPF", "ACT", "IMPT"): form = None
                case ("PLPF", "ACT", "INFN"): form = None
                case ("PLPF", "ACT", "PTCP"): form = None
                case ("PLPF", "PAS", "INDC"): form = stitchPeriphrastic(ppp, endings["sum IMPF INDC"][person])
                case ("PLPF", "PAS", "SUBJ"): form = stitchPeriphrastic(ppp, endings["sum IMPF SUBJ"][person])
                case ("PLPF", "PAS", "IMPT"): form = None
                case ("PLPF", "PAS", "INFN"): form = None
                case ("PLPF", "PAS", "PTCP"): form = None

                case ("FUTR", "ACT", "INDC"): form = stitchConcise(presStem, connector, endings[("ost" if conj in (1, 2) else "mst")][person])
                case ("FUTR", "ACT", "SUBJ"): form = None
                case ("FUTR", "ACT", "IMPT"): form = stitchConcise(presStem, connector, endings["FUTR ACT IMPT"][person])
                case ("FUTR", "ACT", "INFN"): form = f"{ppp.removesuffix("us")}ūrus esse"
                case ("FUTR", "ACT", "PTCP"): form = decline212(f"{ppp.removesuffix("us")}ūrus")
                case ("FUTR", "PAS", "INDC"): form = stitchConcise(presStem, connector, endings["PAS"][person])
                case ("FUTR", "PAS", "SUBJ"): form = None
                case ("FUTR", "PAS", "IMPT"): form = stitchConcise(presStem, connector, endings["FUTR PAS IMPT"][person])
                case ("FUTR", "PAS", "INFN"): form = f"{ppp} īrī"
                case ("FUTR", "PAS", "PTCP"): form = decline212(f"{presStem}{unmacron(vowel)}ndus")

                case ("FTPF", "ACT", "INDC"): form = stitchConcise(perfStem, "", endings["FTPF"][person])
                case ("FTPF", "ACT", "SUBJ"): form = None
                case ("FTPF", "ACT", "IMPT"): form = None
                case ("FTPF", "ACT", "INFN"): form = None
                case ("FTPF", "ACT", "PTCP"): form = None
                case ("FTPF", "PAS", "INDC"): form = stitchPeriphrastic(ppp, endings["sum FUTR"][person])
                case ("FTPF", "PAS", "SUBJ"): form = None
                case ("FTPF", "PAS", "IMPT"): form = None
                case ("FTPF", "PAS", "INFN"): form = None
                case ("FTPF", "PAS", "PTCP"): form = None
                
                case _: raise ValueError
            if isinstance(form, dict): form = form[gender][case][number]
            if voice == "PAS" and not transitive: form = None
        case "deponent":
            match (tense, voice, mood):
                case ("PRES", "ACT", "PTCP"): form = decline33_i(f"{presStem}{vowel}ns", f"{presStem}{unmacron(vowel)}ntis")[gender][case][number]
                case ("PERF", "ACT", "PTCP"): form = decline212(perf.removesuffix(" sum"))[gender][case][number]
                case ("FUTR", "ACT", "PTCP"): form = decline212(f"{perf.removesuffix("us sum")}ūrus")[gender][case][number]
                case ("FUTR", "PAS", "PTCP"): form = decline212(f"{presStem}{unmacron(vowel)}ndus")[gender][case][number]
                case ("PRES", "ACT", "INFN"): form = infn
                case _:
                    if voice == "PAS": form = None
                    elif tense in PRESENT_SYSTEM:
                        form = conjugate(
                            (f"{pres[:-2]}ō", regInf, "???ī", perf.removesuffix(" sum")),
                            tense=tense, voice="PAS", mood=mood, person=person, gender=gender, case=case, number=number
                            )
                    elif tense in PERFECT_SYSTEM:
                        form = conjugate(
                            ("???ō", "???ere", "???ī", perf.removesuffix(" sum")),
                            tense=tense, voice="PAS", mood=mood, person=person, gender=gender, case=case, number=number
                            )
        case "semideponent":
            match (tense, voice, mood):
                case ("FUTR", "ACT", "PTCP"): form = decline212(f"{ptcpStem}ūrus")[gender][case][number]
                case ("FUTR", "ACT", "INFN"): form = f"{ptcpStem}ūrus esse"
                case ("FUTR", "PAS", "PTCP"): form = decline212(f"{presStem}{unmacron(vowel)}ndus")[gender][case][number]
                case _:
                    if voice == "PAS": form = None
                    elif tense in PRESENT_SYSTEM:
                        form = conjugate(
                            (pres, infn, "???ī", "???us"),
                            tense=tense, voice=voice, mood=mood, person=person, gender=gender, case=case, number=number
                            )
                    elif tense in PERFECT_SYSTEM:
                        form = conjugate(
                            ("???ō", "???ere", "???ī", perf.removesuffix(" sum")),
                            tense=tense, voice="PAS", mood=mood, person=person, gender=gender, case=case, number=number
                            )
        case "defective":
            if (tense, voice, mood) == ("PRES", "ACT", "PTCP"):
                form = decline33_i(f"{presStem}{vowel}ns", f"{presStem}{unmacron(vowel)}ntis")[gender][case][number]
                return form
            elif tense in PERFECT_SYSTEM: return
            elif voice == "PAS": return
            else: form = None
            t = dict(zip(PRESENT_SYSTEM, PERFECT_SYSTEM))[tense]
            form = conjugate(
                ("???ō", "???ere", pres, "???us"),
                tense=t, voice="ACT", mood=mood, person=person, gender=gender, case=case, number=number
            )
    # if form is not None: print(tense, voice, mood, person, gender, case, number, form)
    return form
def verb(pres: str, infn: str, perf: str | None = None, ppp: str | None = None, **overrides) -> dict:
    # form the main verb
    parts = (pres, infn, perf, ppp)
    table = emptyVerb()
    analysisOverrides = {}
    o = {k: v for k, v in overrides.items() if not k.startswith("analysis_")}
    for location, override in overrides.items():
        if location.startswith("analysis_"):
            analysisOverrides[location.removeprefix("analysis_")] = override
    overrides = o
    for tense, tenseData in table.items():
        for voice, voiceData in tenseData.items():
            for mood, moodData in voiceData.items():
                match mood:
                    case "INDC" | "SUBJ" | "IMPT":
                        for person, form in moodData.items():
                            table[tense][voice][mood][person] = conjugate(parts, tense=tense, voice=voice, mood=mood, person=person, **analysisOverrides)
                    case "INFN":
                        table[tense][voice][mood] = conjugate(parts, tense=tense, voice=voice, mood=mood, **analysisOverrides)
                    case "PTCP":
                        for gender, genderData in moodData.items():
                            for case, caseData in genderData.items():
                                for number, form in caseData.items():
                                    table[tense][voice][mood][gender][case][number] = conjugate(parts, tense=tense, voice=voice, mood=mood, gender=gender, case=case, number=number, **analysisOverrides)
    # do any overrides
    for location, override in overrides.items():
        # location must be formatted as pres_act_indc_1s; pres_act_infn; pres_act_ptcp_nom_masc_sg
        try:
            location = [l.upper() for l in location.split("_")]  # "pres_act_indc_1s" -> ["PRES", "ACT", "INDC", "1S"]
            location = [f"['{l}']" for l in location]  # "PRES" -> "['PRES']"
            location = "".join((["table"] + location))  # ... -> "table['PRES']['ACT']['INDC']['1S']"
            if isinstance(override, str):
                exec(f"{location} = '{override}'")
            elif isinstance(override, dict):
                exec(f"{location} = {override}")
        except Exception as e:
            raise ValueError(e)

    '''
    # printing code for debugging
    if pres in ("audeō", "meminī"):
        for t, tt in table.items():
            for v, vv in tt.items():
                for m, mm in vv.items():
                    if m in ["INDC", "SUBJ", "IMPT"]:
                        for p, pp in mm.items():
                            if pp: print((t, v, m, p, pp))
                    elif m == "INFN":
                        if mm: print((t, v, m, mm))
                    elif m == "PTCP":
                        if mm["MASC"]["NOM"]["SG"]: print((t, v, m, mm["MASC"]["NOM"]["SG"]))
    '''

    return table

VERBS = {
    # REGULAR
    "AMŌ": verb("amō", "amāre", "amāvī", "amātus"),
    "HABEŌ": verb("habeō", "habēre", "habuī", "habitus"),
    "MITTŌ": verb("mittō", "mittere", "mīsī", "missus"),
    "CAPIŌ": verb("capiō", "capere", "cēpī", "captus"),
    "AUDIŌ": verb("audiō", "audīre", "audīvī", "audītus"),
    # DEPONENT
    "CONOR": verb("conor", "conārī", "conātus sum"),
    "VEREOR": verb("vereor", "verērī", "veritus sum"),
    "LOQUOR": verb("loquor", "loquī", "locūtus sum"),
    "PATIOR": verb("patior", "patī", "passus sum"),
    "ORIOR": verb("orior", "orīrī", "ortus sum", futr_act_ptcp=decline212("oritūrus"), futr_act_infn="oritūrus esse"),
    # IRREGULAR
    "SUM": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "sum",
                    "2S": "es",
                    "3S": "est",
                    "1P": "sumus",
                    "2P": "estis",
                    "3P": "sunt"
                },
                "SUBJ": {
                    "1S": "sim",
                    "2S": "sīs",
                    "3S": "sit",
                    "1P": "sīmus",
                    "2P": "sītis",
                    "3P": "sint"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "es",
                    "3S": None,
                    "1P": None,
                    "2P": "este",
                    "3P": None
                },
                "INFN": "esse",
                "PTCP": EMPTY_PARTICIPLE
            },
            "PAS": EMPTY_VOICE
        },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "eram",
                    "2S": "erās",
                    "3S": "erat",
                    "1P": "erāmus",
                    "2P": "erātis",
                    "3P": "erant"
                },
                "SUBJ": {
                    "1S": "essem",
                    "2S": "essēs",
                    "3S": "esset",
                    "1P": "essēmus",
                    "2P": "essētis",
                    "3P": "essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
            },
            "PAS": EMPTY_VOICE
        },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "fuī",
                    "2S": "fuistī",
                    "3S": "fuit",
                    "1P": "fuimus",
                    "2P": "fuistis",
                    "3P": "fuērunt"
                },
                "SUBJ": {
                    "1S": "fuerim",
                    "2S": "fuerīs",
                    "3S": "fuerit",
                    "1P": "fuerīmus",
                    "2P": "fuerītis",
                    "3P": "fuerint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "fuisse",
                "PTCP": EMPTY_PARTICIPLE
            },
            "PAS": EMPTY_VOICE
        },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "fueram",
                    "2S": "fuerās",
                    "3S": "fuerat",
                    "1P": "fuerāmus",
                    "2P": "fuerātis",
                    "3P": "fuerant"
                },
                "SUBJ": {
                    "1S": "fuissem",
                    "2S": "fuissēs",
                    "3S": "fuisset",
                    "1P": "fuissēmus",
                    "2P": "fuissētis",
                    "3P": "fuissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
            },
            "PAS": EMPTY_VOICE
        },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "erō",
                    "2S": "eris",
                    "3S": "erit",
                    "1P": "erimus",
                    "2P": "eritis",
                    "3P": "erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "estō",
                    "3S": "estō",
                    "1P": None,
                    "2P": "estōte",
                    "3P": "suntō"
                },
                "INFN": "futūrus esse",  # alternative "fore"
                "PTCP": decline212("futūrus")
            },
            "PAS": EMPTY_VOICE
        },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "fuerō",
                    "2S": "fueris",
                    "3S": "fuerit",
                    "1P": "fuerimus",
                    "2P": "fueritis",
                    "3P": "fuerint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
            },
            "PAS": EMPTY_VOICE
        }
    },
    "EŌ": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "eō",
                    "2S": "īs",
                    "3S": "it",
                    "1P": "īmus",
                    "2P": "ītis",
                    "3P": "eunt"
                },
                "SUBJ": {
                    "1S": "eam",
                    "2S": "eās",
                    "3S": "eat",
                    "1P": "eāmus",
                    "2P": "eātis",
                    "3P": "eant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "ī",
                    "3S": None,
                    "1P": None,
                    "2P": "īte",
                    "3P": None
                },
                "INFN": "īre",
                "PTCP": decline33_i("iēns", "euntis")
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "ītur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": {
                    "1S": None,
                    "2S": None,
                    "3S": "eātur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "īrī",
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "ībam",
                    "2S": "ībās",
                    "3S": "ībat",
                    "1P": "ībāmus",
                    "2P": "ībātis",
                    "3P": "ībant"
                },
                "SUBJ": {
                    "1S": "īrem",
                    "2S": "īrēs",
                    "3S": "īret",
                    "1P": "īrēmus",
                    "2P": "īrētis",
                    "3P": "īrent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "ībātur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": {
                    "1S": None,
                    "2S": None,
                    "3S": "īrētur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "iī",
                    "2S": "iistī",
                    "3S": "iit",
                    "1P": "iimus",
                    "2P": "iistis",
                    "3P": "iērunt"
                },
                "SUBJ": {
                    "1S": "ierim",
                    "2S": "ierīs",
                    "3S": "ierit",
                    "1P": "ierīmus",
                    "2P": "ierītis",
                    "3P": "ierint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "iisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "itus est",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": {
                    "1S": None,
                    "2S": None,
                    "3S": "itus sit",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "itus esse",
                "PTCP": decline212("itus")
                }
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "ieram",
                    "2S": "ierās",
                    "3S": "ierat",
                    "1P": "ierāmus",
                    "2P": "ierātis",
                    "3P": "ierant"
                },
                "SUBJ": {
                    "1S": "iissem",
                    "2S": "iissēs",
                    "3S": "iisset",
                    "1P": "iissēmus",
                    "2P": "iissētis",
                    "3P": "iissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "itus erat",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": {
                    "1S": None,
                    "2S": None,
                    "3S": "itus esset",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "ībō",
                    "2S": "ībis",
                    "3S": "ībit",
                    "1P": "ībimus",
                    "2P": "ībitis",
                    "3P": "ībunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "ītō",
                    "3S": "ītō",
                    "1P": None,
                    "2P": "ītōte",
                    "3P": "euntō"
                },
                "INFN": "itūrus esse",
                "PTCP": decline212("itūrus")
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "ībitur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": None,
                    "3S": "ītor",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "INFN": "itus īrī",
                "PTCP": decline212("eundus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "ierō",
                    "2S": "ieris",
                    "3S": "ierit",
                    "1P": "ierimus",
                    "2P": "ieritis",
                    "3P": "ierint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "itus erit",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        },
    "FERŌ": verb(
        "ferō", "ferre", "tulī", "lātus",
        analysis_conj=3, analysis_regularInfinitive="ferre",
        pres_act_indc=inflection("ferō", "fers", "fert", "ferimus", "fertis", "ferunt"),
        pres_pas_indc=inflection("feror", "ferris", "fertur", "ferimur", "feriminī", "feruntur"),
        pres_act_impt_2s="fer", pres_act_impt_2p="ferte",
        futr_act_impt=inflection(None, "fertō", "fertō", None, "fertōte", "feruntō"),
        pres_pas_impt_2s="ferre", futr_pas_impt=inflection(None, "fertor", "fertor", None, None, "feruntor"),
        pres_pas_infn="ferrī"
        ),
    "VOLŌ": verb(
        "volō", "velle", "voluī", "",
        analysis_conj=3, analysis_regularInfinitive="velle",
        pres_act_indc=inflection("volō", "vīs", "vult", "volumus", "vultis", "volunt"),
        pres_act_subj=inflection("velim", "velīs", "velit", "velīmus", "velītis", "velint"),
        pres_act_impt=EMPTY_INFLECTION, futr_act_impt=EMPTY_INFLECTION,
        futr_act_infn="volitūrus esse", futr_act_ptcp=decline212("volitūrus")
        ),
    "FACIŌ": verb(
        "faciō", "facere", "fēcī", "factus",
        pres_act_impt_2s="fac",
        pres_pas_indc=inflection("fīō", "fīs", "fit", "fīmus", "fītis", "fīunt"),
        pres_pas_subj=inflection("fīam", "fīās", "fīat", "fīāmus", "fīātis", "fīant"),
        pres_pas_impt=inflection(None, "fī", None, None, "fīte", None),
        pres_pas_infn="fierī", pres_pas_ptcp=decline33_i("fīēns", "fīentis"),
        impf_pas=verb("fīō", "fiere", "???ī", "???us")["IMPF"]["ACT"],
        futr_pas_indc=inflection("fīam", "fīēs", "fīet", "fīēmus", "fīētis", "fīent"),
        futr_pas_impt=inflection(None, "fītō", "fītō", None, "fītōte", "fīuntō"),
        ),
    # OTHER
    "AUDEŌ": verb("audeō", "audēre", "ausus sum"),
    "MEMINĪ": verb("meminī", "meninisse", analysis_conj=3)
    }

# nouns
NOUNS = {
    "PUELLA": noun("puella", "puellae"),
    "FĪLIA": noun("filia", "filiae", dat_pl="filiābus", abl_pl="filiābus"),
    "SERVUS": noun("servus", "servī"),
    "BELLUM": noun("bellum", "bellī"),
    "RĒX": noun("rēx", "rēgis"),
    "NŌMEN": noun("nōmen", "nōminis", isNeut=True),
    "URBS": noun("urbs", "urbis", i=True),
    "ANIMAL": noun("animal", "animālis", isNeut=True, i=True),
    "MANUS": noun("manus", "manūs"),
    "GENŪ": noun("genū", "genūs"),
    "RĒS": noun("rēs", "reī"),
    "DIĒS": noun("diēs", "diēī")
    }

# adjs
ADJECTIVES = {
    "bonus": decline212("bonus"),
    "ingens": decline33_i("ingens", "ingentis"),
    "tristis": {
        "MASC": {
            "NOM": {
                "SG": "tristis",
                "PL": "tristes"
            },
            "VOC": {
                "SG": "tristis",
                "PL": "tristes"
            },
            "ACC": {
                "SG": "tristem",
                "PL": "tristes"
            },
            "GEN": {
                "SG": "tristis",
                "PL": "tristium"
            },
            "DAT": {
                "SG": "tristi",
                "PL": "tristibus"
            },
            "ABL": {
                "SG": "triste",
                "PL": "tristibus"
            }
        },
        "FEMN": {
            "NOM": {
                "SG": "tristis",
                "PL": "tristes"
            },
            "VOC": {
                "SG": "tristis",
                "PL": "tristes"
            },
            "ACC": {
                "SG": "tristem",
                "PL": "tristes"
            },
            "GEN": {
                "SG": "tristis",
                "PL": "tristium"
            },
            "DAT": {
                "SG": "tristi",
                "PL": "tristibus"
            },
            "ABL": {
                "SG": "triste",
                "PL": "tristibus"
            }
        },
        "NEUT": {
            "NOM": {
                "SG": "triste",
                "PL": "tristia"
            },
            "VOC": {
                "SG": "triste",
                "PL": "tristia"
            },
            "ACC": {
                "SG": "triste",
                "PL": "tristia"
            },
            "GEN": {
                "SG": "tristis",
                "PL": "tristium"
            },
            "DAT": {
                "SG": "tristi",
                "PL": "tristibus"
            },
            "ABL": {
                "SG": "triste",
                "PL": "tristibus"
            }
        } 
    }
}

# vocab
VOCAB = {
    "a, ab": ["from", "away from", "by"],
    "absum": ["i am absent"],
    "abesse": ["to be absent"],
    "afui": ["i was absent"],
    "ac, atque": ["and"],
    "accido": ["i happen"],
    "accidere": ["to happen"],
    "accidi": ["i happened"],
    "accipio": ["i accept", "i receive"],
    "accipere": ["to accept", "to receive"],
    "accepi": ["i accepted", "i received"],
    "acceptus": ["having been accepted", "having been received"],
    "ad (+acc)": ["to"],
    "adeo": ["so much", "so greatly"],
    "adsum": ["i am PRES"],
    "adesse": ["to be PRES"],
    "adfui": ["i was PRES"],
    "advenio": ["i arrive"],
    "advenire": ["to arrive"],
    "adveni": ["i arrived"],
    "aedifico": ["i build"],
    "aedificare": ["to build"],
    "aedificavi": ["i built"],
    "aedificatus": ["having been built"],
    "ager, agri": ["field"],
    "ago": ["i do", "i act", "i drive"],
    "agere": ["to do", "to act", "to drive"],
    "egi": ["i did", "i acted", "i drove"],
    "actus": ["having been done", "having been acted", "having been driven"],
    "alii... alii": ["some... others"],
    "alius, alia, aliud": ["other"],
    "alter, altera, alterum": ["the other", "another"],
    "altus, alta, altum": ["high", "deep"],
    "ambulo": ["i walk"],
    "ambulare": ["to walk"],
    "ambulavi": ["i walked"],
    "amicus, amici": ["friend"],
    "amo": ["i love"],
    "amare": ["to love"],
    "amavi": ["i loved"],
    "amatus": ["having been loved"],
    "amor, amoris": ["love"],
    "ancilla, ancillae": ["slavegirl"],
    "animus, animi": ["spirit", "soul"],
    "annus, anni": ["year"],
    "ante (+acc)": ["before", "in front of"],
    "antea": ["before"],
    "appareo": ["i appear"],
    "apparere": ["to appear"],
    "apparui": ["i appeared"],
    "appropinquo": ["i approach"],
    "appropinquare": ["to approach"],
    "appropinquavi": ["i approached"],
    "apud (+acc)": ["among", "with", "at the house of"],
    "aqua, aquae": ["water"],
    "arma, armorum": ["arms", "weapons"],
    "ars, artis": ["art", "skill"],
    "ascendo": ["i climb"],
    "ascendere": ["to climb"],
    "ascendi": ["i climbed"],
    "ascensus": ["having been climbed"],
    "audax, audacis": ["bold", "daring"],
    "audeo": ["i dare"],
    "audere": ["to dare"],
    "ausus sum": ["i dared"],
    "audio": ["i hear"],
    "audire": ["to hear"],
    "audivi": ["i heard"],
    "auditus": ["having been heard"],
    "aufero": ["i steal", "i take away"],
    "auferre": ["to steal", "to take away"],
    "abstuli": ["i stole", "i took away"],
    "ablatus": ["having been stolen", "having been taken away"],
    "autem": ["but", "however"],
    "auxilium, auxilii": ["help"],
    "bellum, belli": ["war"],
    "bellum gero": ["i wage war"],
    "bellum gerere": ["to wage war"],
    "bellum gessi": ["i waged war"],
    "bellum gestus": ["the war having been waged"],
    "bene": ["well"],
    "benignus, benigna, benignum": ["kind"],
    "bibo": ["i drink"],
    "bibere": ["to drink"],
    "bibi": ["i drank"],
    "bonus, bona, bonum": ["good"],
    "brevis, breve": ["short", "brief"],
    "cado": ["i fall"],
    "cadere": ["to fall"],
    "cecidi": ["i fell"],
    "casus": ["having been fallen"],
    "caelum, caeli": ["sky", "heaven"],
    "canis": ["dog"],
    "capio": ["i take", "i catch", "i capture"],
    "capere": ["to take", "to catch", "to capture"],
    "cepi": ["i took", "i caught", "i captured"],
    "captus": ["having been taken", "having been caught", "having been captured"],
    "captivus, captivi": ["prisoner"],
    "caput, capitis": ["head"],
    "castra, castrorum": ["camp"],
    "celer, celeris, celere": ["quick"],
    "celo": ["i hide"],
    "celare": ["to hide"],
    "celavi": ["i hid"],
    "celatus": ["having been hidden"],
    "cena, cenae": ["dinner"],
    "ceteri, ceterae, cetera": ["the others", "the rest"],
    "cibus, cibi": ["food"],
    "circum (+acc)": ["around"],
    "civis": ["citizen"],
    "clamo": ["i shout"],
    "clamare": ["to shout"],
    "clamavi": ["i shouted"],
    "clamatus": ["having been shouted"],
    "clamor, clamoris": ["shout", "uproar"],
    "clarus, clara, clarum": ["clear", "famous"],
    "coepi": ["i begin"],
    "coepisse": ["to begin"],
    "cogito": ["i think"],
    "cogitare": ["to think"],
    "cogitavi": ["i thought"],
    "cogitatus": ["having been thought"],
    "cognosco": ["i find out", "i get to know"],
    "cognoscere": ["to find out", "to get to know"],
    "cognovi": ["i found out", "i got to know"],
    "cognitus": ["having been found out", "having been got to know"],
    "cogo": ["i force", "i compel"],
    "cogere": ["to force", "to compel"],
    "coegi": ["i forced", "i compelled"],
    "coactus": ["having been forced", "having been compelled"],
    "comes, comitis": ["companion"],
    "conficio": ["i finish", "i wear out"],
    "conficere": ["to finish", "to wear out"],
    "confeci": ["i finished", "i wore out"],
    "confectus": ["having been finished", "having been worn out"],
    "conor": ["i try"],
    "conari": ["to try"],
    "conatus sum": ["i tried"],
    "consilium, consilii": ["plan", "idea"],
    "conspicio": ["i catch sight of"],
    "conspicere": ["to catch sight of"],
    "conspexi": ["i caught sight of"],
    "conspectus": ["having been caught sight of"],
    "constituo": ["i decide"],
    "constituere": ["to decide"],
    "constitui": ["i decided"],
    "constitutus": ["having been decided"],
    "consul, consulis": ["consul", "government official"],
    "consumo": ["i eat"],
    "consumere": ["to eat"],
    "consumpsi": ["i ate"],
    "consumptus": ["having been eaten"],
    "contra (+acc)": ["against"],
    "convenio": ["i gather"],
    "convenire": ["to gather"],
    "conveni": ["i gathered"],
    "copiae, copiarum": ["forces", "troops"],
    "corpus, corporis": ["body"],
    "cras": ["tomorrow"],
    "credo (+dat)": ["i trust", "i believe"],
    "credere (+dat)": ["to trust", "to believe"],
    "credidi (+dat)": ["i trusted", "i believed"],
    "creditus": ["having been trusted", "having been believed"],
    "crudelis, crudele": ["cruel"],
    "cum (+abl)": ["with"],
    "cum (+subj)": ["when"],
    "cupio": ["i want"],
    "cupere": ["to want"],
    "cupivi": ["i wanted"],
    "cupitus": ["having been wanted"],
    "cur?": ["why?"],
    "cura, curae": ["care", "worry"],
    "curro": ["i run"],
    "currere": ["to run"],
    "cucurri": ["i ran"],
    "cursus": ["having been run"],
    "custodio": ["i guard"],
    "custodire": ["to guard"],
    "custodivi": ["i guarded"],
    "custoditus": ["having been guarded"],
    "custos, custodis": ["guard"],
    "dea, deae": ["goddess"],
    "debeo": ["i owe"],
    "debere": ["to owe"],
    "debui": ["i owed"],
    "debitus": ["having been owed"],
    "defendo": ["i defend"],
    "defendere": ["to defend"],
    "defendi": ["i defended"],
    "defensus": ["having been defended"],
    "deinde": ["then"],
    "deleo": ["i destroy"],
    "delere": ["to destroy"],
    "delevi": ["i destroyed"],
    "deletus": ["having been destroyed"],
    "descendo": ["i go down"],
    "descendere": ["to go down"],
    "descendi": ["i went down"],
    "descensus": ["having been gone down"],
    "deus, dei": ["god"],
    "dico": ["i say"],
    "dicere": ["to say"],
    "dixi": ["i said"],
    "dictus": ["having been said"],
    "dies, diei": ["day"],
    "difficilis, difficile": ["difficult"],
    "diligens, diligentis": ["careful"],
    "dirus, dira, dirum": ["dreadful"],
    "discedo": ["i leave"],
    "discedere": ["to leave"],
    "discessi": ["i left"],
    "diu": ["for a long time"],
    "do": ["i give"],
    "dare": ["to give"],
    "dedi": ["i gave"],
    "datus": ["having been given"],
    "doceo": ["i teach"],
    "docere": ["to teach"],
    "docui": ["i taught"],
    "doctus": ["having been taught"],
    "domina, dominae": ["mistress"],
    "dominus, domini": ["master"],
    "domus": ["home"],
    "domi": ["at home"],
    "donum, doni": ["gift"],
    "dormio": ["i sleep"],
    "dormire": ["to sleep"],
    "dormivi": ["i slept"],
    "duco": ["i lead"],
    "ducere": ["to lead"],
    "duxi": ["i led"],
    "ductus": ["having been led"],
    "dum": ["while", "until"],
    "dux, ducis": ["leader"],
    "e, ex (+abl)": ["from", "out of"],
    "ecce!": ["look!"],
    "effugio": ["i escape"],
    "effugere": ["to escape"],
    "effugi": ["i escaped"],
    "egredior": ["i go out", "i exit"],
    "egredi": ["to go out", "to exit"],
    "egressus sum": ["i went out", "i exited"],
    "ego, mei": ["i", "me"],
    "emo": ["i buy"],
    "emere": ["to buy"],
    "emi": ["i bought"],
    "emptus": ["having been bought"],
    "enim": ["for"],
    "eo": ["i go"],
    "ire": ["to go"],
    "ii, ivi": ["i went"],
    "epistula, epistulae": ["letter"],
    "equus, equi": ["horse"],
    "et": ["and"],
    "et... et": ["both... and"],
    "etiam": ["also", "even"],
    "exercitus": ["army"],
    "exspecto": ["i wait for"],
    "exspectare": ["to wait for"],
    "exspectavi": ["i waited for"],
    "exspectatus": ["having been waited for"],
    "facilis, facile": ["easy"],
    "facio": ["i make", "i do"],
    "facere": ["to make", "to do"],
    "feci": ["i made", "i did"],
    "factus": ["having been made", "having been done"],
    "faveo (+dat)": ["i favour", "i support"],
    "favere (+dat)": ["to favour", "to support"],
    "favi (+dat)": ["i favoured", "i supported"],
    "fautus": ["having been favoured", "having been supported"],
    "felix, felicis": ["happy", "lucky", "fortunate"],
    "femina, feminae": ["woman"],
    "fero": ["i bring", "i bear", "i carry"],
    "ferre": ["to bring", "to bear", "to carry"],
    "tuli": ["i brought", "i bore", "i carried"],
    "latus": ["having been brought", "having been bore", "having been carried"],
    "ferox, ferocis": ["fierce"],
    "festino": ["i hurry"],
    "festinare": ["to hurry"],
    "festinavi": ["i hurried"],
    "fidelis, fidele": ["loyal"],
    "filia, filiae": ["daughter"],
    "filius, filii": ["son"],
    "flumen, fluminis": ["river"],
    "forte": ["by chance"],
    "fortis, forte": ["brave"],
    "forum, fori": ["market place"],
    "frater, fratris": ["brother"],
    "frustra": ["in vain"],
    "fugio": ["i flee"],
    "fugere": ["to flee"],
    "fugi": ["i fled"],
    "gravis, grave": ["heavy", "serious"],
    "gaudeo": ["i rejoice", "i am pleased"],
    "gaudere": ["to rejoice", "to be pleased"],
    "gavisus sum": ["i rejoiced", "i was pleased"],
    "gaudium, gaudii": ["joy", "pleasure"],
    "gens, gentis": ["family", "tribe", "race", "people"],
    "gladius, gladii": ["sword"],
    "gravis, grave": ["heavy", "serious"],
    "hic": ["this", "here"],
    "hodie": ["today"],
    "homo, hominis": ["man"],
    "hora, horae": ["hour"],
    "hortor": ["i encourage"],
    "hortari": ["to encourage"],
    "hortatus sum": ["i encouraged"],
    "hortus, horti": ["garden"],
    "hostis, hostis": ["enemy"],
    "habeo": ["i have"],
    "habere": ["to have"],
    "habui": ["i had"],
    "habitus": ["having been had"],
    "habito": ["i live"],
    "habitare": ["to live"],
    "habitavi": ["i lived"],
    "habitatus": ["having been lived"],
    "heri": ["yesterday"],
    "iaceo": ["i lie down"],
    "iacere": ["to lie down", "to throw"],
    "iacui": ["i lay down"],
    "iacio": ["i throw"],
    "ieci": ["i threw"],
    "iactus": ["having been thrown"],
    "iam": ["now"],
    "ianua, ianuae": ["door"],
    "ibi": ["there"],
    "idem, eadem, idem": ["the same"],
    "igitur": ["therefore", "and so"],
    "ille, illa, illud": ["that"],
    "imperator, imperatoris": ["emperor", "general", "leader"],
    "imperium, imperii": ["empire", "power", "command"],
    "impero (+dat)": ["i order", "i command"],
    "imperare (+dat)": ["to order", "to command"],
    "imperavi (+dat)": ["i ordered", "i commanded"],
    "imperatus": ["having been ordered", "having been commanded"],
    "in (+abl)": ["in", "on"],
    "in (+acc)": ["into", "onto"],
    "incendo": ["i burn", "i set on fire"],
    "incendere": ["to burn", "to set on fire"],
    "incendi": ["i burnt", "i set on fire"],
    "incensus": ["having been burnt", "having been set on fire"],
    "infelix, infelicis": ["unlucky", "unhappy"],
    "ingens, ingentis": ["huge"],
    "ingredior": ["i enter"],
    "ingredi": ["to enter"],
    "ingressus sum": ["i entered"],
    "inimicus, inimici": ["enemy"],
    "inquit": ["says", "said"],
    "insula, insulae": ["island", "block of flats"],
    "intellego": ["i understand", "i realise"],
    "intellegere": ["to understand", "to realise"],
    "intellexi": ["i understood", "i realised"],
    "intellectus": ["having been understood", "having been realised"],
    "inter (+acc)": ["among", "between"],
    "interea": ["meanwhile"],
    "interficio": ["i kill"],
    "interficere": ["to kill"],
    "interfeci": ["i killed"],
    "interfectus": ["having been killed"],
    "intro": ["i enter"],
    "intrare": ["to enter"],
    "intravi": ["i entered"],
    "intratus": ["having been entered"],
    "invenio": ["i find"],
    "invenire": ["to find"],
    "inveni": ["i found"],
    "inventus": ["having been found"],
    "invito": ["i invite"],
    "invitare": ["to invite"],
    "invitavi": ["i invited"],
    "invitatus": ["having been invited"],
    "ipse": ["himself"],
    "ipsa": ["herself"],
    "ipsum": ["itself"],
    "ira, irae": ["anger"],
    "iratus, irata, iratum": ["angry"],
    "is": ["he"],
    "ea": ["she"],
    "id": ["it", "that"],
    "ita": ["in this way", "so"],
    "itaque": ["therefore", "and so"],
    "iter, itineris": ["journey"],
    "iterum": ["again"],
    "iubeo": ["i order"],
    "iubere": ["to order"],
    "iussi": ["i ordered"],
    "iussus": ["having been ordered"],
    "iuvenis, iuvenis": ["young man"],
    "labor, laboris": ["work"],
    "laboro": ["i work"],
    "laborare": ["to work"],
    "laboravi": ["i worked"],
    "lacrimo": ["i cry"],
    "lacrimare": ["to cry"],
    "lacrimavi": ["i cried"],
    "laetus, laeta, laetum": ["happy"],
    "laudo": ["i praise"],
    "laudare": ["to praise"],
    "laudavi": ["i praised"],
    "laudatus": ["having been praised"],
    "legio, legionis": ["legion"],
    "lego": ["i read", "i choose"],
    "legere": ["to read", "to choose"],
    "legi": ["i read", "i chose"],
    "lectus": ["having been read", "having been chosen"],
    "lentus, lenta, lentum": ["slow"],
    "leo, leonis": ["lion"],
    "libenter": ["willingly", "gladly"],
    "liber, libri": ["book"],
    "liberi, liberorum": ["children"],
    "libero": ["i set free"],
    "liberare": ["to set free"],
    "liberavi": ["i set free"],
    "liberatus": ["having been set free"],
    "libertus, liberti": ["freedman", "exslave"],
    "locus, loci": ["place"],
    "longus, longa, longum": ["long"],
    "loquor": ["i speak"],
    "loqui": ["to speak"],
    "locutus sum": ["i spoke"],
    "lux, lucis": ["light", "daylight"],
    "magis": ["more"],
    "magnopere": ["greatly"],
    "magnus, magna, magnum": ["large", "great"],
    "malo": ["i prefer"],
    "malle": ["to prefer"],
    "malui": ["i preferred"],
    "malus, mala, malum": ["bad", "evil"],
    "maneo": ["i remain", "stay"],
    "manere": ["to remain", "stay"],
    "mansi": ["i remained", "stayed"],
    "manus, manus": ["hand", "group of people"],
    "mare, maris": ["sea"],
    "maritus, mariti": ["husband"],
    "mater, matris": ["mother"],
    "maxime": ["very greatly"],
    "medius, media, medium": ["middle"],
    "mercator, mercatoris": ["merchant"],
    "meus, mea, meum": ["my"],
    "miles, militis": ["soldier"],
    "minime": ["no", "least"],
    "miror": ["i admire", "i wonder at"],
    "mirari": ["to admire", "to wonder at"],
    "miratus sum": ["i admired", "i wondered at"],
    "miser, misera, miserum": ["miserable", "wretched", "sad"],
    "mitto": ["i send"],
    "mittere": ["to send"],
    "misi": ["i sent"],
    "missus": ["having been sent"],
    "modus, modi": ["manner", "way", "kind"],
    "moneo": ["i warn", "i advise"],
    "monere": ["to warn", "to advise"],
    "monui": ["i warned", "i advised"],
    "monitus": ["having been warned", "having been advised"],
    "mons, montis": ["mountain"],
    "morior": ["i die"],
    "mori": ["to die"],
    "mortuus sum": ["i died"],
    "mors, mortis": ["death"],
    "moveo": ["i move"],
    "movere": ["to move"],
    "movi": ["i moved"],
    "motus": ["having been moved"],
    "mox": ["soon"],
    "multo": ["much"],
    "multus, multa, multum": ["much", "many"],
    "murus, muri": ["wall"],
    "nam": ["for"],
    "narro": ["i tell", "i relate"],
    "narrare": ["to tell", "to relate"],
    "narravi": ["i told", "i related"],
    "narratus": ["having been told", "having been related"],
    "nauta, nautae": ["sailor"],
    "navigo": ["i sail"],
    "navigare": ["to sail"],
    "navigavi": ["i sailed"],
    "navis, navis": ["ship"],
    "ne (+subj)": ["so that... not", "lest"],
    "-ne": ["question word", "?"],
    "nec, neque": ["and not", "nor", "neither"],
    "neco": ["i kill"],
    "necare": ["to kill"],
    "necavi": ["i killed"],
    "necatus": ["having been killed"],
    "nemo, neminis": ["noone"],
    "nescio": ["i don't know", "i do not know"],
    "nescire": ["to not know"],
    "nescivi": ["i didn't know", "i did not know"],
    "nihil": ["nothing"],
    "nisi": ["unless", "except"],
    "nolo": ["i don't want", "i do not want", "i refuse"],
    "nolle": ["to not want", "to refuse"],
    "nolui": ["i didn't want", "i did not want", "i refused"],
    "nomen, nominis": ["name"],
    "non": ["not"],
    "nonne...?": ["surely...?"],
    "nonnulli, nonnullae, nonnulla": ["some", "several"],
    "nos, nostrum": ["we", "us"],
    "noster, nostra, nostrum": ["our"],
    "novus, nova, novum": ["new"],
    "nox, noctis": ["night"],
    "nullus, nulla, nullum": ["not any", "no"],
    "num": ["whether"],
    "num...?": ["surely... not?"],
    "numquam": ["never"],
    "nunc": ["now"],
    "nuntio": ["i announce"],
    "nuntiare": ["to announce"],
    "nuntiavi": ["i announced"],
    "nuntiatus": ["having been announced"],
    "nuntius, nuntii": ["messenger", "message", "news"],
    "occido": ["i kill"],
    "occidere": ["to kill"],
    "occidi": ["i killed"],
    "occisus": ["having been killed"],
    "offero": ["i offer"],
    "offerre": ["to offer"],
    "obtuli": ["i offered"],
    "oblatus": ["having been offered"],
    "olim": ["once", "some time ago"],
    "omnis, omne": ["all", "every"],
    "opprimo": ["i crush", "i overwhelm"],
    "opprimere": ["to crush", "to overwhelm"],
    "oppressi": ["i crushed", "i overwhelmed"],
    "oppressus": ["having been crushed", "having been overwhelmed"],
    "oppugno": ["i attack"],
    "oppugnare": ["to attack"],
    "oppugnavi": ["i attacked"],
    "oppugnatus": ["having been attacked"],
    "oro": ["i beg"],
    "orare": ["to beg"],
    "oravi": ["i begged"],
    "oratus": ["having been begged"],
    "ostendo": ["i show"],
    "ostendere": ["to show"],
    "ostendi": ["i showed"],
    "ostentus": ["having been shown"],
    "paene": ["almost", "nearly"],
    "paro": ["i prepare"],
    "parare": ["to prepare"],
    "paravi": ["i prepared"],
    "paratus": ["having been prepared"],
    "pars, partis": ["part"],
    "parvus, parva, parvum": ["small"],
    "pater, patris": ["father"],
    "patior": ["i suffer", "i endure"],
    "pati": ["to suffer", "to endure"],
    "passus sum": ["i suffered", "i endured"],
    "patria, patriae": ["country", "homeland"],
    "pauci, paucae, pauca": ["few", "a few"],
    "pax, pacis": ["peace"],
    "pecunia, pecuniae": ["money"],
    "pello": ["i drive"],
    "pellere": ["to drive"],
    "pepuli": ["i drove"],
    "pulsus": ["having been driven"],
    "per (+acc)": ["through", "along"],
    "pereo": ["i die", "i perish"],
    "perire": ["to die", "to perish"],
    "perii": ["i died", "i perished"],
    "periculum, periculi": ["danger"],
    "persuadeo": ["i persuade"],
    "persuadere (+dat)": ["to persuade"],
    "persuasi (+dat)": ["i persuaded"],
    "persuasus (+dat)": ["having been persuaded"],
    "perterritus, perterrita, perterritum": ["terrified"],
    "pervenio": ["i reach", "i arrive at"],
    "pervenire": ["to reach", "to arrive at"],
    "perveni": ["i reached", "i arrived at"],
    "perventus": ["having been reached", "having been arrived at"],
    "pes, pedis": ["foot"],
    "peto": ["i make for", "i seek"],
    "petere": ["to make for", "to seek"],
    "petivi": ["i made for", "i sought"],
    "petitus": ["having been made for", "having been sought"],
    "plenus, plena, plenum": ["full"],
    "poena, poenae": ["punishment"],
    "poenas do": ["pay the penalty"],
    "pono": ["i put", "i place", "i put up"],
    "ponere": ["to put", "to place", "to put up"],
    "posui": ["i put", "i placed", "i put up"],
    "positus": ["having been put", "having been placed", "having been put up"],
    "porta, portae": ["gate"],
    "porto": ["i carry"],
    "portare": ["to carry"],
    "portavi": ["i carried"],
    "portatus": ["having been carried"],
    "portus, portus": ["harbour", "port"],
    "possum": ["i am able", "i can"],
    "posse": ["to be able to", "to can"],
    "potui": ["i was able", "i could"],
    "post (+acc)": ["after", "behind"],
    "postea": ["afterwards"],
    "postquam": ["after", "when"],
    "postridie": ["on the next day"],
    "praemium, praemii": ["prize", "reward", "profit", "gift"],
    "precor": ["i pray", "i beg"],
    "precari": ["to pray", "to beg"],
    "precatus sum": ["i prayed", "i begged"],
    "primo": ["at first"],
    "primus, prima, primum": ["first"],
    "princeps, principis": ["chief", "emperor"],
    "pro (+abl)": ["in front of", "for", "in return for"],
    "procedo": ["i advance", "i proceed"],
    "procedere": ["to advance", "to proceed"],
    "processi": ["i advanced", "i proceeded"],
    "proelium, proelii": ["battle"],
    "proficiscor": ["i set out"],
    "proficisci": ["to set out"],
    "profectus sum": ["i set out"],
    "progredior": ["i advance"],
    "progredi": ["to advance"],
    "progressus sum": ["i advanced"],
    "promitto": ["i promise"],
    "promittere": ["to promise"],
    "promisi": ["i promised"],
    "promissus": ["having been promised"],
    "prope (+acc)": ["near"],
    "propter (+acc)": ["on account of", "because of"],
    "proximus, proxima, proximum": ["nearest", "next to"],
    "puella, puellae": ["girl"],
    "puer, pueri": ["boy"],
    "pugno": ["i fight"],
    "pugnare": ["to fight"],
    "pugnavi": ["i fought"],
    "pulcher, pulchra, pulchrum": ["beautiful", "handsome"],
    "punio": ["i punish"],
    "punire": ["to punish"],
    "punivi": ["i punished"],
    "punitus": ["having been punished"],
    "puto": ["i think"],
    "putare": ["to think"],
    "putavi": ["i thought"],
    "putatus": ["having been thought"],
    "quaero": ["i search for", "ask"],
    "quaerere": ["to search for", "ask"],
    "quaesivi": ["i searched for", "asked"],
    "quaesitus": ["having been searched for", "asked"],
    "qualis? quale?": ["what sort of?"],
    "quam (+ splat. adv)": ["as ... as possible"],
    "quam": ["than"],
    "quam?": ["how?"],
    "quam!": ["how!"],
    "quamquam": ["although"],
    "quando?": ["when?"],
    "quantus? quanta? quantum?": ["how much?"],
    "-que": ["and"],
    "qui, quae, quod": ["who", "which", "what"],
    "quidam, quaedam, quoddam": ["one", "a certain", "some"],
    "quis?": ["who?"],
    "quid?": ["what?"],
    "quo?": ["to where?"],
    "quod": ["because"],
    "quomodo?": ["in what way? how?"],
    "quoque": ["also", "too"],
    "quot?": ["how many?"],
    "rapio": ["i seize", "i grab"],
    "rapere": ["to seize", "to grab"],
    "rapui": ["i seized", "i grabbed"],
    "raptus": ["having been seized", "having been grabbed"],
    "re-": ["-back", "back"],
    "reddo": ["i give back", "i restore"],
    "reddere": ["to give back", "to restore"],
    "reddidi": ["i gave back", "i restored"],
    "redditus": ["having been given back", "having been restored"],
    "redeo": ["i return", "i go back"],
    "redire": ["to return", "to go back"],
    "redii": ["i returned", "i went back"],
    "refero": ["i bring back", "i report", "i tell"],
    "referre": ["to bring back", "to report", "to tell"],
    "rettuli": ["i brought back", "i reported", "i told"],
    "relatus": ["having been brought back", "having been reported", "having been told"],
    "regina, reginae": ["queen"],
    "regnum, regni": ["kingdom"],
    "rego": ["i rule"],
    "regere": ["to rule"],
    "rexi": ["i ruled"],
    "rectus": ["having been ruled"],
    "regredior": ["i return", "i go back"],
    "regredi": ["to return", "to go back"],
    "regressus sum": ["i returned", "i went back"],
    "relinquo": ["i leave"],
    "relinquere": ["to leave"],
    "reliqui": ["i left"],
    "relictus": ["having been left"],
    "res, rei": ["thing", "matter", "event"],
    "resisto (+dat)": ["i resist"],
    "resistere (+dat)": ["to resist"],
    "restiti (+dat)": ["i resisted"],
    "respondeo": ["i reply"],
    "respondere": ["to reply"],
    "respondi": ["i replied"],
    "responsus": ["having been replied"],
    "rex, regis": ["king"],
    "rideo": ["i laugh", "i smile"],
    "ridere": ["to laugh", "to smile"],
    "risi": ["i laughed", "i smiled"],
    "rogo": ["i ask", "i ask for"],
    "rogare": ["to ask", "to ask for"],
    "rogavi": ["i asked", "i asked for"],
    "rogatus": ["having been asked", "having been asked for"],
    "Roma": ["Rome"],
    "Romae": ["in Rome", "at Rome"],
    "Romanus, Romana, Romanum": ["Roman"],
    "rumpo": ["i break", "i burst"],
    "rumpere": ["to break", "to burst"],
    "rupi": ["i broke", "i burst"],
    "ruptus": ["having been broken", "having been burst"],
    "sacer, sacra, sacrum": ["sacred"],
    "saepe": ["often"],
    "saevus, saeva, saevum": ["savage", "cruel"],
    "saluto": ["i greet"],
    "salutare": ["to greet"],
    "salutavi": ["i greeted"],
    "salutatus": ["having been greeted"],
    "salve! salvete!": ["hello!"],
    "sanguis, sanguinis": ["blood"],
    "sapiens, sapientis": ["wise"],
    "satis": ["enough"],
    "scelestus, scelesta, scelestum": ["wicked"],
    "scelus, sceleris": ["crime"],
    "scio": ["i know"],
    "scire": ["to know"],
    "scivi": ["i knew"],
    "scitus": ["having been known"],
    "scribo": ["i write"],
    "scribere": ["to write"],
    "scripsi": ["i wrote"],
    "scriptus": ["having been written"],
    "se, sui": ["himself", "herself", "itself", "themselves"],
    "sed": ["but"],
    "sedeo": ["i sit"],
    "sedere": ["to sit"],
    "sedi": ["i sat"],
    "semper": ["always"],
    "senator, senatoris": ["senator"],
    "senex, senis": ["old man"],
    "sentio": ["i feel", "i notice"],
    "sentire": ["to feel", "to notice"],
    "sensi": ["i felt", "i noticed"],
    "sensus": ["having been felt", "having been noticed"],
    "sequor": ["i follow"],
    "sequi": ["to follow"],
    "secutus sum": ["i followed"],
    "servo": ["i save", "i protect", "i keep"],
    "servare": ["to save", "to protect", "to keep"],
    "servavi": ["i saved", "i protected", "i kept"],
    "servatus": ["having been saved", "having been protected", "having been kept"],
    "servus, servi": ["slave"],
    "si": ["if"],
    "sic": ["thus", "in this way"],
    "signum, signi": ["sign", "signal", "standard"],
    "silva, silvae": ["wood"],
    "simul": ["at the same time"],
    "simulac, simulatque": ["as soon as"],
    "sine (+abl)": ["without"],
    "soleo": ["i am accustomed to"],
    "solere": ["to be accustomed to"],
    "solitus sum": ["i was accustomed to"],
    "solus, sola, solum": ["alone", "lonely", "only"],
    "specto": ["i look at", "i watch"],
    "spectare": ["to look at", "to watch"],
    "spectavi": ["i looked at", "i watched"],
    "spectatus": ["having been looked at", "having been watched"],
    "spero": ["i hope", "i expect"],
    "sperare": ["to hope", "to expect"],
    "speravi": ["i hoped", "i expected"],
    "speratus": ["having been hoped", "having been expected"],
    "spes, spei": ["hope"],
    "statim": ["at once", "immediately"],
    "sto": ["i stand"],
    "stare": ["to stand"],
    "steti": ["i stood"],
    "stultus, stulta, stultum": ["stupid", "foolish"],
    "sub (+acc/abl)": ["under", "beneath"],
    "subito": ["suddenly"],
    "sum": ["i am"],
    "esse": ["to be"],
    "fui": ["i was"],
    "summus, summa, summum": ["highest", "greatest", "top of"],
    "supero": ["i overcome", "i overpower"],
    "superare": ["to overcome", "to overpower"],
    "superavi": ["i overcame", "i overpowered"],
    "superatus": ["having been overcome", "having been overpowered"],
    "surgo": ["i stand up", "i rise"],
    "surgere": ["to stand up", "to rise"],
    "surrexi": ["i stood up", "i rose"],
    "suus, sua, suum": ["his own", "her own", "its own", "their own"],
    "taberna, tabernae": ["shop", "inn"],
    "taceo": ["i am silent"],
    "tacere": ["to be silent"],
    "tacui": ["i was silent"],
    "tacitus": ["having been silent"],
    "talis, tale": ["such"],
    "tam": ["so"],
    "tamen": ["however"],
    "tandem": ["at last", "finally"],
    "tantus, tanta, tantum": ["so great"],
    "tempestas, tempestatis": ["storm"],
    "templum, templi": ["temple"],
    "tempus, temporis": ["time"],
    "teneo": ["i hold"],
    "tenere": ["to hold"],
    "tenui": ["i held"],
    "tentus": ["having been held"],
    "terra, terrae": ["ground", "land", "country"],
    "terreo": ["i frighten"],
    "terrere": ["to frighten"],
    "terrui": ["i frightened"],
    "territus": ["having been frightened"],
    "timeo": ["i fear", "i am afraid"],
    "timere": ["to fear", "to be afraid"],
    "timui": ["i feared", "i was afraid"],
    "tollo": ["i lift", "i hold up"],
    "tollere": ["to lift", "to hold up"],
    "sustuli": ["i lifted", "i held up"],
    "sublatus": ["having been lifted", "having been held up"],
    "tot": ["so many"],
    "totus, tota, totum": ["whole"],
    "trado": ["i hand over"],
    "tradere": ["to hand over"],
    "tradidi": ["i handed over"],
    "traditus": ["having been handed over"],
    "traho": ["i drag"],
    "trahere": ["to drag"],
    "traxi": ["i dragged"],
    "tractus": ["having been dragged"],
    "trans (+acc)": ["across"],
    "tristis, triste": ["sad"],
    "tu, tui": ["you (sg)"],
    "tum": ["then"],
    "turba, turbae": ["crowd"],
    "tuus, tua, tuum": ["your (sg)"],
    "ubi": ["where", "when?"],
    "umquam": ["ever"],
    "unde": ["from where", "whence"],
    "urbs, urbis": ["city", "town"],
    "ut (+subj": ["that", "so that", "in order to"],
    "ut (+indc)": ["as", "when"],
    "uxor, uxoris": ["wife"],
    "vale! valete!": ["goodbye"],
    "validus, valida, validum": ["strong"],
    "vehementer": ["violently", "loudly"],
    "vendo": ["i sell"],
    "vendere": ["to sell"],
    "vendidi": ["i sold"],
    "venditus": ["having been sold"],
    "venio": ["i come"],
    "venire": ["to come"],
    "veni": ["i came"],
    "verbum, verbi": ["word"],
    "verto": ["i turn"],
    "vertere": ["to turn"],
    "verti": ["i turned"],
    "versus": ["having been turned"],
    "verus, vera, verum": ["true", "real"],
    "vester, vestra, vestrum": ["your"],
    "via, viae": ["road", "way"],
    "victoria, victoriae": ["victory"],
    "video": ["i see"],
    "videre": ["to see"],
    "vidi": ["i saw"],
    "visus": ["having been seen"],
    "videor": ["i seem", "i appear"],
    "videri": ["to seem", "to appear"],
    "visus sum": ["i seemed", "i appeared"],
    "villa, villae": ["house"],
    "vinco": ["i conquer", "i win"],
    "vincere": ["to conquer", "to win"],
    "vici": ["i conquered", "i won"],
    "victus": ["having been conquered", "having been won"],
    "vinum, vini": ["wine"],
    "vir, viri": ["man"],
    "virtus, virtutis": ["courage", "virtue"],
    "vita, vitae": ["life"],
    "vivo": ["i live"],
    "vivere": ["to live"],
    "vixi": ["i lived"],
    "vivus, viva, vivum": ["alive", "living"],
    "voco": ["i call"],
    "vocare": ["to call"],
    "vocavi": ["i called"],
    "vocatus": ["having been called"],
    "volo": ["i want"],
    "velle": ["to want"],
    "volui": ["i wanted"],
    "vos, vestrum": ["you (pl)"],
    "vox, vocis": ["voice", "shout"],
    "vulnero": ["i wound", "i injure"],
    "vulnerare": ["to wound", "to injure"],
    "vulneravi": ["i wounded", "i injured"],
    "vulneratus": ["having been wounded", "having been injured"],
    "vulnus, vulneris": ["wound", "injury"],
    "vultus, vultus": ["expression", "face"]
}
