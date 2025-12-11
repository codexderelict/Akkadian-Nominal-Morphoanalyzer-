import re 
from noun_patterns import patterns 
class Noun:
    patterns = patterns
    def __init__(self, noun):
        self.noun = noun 
        self.gender, self.number, self.case = Noun.get_features(noun)
    @classmethod
    def get_features(cls, noun):
        for pattern, (gender, number, case) in cls.patterns.items(): # Mane, you gotta do that! 
            if re.search(pattern, noun):
                gender, number, case = cls.patterns[pattern]
                return gender, number, case 
        return None, None, None
