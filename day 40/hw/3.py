def spin_words(sentence):
    words = sentence.split()
    
    spun_words = []
    for word in words:
        if len(word) >= 5:
            spun_words.append(word[::-1])
        else:
            spun_words.append(word)
    
    return ' '.join(spun_words)

print(spin_words("Hey fellow warriors"))  
print(spin_words("This is a test"))       
print(spin_words("This is another test")) 