def get_num_words(content):
    return content.split()

def get_char_count(content):
    content = content.lower()
    chars = {}

    for char in content:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def pretty_dict(dict):
    organized = []
    for key, val in dict.items():
        organized.append({"char": key, "num": val})
    organized.sort(reverse=True, key=sort_on)
    return organized