case_dict = {
    "u":"Nominative",
    "i":"Dative",
    "a":"Accusative"
}
def get_word():
    word = input("Please input an Akkadian word: ")
    return word
def get_lemma_and_case_ending(word):
    if word.endswith("m") or word.endswith("n"): # Nunation taken into account 
        ending = word[-2:]
    else:
        ending = word[-1]
    lemma = word[:-len(ending)]
    return lemma, ending 
def get_gender(lemma):
    if lemma.endswith("t"):
        return "Feminine"
    return "Masculine"
def get_number(lemma, ending, gender):
    if ending.endswith("n"):
        return "Dual"
    elif gender == "Feminine":
        if lemma.endswith("aat") or lemma.endswith("eet"):
            return "Plural"
    if ending.endswith("m"): # This is here because feminine plurals do end with "m", so it should return beforehand.
        return "Singular"
def get_case(ending, case_dict):
    ending = case_dict.get(ending[0])
    return ending
def main():
    word = get_word()
    lemma, ending = get_lemma_and_case_ending(word)
    gender = get_gender(lemma)
    number = get_number(lemma, ending, gender)
    case = get_case(ending, case_dict)
    print(f"Word: {word}\n Gender: {gender}\n Number: {number}\n Case: {case}")

if __name__ == "__main__":
    main()
