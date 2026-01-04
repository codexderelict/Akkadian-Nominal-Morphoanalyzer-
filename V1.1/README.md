### REQUIREMENTS
Python 3.13  
FreeSimpleGUI/PySimpleGUI  
Cursory knowledge of Akkadian (or Semitic more generally) noun morphology  
### HOW IT WORKS
It is a purely rule-based analyzer, that does not rely on probabilistic parsing or neural techniques. It only uses regular expressions and pattern matching. When a word is inputted in the GUI (in Latin characters and not cuneiform) and one clicks "Analyze" (in main.py), an instance of the Noun class is created, and the engine (akkadian_engine.py) loops through the dictionary of regex patterns (noun_patterns.py), and when a match is found, the value of the matched key, the regex pattern, is returned as a 4-tuple of noun, case, gender, and state as the attributes of the Noun object. If there is no match, it returns a 4-tuple of None.

The regular expressions function as suffix checks, and so each end with the end-of-string symbol. For example, if a word ends with "um" or "u" (without mimation) that is not preceded by "t", it's known to be in the masculine singular nominative, for example. The regex pattern for that is "[^t]um?$".
### CONTEXT
Akkadian is an ancient East Semitic language formerly spoken in Mesopotamia from about the 2nd millennium BC to the 5th century BC. It was the language of the Akkadian Empire, often considered the first known imperial regime, and the subsequent Mesopotamian empires (Old and Middle Assyrian empires, Babylonia, and the early Neo-Assyrian empire). when Aramaic was included as a language of government around the 8th century BC, the Akkadian language's use slowly dwindled. It is the language used for the Code of Hammurabi, one of the earliest legal codes written as well as the language of the Epic of Gilgamesh, the oldest surviving great work of literature.

As a Semitic language, it has many of the same features as others; non-concatenative root and stem based morphology, 3 cases (which Arabic conserved, unlike Aramaic and Hebrew), a state system (with three states, governed, absolute and construct, though the absolute was less used), two genders (masculine and feminine) with the marking for feminine being a -t suffix (just like Arabic and to a lesser extent Hebrew). I chose it precisely because it retained many of the interesting features of Semitic languages, while not being comparatively difficult to work with. Classical/MS Arabic and Biblical Hebrew grammar would require a lot more work, and I wanted a proof of concept.

### WHAT'S NEW 
The addition of state analysis (governed, absolute, construct)
### POTENTIAL IMPROVEMENTS
Support for two words instead of just one  
Tree-based constituency mini-parser for valency/head marking in order to disambiguate the absolute and construct states. What I have in mind is this small CFG:  

S  => NP  

NP => N[state=governed] N[state=absolute]  
Where the first noun is a subject and the latter is a predicate.  

NP => N[state=construct] N[state=governed, case=gen]  
Where the relation is of possession, hence the genitive case.   

### CONTACT
If you'd like to critique my code or just talk, my email is codexderelict@proton.me.
