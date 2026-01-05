from akkadian_engine import Noun 
class NounPhrase:
    def __init__(self, noun1, noun2):
        self.noun1 = noun1
        self.noun2 = noun2
    def disambiguate(self):
        if not (self.noun1.valid and self.noun2.valid):
            return
        if self.noun1.state == "rect" and self.noun2.state == "abs/con":
            self.noun2.state = "abs"
        elif self.noun1.state == "abs/con" and self.noun2.state == "rect":
            self.noun1.state = "con"