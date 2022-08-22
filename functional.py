# Write a function flatten_dict() to flatten a nested dictionary by joining the keys with . character.
# flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}) 
# {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}

def flatten_dict(dictionary):
    flat = {}
    for top_key in dictionary:
        if isinstance(dictionary[top_key], dict):
            for inner_key in dictionary[top_key]:
                key = top_key + "." + inner_key
                flat[key] = dictionary[top_key][inner_key]
        else:
            key = top_key
            flat[key] = dictionary[top_key]

    return flat

print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))    

# Write a function unflatten_dict() to do reverse of flatten_dict.
# unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}) 
# {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}

def unflatten_dict(dictionary):
    unflat = {}
    for key in dictionary:
        split = key.partition('.')
        if split[2] == '':
            unflat[split[0]] = dictionary[key]
        else:
            if unflat.get(split[0]):
              unflat[split[0]][split[2]] = dictionary[key] 
            else:
               unflat[split[0]] = {}
               unflat[split[0]][split[2]] = dictionary[key]
    return unflat           
print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))


# Write a function treemap() to map a function over nested list.
# treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]) [1, 4, [9, 16, [25]]]
