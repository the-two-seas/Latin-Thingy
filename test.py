# functions
def decline212(word: str) -> dict[str, dict[str, dict[str, str]]]:
    stem = word[:-2]
    return {
        "masculine": {
            "nominative": {
                "singular": stem + "us",
                "plural": stem + "i"
            },
            "vocative": {
                "singular": stem + "e",
                "plural": stem + "i"
            },
            "accusative": {
                "singular": stem + "um",
                "plural": stem + "os"
            },
            "genitive": {
                "singular": stem + "i",
                "plural": stem + "orum"
            },
            "dative": {
                "singular": stem + "o",
                "plural": stem + "is"
            },
            "ablative": {
                "singular": stem + "o",
                "plural": stem + "is"
            }
        },
        "feminine": {
            "nominative": {
                "singular": stem + "a",
                "plural": stem + "ae"
            },
            "vocative": {
                "singular": stem + "a",
                "plural": stem + "ae"
            },
            "accusative": {
                "singular": stem + "am",
                "plural": stem + "as"
            },
            "genitive": {
                "singular": stem + "ae",
                "plural": stem + "arum"
            },
            "dative": {
                "singular": stem + "ae",
                "plural": stem + "is"
            },
            "ablative": {
                "singular": stem + "a",
                "plural": stem + "is"
            }
        },
        "neuter": {
            "nominative": {
                "singular": stem + "um",
                "plural": stem + "a"
            },
            "vocative": {
                "singular": stem + "um",
                "plural": stem + "a"
            },
            "accusative": {
                "singular": stem + "um",
                "plural": stem + "a"
            },
            "genitive": {
                "singular": stem + "i",
                "plural": stem + "orum"
            },
            "dative": {
                "singular": stem + "o",
                "plural": stem + "is"
            },
            "ablative": {
                "singular": stem + "o",
                "plural": stem + "is"
            }
        }
    }
def decline33_i(word: str, gen: str) -> dict[str, dict[str, dict[str, str]]]:
    stem = gen[:-2]
    return {
        "masculine": {
            "nominative": {
                "singular": word,
                "plural": stem + "es"
            },
            "vocative": {
                "singular": word,
                "plural": stem + "es"
            },
            "accusative": {
                "singular": stem + "em",
                "plural": stem + "es"
            },
            "genitive": {
                "singular": stem + "is",
                "plural": stem + "ium"
            },
            "dative": {
                "singular": stem + "i",
                "plural": stem + "ibus"
            },
            "ablative": {
                "singular": stem + "e",
                "plural": stem + "ibus"
            }
        },
        "feminine": {
            "nominative": {
                "singular": word,
                "plural": stem + "es"
            },
            "vocative": {
                "singular": word,
                "plural": stem + "es"
            },
            "accusative": {
                "singular": stem + "em",
                "plural": stem + "es"
            },
            "genitive": {
                "singular": stem + "is",
                "plural": stem + "ium"
            },
            "dative": {
                "singular": stem + "i",
                "plural": stem + "ibus"
            },
            "ablative": {
                "singular": stem + "e",
                "plural": stem + "ibus"
            }
        },
        "neuter": {
            "nominative": {
                "singular": word,
                "plural": stem + "ia"
            },
            "vocative": {
                "singular": word,
                "plural": stem + "ia"
            },
            "accusative": {
                "singular": word,
                "plural": stem + "ia"
            },
            "genitive": {
                "singular": stem + "is",
                "plural": stem + "ium"
            },
            "dative": {
                "singular": stem + "i",
                "plural": stem + "ibus"
            },
            "ablative": {
                "singular": stem + "e",
                "plural": stem + "ibus"
            }
        } 
    }
def inflection(s1, s2, s3, p1, p2, p3) -> dict[str, str]:
    return {
        "1s": s1,
        "2s": s2,
        "3s": s3,
        "1p": p1,
        "2p": p2,
        "3p": p3
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


# empty stuff
EMPTY_PARTICIPLE = {
    gender: {
        case: {"singular": None, "plural": None}
        for case in ["nominative", "vocative", "accusative", "genitive", "dative", "ablative"]
    }
    for gender in ["masculine", "feminine", "neuter"]
}
EMPTY_INFLECTION = {
    person: None
    for person in ["1s", "2s", "3s", "1p", "2p", "3p"]
}
EMPTY_VOICE = {
    "indicative": EMPTY_INFLECTION,
    "subjunctive": EMPTY_INFLECTION,
    "imperative": EMPTY_INFLECTION,
    "infinitive": None,
    "participle": EMPTY_PARTICIPLE
}
EMPTY = [EMPTY_PARTICIPLE, EMPTY_INFLECTION, EMPTY_VOICE, None]
# verbs
DEPONENTS = ["conor", "vereor", "loquor", "patior", "orior"]


def verb(pres: str | None = None, inf: str | None = None, perf: str | None = None, ppp: str | None = None) -> dict:
    # general
    transitivity = bool(ppp)  # a verb is transitive if it takes a direct object, :. if it can be passive
    

    if (pres[-1], inf[-1], perf[-6:], ppp) == ("r", "i", "us sum", None): kind = "deponent"
    elif (pres[-1], inf[-2:], perf[-1], ppp[-2:]) == ("o", "re", "i", "us"): kind = "regular"
    elif (pres[-1], inf[-2:], perf[-6:], ppp) == ("o", "re", "us sum", None): kind = "semideponent"
    elif (pres[-1], inf[-4:], perf, ppp) == ("i", "isse", None, None): kind = "defective"
    else: raise ValueError

    


verb("amo", "amare", "amavi", "amatus")
