# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

def verify_sentence_grammar(text):
    punctuation_marks = ['.', '!', '?']
    if len(text) == 0:
        return False
    elif text[0].isupper() and text[-1] in punctuation_marks:
        return True
    else:
        return False