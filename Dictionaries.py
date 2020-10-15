# Learn Python Dictionaries

# Different types of Dictionaries
dictionary1 = {1: "Taylor Swift", 2: "Selena Gomez", 3: "Ariana Grande"}

# dictionary with mixed keys
dictionary2 = {1: 'hola', 'two': True, '3': [1, 2, 3], 'Four': {'fun': 'window'}, 10.0: 5.9}

# from sequence having each item as a pair
dictionary3 = dict([("Dan Brown", 'The Da Vinci Code'), ("John Green", 'The fault in our Stars'),
                    ("Paulo Coelho", 'The Alchemist')])
print("\n")


# demo of keys and values
dictionary4 = {"a": "ant", "b": "bee", "c": "cat", "d": "dog"}
print(dictionary4.keys())
# Output: dict_keys(['a', 'b', 'c', 'd'])
print(dictionary4.values())
# Output: dict_values(['ant', 'bee', 'cat', 'dog'])
print(dictionary4.items())
# Output: dict_items([('a', 'ant'), ('b', 'bee'), ('c', 'cat'), ('d', 'dog')])
print("\n")


# Accessing and writing data in a Python dictionary
dictionary5 = {"song": "The Hills", "artist": "Weeknd"}
# To access value of a particular key
print(dictionary5["song"])
# To Overwrite
dictionary5["song"] = "Starboy"
print(dictionary5.items())
print("\n")


# Merging Dictionaries with the .update() Method
dict1 = {'color': 'black', 'shape': 'circle'}
dict2 = {'color': 'pink', 'number': 4}
dict1.update(dict2)
# dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}
print("\n")


capitals = {'India': 'New Delhi', 'France': 'Paris', 'Greece': 'Athens'}
capitals.pop('Greece')
print(capitals)
# Output: {'India': 'New Delhi', 'France': 'Paris'}
# To delete all elements
capitals.clear()
print(capitals)
print("\n")


movies = {}.fromkeys(['Inception', 'Memento', 'Interstellar'], "Christopher Nolan")

print(movies)
# Output: {'Inception': 'Christopher Nolan', 'Memento': 'Christopher Nolan', 'Interstellar': 'Christopher Nolan'}

# To print all Movies
for item in movies.items():
    print(item)

print(list(sorted(movies.keys())))
# Output: ['Inception', 'Interstellar', 'Memento']
print("\n")

# Imposter among us?
lobby = {"Imposter": 1, "Red": 2, "Yellow": 25, "Black": 49, "Green": 81}

print("Yellow" in lobby)
# Output: True

print("Imposter" not in lobby)
# Output: False

# membership tests for only keys not values
print("Imposter" in lobby)
# Output: True
print("\n")


# Dictionary Functions
food = {"pizza": 20, "Mdew": 5, "fries": 50, "Pepsi": 0, "Pasta": 2}

print(sorted(food))
# Output: ['Mdew', 'Pasta', 'Pepsi', 'fries', 'pizza'] (sorted keys)

print(len(food))
# Output: 5

print(all(food))
# Output: False

print(any(food))
# Output: True (since the dictionary is not empty)



