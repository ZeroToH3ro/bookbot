def count_words(text):  
    # Split the text into words using whitespace as delimiter  
    words = text.split()  
    return len(words)  

def count_characters(text):  
    # Create an empty dictionary to store character counts  
    char_counts = {}  

    # Convert text to lowercase and iterate through each character  
    for char in text.lower():  
        # Only count if the character is already in the dictionary  
        if char in char_counts:  
            char_counts[char] += 1  
        # If it's not in the dictionary, add it with a count of 1  
        else:  
            char_counts[char] = 1  

    return char_counts  

with open("./books/frankenstein.txt") as f:  
    file_contents = f.read()  
  
# Count words and print the result  
word_count = count_words(file_contents)  
print(f"Total word count: {word_count}")  

# Assuming you have the file contents in file_contents  
char_count = count_characters(file_contents)  

# Print the results in a readable format  
print("Character counts:")  
for char, count in sorted(char_count.items()):  
    if char.isalpha():  # Only print alphabetic characters  
        print(f"The '{char}' character appears {count} times")  

