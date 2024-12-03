char_array_test = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
char_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    car_array = get_char_array(text)
    get_each_char_count(car_array)
    print(f"{num_words} words found in the document")
    print(f"{len(get_char_array(text))} chars found in the document")
    print(char_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_array(text):
    char_array = []
    for char in text:
        if char.lower() in char_array_test:
            char_array.append(char.lower())
    #print(char_array)
    return char_array

def get_each_char_count(char_array):
    for char in char_array:
        char_dict[char] += 1
    #print(char_dict)


main()