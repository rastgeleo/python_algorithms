def string_rot(text):
    """return a list of possible rotated input text"""
    result = []
    for i in range(len(text)):
        new_text = text[i+1:] + text[0:i+1]
        result.append(new_text)
    return result

print(string_rot('tokyo'))
#['okyot', 'kyoto', 'yotok', 'otoky', 'tokyo']