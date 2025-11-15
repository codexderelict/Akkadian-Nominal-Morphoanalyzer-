This is a rule-based Akkadian nominal morphoanalyzer that is currently in the prototype stage. I worked on this first version while feeling sick and sleep-deprived, so it's not exactly the best. This is my very first computational linguistics project, and I hope for the more complete version to be my CS50P final. I've only done number, case and gender for now, but states, roots and stems are on the way. 

I chose Akkadian mainly for its simplicity. Its noun system is one of the easiest in the Semitic realm for its agglutinative quality alongside the more traditional non-concatenative morphology of Semitic languages (possibly something from Sumerian influence?). I hope for this to be a launchpad to work on other Semitic languages, especially Arabic, my native language, but I'm also interested in maybe working on similar projects for Ge'ez, Syriac or Biblical Hebrew. These will, however, require a lot more transformation rules than this. 
How this version works:
Run the Python program. It asks you to input an Akkadian noun, then returns the number, case and gender. Simple as that, I guess. 
Future additions:
A simple GUI with PySimpleGUI (what an accurate name!)
More robust analysis of roots, stems, and states using regular expressions
An executable form with PyInstaller
Feature-state OOP with case, number, state, gender, root and stem as self attributes
Possibly probabilistic analysis, but I'm not sure if Akkadian needs it. 
Thanks go out to:
Jeff Benner and his Ancient Hebrew Research Center, looking through the site when I was a child was partly what made me appreciate Semitic languages as a native Arabic speaker
Simon Ager and Omniglot, another site about languages that I spent ages looking through when I was a kid
My parents, for their speaking German intrigued me and got me to study language and linguistics... also for making me but that's another thing.
All of my friends, for being my friends and that
