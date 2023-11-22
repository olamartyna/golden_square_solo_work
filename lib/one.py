# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

def estimate_reading_time(text):
    text_length = text.count(' ')
    if text_length >= 200:
        minutes =  text_length / 200
        return minutes
    else:
        return "Reading time is below 1 minute"
