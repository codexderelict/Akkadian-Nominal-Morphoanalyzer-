import re 
from noun_patterns import patterns 
class Noun:
    patterns = patterns
    def __init__(self, noun):
        self.noun = noun 
        self.gender, self.number, self.case, self.state = Noun.get_features(noun)
    @classmethod
    def get_features(cls, noun):
        for pattern, (gender, number, case, state) in cls.patterns.items(): # A tuple? Cool! 
            if re.search(pattern, noun):
                gender, number, case, state = cls.patterns[pattern]
                return gender, number, case, state
        return None, None, None, None
