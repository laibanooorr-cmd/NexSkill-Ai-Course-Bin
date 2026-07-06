# 1.	Count Vowels and Consonants (Unicode-aware)
sentence = input("Enter a sentence: ") #input: "Hello, World!"
import unicodedata
sentence = unicodedata.normalize('NFKC', sentence)
sentence = sentence.casefold()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count) #output: Vowels: 3
print("Consonants:", consonant_count) #output: Consonants: 7


# 2.	Title Case with Minor Words Exempt
# o	Task: Convert a sentence to title case but keep minor words (like “and”, “of”, “the”) in lowercase unless first/last.
sentence = input("Enter a sentence: ") #input: "the quick brown fox jumps over the lazy dog"
import string
minor_words = {"and", "of", "the"}
words = sentence.split()
for i, word in enumerate(words):
    stripped_word = word.strip(string.punctuation)
    if i == 0 or i == len(words) - 1 or stripped_word.lower() not in minor_words:
        words[i] = stripped_word.capitalize()
    else:
        words[i] = stripped_word.lower()
        
print(" ".join(words)) #output: The Quick Brown Fox Jumps over the Lazy Dog




# 3.	Find and Replace with Whole-Word Matching
# o	Task: Replace a target word only when it appears as a whole word (not inside other words).
import re
sentence = input("Enter a sentence: ") #input: "The cat sat on the mat."
target_word = input("Enter the target word to replace: ") #input: "cat" 
replacement_word = input("Enter the replacement word: ") #input: "dog"
sentence = re.sub(r'\b{}\b'.format(re.escape(target_word)), replacement_word, sentence)
print("Modified sentence:", sentence) #output: Modified sentence: The dog sat on the mat.


# 4.	Compress Runs (Run-Length Encoding)
# o	Task: Compress a string: "aaabbc" → "a3b2c1". Provide a switch to only write counts if >1.
def rle_encode(s, only_if_gt_1=False):
    if not s:
        return ""

    result = []
    current = s[0]
    count = 1

    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            result.append(current + (str(count) if (not only_if_gt_1 or count > 1) else ""))
            current = ch
            count = 1

    result.append(current + (str(count) if (not only_if_gt_1 or count > 1) else ""))
    return "".join(result)


def rle_decode(s):
    result = []
    i = 0

    while i < len(s):
        char = s[i]
        i += 1

        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        count = int(num) if num else 1
        result.append(char * count)

    return "".join(result)


# Example usage
print(rle_encode("aaabbc"))                  # a3b2c1
print(rle_encode("aaabbc", True))            # a3b2c
print(rle_decode("a3b2c1"))                  # aaabbc
# ""

# # 5.	Check Balanced Brackets with Types ()[]{}
# # o	Task: Return True if brackets are balanced and correctly nested.
def is_balanced_brackets(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(bracket_map.values())
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
#     return len(stack) == 0
# print(is_balanced_brackets("([]{})")) #output: True


# 6.	Longest Word and Its Frequency
# o	Task: Find the length of the longest word(s) and how many times that length occurs.
length_count = {}
sentence = input("Enter a sentence: ") #input: "The quick brown fox jumps over the lazy dog"
import re
words = re.findall(r"[A-Za-z]+", sentence)
for word in words:
    word_length = len(word)
    if word_length in length_count:
        length_count[word_length] += 1
    else:
        length_count[word_length] = 1

if length_count:
    max_length = max(length_count.keys())
    print(f"Longest word length: {max_length}")
    print(f"Frequency of longest word length: {length_count[max_length]}")
else:
    print("No words found.") #output: Longest word length: 5, Frequency of longest word length: 4
    

# 7.	Anagram Checker Ignoring Spaces/Punct/Case
# o	Task: Determine if two strings are anagrams ignoring spaces, punctuation, and case.
sentence = input("Enter the first string: ") #input: "Listen"
sentence2 = input("Enter the second string: ") #input: "Silent"

# Normalize strings
sentence = ''.join(c.lower() for c in sentence if c.isalnum())
sentence2 = ''.join(c.lower() for c in sentence2 if c.isalnum())

# Check if they are anagrams
if sorted(sentence) == sorted(sentence2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.") #output: The strings are anagrams
    

# 8.	Extract Email-like Tokens
# o	Task: Extract email-like patterns from text (not full RFC), e.g., name.surname@domain.tld.
import re 
text = input("Enter a text:") #input lease contact us at info@example.com or support@company.com
patterns = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}\b'
emails = re.findall(patterns, text)
print("Extracted Emails:")
for email in emails:
    print(email) #output  Extracted Emails:info@example.com , support@company.org
    

