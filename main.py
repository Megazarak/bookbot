def main():

    path = "books/frankenstein.txt"
    '''
    with open(path) as f:
        text = f.read()
    '''
    print(f"--- Begin report of {path} ---")

    text = book_path(path)
    #wordList = text.split()

    wc = word_count(text)
    print(f"{wc} words found in the document.\n")

    char_ct = char_counter(text)
    #print(char_ct)
    
    char_list = []
    for char in char_ct:
        if char.isalpha():
            temp_dict = {}
            temp_dict["letter"] = char
            temp_dict["count"] = char_ct[char]
            char_list.append(temp_dict)
    
    sorted_dicts = sort_dict(char_list)
    #print(sorted_dicts)

    for pair in sorted_dicts:
        print(f"The '{pair["letter"]}' character was found {pair["count"]} times")

    print("--- End report ---")

    '''
    #print(wordList)
    wc = 0
    
    for word in wordList:
        wc += 1
    print(wc)
    '''
    #print(len(wordList))

def book_path(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    wc = text.split()
    return len(wc)

def char_counter(text):
    lc_text = text.lower() #lower case text
    char_dict = {}
    for char in lc_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(list):
    list.sort(reverse=True, key=sort_on)
    return list

main()