# Assignment 1:
# Write a program, to list all words, with vowel in it
sentence = input("Please enter a sentence: ") #input: Hello, World
words = sentence.split()

print("Words with vowels:")

for word in words:
    if any(char.lower() in 'aeiou' for char in word):
        print(word) # output: Words with vowels: Hello, World
        
# Assignment 2:
# Write a program , to have “List” , with all “noun” in story. Print them. 
story = input("Please enter a story: ") #input: Ali has a dog and a cat
noun_list = ['ali', 'dog', 'cat', 'car', 'house']  
words_in_story = story.split()
noun = []
for word in words_in_story:
    if word.lower() in noun_list:
        noun.append(word)
print("Nouns in the story:")
for n in noun:
    print(n) # output: Nouns in the story: Ali, dog, cat
    
# Assignment 2b:
# Write a program , to have “List” , with all “noun” in story. Last Element should a nested List, with 
# Numbers in story. Print them. 
story = input("Please enter a story: ")
noun_list = ['ali', 'dog', 'cat', 'car', 'house']  
words_in_story = story.split()
noun = []
numbers = []
for word in words_in_story:
    if word.lower() in noun_list:
        noun.append(word)
    if word.isdigit():
        numbers.append(int(word))
noun.append(numbers)  
print("Nouns in the story:")
for n in noun:
    print(n) #output Ali, dog, cat, [1, 2, 3]
    

# Assignment 3: 
# Write a program , to have “Tuples” , with all “noun” in story. Print them.
story = input("Please enter a story: ")
noun_list = ['ali', 'dog', 'cat', 'car', 'house']
words_in_story = story.split()  
noun = []
for word in words_in_story:
    if word.lower() in noun_list:
        noun.append(word)
noun_tuple = tuple(noun)
print("Nouns in the story:")
for n in noun_tuple:
    print(n) #output: Nouns in the story: Ali, dog, cat
    

# Assignment 3 b: 
# Write a program , to have “Tuples” , with all “noun” in story. Print them. Last Element should a nested 
# Tuples, with Numbers in story. Print them. 
story = input("Please enter a story: ")
noun_list = ['ali', 'dog', 'cat', 'car', 'house']   
words_in_story = story.split()
noun = []
numbers = []

for word in words_in_story:
    if word.lower() in noun_list:
        noun.append(word)
    if word.isdigit():
        numbers.append(int(word))

noun_tuple = tuple(noun)
print("Nouns in the story:")
for n in noun_tuple:
    print(n)

print("Numbers in the story:")
for num in numbers:
    print(num) #output: Nouns in the story: Ali, dog, cat, (2, 5, 10)
    

# Assignment 4: 
# Write a program , to have “Sets” , with all noun in story. Print them. . Last Element should a nested Sets, 
# with Numbers in story. Print them
story = input("Please enter a story: ")
noun_list = ['ali', 'dog', 'cat', 'car', 'house']
words_in_story = story.split()
noun = set()
numbers = set()
for word in words_in_story:
    if word.lower() in noun_list:
        noun.add(word)
    if word.isdigit():
        numbers.add(int(word))
number_set = frozenset(numbers)
result_set = noun.copy()
result_set.add(number_set)
print("Nouns in the story:")
print(result_set) #output: Nouns in the story: {'dog', frozenset({2, 10, 4}), 'Ali'}


# Assignment 2: 
# Write a program , to have “Dictionaries” , with all noun in story. Print them. Last Element should a 
# nested Dictionaries, with Numbers in story. Print them. 
story = input("Please enter a story: ")
noun_list = ['ali', 'dog', 'cat', 'car', 'house']   
words_in_story = story.split()
noun = {} 
numbers = {} 
for word in words_in_story:
    if word.lower() in noun_list:
        noun[word] = "noun"
    if word.isdigit():
        numbers[word] = "number"
        result_set = noun.copy()
        Nested_dict = {"numbers": numbers}
        result_set.update(Nested_dict)
print("Nouns and Numbers in the story:")    
print(result_set) #output: Nouns and Numbers in the story: {'Ali': 'noun', 'numbers': {'2': 'number', '3': 'number', '5': 'number'}}



# Assignment 2: 
# Write a program , to have “List” , with all noun in story. Print them
story = input("Please enter a story: ")
noun_list = ['ali', 'dog', 'cat', 'car', 'house']
words_in_story = story.split()
noun = []
for word in words_in_story:
    if word.lower() in noun_list:
        noun.append(word)
print("Nouns in the story:")
print(noun) #output: Nouns in the story: ['Ali', 'dog', 'cat', 'car']