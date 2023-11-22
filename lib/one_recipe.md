1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def calculate_reading_time(word_count):
""" This function is going to take count of words and return estimated reading time
    based on speed of 200 per minute

    Parameters: (list all parameters and their types)
        word_count: a string containing words

    Returns: (state the return value and its type)
        integer, being amount of minutes, estimated reading time

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """

3. Create Examples as Tests

"""
Given a string with 200 words
It returns 1 minute
"""

"""
Given a string containing 400 words
It returns 2 minutes
"""

"""
Given a string containing 1600 words
It returns 8 minutes
"""

"""
Given a string containing less than 200 words, e.g. 100
It returns: reading time below 1 minute
"""

4. Implement the Behaviour