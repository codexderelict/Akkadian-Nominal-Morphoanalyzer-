### INTRODUCTION

Well, hello! Welcome to V1.1 of the Akkadian Nominal Morphoanalyzer, or Akkadian Noun Morphoanalyzer, ANM for short. For those unfamiliar, this is an application/program I made to analyze Akkadian nouns, obviously. When a noun is inputted, information on the noun is outputted. For those unfamiliar with Akkadian, it's an ancient Semitic language spoken in Mesopotamia, which mainly comprises Iraq in the modern day. It was the language of the Akkadian Empire, the first known imperial state, as well as the language of the Code of Hammurabi.  

In fact, I may give this a fun name like Bashmu, named after the Mesopotamian snake god (since it's written in Python). I may also add a Sumerogram as the favicon, the one for "snake" (𒈲, can you see it?)  

One issue I'm facing is disambiguating status absolutus from constructus, which can only be done syntactically if there's multiple words and would require more than just regexes (i.e. the backbone of the project). Right now, it's written as "abs/con", since it could be both.  

### REQUIREMENTS
Python 3.13  
FreeSimpleGUI/PySimpleGUI  
Cursory knowledge of Akkadian (or Semitic more generally) noun morphology  
### HOW TO USE
Run main.py, and you'll be greeted with the GUI. Input the noun in the text prompt (in Latin characters, no cuneiform support, sorry!), and click "Analyze". You'll then see the noun's information below: case (nominative, accusative or genitive), gender (masculine, feminine), number (singular, dual, plural), and state (rectus, absolutus/constructus, or in English, governed, absolute/construct).  
### WHAT'S NEW 
A half-baked state analysis system! Well, maybe 3/4ths baked, since the absolute state is not often used. That's it! 
### POTENTIAL IMPROVEMENTS
Support for two words instead of just one  
The use of said two words to disambiguate status absolutus from constructus  
To that end, a VERY small Minimalistic syntax system (as in Chomskyan minimalism, with a capital M) to merge two nouns and analyze their relationship (no Move nor Agree, sorry!)    
