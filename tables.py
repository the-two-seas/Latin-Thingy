# functions
def decline212(word: str) -> dict[str, dict[str, dict[str, str]]]:
    stem = word[:-2]
    return {
        "MASC": {
            "NOM": {
                "SG": stem + "us",
                "PL": stem + "i"
            },
            "VOC": {
                "SG": stem + "e",
                "PL": stem + "i"
            },
            "ACC": {
                "SG": stem + "um",
                "PL": stem + "os"
            },
            "GEN": {
                "SG": stem + "i",
                "PL": stem + "orum"
            },
            "DAT": {
                "SG": stem + "o",
                "PL": stem + "is"
            },
            "ABL": {
                "SG": stem + "o",
                "PL": stem + "is"
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
                "PL": stem + "as"
            },
            "GEN": {
                "SG": stem + "ae",
                "PL": stem + "arum"
            },
            "DAT": {
                "SG": stem + "ae",
                "PL": stem + "is"
            },
            "ABL": {
                "SG": stem + "a",
                "PL": stem + "is"
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
                "SG": stem + "i",
                "PL": stem + "orum"
            },
            "DAT": {
                "SG": stem + "o",
                "PL": stem + "is"
            },
            "ABL": {
                "SG": stem + "o",
                "PL": stem + "is"
            }
        }
    }
def decline33_i(word: str, gen: str) -> dict[str, dict[str, dict[str, str]]]:
    stem = gen[:-2]
    return {
        "MASC": {
            "NOM": {
                "SG": word,
                "PL": stem + "es"
            },
            "VOC": {
                "SG": word,
                "PL": stem + "es"
            },
            "ACC": {
                "SG": stem + "em",
                "PL": stem + "es"
            },
            "GEN": {
                "SG": stem + "is",
                "PL": stem + "ium"
            },
            "DAT": {
                "SG": stem + "i",
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
                "PL": stem + "es"
            },
            "VOC": {
                "SG": word,
                "PL": stem + "es"
            },
            "ACC": {
                "SG": stem + "em",
                "PL": stem + "es"
            },
            "GEN": {
                "SG": stem + "is",
                "PL": stem + "ium"
            },
            "DAT": {
                "SG": stem + "i",
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
                "SG": stem + "i",
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
def addEndings(stem: str, endings: tuple[str]) -> dict[str, str]:
    return inflection(
        stem + endings[0],
        stem + endings[1],
        stem + endings[2],
        stem + endings[3],
        stem + endings[4],
        stem + endings[5]
    )
def constantInflection(s) -> dict[str, str]:
    return inflection(s, s, s, s, s, s)
def unmacron(s: str) -> str:
    return s.translate(str.maketrans({
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"
    }))

# empty stuff
EMPTY_PARTICIPLE = {
    gender: {
        case: {"SG": None, "PL": None}
        for case in ["NOM", "VOC", "ACC", "GEN", "DAT", "ABL"]
    }
    for gender in ["MASC", "FEMN", "NEUT"]
}
EMPTY_INFLECTION = {
    person: None
    for person in ["1S", "2S", "3S", "1P", "2P", "3P"]
}
EMPTY_VOICE = {
    "INDC": EMPTY_INFLECTION,
    "SUBJ": EMPTY_INFLECTION,
    "IMPT": EMPTY_INFLECTION,
    "INFN": None,
    "PTCP": EMPTY_PARTICIPLE
}
EMPTY = [EMPTY_PARTICIPLE, EMPTY_INFLECTION, EMPTY_VOICE, None]
# verbs
'''
# create endings and connectors dicts
endings = {
    "o s t": inflection("ó", "s", "t", "mus", "tis", "nt"),
    "m s t": inflection("m", "s", "t", "mus", "tis", "nt"),
    "PERF": inflection("í", "istí", "it", "imus", "istis", "érunt"),
    "PAS": inflection("r", "ris", "tur", "mur", "miní", "ntur"),
    "sum PRES INDC": inflection("us sum", "us es", "us est", "í sumus", "í estis", "í sunt"),
    "sum IMPF INDC": inflection("us eram", "us erás", "us erat", "í erámus", "í erátis", "í erant"),
    "sum FUTR": inflection("us ero", "us eris", "us erit", "í erimus", "í eritis", "í erunt"),
    "sum IMPF INDC plain": inflection("eram", "erás", "erat", "erámus", "erátis", "erant"),
    "sum PRES SUBJ": inflection("us sim", "us sís", "us sit", "í símus", "í sítis", "í sint"),
    "sum IMPF SUBJ": inflection("us essem", "us essés", "us essét", "í essémus", "í essétis", "í essent"),
    "thematic vowel": {1: "á", 2: "é", 3: "é", 3.5: "ié", 4: "ié"},
    "PRES ACT INFN": "re",
    "PRES PAS INFN": {1: "árí", 2: "érí", 3: "í", 3.5: "í", 4: "írí"},
    "PERF INFN": "isse",
    "PRES ACT IMPT": inflection(None, "", None, None, "te", None),
    "PRES PAS IMPT": inflection(None, "re", None, None, "miní", None),
    "FUTR ACT IMPT": inflection(None, "tó", "tó", None, "tóte", "ntó"),
    "FUTR PAS IMPT": inflection(None, "tor", "tor", None, None, "ntor")
}
connectors = {
    1: {
        "PRES": {
            "ACT": {
                "INDC": inflection("", "á", "a", "á", "á", "a"),
                "SUBJ": inflection("e", "é", "e", "é", "é", "e"),
                "IMPT": inflection(None, "á", None, None, "á", None),
                "INFN": "á"
            },
            "PAS": {
                "INDC": inflection("o", "á", "a", "á", "á", "a"),
                "SUBJ": inflection("e", "é", "é", "é", "é", "e"),
                "IMPT": inflection(None, "á", None, None, "á", None),
                "INFN": "á"
            }
        },
        "IMPF": {
            "ACT": {
                "INDC": inflection("ába", "ábá", "ába", "ábá", "ábá", "ába"),
                "SUBJ": inflection("áre", "áré", "áre", "áré", "áré", "áre"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": inflection("ába", "ábá", "ábá", "ábá", "ábá", "ába"),
                "SUBJ": inflection("áre", "áré", "áré", "áré", "áré", "áre"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "PERF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("eri", "erí", "eri", "erí", "erí", "eri"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": ""
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": " "
            }
        },
        "PLPF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("isse", "issé", "isse", "issé", "issé", "isse"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "FUTR": {
            "ACT": {
                "INDC": inflection("áb", "ábi", "ábi", "ábi", "ábi", "ábu"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "á", "á", None, "á", "a"),
                "INFN": " "
            },
            "PAS": {
                "INDC": inflection("ábo", "ábe", "ábi", "ábi", "ábi", "ábu"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "á", "á", None, None, "a"),
                "INFN": " "
            }
        },
        "FTPF": {
            "ACT": {
                "INDC": inflection("er", "eri", "eri", "eri", "eri", "eri"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        }
    },
    2: {
        "PRES": {
            "ACT": {
                "INDC": inflection("e", "é", "e", "é", "é", "e"),
                "SUBJ": inflection("ea", "eá", "ea", "eá", "eá", "ea"),
                "IMPT": inflection(None, "é", None, None, "é", None),
                "INFN": "é"
            },
            "PAS": {
                "INDC": inflection("eo", "é", "é", "é", "é", "e"),
                "SUBJ": inflection("ea", "eá", "eá", "eá", "eá", "ea"),
                "IMPT": inflection(None, "é", None, None, "é", None),
                "INFN": "é"
            }
        },
        "IMPF": {
            "ACT": {
                "INDC": inflection("éba", "ébá", "éba", "ébá", "ébá", "éba"),
                "SUBJ": inflection("ére", "éré", "éré", "éré", "éré", "ére"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": inflection("éba", "ébá", "ébá", "ébá", "ébá", "éba"),
                "SUBJ": inflection("ére", "éré", "éré", "éré", "éré", "ére"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "PERF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("eri", "erí", "eri", "erí", "erí", "eri"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": ""
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": " "
            }
        },
        "PLPF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("isse", "issé", "isse", "issé", "issé", "isse"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "FUTR": {
            "ACT": {
                "INDC": inflection("éb", "ébi", "ébi", "ébi", "ébi", "ébu"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "é", "é", None, "é", "e"),
                "INFN": " "
            },
            "PAS": {
                "INDC": inflection("ébo", "ébe", "ébi", "ébi", "ébi", "ébu"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "é", "é", None, None, "e"),
                "INFN": " "
            }
        },
        "FTPF": {
            "ACT": {
                "INDC": inflection("er", "eri", "eri", "eri", "eri", "eri"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        }
    },
    3: {
        "PRES": {
            "ACT": {
                "INDC": inflection("", "i", "i", "i", "i", "u"),
                "SUBJ": inflection("a", "á", "a", "á", "á", "a"),
                "IMPT": inflection(None, "e", None, None, "i", None),
                "INFN": "e"
            },
            "PAS": {
                "INDC": inflection("o", "e", "i", "i", "i", "u"),
                "SUBJ": inflection("a", "á", "á", "á", "á", "a"),
                "IMPT": inflection(None, "e", None, None, "i", None),
                "INFN": ""
            }
        },
        "IMPF": {
            "ACT": {
                "INDC": inflection("éba", "ébá", "éba", "ébá", "ébá", "éba"),
                "SUBJ": inflection("ere", "eré", "ere", "eré", "eré", "ere"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": inflection("éba", "ébá", "ébá", "ébá", "ébá", "éba"),
                "SUBJ": inflection("ere", "eré", "eré", "eré", "eré", "ere"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "PERF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("eri", "erí", "eri", "erí", "erí", "eri"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": ""
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": " "
            }
        },
        "PLPF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("isse", "issé", "isse", "issé", "issé", "isse"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "FUTR": {
            "ACT": {
                "INDC": inflection("a", "é", "e", "é", "é", "e"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "i", "i", None, "i", "u"),
                "INFN": " "
            },
            "PAS": {
                "INDC": inflection("a", "é", "é", "é", "é", "e"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "i", "i", None, None, "u"),
                "INFN": " "
            }
        },
        "FTPF": {
            "ACT": {
                "INDC": inflection("er", "eri", "eri", "eri", "eri", "eri"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        }
    },
    3.5: {
        "PRES": {
            "ACT": {
                "INDC": inflection("i", "i", "i", "i", "i", "iu"),
                "SUBJ": inflection("ia", "iá", "ia", "iá", "iá", "ia"),
                "IMPT": inflection(None, "e", None, None, "i", None),
                "INFN": "e"
            },
            "PAS": {
                "INDC": inflection("io", "e", "i", "i", "i", "iu"),
                "SUBJ": inflection("ia", "iá", "iá", "iá", "iá", "ia"),
                "IMPT": inflection(None, "e", None, None, "i", None),
                "INFN": ""
            }
        },
        "IMPF": {
            "ACT": {
                "INDC": inflection("iéba", "iébá", "iéba", "iébá", "iébá", "iéba"),
                "SUBJ": inflection("ere", "eré", "ere", "eré", "eré", "ere"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": inflection("iéba", "iébá", "iébá", "iébá", "iébá", "iéba"),
                "SUBJ": inflection("ere", "eré", "eré", "eré", "eré", "ere"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "PERF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("eri", "erí", "eri", "erí", "erí", "eri"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": ""
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": " "
            }
        },
        "PLPF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("isse", "issé", "isse", "issé", "issé", "isse"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "FUTR": {
            "ACT": {
                "INDC": inflection("ia", "ié", "ie", "ié", "ié", "ie"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "i", "i", None, "i", "iu"),
                "INFN": " "
            },
            "PAS": {
                "INDC": inflection("ia", "ié", "ié", "ié", "ié", "ie"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "i", "i", None, None, "iu"),
                "INFN": " "
            }
        },
        "FTPF": {
            "ACT": {
                "INDC": inflection("er", "eri", "eri", "eri", "eri", "eri"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        }
    },
    4: {
        "PRES": {
            "ACT": {
                "INDC": inflection("i", "í", "i", "í", "í", "iu"),
                "SUBJ": inflection("ia", "iá", "ia", "iá", "iá", "ia"),
                "IMPT": inflection(None, "í", None, None, "í", None),
                "INFN": "í"
            },
            "PAS": {
                "INDC": inflection("io", "í", "í", "í", "í", "iu"),
                "SUBJ": inflection("ia", "iá", "iá", "iá", "iá", "ia"),
                "IMPT": inflection(None, "í", None, None, "í", None),
                "INFN": "í"
            }
        },
        "IMPF": {
            "ACT": {
                "INDC": inflection("iéba", "iébá", "iéba", "iébá", "iébá", "iéba"),
                "SUBJ": inflection("íre", "íré", "íre", "íré", "íré", "íre"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": inflection("iéba", "iébá", "iébá", "iébá", "iébá", "iéba"),
                "SUBJ": inflection("íre", "íré", "íré", "íré", "íré", "íre"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "PERF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("eri", "erí", "eri", "erí", "erí", "eri"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": ""
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": " "
            }
        },
        "PLPF": {
            "ACT": {
                "INDC": constantInflection(""),
                "SUBJ": inflection("isse", "issé", "isse", "issé", "issé", "isse"),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": constantInflection(""),
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        },
        "FUTR": {
            "ACT": {
                "INDC": inflection("ia", "ié", "ie", "ié", "ié", "ie"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "í", "í", None, "í", "iu"),
                "INFN": " "
            },
            "PAS": {
                "INDC": inflection("ia", "ié", "ié", "ié", "ié", "ie"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": inflection(None, "í", "í", None, None, "iu"),
                "INFN": " "
            }
        },
        "FTPF": {
            "ACT": {
                "INDC": inflection("er", "eri", "eri", "eri", "eri", "eri"),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            },
            "PAS": {
                "INDC": constantInflection(""),
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None
            }
        }
    }
}

def makeInflection(kind, *, conj, stem, tense, voice, mood, ending) -> dict:
    if kind == "regular":
        infl = dict(zip(EMPTY_INFLECTION.keys(), [(stem, connectors[conj][tense][voice][mood][p], endings[ending][p]) for p in EMPTY_INFLECTION.keys()]))
        newInfl = {}
        for k, word in infl.items():
            newInfl[k] = None if any([x is None for x in word]) else word
        infl = {k: v if v is None else "".join(v) for k, v in newInfl.items()}
        print(infl.values())
        return infl
def verb(pres: str = None, inf: str = None, perf: str = None, ppp: str = None) -> dict:
    # general
    transitivity = bool(ppp)  # a verb is transitive if it takes a direct object, :. if it can be PAS
    # find kind
    if pres.endswith("í") and inf.endswith("isse") and perf is None and ppp is None:
        kind = "defective"
    elif perf is not None and pres.endswith("ó") and inf.endswith("re") and perf.endswith("us sum") and ppp is None:
        kind = "semideponent"
    elif perf is not None and pres.endswith("or") and inf.endswith("í") and perf.endswith("us sum") and ppp is None:
        kind = "deponent"
    elif perf is not None and pres.endswith("ó") and inf.endswith("re") and perf.endswith("í") and ppp is None:
        kind = "regular"
    elif perf is not None and ppp is not None and pres.endswith("ó") and inf.endswith("re") and perf.endswith("í") and ppp.endswith("us"):
        kind = "regular"
        pppStem = ppp.removesuffix("us")
    else: raise ValueError
    # find conjugation and stems
    match kind:
        case "regular" | "semideponent":
            if inf.endswith("áre"):
                conj = 1
                stem = pres.removesuffix("ó")
            elif inf.endswith("ére"):
                conj = 2
                stem = pres[:-2]
            elif inf.endswith("ere") and pres.endswith("ió"):
                conj = 3.5
                stem = pres[:-2]
            elif inf.endswith("ere") and pres.endswith("ó"):
                conj = 3
                stem = pres.removesuffix("ó")
            elif inf.endswith("íre"):
                conj = 4
                stem = pres[:-2]
            else: raise ValueError
            if kind == "regular":
                perfStem = perf.removesuffix("í")
            if ppp is not None:
                pppStem = ppp.removesuffix("us")
            else:
                ppp = "us"
                pppStem = "???????"
        case "deponent":
            if inf.endswith("árí"):
                conj = 1
                stem = pres.removesuffix("or")
            elif inf.endswith("érí"):
                conj = 2
                stem = pres[:-3]
            elif inf.endswith("írí"):
                conj = 4
                stem = pres[:-3]
            elif inf.endswith("í") and pres.endswith("ior"):
                conj = 3.5
                stem = pres[:-3]
            elif inf.endswith("í") and pres.endswith("or"):
                conj = 3
                stem = pres.removesuffix("or")
            else: raise ValueError
        case "defective":
            conj = -1  # doesn't matter
            stem = pres.removesuffix("í")
    # form the verb
    match kind:
        case "regular":
            pres_act_indc = makeInflection("regular", conj=conj, stem=stem, tense="PRES", voice="ACT", mood="INDC", ending="o s t")
            pres_act_subj = makeInflection("regular", conj=conj, stem=stem, tense="PRES", voice="ACT", mood="SUBJ", ending="m s t")
            pres_act_impt = makeInflection("regular", conj=conj, stem=stem, tense="PRES", voice="ACT", mood="IMPT", ending="PRES ACT IMPT")
            pres_act_infn = inf
            pres_act_ptcp = decline33_i(stem + endings["thematic vowel"][conj] + "ns", stem + endings["thematic vowel"][conj] + "ntis")
            impf_act_indc = makeInflection("regular", conj=conj, stem=stem, tense="IMPF", voice="ACT", mood="INDC", ending="m s t")
            impf_act_subj = makeInflection("regular", conj=conj, stem=stem, tense="IMPF", voice="ACT", mood="SUBJ", ending="m s t")
            impf_act_impt = EMPTY_INFLECTION
            impf_act_infn = None
            impf_act_ptcp = EMPTY_PARTICIPLE
            perf_act_indc = makeInflection("regular", conj=conj, stem=perfStem, tense="PERF", voice="ACT", mood="INDC", ending="PERF")
            perf_act_subj = makeInflection("regular", conj=conj, stem=perfStem, tense="PERF", voice="ACT", mood="SUBJ", ending="m s t")
            perf_act_impt = EMPTY_INFLECTION
            perf_act_infn = perfStem + "isse"
            perf_act_ptcp = EMPTY_PARTICIPLE
            plpf_act_indc = makeInflection("regular", conj=conj, stem=perfStem, tense="PLPF", voice="ACT", mood="INDC", ending="sum IMPF INDC plain")
            plpf_act_subj = makeInflection("regular", conj=conj, stem=perfStem, tense="PLPF", voice="ACT", mood="SUBJ", ending="m s t")
            plpf_act_impt = EMPTY_INFLECTION
            plpf_act_infn = None
            plpf_act_ptcp = EMPTY_PARTICIPLE
            futr_act_indc = makeInflection("regular", conj=conj, stem=stem, tense="FUTR", voice="ACT", mood="INDC", ending="o s t")
            futr_act_subj = EMPTY_INFLECTION
            futr_act_impt = makeInflection("regular", conj=conj, stem=stem, tense="FUTR", voice="ACT", mood="IMPT", ending="FUTR ACT IMPT")
            futr_act_infn = f"{pppStem}úrus esse"
            futr_act_ptcp = decline212(pppStem + "úrus")
            ftpf_act_indc = makeInflection("regular", conj=conj, stem=perfStem, tense="FTPF", voice="ACT", mood="INDC", ending="o s t")
            ftpf_act_subj = EMPTY_INFLECTION
            ftpf_act_impt = EMPTY_INFLECTION
            ftpf_act_infn = None
            ftpf_act_ptcp = EMPTY_PARTICIPLE
            
            if transitivity:
                pres_pas_indc = makeInflection("regular", conj=conj, stem=stem, tense="PRES", voice="PAS", mood="INDC", ending="PAS")
                pres_pas_subj = makeInflection("regular", conj=conj, stem=stem, tense="PRES", voice="PAS", mood="SUBJ", ending="PAS")
                pres_pas_impt = makeInflection("regular", conj=conj, stem=stem, tense="PRES", voice="PAS", mood="IMPT", ending="PRES PAS IMPT")
                pres_pas_infn = stem + endings["PRES PAS INFN"][conj]
                pres_pas_ptcp = EMPTY_PARTICIPLE
                impf_pas_indc = makeInflection("regular", conj=conj, stem=stem, tense="IMPF", voice="PAS", mood="INDC", ending="PAS")
                impf_pas_subj = makeInflection("regular", conj=conj, stem=stem, tense="IMPF", voice="PAS", mood="SUBJ", ending="PAS")
                impf_pas_impt = EMPTY_INFLECTION
                impf_pas_infn = None
                impf_pas_ptcp = EMPTY_PARTICIPLE
                perf_pas_indc = makeInflection("regular", conj=conj, stem=pppStem, tense="PERF", voice="PAS", mood="INDC", ending="sum PRES INDC")
                perf_pas_subj = makeInflection("regular", conj=conj, stem=pppStem, tense="PERF", voice="PAS", mood="SUBJ", ending="sum PRES SUBJ")
                perf_pas_impt = EMPTY_INFLECTION
                perf_pas_infn = f"{ppp} esse"
                perf_pas_ptcp = decline212(ppp)
                plpf_pas_indc = makeInflection("regular", conj=conj, stem=pppStem, tense="PLPF", voice="PAS", mood="INDC", ending="sum IMPF INDC")
                plpf_pas_subj = makeInflection("regular", conj=conj, stem=pppStem, tense="PLPF", voice="PAS", mood="SUBJ", ending="sum IMPF SUBJ")
                plpf_pas_impt = EMPTY_INFLECTION
                plpf_pas_infn = None
                plpf_pas_ptcp = EMPTY_PARTICIPLE
                futr_pas_indc = makeInflection("regular", conj=conj, stem=stem, tense="FUTR", voice="PAS", mood="INDC", ending="PAS")
                futr_pas_subj = EMPTY_INFLECTION
                futr_pas_impt = makeInflection("regular", conj=conj, stem=stem, tense="FUTR", voice="PAS", mood="IMPT", ending="FUTR PAS IMPT")
                futr_pas_infn = f"{ppp} írí"
                futr_pas_ptcp = decline212(stem + unmacron(endings["thematic vowel"][conj]) + "ndus")
                ftpf_pas_indc = makeInflection("regular", conj=conj, stem=pppStem, tense="FTPF", voice="PAS", mood="INDC", ending="sum FUTR")
                ftpf_pas_subj = EMPTY_INFLECTION
                ftpf_pas_impt = EMPTY_INFLECTION
                ftpf_pas_infn = None
                ftpf_pas_ptcp = EMPTY_PARTICIPLE
            else:
                pres_pas_indc = pres_pas_subj = pres_pas_impt = impf_pas_indc = impf_pas_subj = impf_pas_impt = perf_pas_indc = perf_pas_subj = perf_pas_impt = plpf_pas_indc = plpf_pas_subj = plpf_pas_impt = futr_pas_indc = futr_pas_subj = futr_pas_impt = ftpf_pas_indc = ftpf_pas_subj = ftpf_pas_impt = EMPTY_INFLECTION
                pres_pas_infn = impf_pas_infn = plpf_pas_infn = perf_pas_infn = futr_pas_infn = ftpf_pas_infn = None
                pres_pas_ptcp = impf_pas_ptcp = perf_pas_ptcp = plpf_pas_ptcp = futr_pas_ptcp = ftpf_pas_ptcp = EMPTY_PARTICIPLE

verb("amó", "amáre", "amáví", "amátus"),
verb("accidó", "accidere", "accidí")
verb("audeó", "audére", "ausus sum")
verb("conor", "conárí", "conátus sum")
verb("ódí", "ódisse")
'''

DEPONENTS = ["conor", "vereor", "loquor", "patior", "orior"]

VERBS = {
    # REGULAR
    "AMO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "amo",
                    "2S": "amas",
                    "3S": "amat",
                    "1P": "amamus",
                    "2P": "amatis",
                    "3P": "amant"
                },
                "SUBJ": {
                    "1S": "amem",
                    "2S": "ames",
                    "3S": "amet",
                    "1P": "amemus",
                    "2P": "ametis",
                    "3P": "ament"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "ama",
                    "3S": None,
                    "1P": None,
                    "2P": "amate",
                    "3P": None
                },
                "INFN": "amare",
                "PTCP": decline33_i("amans", "amantis")
                },
            "PAS": {
                "INDC": {
                    "1S": "amor",
                    "2S": "amaris",
                    "3S": "amatur",
                    "1P": "amamur",
                    "2P": "amamini",
                    "3P": "amantur"
                },
                "SUBJ": {
                    "1S": "amer",
                    "2S": "ameris",
                    "3S": "ametur",
                    "1P": "amemur",
                    "2P": "amemini",
                    "3P": "amentur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "amare",
                    "3S": None,
                    "1P": None,
                    "2P": "amamini",
                    "3P": None
                },
                "INFN": "amari",
                "PTCP": EMPTY_PARTICIPLE
                },
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "amabam",
                    "2S": "amabas",
                    "3S": "amabat",
                    "1P": "amabamus",
                    "2P": "amabatis",
                    "3P": "amabant"
                },
                "SUBJ": {
                    "1S": "amarem",
                    "2S": "amares",
                    "3S": "amaret",
                    "1P": "amaremus",
                    "2P": "amaretis",
                    "3P": "amarent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "amabar",
                    "2S": "amabaris",
                    "3S": "amabatur",
                    "1P": "amabamur",
                    "2P": "amabamini",
                    "3P": "amabantur"
                },
                "SUBJ": {
                    "1S": "amarer",
                    "2S": "amareris",
                    "3S": "amaretur",
                    "1P": "amaremur",
                    "2P": "amaremini",
                    "3P": "amarentur"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "amavi",
                    "2S": "amavisti",
                    "3S": "amavit",
                    "1P": "amavimus",
                    "2P": "amavistis",
                    "3P": "amaverunt"
                },
                "SUBJ": {
                    "1S": "amaverim",
                    "2S": "amaveris",
                    "3S": "amaverit",
                    "1P": "amaverimus",
                    "2P": "amaveritis",
                    "3P": "amaverint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "amavisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "amatus sum",
                    "2S": "amatus es",
                    "3S": "amatus est",
                    "1P": "amati sumus",
                    "2P": "amati estis",
                    "3P": "amati sunt"
                },
                "SUBJ": {
                    "1S": "amatus sim",
                    "2S": "amatus sis",
                    "3S": "amatus sit",
                    "1P": "amati simus",
                    "2P": "amati sitis",
                    "3P": "amati sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "amatus esse",
                "PTCP": decline212("amatus")
                },
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "amaveram",
                    "2S": "amaveras",
                    "3S": "amaverat",
                    "1P": "amaveramus",
                    "2P": "amaveratis",
                    "3P": "amaverant"
                },
                "SUBJ": {
                    "1S": "amavissem",
                    "2S": "amavisses",
                    "3S": "amavisset",
                    "1P": "amavissemus",
                    "2P": "amavissetis",
                    "3P": "amavissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "amatus eram",
                    "2S": "amatus eras",
                    "3S": "amatus erat",
                    "1P": "amati eramus",
                    "2P": "amati eratis",
                    "3P": "amati erant"
                },
                "SUBJ": {
                    "1S": "amatus essem",
                    "2S": "amatus esses",
                    "3S": "amatus esset",
                    "1P": "amati essemus",
                    "2P": "amati essetis",
                    "3P": "amati essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "amabo",
                    "2S": "amabis",
                    "3S": "amabit",
                    "1P": "amabimus",
                    "2P": "amabitis",
                    "3P": "amabunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "amato",
                    "3S": "amato",
                    "1P": None,
                    "2P": "amatote",
                    "3P": "amanto"
                },
                "INFN": "amaturus esse",
                "PTCP": decline212("amaturus")
                },
            "PAS": {
                "INDC": {
                    "1S": "amabor",
                    "2S": "amaberis",
                    "3S": "amabitur",
                    "1P": "amabimur",
                    "2P": "amabimini",
                    "3P": "amabuntur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "amator",
                    "3S": "amator",
                    "1P": None,
                    "2P": None,
                    "3P": "amantor"
                },
                "INFN": "amatus iri",
                "PTCP": decline212("amandus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "amavero",
                    "2S": "amaveris",
                    "3S": "amaverit",
                    "1P": "amaverimus",
                    "2P": "amaveritis",
                    "3P": "amaverint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "amatus ero",
                    "2S": "amatus eris",
                    "3S": "amatus erit",
                    "1P": "amati erimus",
                    "2P": "amati eritis",
                    "3P": "amati erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        },
    "HABEO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "habeo",
                    "2S": "habes",
                    "3S": "habet",
                    "1P": "habemus",
                    "2P": "habetis",
                    "3P": "habent"
                },
                "SUBJ": {
                    "1S": "habeam",
                    "2S": "habeas",
                    "3S": "habeat",
                    "1P": "habeamus",
                    "2P": "habeatis",
                    "3P": "habeant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "habe",
                    "3S": None,
                    "1P": None,
                    "2P": "habete",
                    "3P": None
                },
                "INFN": "habere",
                "PTCP": decline33_i("habens", "habentis")
                },
            "PAS": {
                "INDC": {
                    "1S": "habeor",
                    "2S": "haberis",
                    "3S": "habetur",
                    "1P": "habemur",
                    "2P": "habemini",
                    "3P": "habentur"
                },
                "SUBJ": {
                    "1S": "habear",
                    "2S": "habearis",
                    "3S": "habeatur",
                    "1P": "habeamur",
                    "2P": "habeamini",
                    "3P": "habeantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "habere",
                    "3S": None,
                    "1P": None,
                    "2P": "habemini",
                    "3P": None
                },
                "INFN": "haberi",
                "PTCP": EMPTY_PARTICIPLE
                },
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "habebam",
                    "2S": "habebas",
                    "3S": "habebat",
                    "1P": "habebamus",
                    "2P": "habebatis",
                    "3P": "habebant"
                },
                "SUBJ": {
                    "1S": "haberem",
                    "2S": "haberes",
                    "3S": "haberet",
                    "1P": "haberemus",
                    "2P": "haberetis",
                    "3P": "haberent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "habebar",
                    "2S": "habebaris",
                    "3S": "habebatur",
                    "1P": "habebamur",
                    "2P": "habebamini",
                    "3P": "habebantur"
                },
                "SUBJ": {
                    "1S": "haberer",
                    "2S": "habereris",
                    "3S": "haberetur",
                    "1P": "haberemur",
                    "2P": "haberemini",
                    "3P": "haberentur"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "habui",
                    "2S": "habuisti",
                    "3S": "habuit",
                    "1P": "habuimus",
                    "2P": "habuistis",
                    "3P": "habuerunt"
                },
                "SUBJ": {
                    "1S": "habuerim",
                    "2S": "habueris",
                    "3S": "habuerit",
                    "1P": "habuerimus",
                    "2P": "habueritis",
                    "3P": "habuerint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "habuisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "habitus sum",
                    "2S": "habitus es",
                    "3S": "habitus est",
                    "1P": "habiti sumus",
                    "2P": "habiti estis",
                    "3P": "habiti sunt"
                },
                "SUBJ": {
                    "1S": "habitus sim",
                    "2S": "habitus sis",
                    "3S": "habitus sit",
                    "1P": "habiti simus",
                    "2P": "habiti sitis",
                    "3P": "habiti sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "habitus esse",
                "PTCP": decline212("habitus")
                }
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "habueram",
                    "2S": "habueras",
                    "3S": "habuerat",
                    "1P": "habueramus",
                    "2P": "habueratis",
                    "3P": "habuerant"
                },
                "SUBJ": {
                    "1S": "habuissem",
                    "2S": "habuisses",
                    "3S": "habuisset",
                    "1P": "habuissemus",
                    "2P": "habuissetis",
                    "3P": "habuissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "habitus eram",
                    "2S": "habitus eras",
                    "3S": "habitus erat",
                    "1P": "habiti eramus",
                    "2P": "habiti eratis",
                    "3P": "habiti erant"
                },
                "SUBJ": {
                    "1S": "habitus essem",
                    "2S": "habitus esses",
                    "3S": "habitus esset",
                    "1P": "habiti essemus",
                    "2P": "habiti essetis",
                    "3P": "habiti essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "habebo",
                    "2S": "habebis",
                    "3S": "habebit",
                    "1P": "habebimus",
                    "2P": "habebitis",
                    "3P": "habebunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "habeto",
                    "3S": "habeto",
                    "1P": None,
                    "2P": "habetote",
                    "3P": "habento"
                },
                "INFN": "habiturus esse",
                "PTCP": decline212("habiturus")
                },
            "PAS": {
                "INDC": {
                    "1S": "habebor",
                    "2S": "habeberis",
                    "3S": "habebitur",
                    "1P": "habebimur",
                    "2P": "habebimini",
                    "3P": "habebuntur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "habetor",
                    "3S": "habetor",
                    "1P": None,
                    "2P": None,
                    "3P": "habentor"
                },
                "INFN": "habitus iri",
                "PTCP": decline212("habendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "habuero",
                    "2S": "habueris",
                    "3S": "habuerit",
                    "1P": "habuerimus",
                    "2P": "habueritis",
                    "3P": "habuerint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "habitus ero",
                    "2S": "habitus eris",
                    "3S": "habitus erit",
                    "1P": "habiti erimus",
                    "2P": "habiti eritis",
                    "3P": "habiti erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        },
    "MITTO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "mitto",
                    "2S": "mittis",
                    "3S": "mittit",
                    "1P": "mittimus",
                    "2P": "mittitis",
                    "3P": "mittunt"
                },
                "SUBJ": {
                    "1S": "mittam",
                    "2S": "mittas",
                    "3S": "mittat",
                    "1P": "mittamus",
                    "2P": "mittatis",
                    "3P": "mittant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "mitte",
                    "3S": None,
                    "1P": None,
                    "2P": "mittite",
                    "3P": None
                },
                "INFN": "mittere",
                "PTCP": decline33_i("mittens", "mittentis")
                },
            "PAS": {
                "INDC": {
                    "1S": "mittor",
                    "2S": "mitteris",
                    "3S": "mittitur",
                    "1P": "mittimur",
                    "2P": "mittimini",
                    "3P": "mittuntur"
                },
                "SUBJ": {
                    "1S": "mittar",
                    "2S": "mittaris",
                    "3S": "mittatur",
                    "1P": "mittamur",
                    "2P": "mittamini",
                    "3P": "mittantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "mittere",
                    "3S": None,
                    "1P": None,
                    "2P": "mittemini",
                    "3P": None
                },
                "INFN": "mitti",
                "PTCP": EMPTY_PARTICIPLE
                },
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "mittebam",
                    "2S": "mittebas",
                    "3S": "mittebat",
                    "1P": "mittebamus",
                    "2P": "mittebatis",
                    "3P": "mittebant"
                },
                "SUBJ": {
                    "1S": "mitterem",
                    "2S": "mitteres",
                    "3S": "mitteret",
                    "1P": "mitteremus",
                    "2P": "mitteretis",
                    "3P": "mitterent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "mittebar",
                    "2S": "mittebaris",
                    "3S": "mittebatur",
                    "1P": "mittebamur",
                    "2P": "mittebamini",
                    "3P": "mittebantur"
                },
                "SUBJ": {
                    "1S": "mitterer",
                    "2S": "mittereris",
                    "3S": "mitteretur",
                    "1P": "mitteremur",
                    "2P": "mitteremini",
                    "3P": "mitterentur"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "misi",
                    "2S": "misisti",
                    "3S": "misit",
                    "1P": "misimus",
                    "2P": "misistis",
                    "3P": "miserunt"
                },
                "SUBJ": {
                    "1S": "miserim",
                    "2S": "miseris",
                    "3S": "miserit",
                    "1P": "miserimus",
                    "2P": "miseritis",
                    "3P": "miserint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "misisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "missus sum",
                    "2S": "missus es",
                    "3S": "missus est",
                    "1P": "missi sumus",
                    "2P": "missi estis",
                    "3P": "missi sunt"
                },
                "SUBJ": {
                    "1S": "missus sim",
                    "2S": "missus sis",
                    "3S": "missus sit",
                    "1P": "missi simus",
                    "2P": "missi sitis",
                    "3P": "missi sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "missus esse",
                "PTCP": decline212("missus")
                }
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "miseram",
                    "2S": "miseras",
                    "3S": "miserat",
                    "1P": "miseramus",
                    "2P": "miseratis",
                    "3P": "miserant"
                },
                "SUBJ": {
                    "1S": "misissem",
                    "2S": "misisses",
                    "3S": "misisset",
                    "1P": "misissemus",
                    "2P": "misissetis",
                    "3P": "misissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "missus eram",
                    "2S": "missus eras",
                    "3S": "missus erat",
                    "1P": "missi eramus",
                    "2P": "missi eratis",
                    "3P": "missi erant"
                },
                "SUBJ": {
                    "1S": "missus essem",
                    "2S": "missus esses",
                    "3S": "missus esset",
                    "1P": "missi essemus",
                    "2P": "missi essetis",
                    "3P": "missi essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "mittam",
                    "2S": "mittes",
                    "3S": "mittet",
                    "1P": "mittemus",
                    "2P": "mittetis",
                    "3P": "mittent"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "mittito",
                    "3S": "mittito",
                    "1P": None,
                    "2P": "mittitote",
                    "3P": "mittunto"
                },
                "INFN": "missurus esse",
                "PTCP": decline212("missurus")
                },
            "PAS": {
                "INDC": {
                    "1S": "mittar",
                    "2S": "mitteris",
                    "3S": "mittetur",
                    "1P": "mittemur",
                    "2P": "mittemini",
                    "3P": "mittentur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "mittitor",
                    "3S": "mittitor",
                    "1P": None,
                    "2P": None,
                    "3P": "mittuntor"
                },
                "INFN": "missus iri",
                "PTCP": decline212("mittendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "misero",
                    "2S": "miseris",
                    "3S": "miserit",
                    "1P": "miserimus",
                    "2P": "miseritis",
                    "3P": "miserint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "missus ero",
                    "2S": "missus eris",
                    "3S": "missus erit",
                    "1P": "missi erimus",
                    "2P": "missi eritis",
                    "3P": "missi erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        },
    "CAPIO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "capio",
                    "2S": "capis",
                    "3S": "capit",
                    "1P": "capimus",
                    "2P": "capitis",
                    "3P": "capiunt"
                },
                "SUBJ": {
                    "1S": "capiam",
                    "2S": "capias",
                    "3S": "capiat",
                    "1P": "capiamus",
                    "2P": "capiatis",
                    "3P": "capiant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "cape",
                    "3S": None,
                    "1P": None,
                    "2P": "capite",
                    "3P": None
                },
                "INFN": "capere",
                "PTCP": decline33_i("capiens", "capientis")
                },
            "PAS": {
                "INDC": {
                    "1S": "capior",
                    "2S": "caperis",
                    "3S": "capitur",
                    "1P": "capimur",
                    "2P": "capimini",
                    "3P": "capiuntur"
                },
                "SUBJ": {
                    "1S": "capiar",
                    "2S": "capiaris",
                    "3S": "capiatur",
                    "1P": "capiamur",
                    "2P": "capiamini",
                    "3P": "capiantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "capere",
                    "3S": None,
                    "1P": None,
                    "2P": "capimini",
                    "3P": None
                },
                "INFN": "capi",
                "PTCP": EMPTY_PARTICIPLE
                },
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "capiebam",
                    "2S": "capiebas",
                    "3S": "capiebat",
                    "1P": "capiebamus",
                    "2P": "capiebatis",
                    "3P": "capiebant"
                },
                "SUBJ": {
                    "1S": "caperem",
                    "2S": "caperes",
                    "3S": "caperet",
                    "1P": "caperemus",
                    "2P": "caperetis",
                    "3P": "caperent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "capiebar",
                    "2S": "capiebaris",
                    "3S": "capiebatur",
                    "1P": "capiebamur",
                    "2P": "capiebamini",
                    "3P": "capiebantur"
                },
                "SUBJ": {
                    "1S": "caperer",
                    "2S": "capereris",
                    "3S": "caperetur",
                    "1P": "caperemur",
                    "2P": "caperemini",
                    "3P": "caperentur"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "cepi",
                    "2S": "cepisti",
                    "3S": "cepit",
                    "1P": "cepimus",
                    "2P": "cepistis",
                    "3P": "ceperunt"
                },
                "SUBJ": {
                    "1S": "ceperim",
                    "2S": "ceperis",
                    "3S": "ceperit",
                    "1P": "ceperimus",
                    "2P": "ceperitis",
                    "3P": "ceperint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "cepisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "captus sum",
                    "2S": "captus es",
                    "3S": "captus est",
                    "1P": "capti sumus",
                    "2P": "capti estis",
                    "3P": "capti sunt"
                },
                "SUBJ": {
                    "1S": "captus sim",
                    "2S": "captus sis",
                    "3S": "captus sit",
                    "1P": "capti simus",
                    "2P": "capti sitis",
                    "3P": "capti sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "captus esse",
                "PTCP": decline212("captus")
                }
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "ceperam",
                    "2S": "ceperas",
                    "3S": "ceperat",
                    "1P": "ceperamus",
                    "2P": "ceperatis",
                    "3P": "ceperant"
                },
                "SUBJ": {
                    "1S": "cepissem",
                    "2S": "cepisses",
                    "3S": "cepisset",
                    "1P": "cepissemus",
                    "2P": "cepissetis",
                    "3P": "cepissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "captus eram",
                    "2S": "captus eras",
                    "3S": "captus erat",
                    "1P": "capti eramus",
                    "2P": "capti eratis",
                    "3P": "capti erant"
                },
                "SUBJ": {
                    "1S": "captus essem",
                    "2S": "captus esses",
                    "3S": "captus esset",
                    "1P": "capti essemus",
                    "2P": "capti essetis",
                    "3P": "capti essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "capiam",
                    "2S": "capies",
                    "3S": "capiet",
                    "1P": "capiemus",
                    "2P": "capietis",
                    "3P": "capient"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "capito",
                    "3S": "capito",
                    "1P": None,
                    "2P": "capitote",
                    "3P": "capiunto"
                },
                "INFN": "capturus esse",
                "PTCP": decline212("capturus")
                },
            "PAS": {
                "INDC": {
                    "1S": "capiar",
                    "2S": "capieris",
                    "3S": "capietur",
                    "1P": "capiemur",
                    "2P": "capiemini",
                    "3P": "capientur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "capitor",
                    "3S": "capitor",
                    "1P": None,
                    "2P": None,
                    "3P": "capiuntor"
                },
                "INFN": "captus iri",
                "PTCP": decline212("capiendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "cepero",
                    "2S": "ceperis",
                    "3S": "ceperit",
                    "1P": "ceperimus",
                    "2P": "ceperitis",
                    "3P": "ceperint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "captus ero",
                    "2S": "captus eris",
                    "3S": "captus erit",
                    "1P": "capti erimus",
                    "2P": "capti eritis",
                    "3P": "capti erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        },
    "AUDIO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "audio",
                    "2S": "audis",
                    "3S": "audit",
                    "1P": "audimus",
                    "2P": "auditis",
                    "3P": "audiunt"
                },
                "SUBJ": {
                    "1S": "audiam",
                    "2S": "audias",
                    "3S": "audiat",
                    "1P": "audiamus",
                    "2P": "audiatis",
                    "3P": "audiant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "audi",
                    "3S": None,
                    "1P": None,
                    "2P": "audite",
                    "3P": None
                },
                "INFN": "audire",
                "PTCP": decline33_i("audiens", "audientis")
                },
            "PAS": {
                "INDC": {
                    "1S": "audior",
                    "2S": "audiris",
                    "3S": "auditur",
                    "1P": "audimur",
                    "2P": "audimini",
                    "3P": "audiuntur"
                },
                "SUBJ": {
                    "1S": "audiar",
                    "2S": "audiaris",
                    "3S": "audiatur",
                    "1P": "audiamur",
                    "2P": "audiamini",
                    "3P": "audiantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "audire",
                    "3S": None,
                    "1P": None,
                    "2P": "audimini",
                    "3P": None
                },
                "INFN": "audiri",
                "PTCP": EMPTY_PARTICIPLE
                },
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "audiebam",
                    "2S": "audiebas",
                    "3S": "audiebat",
                    "1P": "audiebamus",
                    "2P": "audiebatis",
                    "3P": "audiebant"
                },
                "SUBJ": {
                    "1S": "audirem",
                    "2S": "audires",
                    "3S": "audiret",
                    "1P": "audiremus",
                    "2P": "audiretis",
                    "3P": "audirent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "audiebar",
                    "2S": "audiebaris",
                    "3S": "audiebatur",
                    "1P": "audiebamur",
                    "2P": "audiebamini",
                    "3P": "audiebantur"
                },
                "SUBJ": {
                    "1S": "audirer",
                    "2S": "audireris",
                    "3S": "audiretur",
                    "1P": "audiremur",
                    "2P": "audiremini",
                    "3P": "audirentur"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "audivi",
                    "2S": "audivisti",
                    "3S": "audivit",
                    "1P": "audivimus",
                    "2P": "audivistis",
                    "3P": "audiverunt"
                },
                "SUBJ": {
                    "1S": "audiverim",
                    "2S": "audiveris",
                    "3S": "audiverit",
                    "1P": "audiverimus",
                    "2P": "audiveritis",
                    "3P": "audiverint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "audivisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "auditus sum",
                    "2S": "auditus es",
                    "3S": "auditus est",
                    "1P": "auditi sumus",
                    "2P": "auditi estis",
                    "3P": "auditi sunt"
                },
                "SUBJ": {
                    "1S": "auditus sim",
                    "2S": "auditus sis",
                    "3S": "auditus sit",
                    "1P": "auditi simus",
                    "2P": "auditi sitis",
                    "3P": "auditi sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "auditus esse",
                "PTCP": decline212("auditus")
                }
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "audiveram",
                    "2S": "audiveras",
                    "3S": "audiverat",
                    "1P": "audiveramus",
                    "2P": "audiveratis",
                    "3P": "audiverant"
                },
                "SUBJ": {
                    "1S": "audivissem",
                    "2S": "audivisses",
                    "3S": "audivisset",
                    "1P": "audivissemus",
                    "2P": "audivissetis",
                    "3P": "audivissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "auditus eram",
                    "2S": "auditus eras",
                    "3S": "auditus erat",
                    "1P": "auditi eramus",
                    "2P": "auditi eratis",
                    "3P": "auditi erant"
                },
                "SUBJ": {
                    "1S": "auditus essem",
                    "2S": "auditus esses",
                    "3S": "auditus esset",
                    "1P": "auditi essemus",
                    "2P": "auditi essetis",
                    "3P": "auditi essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "audiam",
                    "2S": "audies",
                    "3S": "audiet",
                    "1P": "audiemus",
                    "2P": "audietis",
                    "3P": "audient"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "audito",
                    "3S": "audito",
                    "1P": None,
                    "2P": "auditote",
                    "3P": "audiunto"
                },
                "INFN": "auditurus esse",
                "PTCP": decline212("auditurus")
                },
            "PAS": {
                "INDC": {
                    "1S": "audiar",
                    "2S": "audieris",
                    "3S": "audietur",
                    "1P": "audiemur",
                    "2P": "audiemini",
                    "3P": "audientur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "auditor",
                    "3S": "auditor",
                    "1P": None,
                    "2P": None,
                    "3P": "audiuntor"
                },
                "INFN": "auditus iri",
                "PTCP": decline212("audiendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "audivero",
                    "2S": "audiveris",
                    "3S": "audiverit",
                    "1P": "audiverimus",
                    "2P": "audiveritis",
                    "3P": "audiverint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "auditus ero",
                    "2S": "auditus eris",
                    "3S": "auditus erit",
                    "1P": "auditi erimus",
                    "2P": "auditi eritis",
                    "3P": "auditi erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        },
    # DEPONENT
    "CONOR": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "conor",
                    "2S": "conaris",
                    "3S": "conatur",
                    "1P": "conamur",
                    "2P": "conamini",
                    "3P": "conantur"
                },
                "SUBJ": {
                    "1S": "coner",
                    "2S": "coneris",
                    "3S": "conetur",
                    "1P": "conemur",
                    "2P": "conemini",
                    "3P": "conentur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "conare",
                    "3S": None,
                    "1P": None,
                    "2P": "conamini",
                    "3P": None
                },
                "INFN": "conari",
                "PTCP": decline33_i("conans", "conantis")
                },
            "PAS": EMPTY_VOICE,
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "conabar",
                    "2S": "conabaris",
                    "3S": "conabatur",
                    "1P": "conabamur",
                    "2P": "conabamini",
                    "3P": "conabantur"
                },
                "SUBJ": {
                    "1S": "conarem",
                    "2S": "conares",
                    "3S": "conaret",
                    "1P": "conaremus",
                    "2P": "conaretis",
                    "3P": "conarent"
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
                    "1S": "conatus sum",
                    "2S": "conatus es",
                    "3S": "conatus est",
                    "1P": "conati sumus",
                    "2P": "conati estis",
                    "3P": "conati sunt"
                },
                "SUBJ": {
                    "1S": "conatus sim",
                    "2S": "conatus sis",
                    "3S": "conatus sit",
                    "1P": "conati simus",
                    "2P": "conati sitis",
                    "3P": "conati sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "conatus esse",
                "PTCP": decline212("conatus")
                },
            "PAS": EMPTY_VOICE
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "conatus eram",
                    "2S": "conatus eras",
                    "3S": "conatus erat",
                    "1P": "conati eramus",
                    "2P": "conati eratis",
                    "3P": "conati erant"
                },
                "SUBJ": {
                    "1S": "conatus essem",
                    "2S": "conatus esses",
                    "3S": "conatus esset",
                    "1P": "conati essemus",
                    "2P": "conati essetis",
                    "3P": "conati essent"
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
                    "1S": "conabor",
                    "2S": "conaberis",
                    "3S": "conabitur",
                    "1P": "conabimur",
                    "2P": "conabimini",
                    "3P": "conabuntur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "conator",
                    "3S": "conator",
                    "1P": None,
                    "2P": None,
                    "3P": "conantor"
                },
                "INFN": "conaturus esse",
                "PTCP": decline212("conaturus")
                },
            "PAS": {
                "INDC": EMPTY_INFLECTION,
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": decline212("conandus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "conatus ero",
                    "2S": "conatus eris",
                    "3S": "conatus erit",
                    "1P": "conati erimus",
                    "2P": "conati eritis",
                    "3P": "conati erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            }
        },
    "VEREOR": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "vereor",
                    "2S": "vereris",
                    "3S": "veretur",
                    "1P": "veremur",
                    "2P": "veremini",
                    "3P": "verentur"
                },
                "SUBJ": {
                    "1S": "verear",
                    "2S": "verearis",
                    "3S": "vereatur",
                    "1P": "vereamur",
                    "2P": "vereamini",
                    "3P": "vereantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "verere",
                    "3S": None,
                    "1P": None,
                    "2P": "veremini",
                    "3P": None
                },
                "INFN": "vereri",
                "PTCP": decline33_i("verens", "verentis")
                },
            "PAS": EMPTY_VOICE,
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "verebar",
                    "2S": "verebaris",
                    "3S": "verebatur",
                    "1P": "verebamur",
                    "2P": "verebamini",
                    "3P": "verebantur"
                },
                "SUBJ": {
                    "1S": "vererer",
                    "2S": "verereris",
                    "3S": "vereretur",
                    "1P": "vereremur",
                    "2P": "vereremini",
                    "3P": "vererentur"
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
                    "1S": "veritus sum",
                    "2S": "veritus es",
                    "3S": "veritus est",
                    "1P": "veriti sumus",
                    "2P": "veriti estis",
                    "3P": "veriti sunt"
                },
                "SUBJ": {
                    "1S": "veritus sim",
                    "2S": "veritus sis",
                    "3S": "veritus sit",
                    "1P": "veriti simus",
                    "2P": "veriti sitis",
                    "3P": "veriti sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "veritus esse",
                "PTCP": decline212("veritus")
                },
            "PAS": EMPTY_VOICE,
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "veritus eram",
                    "2S": "veritus eras",
                    "3S": "veritus erat",
                    "1P": "veriti eramus",
                    "2P": "veriti eratis",
                    "3P": "veriti erant"
                },
                "SUBJ": {
                    "1S": "veritus essem",
                    "2S": "veritus esses",
                    "3S": "veritus esset",
                    "1P": "veriti essemus",
                    "2P": "veriti essetis",
                    "3P": "veriti essent"
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
                    "1S": "verebor",
                    "2S": "vereberis",
                    "3S": "verebitur",
                    "1P": "verebimur",
                    "2P": "verebimini",
                    "3P": "verebuntur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "veretor",
                    "3S": "veretor",
                    "1P": None,
                    "2P": None,
                    "3P": "verentor"
                },
                "INFN": "veriturus esse",
                "PTCP": decline212("veriturus")
                },
            "PAS": {
                "INDC": EMPTY_INFLECTION,
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": decline212("verendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "veritus ero",
                    "2S": "veritus eris",
                    "3S": "veritus erit",
                    "1P": "veriti erimus",
                    "2P": "veriti eritis",
                    "3P": "veriti erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            }
        },
    "LOQUOR": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "loquor",
                    "2S": "loqueris",
                    "3S": "loquitur",
                    "1P": "loquimur",
                    "2P": "loquimini",
                    "3P": "loquuntur"
                },
                "SUBJ": {
                    "1S": "loquar",
                    "2S": "loquaris",
                    "3S": "loquatur",
                    "1P": "loquamur",
                    "2P": "loquamini",
                    "3P": "loquantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "loquere",
                    "3S": None,
                    "1P": None,
                    "2P": "loquimini",
                    "3P": None
                },
                "INFN": "loqui",
                "PTCP": decline33_i("loquens", "loquentis")
                },
            "PAS": EMPTY_VOICE,
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "loquebar",
                    "2S": "loquebaris",
                    "3S": "loquebatur",
                    "1P": "loquebamur",
                    "2P": "loquebamini",
                    "3P": "loquebantur"
                },
                "SUBJ": {
                    "1S": "loquerer",
                    "2S": "loquereris",
                    "3S": "loqueretur",
                    "1P": "loqueremur",
                    "2P": "loqueremini",
                    "3P": "loquerentur"
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
                    "1S": "locutus sum",
                    "2S": "locutus es",
                    "3S": "locutus est",
                    "1P": "locuti sumus",
                    "2P": "locuti estis",
                    "3P": "locuti sunt"
                },
                "SUBJ": {
                    "1S": "locutus sim",
                    "2S": "locutus sis",
                    "3S": "locutus sit",
                    "1P": "locuti simus",
                    "2P": "locuti sitis",
                    "3P": "locuti sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "locutus esse",
                "PTCP": decline212("locutus")
                },
            "PAS": EMPTY_VOICE,
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "locutus eram",
                    "2S": "locutus eras",
                    "3S": "locutus erat",
                    "1P": "locuti eramus",
                    "2P": "locuti eratis",
                    "3P": "locuti erant"
                },
                "SUBJ": {
                    "1S": "locutus essem",
                    "2S": "locutus esses",
                    "3S": "locutus esset",
                    "1P": "locuti essemus",
                    "2P": "locuti essetis",
                    "3P": "locuti essent"
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
                    "1S": "loquar",
                    "2S": "loqueris",
                    "3S": "loquetur",
                    "1P": "loquemur",
                    "2P": "loquemini",
                    "3P": "loquentur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "loquitor",
                    "3S": "loquitor",
                    "1P": None,
                    "2P": None,
                    "3P": "loquuntor"
                },
                "INFN": "locuturus esse",
                "PTCP": decline212("locuturus")
                },
            "PAS": {
                "INDC": EMPTY_INFLECTION,
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": decline212("loquendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "locutus ero",
                    "2S": "locutus eris",
                    "3S": "locutus erit",
                    "1P": "locuti erimus",
                    "2P": "locuti eritis",
                    "3P": "locuti erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            }
        },
    "PATIOR": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "patior",
                    "2S": "pateris",
                    "3S": "patitur",
                    "1P": "patimur",
                    "2P": "patimini",
                    "3P": "patiuntur"
                },
                "SUBJ": {
                    "1S": "patiar",
                    "2S": "patiaris",
                    "3S": "patiatur",
                    "1P": "patiamur",
                    "2P": "patiamini",
                    "3P": "patiantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "patere",
                    "3S": None,
                    "1P": None,
                    "2P": "patimini",
                    "3P": None
                },
                "INFN": "pati",
                "PTCP": decline33_i("patiens", "patientis")
                },
            "PAS": EMPTY_VOICE,
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "patiebar",
                    "2S": "patiebaris",
                    "3S": "patiebatur",
                    "1P": "patiebamur",
                    "2P": "patiebamini",
                    "3P": "patiebantur"
                },
                "SUBJ": {
                    "1S": "paterer",
                    "2S": "patereris",
                    "3S": "pateretur",
                    "1P": "pateremur",
                    "2P": "pateremini",
                    "3P": "paterentur"
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
                    "1S": "passus sum",
                    "2S": "passus es",
                    "3S": "passus est",
                    "1P": "passi sumus",
                    "2P": "passi estis",
                    "3P": "passi sunt"
                },
                "SUBJ": {
                    "1S": "passus sim",
                    "2S": "passus sis",
                    "3S": "passus sit",
                    "1P": "passi simus",
                    "2P": "passi sitis",
                    "3P": "passi sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "passus esse",
                "PTCP": decline212("passus")
                },
            "PAS": EMPTY_VOICE,
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "passus eram",
                    "2S": "passus eras",
                    "3S": "passus erat",
                    "1P": "passi eramus",
                    "2P": "passi eratis",
                    "3P": "passi erant"
                },
                "SUBJ": {
                    "1S": "passus essem",
                    "2S": "passus esses",
                    "3S": "passus esset",
                    "1P": "passi essemus",
                    "2P": "passi essetis",
                    "3P": "passi essent"
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
                    "1S": "patiar",
                    "2S": "patieris",
                    "3S": "patietur",
                    "1P": "patiemur",
                    "2P": "patiemini",
                    "3P": "patientur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "patitor",
                    "3S": "patitor",
                    "1P": None,
                    "2P": None,
                    "3P": "patiuntor"
                },
                "INFN": "passurus esse",
                "PTCP": decline212("passurus")
                },
            "PAS": {
                "INDC": EMPTY_INFLECTION,
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": decline212("patiendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "passus ero",
                    "2S": "passus eris",
                    "3S": "passus erit",
                    "1P": "passi erimus",
                    "2P": "passi eritis",
                    "3P": "passi erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            }
        },
    "ORIOR": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "orior",
                    "2S": "oriris",
                    "3S": "oritur",
                    "1P": "orimur",
                    "2P": "orimini",
                    "3P": "oriuntur"
                },
                "SUBJ": {
                    "1S": "oriar",
                    "2S": "oriaris",
                    "3S": "oriatur",
                    "1P": "oriamur",
                    "2P": "oriamini",
                    "3P": "oriantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "orire",
                    "3S": None,
                    "1P": None,
                    "2P": "orimini",
                    "3P": None
                },
                "INFN": "oriri",
                "PTCP": decline33_i("oriens", "orientis")
                },
            "PAS": EMPTY_VOICE,
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "oriebar",
                    "2S": "oriebaris",
                    "3S": "oriebatur",
                    "1P": "oriebamur",
                    "2P": "oriebamini",
                    "3P": "oriebantur"
                },
                "SUBJ": {
                    "1S": "orirer",
                    "2S": "orireris",
                    "3S": "oriretur",
                    "1P": "oriremur",
                    "2P": "oriremini",
                    "3P": "orirentur"
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
                    "1S": "ortus sum",
                    "2S": "ortus es",
                    "3S": "ortus est",
                    "1P": "orti sumus",
                    "2P": "orti estis",
                    "3P": "orti sunt"
                },
                "SUBJ": {
                    "1S": "ortus sim",
                    "2S": "ortus sis",
                    "3S": "ortus sit",
                    "1P": "orti simus",
                    "2P": "orti sitis",
                    "3P": "orti sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "ortus esse",
                "PTCP": decline212("ortus")
                },
            "PAS": EMPTY_VOICE,
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "ortus eram",
                    "2S": "ortus eras",
                    "3S": "ortus erat",
                    "1P": "orti eramus",
                    "2P": "orti eratis",
                    "3P": "orti erant"
                },
                "SUBJ": {
                    "1S": "ortus essem",
                    "2S": "ortus esses",
                    "3S": "ortus esset",
                    "1P": "orti essemus",
                    "2P": "orti essetis",
                    "3P": "orti essent"
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
                    "1S": "oriar",
                    "2S": "orieris",
                    "3S": "orietur",
                    "1P": "oriemur",
                    "2P": "oriemini",
                    "3P": "orientur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "oritor",
                    "3S": "oritor",
                    "1P": None,
                    "2P": None,
                    "3P": "oriuntor"
                },
                "INFN": "oriturus esse",
                "PTCP": decline212("oriturus")
                },
            "PAS": {
                "INDC": EMPTY_INFLECTION,
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": decline212("oriendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "ortus ero",
                    "2S": "ortus eris",
                    "3S": "ortus erit",
                    "1P": "orti erimus",
                    "2P": "orti eritis",
                    "3P": "orti erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            }
        },
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
                    "2S": "sis",
                    "3S": "sit",
                    "1P": "simus",
                    "2P": "sitis",
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
                    "2S": "eras",
                    "3S": "erat",
                    "1P": "eramus",
                    "2P": "eratis",
                    "3P": "erant"
                },
                "SUBJ": {
                    "1S": "essem",
                    "2S": "esses",
                    "3S": "esset",
                    "1P": "essemus",
                    "2P": "essetis",
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
                    "1S": "fui",
                    "2S": "fuisti",
                    "3S": "fuit",
                    "1P": "fuimus",
                    "2P": "fuistis",
                    "3P": "fuerunt"
                },
                "SUBJ": {
                    "1S": "fuerim",
                    "2S": "fueris",
                    "3S": "fuerit",
                    "1P": "fuerimus",
                    "2P": "fueritis",
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
                    "2S": "fueras",
                    "3S": "fuerat",
                    "1P": "fueramus",
                    "2P": "fueratis",
                    "3P": "fuerant"
                },
                "SUBJ": {
                    "1S": "fuissem",
                    "2S": "fuisses",
                    "3S": "fuisset",
                    "1P": "fuissemus",
                    "2P": "fuissetis",
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
                    "1S": "ero",
                    "2S": "eris",
                    "3S": "erit",
                    "1P": "erimus",
                    "2P": "eritis",
                    "3P": "erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "esto",
                    "3S": "esto",
                    "1P": None,
                    "2P": "estote",
                    "3P": "sunto"
                },
                "INFN": "futurus esse",  # alternative "fore"
                "PTCP": decline212("futurus")
            },
            "PAS": EMPTY_VOICE
        },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "fuero",
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
    "EO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "eo",
                    "2S": "is",
                    "3S": "it",
                    "1P": "imus",
                    "2P": "itis",
                    "3P": "eunt"
                },
                "SUBJ": {
                    "1S": "eam",
                    "2S": "eas",
                    "3S": "eat",
                    "1P": "eamus",
                    "2P": "eatis",
                    "3P": "eant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "i",
                    "3S": None,
                    "1P": None,
                    "2P": "ite",
                    "3P": None
                },
                "INFN": "ire",
                "PTCP": decline33_i("iens", "euntis")
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "itur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": {
                    "1S": None,
                    "2S": None,
                    "3S": "eatur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "iri",
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "ibam",
                    "2S": "ibas",
                    "3S": "ibat",
                    "1P": "ibamus",
                    "2P": "ibatis",
                    "3P": "ibant"
                },
                "SUBJ": {
                    "1S": "irem",
                    "2S": "ires",
                    "3S": "iret",
                    "1P": "iremus",
                    "2P": "iretis",
                    "3P": "irent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "ibatur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": {
                    "1S": None,
                    "2S": None,
                    "3S": "iretur",
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
                    "1S": "ii",
                    "2S": "iisti",
                    "3S": "iit",
                    "1P": "iimus",
                    "2P": "iistis",
                    "3P": "ierunt"
                },
                "SUBJ": {
                    "1S": "ierim",
                    "2S": "ieris",
                    "3S": "ierit",
                    "1P": "ierimus",
                    "2P": "ieritis",
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
                    "2S": "ieras",
                    "3S": "ierat",
                    "1P": "ieramus",
                    "2P": "ieratis",
                    "3P": "ierant"
                },
                "SUBJ": {
                    "1S": "iissem",
                    "2S": "iisses",
                    "3S": "iisset",
                    "1P": "iissemus",
                    "2P": "iissetis",
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
                    "1S": "ibo",
                    "2S": "ibis",
                    "3S": "ibit",
                    "1P": "ibimus",
                    "2P": "ibitis",
                    "3P": "ibunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "ito",
                    "3S": "ito",
                    "1P": None,
                    "2P": "itote",
                    "3P": "eunto"
                },
                "INFN": "iturus esse",
                "PTCP": decline212("iturus")
                },
            "PAS": {
                "INDC": {
                    "1S": None,
                    "2S": None,
                    "3S": "ibitur",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": None,
                    "3S": "itor",
                    "1P": None,
                    "2P": None,
                    "3P": None
                },
                "INFN": "itus iri",
                "PTCP": decline212("eundus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "iero",
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
    "FERO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "fero",
                    "2S": "fers",
                    "3S": "fert",
                    "1P": "ferimus",
                    "2P": "fertis",
                    "3P": "ferunt"
                },
                "SUBJ": {
                    "1S": "feram",
                    "2S": "feras",
                    "3S": "ferat",
                    "1P": "feramus",
                    "2P": "feratis",
                    "3P": "ferant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "fer",
                    "3S": None,
                    "1P": None,
                    "2P": "ferte",
                    "3P": None
                },
                "INFN": "ferre",
                "PTCP": decline33_i("ferens", "ferentis")
                },
            "PAS": {
                "INDC": {
                    "1S": "feror",
                    "2S": "ferris",
                    "3S": "fertur",
                    "1P": "ferimur",
                    "2P": "ferimini",
                    "3P": "feruntur"
                },
                "SUBJ": {
                    "1S": "ferar",
                    "2S": "feraris",
                    "3S": "feratur",
                    "1P": "feramur",
                    "2P": "feramini",
                    "3P": "ferantur"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "ferre",
                    "3S": None,
                    "1P": None,
                    "2P": "ferimini",
                    "3P": None
                },
                "INFN": "ferri",
                "PTCP": EMPTY_PARTICIPLE
                },
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "ferebam",
                    "2S": "ferebas",
                    "3S": "ferebat",
                    "1P": "ferebamus",
                    "2P": "ferebatis",
                    "3P": "ferebant"
                },
                "SUBJ": {
                    "1S": "ferrem",
                    "2S": "ferres",
                    "3S": "ferret",
                    "1P": "ferremus",
                    "2P": "ferretis",
                    "3P": "ferrent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "ferebar",
                    "2S": "ferebaris",
                    "3S": "ferebatur",
                    "1P": "ferebamur",
                    "2P": "ferebamini",
                    "3P": "ferebantur"
                },
                "SUBJ": {
                    "1S": "ferrer",
                    "2S": "ferreris",
                    "3S": "ferretur",
                    "1P": "ferremur",
                    "2P": "ferremini",
                    "3P": "ferrentur"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "tuli",
                    "2S": "tulisti",
                    "3S": "tulit",
                    "1P": "tulimus",
                    "2P": "tulistis",
                    "3P": "tulerunt"
                },
                "SUBJ": {
                    "1S": "tulerim",
                    "2S": "tuleris",
                    "3S": "tulerit",
                    "1P": "tulerimus",
                    "2P": "tuleritis",
                    "3P": "tulerint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "tulisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "latus sum",
                    "2S": "latus es",
                    "3S": "latus est",
                    "1P": "lati sumus",
                    "2P": "lati estis",
                    "3P": "lati sunt"
                },
                "SUBJ": {
                    "1S": "latus sim",
                    "2S": "latus sis",
                    "3S": "latus sit",
                    "1P": "lati simus",
                    "2P": "lati sitis",
                    "3P": "lati sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "latus esse",
                "PTCP": decline212("latus")
                }
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "tuleram",
                    "2S": "tuleras",
                    "3S": "tulerat",
                    "1P": "tuleramus",
                    "2P": "tuleratis",
                    "3P": "tulerant"
                },
                "SUBJ": {
                    "1S": "tulissem",
                    "2S": "tulisses",
                    "3S": "tulisset",
                    "1P": "tulissemus",
                    "2P": "tulissetis",
                    "3P": "tulissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "latus eram",
                    "2S": "latus eras",
                    "3S": "latus erat",
                    "1P": "lati eramus",
                    "2P": "lati eratis",
                    "3P": "lati erant"
                },
                "SUBJ": {
                    "1S": "latus essem",
                    "2S": "latus esses",
                    "3S": "latus esset",
                    "1P": "lati essemus",
                    "2P": "lati essetis",
                    "3P": "lati essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "feram",
                    "2S": "feres",
                    "3S": "feret",
                    "1P": "feremus",
                    "2P": "feretis",
                    "3P": "ferent"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "ferto",
                    "3S": "ferto",
                    "1P": None,
                    "2P": "fertote",
                    "3P": "ferunto"
                },
                "INFN": "laturus esse",
                "PTCP": decline212("laturus")
                },
            "PAS": {
                "INDC": {
                    "1S": "ferar",
                    "2S": "fereris",
                    "3S": "feretur",
                    "1P": "feremur",
                    "2P": "feremini",
                    "3P": "ferentur"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "fertor",
                    "3S": "fertor",
                    "1P": None,
                    "2P": None,
                    "3P": "feruntor"
                },
                "INFN": "latus iri",
                "PTCP": decline212("ferendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "tulero",
                    "2S": "tuleris",
                    "3S": "tulerit",
                    "1P": "tulerimus",
                    "2P": "tuleritis",
                    "3P": "tulerint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "latus ero",
                    "2S": "latus eris",
                    "3S": "latus erit",
                    "1P": "lati erimus",
                    "2P": "lati eritis",
                    "3P": "lati erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        },
    "VOLO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "volo",
                    "2S": "vis",
                    "3S": "vult",
                    "1P": "volumus",
                    "2P": "vultis",
                    "3P": "volunt"
                },
                "SUBJ": {
                    "1S": "velim",
                    "2S": "velis",
                    "3S": "velit",
                    "1P": "velimus",
                    "2P": "velitis",
                    "3P": "velint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "velle",  # vella?
                "PTCP": decline33_i("volens", "volentis")
                },
            "PAS": EMPTY_VOICE
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "volebam",
                    "2S": "volebas",
                    "3S": "volebat",
                    "1P": "volebamus",
                    "2P": "volebatis",
                    "3P": "volebant"
                },
                "SUBJ": {
                    "1S": "vellem",
                    "2S": "velles",
                    "3S": "vellet",
                    "1P": "vellemus",
                    "2P": "velletis",
                    "3P": "vellent"
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
                    "1S": "volui",
                    "2S": "voluisti",
                    "3S": "voluit",
                    "1P": "voluimus",
                    "2P": "voluistis",
                    "3P": "voluerunt"
                },
                "SUBJ": {
                    "1S": "voluerim",
                    "2S": "volueris",
                    "3S": "voluerit",
                    "1P": "voluerimus",
                    "2P": "volueritis",
                    "3P": "voluerint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "voluisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "volueram",
                    "2S": "volueras",
                    "3S": "voluerat",
                    "1P": "volueramus",
                    "2P": "volueratis",
                    "3P": "voluerant"
                },
                "SUBJ": {
                    "1S": "voluissem",
                    "2S": "voluisses",
                    "3S": "voluisset",
                    "1P": "voluissemus",
                    "2P": "voluissetis",
                    "3P": "voluissent"
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
                    "1S": "volam",
                    "2S": "voles",
                    "3S": "volet",
                    "1P": "volemus",
                    "2P": "voletis",
                    "3P": "volent"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "voluero",
                    "2S": "volueris",
                    "3S": "voluerit",
                    "1P": "voluerimus",
                    "2P": "volueritis",
                    "3P": "voluerint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": EMPTY_VOICE
            }
        },
    "FACIO": {
        "PRES": {
            "ACT": {
                "INDC": {
                    "1S": "facio",
                    "2S": "facis",
                    "3S": "facit",
                    "1P": "facimus",
                    "2P": "facitis",
                    "3P": "faciunt"
                },
                "SUBJ": {
                    "1S": "faciam",
                    "2S": "facias",
                    "3S": "faciat",
                    "1P": "faciamus",
                    "2P": "faciatis",
                    "3P": "faciant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "fac",
                    "3S": None,
                    "1P": None,
                    "2P": "facite",
                    "3P": None
                },
                "INFN": "facere",
                "PTCP": decline33_i("faciens", "facientis")
                },
            "PAS": {
                "INDC": {
                    "1S": "fio",
                    "2S": "fis",
                    "3S": "fit",
                    "1P": "fimus",
                    "2P": "fitis",
                    "3P": "fiunt"
                },
                "SUBJ": {
                    "1S": "fiam",
                    "2S": "fias",
                    "3S": "fiat",
                    "1P": "fiamus",
                    "2P": "fiatis",
                    "3P": "fiant"
                },
                "IMPT": {
                    "1S": None,
                    "2S": "fi",
                    "3S": None,
                    "1P": None,
                    "2P": "fite",
                    "3P": None
                },
                "INFN": "fieri",
                "PTCP": decline33_i("fiens", "fientis")
                },
            },
        "IMPF": {
            "ACT": {
                "INDC": {
                    "1S": "faciebam",
                    "2S": "faciebas",
                    "3S": "faciebat",
                    "1P": "faciebamus",
                    "2P": "faciebatis",
                    "3P": "faciebant"
                },
                "SUBJ": {
                    "1S": "facerem",
                    "2S": "faceres",
                    "3S": "faceret",
                    "1P": "faceremus",
                    "2P": "faceretis",
                    "3P": "facerent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "fiebam",
                    "2S": "fiebas",
                    "3S": "fiebat",
                    "1P": "fiebamus",
                    "2P": "fiebatis",
                    "3P": "fiebant"
                },
                "SUBJ": {
                    "1S": "fierem",
                    "2S": "fieres",
                    "3S": "fieret",
                    "1P": "fieremus",
                    "2P": "fieretis",
                    "3P": "fierent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "PERF": {
            "ACT": {
                "INDC": {
                    "1S": "feci",
                    "2S": "fecisti",
                    "3S": "fecit",
                    "1P": "fecimus",
                    "2P": "fecistis",
                    "3P": "fecerunt"
                },
                "SUBJ": {
                    "1S": "fecerim",
                    "2S": "feceris",
                    "3S": "fecerit",
                    "1P": "fecerimus",
                    "2P": "feceritis",
                    "3P": "fecerint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "fecisse",
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "factus sum",
                    "2S": "factus es",
                    "3S": "factus est",
                    "1P": "facti sumus",
                    "2P": "facti estis",
                    "3P": "facti sunt"
                },
                "SUBJ": {
                    "1S": "factus sim",
                    "2S": "factus sis",
                    "3S": "factus sit",
                    "1P": "facti simus",
                    "2P": "facti sitis",
                    "3P": "facti sint"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": "factus esse",
                "PTCP": decline212("factus")
                }
            },
        "PLPF": {
            "ACT": {
                "INDC": {
                    "1S": "feceram",
                    "2S": "feceras",
                    "3S": "fecerat",
                    "1P": "feceramus",
                    "2P": "feceratis",
                    "3P": "fecerant"
                },
                "SUBJ": {
                    "1S": "fecissem",
                    "2S": "fecisses",
                    "3S": "fecisset",
                    "1P": "fecissemus",
                    "2P": "fecissetis",
                    "3P": "fecissent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "factus eram",
                    "2S": "factus eras",
                    "3S": "factus erat",
                    "1P": "facti eramus",
                    "2P": "facti eratis",
                    "3P": "facti erant"
                },
                "SUBJ": {
                    "1S": "factus essem",
                    "2S": "factus esses",
                    "3S": "factus esset",
                    "1P": "facti essemus",
                    "2P": "facti essetis",
                    "3P": "facti essent"
                },
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            },
        "FUTR": {
            "ACT": {
                "INDC": {
                    "1S": "faciam",
                    "2S": "facies",
                    "3S": "faciet",
                    "1P": "faciemus",
                    "2P": "facietis",
                    "3P": "facient"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "facito",
                    "3S": "facito",
                    "1P": None,
                    "2P": "facitote",
                    "3P": "faciunto"
                },
                "INFN": "facturus esse",
                "PTCP": decline212("facturus")
                },
            "PAS": {
                "INDC": {
                    "1S": "fiam",
                    "2S": "fies",
                    "3S": "fiet",
                    "1P": "fiemus",
                    "2P": "fietis",
                    "3P": "fient"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": {
                    "1S": None,
                    "2S": "fito",
                    "3S": "fito",
                    "1P": None,
                    "2P": "fitote",
                    "3P": "fiunto"
                },
                "INFN": "factus iri",
                "PTCP": decline212("faciendus")
                }
            },
        "FTPF": {
            "ACT": {
                "INDC": {
                    "1S": "fecero",
                    "2S": "feceris",
                    "3S": "fecerit",
                    "1P": "fecerimus",
                    "2P": "feceritis",
                    "3P": "fecerint"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                },
            "PAS": {
                "INDC": {
                    "1S": "factus ero",
                    "2S": "factus eris",
                    "3S": "factus erit",
                    "1P": "facti erimus",
                    "2P": "facti eritis",
                    "3P": "facti erunt"
                },
                "SUBJ": EMPTY_INFLECTION,
                "IMPT": EMPTY_INFLECTION,
                "INFN": None,
                "PTCP": EMPTY_PARTICIPLE
                }
            }
        }
    }

# nouns
NOUNS = {
    "PUELLA": {
        "NOM": {
            "SG": "puella",
            "PL": "puellae"
        },
        "VOC": {
            "SG": "puella",
            "PL": "puellae"
        },
        "ACC": {
            "SG": "puellam",
            "PL": "puellas"
        },
        "GEN": {
            "SG": "puellae",
            "PL": "puellarum"
        },
        "DAT": {
            "SG": "puellae",
            "PL": "puellis"
        },
        "ABL": {
            "SG": "puella",
            "PL": "puellis"
        }           
    },
    "FILIA": {
        "NOM": {
            "SG": "filia",
            "PL": "filiae"
        },
        "VOC": {
            "SG": "filia",
            "PL": "filiae"
        },
        "ACC": {
            "SG": "filiam",
            "PL": "filias"
        },
        "GEN": {
            "SG": "filiae",
            "PL": "filiarum"
        },
        "DAT": {
            "SG": "filiae",
            "PL": "filiabus"
        },
        "ABL": {
            "SG": "filia",
            "PL": "filiabus"
        }           
    },
    "SERVUS": {
        "NOM": {
            "SG": "servus",
            "PL": "servi"
        },
        "VOC": {
            "SG": "serve",
            "PL": "servi"
        },
        "ACC": {
            "SG": "servum",
            "PL": "servos"
        },
        "GEN": {
            "SG": "servi",
            "PL": "servorum"
        },
        "DAT": {
            "SG": "servo",
            "PL": "servis"
        },
        "ABL": {
            "SG": "servo",
            "PL": "servis"
        }           
    },
    "BELLUM": {
        "NOM": {
            "SG": "bellum",
            "PL": "bella"
        },
        "VOC": {
            "SG": "bellum",
            "PL": "bella"
        },
        "ACC": {
            "SG": "bellum",
            "PL": "bella"
        },
        "GEN": {
            "SG": "belli",
            "PL": "bellorum"
        },
        "DAT": {
            "SG": "bello",
            "PL": "bellis"
        },
        "ABL": {
            "SG": "bello",
            "PL": "bellis"
        }           
    },
    "REX": {
        "NOM": {
            "SG": "rex",
            "PL": "reges"
        },
        "VOC": {
            "SG": "rex",
            "PL": "reges"
        },
        "ACC": {
            "SG": "regem",
            "PL": "reges"
        },
        "GEN": {
            "SG": "regis",
            "PL": "regum"
        },
        "DAT": {
            "SG": "regi",
            "PL": "regibus"
        },
        "ABL": {
            "SG": "rege",
            "PL": "regibus"
        }           
    },
    "NAVIS": {
        "NOM": {
            "SG": "navis",
            "PL": "naves"
        },
        "VOC": {
            "SG": "navis",
            "PL": "naves"
        },
        "ACC": {
            "SG": "navem",
            "PL": "naves"
        },
        "GEN": {
            "SG": "navis",
            "PL": "navium"
        },
        "DAT": {
            "SG": "navi",
            "PL": "navibus"
        },
        "ABL": {
            "SG": "nave",
            "PL": "navibus"
        }           
    },
    "NOMEN": {
        "NOM": {
            "SG": "nomen",
            "PL": "nomina"
        },
        "VOC": {
            "SG": "nomen",
            "PL": "nomina"
        },
        "ACC": {
            "SG": "nomen",
            "PL": "nomina"
        },
        "GEN": {
            "SG": "nominis",
            "PL": "nominum"
        },
        "DAT": {
            "SG": "nomini",
            "PL": "nominibus"
        },
        "ABL": {
            "SG": "nomine",
            "PL": "nominibus"
        }           
    },
    "ANIMAL": {
        "NOM": {
            "SG": "animal",
            "PL": "animalia"
        },
        "VOC": {
            "SG": "animal",
            "PL": "animalia"
        },
        "ACC": {
            "SG": "animal",
            "PL": "animalia"
        },
        "GEN": {
            "SG": "animalis",
            "PL": "animalium"
        },
        "DAT": {
            "SG": "animali",
            "PL": "animalibus"
        },
        "ABL": {
            "SG": "animale",
            "PL": "animalibus"
        }           
    },
    "MANUS": {
        "NOM": {
            "SG": "manus",
            "PL": "manus"
        },
        "VOC": {
            "SG": "manus",
            "PL": "manus"
        },
        "ACC": {
            "SG": "manum",
            "PL": "manus"
        },
        "GEN": {
            "SG": "manus",
            "PL": "manuum"
        },
        "DAT": {
            "SG": "manui",
            "PL": "manibus"
        },
        "ABL": {
            "SG": "manu",
            "PL": "manibus"
        }           
    },
    "GENU": {
        "NOM": {
            "SG": "genu",
            "PL": "genua"
        },
        "VOC": {
            "SG": "genu",
            "PL": "genua"
        },
        "ACC": {
            "SG": "genu",
            "PL": "genua"
        },
        "GEN": {
            "SG": "genus",
            "PL": "genuum"
        },
        "DAT": {
            "SG": "genu",
            "PL": "genibus"
        },
        "ABL": {
            "SG": "genu",
            "PL": "genibus"
        }           
    },
    "RES": {
        "NOM": {
            "SG": "res",
            "PL": "res"
        },
        "VOC": {
            "SG": "res",
            "PL": "res"
        },
        "ACC": {
            "SG": "rem",
            "PL": "res"
        },
        "GEN": {
            "SG": "rei",
            "PL": "rerum"
        },
        "DAT": {
            "SG": "rei",
            "PL": "rebus"
        },
        "ABL": {
            "SG": "re",
            "PL": "rebus"
        }           
    }
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



