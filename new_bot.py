from transliterate import to_latin,to_cyrillic
def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message.isascii():
        return to_cyrillic(input_text)
    else:
       return to_latin(input_text)