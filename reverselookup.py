def reverseLookup(dictionary, value):
    keys = []

    for key in dictionary:
        if dictionary[key] == value:
            keys.append(key)
    return keys

def main():
    definitions = {"haha" : "laugh", "lol" : "laugh", "angry" : "furious"}
    print("The words for 'laugh' are: ", reverseLookup(definitions, "laugh"))
    print()
    print("The word for 'furious' is: ", reverseLookup(definitions, "furious"))
    print()
    print("The word for 'happy is: ", reverseLookup(definitions, "happy"))
    print()