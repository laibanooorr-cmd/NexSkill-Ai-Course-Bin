 #1. reads a string and prints its length.
MyName = "Hello World"
print(len(MyName)) #output 11


#2. input string to uppercase and lowercase.
s = "python3"
print(s.lower())#output python3
print(s.upper())#output PYTHON3


#3. Count how many times a given character appears in a string 
s = "banana"
ch = "a"
print(s.count(ch))#output 3

#4. Print the first and last character of a string; handle empty input.
Thing = "drawer"
print(Thing[0])#output d
print(Thing[-1])#output r

#5. Check if a substring exists in a string.
s = "data science"
sub = "science"
print(sub in s)#output True

#6. Print a substring from index start to end (exclusive)
s = "programming"
print(s[3:8:1])#output gramm

#7. Reverse the string.
s = "Python1"
print(s[::-1])#output 1nohtyp

#8. Replace all occurrences of a word with another 
s = ("I love apples.Apples are great!")
result = s.replace("apples", "oranges")
print(result)#output I love oranges.Apples are great!


#9. Split a sentence on spaces and join with -
s = "split this sentence"
words = s.split()
result = "-".join(words)
print(result)#output split-this-sentence

#10. Remove leading and trailing spaces
s = "padded text"
print(s.strip())#output padded text


#1. count vowel and consonent
s = "Hello, World! 123"
vowels = 0
consonents = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonents +=1
            
print("vowels:", vowels)#output 3
print("consonents:", consonents)#output 7


#2. Input: "A man, a plan, a canal: Panama!" 
s = "A man, a plan, a canal: panama!"
"".join(ch.lower() for ch in s if ch.isalnum());
print(ch.isalnum())#output True

#3. Convert a sentence to title case without using .title() 
s = "hELLO wORLD from PYTHON"
words = s.split()
result = []
for word in words:
    if word:
        new_word = word[0].upper() + word[1:].lower() 
        result.append(new_word)
output = " ".join(result)
print(output)#output Hello World From Python

#4. Return a list of starting indices where a substring occurs
s = "aaaa"
sub = "aa"

indices = []

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        indices.append(i)

print(indices) #output [0, 1, 2]


#5. Build a frequency dictionary for characters (case-insensitive, skip spaces).
s = "Baa Baa Black Sheep"

freq = {}
for ch in s.lower():
    if ch != ' ':
     freq[ch]= freq.get(ch, 0) + 1

print(freq) #output {'b':3,'a':5,'l':1,'c':1,'k':1,'s':1,'h':1,'e':3,'p':1}


#6. Check if two strings are anagrams (ignore spaces, punctuation, and case).
s1 = "Listen"
s2 = "Silent"
freq1 = {}
freq2 = {}
for ch in s1.lower():
    if ch.isalpha():
        freq1[ch] = freq1.get(ch, 0) + 1
        
for ch in s2.lower():
    if ch.isalpha():
        freq2[ch] = freq2.get(ch, 0) + 1
print(freq1 == freq2) #output True



#7. Compress runs of the same character as <char><count>
s = "aaabbcaaaa"

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1
if len(s) > 0:
    result += s[-1] + str(count)
print(result) #output a3b21a4


# 8.	Longest Word in a Sentence
# Find the longest word; if multiple, return the first. Consider words as alphabetic sequences
name = input("programming language")
longest = ""
for token in name.split():
    data = "".join(ch for ch in token if ch.isalpha())
    if len(data) > len(longest):
        longest = word
        print("longest word:", longest) #output longest word: PYTHON
        


# 9.	Remove Duplicate Characters but Keep Order
# Remove duplicates while preserving the first occurrence order.
letters =("banana") 
seen = set()
result = ""
for ch in letters:
    if ch not in seen:
        seen.add(ch)
        result += ch
        print("result:", result) #output result: ban
        
# 10.	Mask Email Username
# Mask all but the first and last character of the username with *; keep domain intact.
Email = input("please enter your email:")
username, domain = Email.split('@')

if len(username) >= 2:
    masked_username = username[0] + '*' * (len(username) - 2) + username[-1]
else:
    masked_username = username  
masked_username = masked_username + '@' + domain
print("masked_username:", masked_username) #output masked_username: l**********r@gmail.com