def remove_vowels(text):
    vowels = "aeiouAEIOU"
    
    
    result = ''
    for char in text:
        if char not in vowels:  
            result += char      
    
    return result 

# Example usage
input_text = "This website is for losers LOL!"
output_text = remove_vowels(input_text)
print(output_text)  