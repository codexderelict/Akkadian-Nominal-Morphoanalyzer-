patterns = {
    r"[^t]um?$": ["masc", "sg", "nom"],
    r"[^t]im?$": ["masc", "sg", "gen"],
    r"[^t]am?$": ["masc", "sg", "acc"],
    r"[^t][āa]n":["masc", "dual", "nom"],
    r"[^t][īi]n":["masc", "dual", "obl"],
    r"[^t]ū$":["masc", "pl", "nom"],
    r"[^t]ī$":["masc", "pl", "obl"],
    r"[^āīē]tum?$": ["fem", "sg", "nom"],
    r"[^āīē]tim?$": ["fem", "sg", "gen"],
    r"[^āīē]tam?$": ["fem", "sg", "acc"],
    r"t[āa]n$":["fem", "dual", "nom"],
    r"t[īi]n$":["fem", "dual", "obl"],
    r"[āīē]tum?$": ["fem", "pl", "nom"],
    r"[āīē]tim?$": ["fem", "pl", "obl"]
    
}