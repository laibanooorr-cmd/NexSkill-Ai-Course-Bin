# # 1.	Count Word Frequencies
# # •	Task: Create a frequency dictionary (word → count) from a string.
from collections import defaultdict
def group_by_first_letter (names):
    d = defaultdict(list)
    for name in names:
        first_letter = name[0].casefold()
        d[first_letter].append(name)
        print(dict(d))
        return dict(d)
names = ["Ali", "Ayesha", "Bilal", "Babar"]
group_by_first_letter(names) #output {'a': ['Ali']}


# # 1.	Invert a Dictionary (Values to Keys)
# # •	Task: Invert a dict where values are unique: {k:v} → {v:k}.

d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print("inverted:", inverted) #output: inverted: {1: 'a', 2: 'b', 3: 'c'}


# # 1.	Merge Dictionaries with Conflict Policy
# # •	Task: Merge two dicts; on conflict, prefer the second dict’s value.
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = {**d1, **d2}
print("merged:", merged) #output: merged: {'a': 1, 'b': 99, 'c': 3}


# # 1.	Group Names by First Letter
# # •	Task: Given list of names, build dict mapping first letter → list of names with that letter.
names = ["Ali", "Ahmed", "Asad", "Bilal", "bushra", "ammar"]
grouped = {}
for name in names:
    key = name[0].lower()   # normalize case
    grouped.setdefault(key, []).append(name)
print(grouped)


# 1.	Safe Lookup with Default
# •	Task: Implement a function that looks up a key with a default value if missing and records how many defaults were used.
def make_safe_lookup(d, default=None):
    used_defaults = 0
    def lookup(key):
        nonlocal used_defaults
        if key not in d:
            used_defaults += 1
            return default
        return d[key]
    def get_count():
        return used_defaults
    return lookup, get_count
data = {"a": 10, "b": None, "c": 30}

lookup, count_defaults = make_safe_lookup(data, default=-1)

print(lookup("a")) #output: 10
print(lookup("b")) #output: None
print(lookup("x")) #output: -1
print(count_defaults()) #output: 1