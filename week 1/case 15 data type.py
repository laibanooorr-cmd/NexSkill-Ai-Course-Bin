# 1.	Type-safe Input Parser
# o	Task: Parse a dictionary of strings into typed fields (int, float, bool, date-like) with defaults.
from datetime import datetime

def to_int(value):
    return int(value)

def to_float(value):
    return float(value)

def to_bool(value):
    value = value.strip().lower()
    if value in ("true", "1", "yes"):
        return True
    elif value in ("false", "0", "no"):
        return False
    else:
        raise ValueError("Expected true/false, yes/no, or 1/0.")

def to_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()

def parse_input(data, schema):
    """
    data: dictionary containing string values
    schema: field -> (converter, default)
    """
    result = {}

    for field, (converter, default) in schema.items():
        value = data.get(field)

        if value is None or value == "":
            result[field] = default
            continue

        try:
            result[field] = converter(value)
        except Exception as e:
            print(f"Error parsing '{field}': {e}")
            result[field] = default

    return result

data = {
    "age": "20",
    "height": "5.8",
    "student": "Yes",
    "dob": "2005-08-15"
}

schema = {
    "age": (to_int, 0),
    "height": (to_float, 0.0),
    "student": (to_bool, False),
    "dob": (to_date, None)
}

parsed = parse_input(data, schema)

print("Parsed Data:") #output: Parsed Data:age: 20 (int), height: 5.8 (float), student: True (bool), dob: 2005-08-15 (date)
for key, value in parsed.items():
    print(f"{key}: {value} ({type(value).__name__})")
    

# 2.	List vs Tuple Mutability Demo
# o	Task: Show how changing a list inside a tuple affects immutability semantics (tuple is immutable but can contain mutables).
t = ([1, 2, 3], "fixed", 100)

print("Original tuple:", t) #output: Original tuple: ([1, 2, 3], 'fixed', 100)
print("Tuple id:", id(t)) #output: Tuple id: 1980065024704

t[0].append(999)

print("\nAfter modifying inner list:") 
print("Tuple:", t) #output: After modifying inner list: Tuple: ([1, 2, 3, 999], 'fixed', 100)
print("Tuple id (unchanged):", id(t)) #output: Tuple id (unchanged): 1980065024704

try:
    t[1] = "changed"
except TypeError as e:
    print("\nError when trying to modify tuple element:") #Error when trying to modify tuple element:
    print(e) #output: 'tuple' object does not support item assignment
    

# 3.	Dictionary Keys: Hashability Rules
# o	Task: Demonstrate valid/invalid types for dict keys and why (hashable/immutable)

print("=== VALID KEYS ===") #output: === VALID KEYS ===

d = {
    10: "integer key",
    "name": "string key",
    3.14: "float key",
    (1, 2, 3): "tuple key"
}

print(d) # output: {10: 'integer key', 'name': 'string key', 3.14: 'float key', (1, 2, 3): 'tuple key'}

print("\n=== HASH TESTS ===")

print("hash(10):", hash(10)) #output: hash(10): 10
print("hash('hello'):", hash("hello")) # output: hash('hello'): 5077002823612394855
print("hash((1,2,3)):", hash((1, 2, 3))) # output: hash((1,2,3)): 529344067295497451

print("\n=== INVALID KEYS (will raise errors) ===")

# List as key (NOT allowed)
try:
    d = {}
    d[[1, 2, 3]] = "list key"
except TypeError as e:
    print("List key error:", e) #output: List key error: unhashable type: 'list'

# Set as key (NOT allowed)
try:
    d = {}
    d[{1, 2, 3}] = "set key"
except TypeError as e:
    print("Set key error:", e) # output: Set key error: unhashable type: 'set'

print("\n=== TUPLE EDGE CASE ===")

# Tuple is valid only if all elements are hashable
try:
    d = {}
    key = (1, [2, 3])
    d[key] = "invalid tuple"
except TypeError as e:
    print("Tuple error:", e) # output: Tuple error: unhashable type: 'list'
    

# 4.	Shallow Copy vs Deep Copy
# o	Task: Given nested structures, show differences between copy.copy and copy.deepcopy.
import copy
original = [1, 2, [3, 4]]
shallow = copy.copy(original)

deep = copy.deepcopy(original)

print("=== ORIGINAL OBJECT ===")
print(original) # output: === ORIGINAL OBJECT === [1, 2, [3, 4]]

print("\n=== SHALLOW COPY ===")
print(shallow) # output: === SHALLOW COPY === [1, 2, [3, 4]]

print("\n=== DEEP COPY ===")
print(deep) # output: === DEEP COPY === [1, 2, [3, 4]]

original[2][0] = 999

print("\n\n=== AFTER MODIFYING original[2][0] = 999 ===")

print("Original:", original) # output: Original: [1, 2, [999, 4]]
print("Shallow :", shallow) # output: Shallow : [1, 2, [999, 4]]
print("Deep    :", deep) # output: Deep    : [1, 2, [3, 4]]


# 5.	Custom Sorting with Key Functions
# o	Task: Sort a list of mixed case strings case-insensitively while putting numbers (as strings) first.
def custom_sort_key(s):
    if s.isdigit():
        return (0, int(s)) 
    else:
        return (1, s.casefold()) 

items = ["Banana", "apple", "10", "2", "Orange", "100", "grape", "5A"]
sorted_items = sorted(items, key=custom_sort_key)

print("Original List:")
print(items) #output: Original List:  ['Banana', 'apple', '10', '2', 'Orange', '100', 'grape', '5A']
print("\nSorted List:")
print(sorted_items) # output: Sorted List: ['2', '10', '100', '5A', 'apple', 'Banana', 'grape', 'Orange']


# 6.	Duck Typing vs Type Checking
# o	Task: Write a function that accepts any “sequence-like” object (supports iteration and len) and processes it.
def process_sequence(seq):
    try:
        print("Length:", len(seq))
        for item in seq:
            print("Item:", item)

    except TypeError as e:
        print("Object is not sequence-like:", e)
process_sequence([1, 2, 3])        #output: Length: 3, Item: 1, Item: 2, Item: 3
process_sequence((10, 20, 30))     #output: Length: 3, Item: 10, Item: 20, Item: 30
process_sequence("hello")         #output: Length: 5,  Item: h, Item: e, Item: l, item: l, item: o
process_sequence({1, 2, 3})         #output: Length: 3, Item: 1, Item: 2, Item: 3


# 7.	Named Tuple for Simple Records
# o	Task: Use collections.namedtuple to represent a student record and compute derived fields (e.g., average).
from collections import namedtuple
Student = namedtuple("Student", ["name", "math", "science", "english"])
s1 = Student(name="Ali", math=85, science=90, english=80)
print("Student Record:")
print(s1) # output: Student(name='Ali', math=85, science=90, english=80)

print("\nName:", s1.name) # output: Name: Ali
print("Math:", s1.math) #output: Math: 85
print("Science:", s1.science) #output: Science: 90
print("English:", s1.english) # output: English: 80

average = (s1.math + s1.science + s1.english) / 3
print("\nAverage Marks:", average) # output: Average Marks: 85.0


