## INTRODUCTION  

This is version 2.0 of my Akkadian noun analyzer. I numbered it V2.0 because it's the first version that went beyond the plans I had originally set for it, which was a small regex-based analyzer for single nouns with no syntax. However, because state disambiguation is syntactic, I implemented a small constraint-based noun-phrase level state disambiguator with it, as both the absolute and construct states are zero suffixed. So, if the noun to be disambiguated is in the absolute, it must be a predicate and preceded by a noun in the governed state. If the noun is a construct noun, it must be possessed, and so proceeded by a noun in the genitive.  

Furthermore, the regular expressions were originally such that just typing in a suffix like "tum" on its own would be analyzed normally. Now, they must function like suffixes and be preceded by at least one character (\w+).  

## CONTEXT  

Akkadian is an ancient East Semitic language formerly spoken in Mesopotamia from about the 2nd millennium BC to the 5th century BC. It was the language of the Akkadian Empire, often considered the first known imperial regime, and the subsequent Mesopotamian empires (Old and Middle Assyrian empires, Babylonia, and the early Neo-Assyrian empire). when Aramaic was included as a language of government around the 8th century BC, the Akkadian language's use slowly dwindled. It is the language used for the Code of Hammurabi, one of the earliest legal codes written as well as the language of the Epic of Gilgamesh, the oldest surviving great work of literature.  

As a Semitic language, it has many of the same features as others; non-concatenative root and stem based morphology, 3 cases (which Arabic conserved, unlike Aramaic and Hebrew), a state system (with three states, governed, absolute and construct, though the absolute was less used), two genders (masculine and feminine) with the marking for feminine being a -t suffix (just like Arabic and to a lesser extent Hebrew). I chose it precisely because it retained many of the interesting features of Semitic languages, while not being comparatively difficult to work with. Classical/MS Arabic and Biblical Hebrew grammar would require a lot more work, and I wanted a proof of concept.  

## WHAT'S NEW   
Support for two nouns, not just one  
Noun-phrase level disambiguation between the absolute and construct states  
Suffix regexes must be preceded by at least one letter   

## POTENTIAL ADDITIONS:
Probabilistic parsing/analysis
Support for other Semitic languages 

### REQUIREMENTS
Python 3.13  
FreeSimpleGUI/PySimpleGUI  
Cursory knowledge of Akkadian (or Semitic more generally) noun morphology  

## HOW TO USE
Run main.py, and you'll be presented with a GUI with a text-field with a button labeled "Analyze" after it. Input a maximum of two nouns. When you click "Analyze", you will find the noun(s)' case, number, gender and state.

## CONTACT  
My email is codexderelict@proton.me, and I respond to any message and don't mind messages of any nature. 
