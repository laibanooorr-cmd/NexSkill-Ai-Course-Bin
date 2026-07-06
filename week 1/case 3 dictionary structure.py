#1.	Create a dictionary {'name': 'Ali', 'age': 25} and print the name
dic = {'name': 'Ali', 'age':25 }
print(dic['name']) #output Ali


#2.	Add key 'city': 'Lahore' to a dictionary.
dic = {}
dic['city'] = 'Lahore'
print(dic) #output {'city': 'Lahore'}


#3.	Change 'age' in {'name': 'Ali', 'age': 25} to 30.
dic = {'name': 'Ali', 'age': 25}
dic['age'] = 30
print(dic) #output {'name': 'Ali', 'age': 30}



#4.	Delete key 'age' from a dictionary.
dic = {'name': 'Ali', 'age': 25}
del dic['age']
print(dic) #output {'name': 'ALi'}


#5.	Check if key 'salary' exists in a dictionary.
dic = {'name': 'Ali', 'age': 25}
print('salary' in(dic)) #output False

#6.	Print all keys from {'a': 1, 'b': 2}
dic = {'a': 1, 'b': 2}
dic.keys()
print(dic) #output {'a': 1, 'b': 2}


#7.	Print all values from a dictionary.
#Tip: Use d.values().
dic = {'a': 1, 'b': 2}
print(dic.values()) #output dic_values([1, 2])


#8.	Iterate and print key‑value pairs from {'x': 10, 'y': 20}
dic = {'x': 10, 'y': 20}
for k, v in dic.items():
    print(k, v) #output x = 10, y = 20
    

#9.	Use get() to safely read key 'score' from an empty dictionary
dic = {}
dic2 = dic.get('score', 0)
print(dic2) #output 0


#10.	Create a dictionary from two lists: keys = ['a','b'], values = [1,2]
keys = ['a', 'b']
values = [1, 2]
dic =  dict(zip(keys, values))
print(dic) #output {'a': 1, 'b': 2}