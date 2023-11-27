1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
# We will ignore any intermediate sentences.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# def verify_sentence_grammar(text):
 """ This function is going to take count of words and   return estimated reading time
     based on speed of 200 per minute

#    Parameters: (list all parameters and their types)
#        text:  a string respresenting human-readable text

#    Returns: (state the return value and its type)
#        False / True: boolean

#    Side effects: (state any side effects)
#        This function doesn't print anything or have any other side-effects
    """

3. Create Examples as Tests

'''
Given a valid sentence with a capital letter and a fill stop
Returns true
'''
verify_sentence_grammar("Hello, this is a fine day.")
# => True

"""
Given an empty string
It returns: False
"""
verify_sentence_grammar("")
# => False


"""
Given a string "hello"
It returns: False
"""
verify_sentence_grammar("hello")
# => False


"""
Given a string "Hello"
It returns: False
"""
verify_sentence_grammar("Hello")
# => False

"""
Given a string "hello!"
It returns: False
"""
verify_sentence_grammar("hello!")
# => False

"""
Given a string "Hello!"
It returns: True
"""
verify_sentence_grammar("Hello!")
# => True

"""
Given a string "Hello! How are you?"
It returns: True
"""
verify_sentence_grammar("Hello! How are you?")
# => True

4. Implement the Behaviour