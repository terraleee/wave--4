def piglatin(word):
    if word[0] in "aeiou":
        return word + 'way'
    else:
        if word[1] in "aeiou":
            return word[1:] + word[0] + 'ay'
        elif word[2] in "aeiou":
            return word[2:] + word[0] + word[1] + 'ay'

sentence = input ("Enter a line of text: ")

print(' '.join(piglatin(word) for word in sentence.split()))
