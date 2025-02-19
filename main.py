def sort_key_value(dict, key):
    new_dict = {
        "char" : key,
        "num" : dict[key]
                }
    return new_dict    

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def main():

    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    lowered_text = file_contents.lower()

    words = file_contents.split()
    #print(f"{len(words)}")
    
    dictionary = {}
    alpha = "abcdefghijklmnopqrstuvwxyz "
    for char in alpha:
        dictionary[char] = 0

    for char in lowered_text:
        if char in alpha:
            dictionary[char] += 1
    
    print(f"--- Begin report of {path} ---")
    print(f"{len(words)} words found in the document")
    
    dict_list = []

    for key in dictionary:
        if key.isalpha():
            dict_list.append(sort_key_value(dictionary, key))

    dict_list.sort(reverse=True, key=sort_on)

    for dict in dict_list:
        print(f"The '{dict["char"]}' character was found {dict["num"]} times")

    print("--- End report ---")
    

if __name__ == "__main__":
    main()
