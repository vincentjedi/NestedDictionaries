def flattened_json(d): # defined function taking one argument d which is a nested dictionary. 
    flat_dict = {} # initializing an empty dictionary to hold flattened key-value pairs as the function processes input dictionary. 
    for key, value in d.items(): # looping through each key-value pair in the input dictionary d. 
        if isinstance(value,dict): # checking if the value is a dictionary
            flat_value = flattened_json(value) # Recursive call for nested function. If the value is a dictionary the function calls itself with the nested dictionary as the argument. A recursive function calls itself until it reaches the deepest level of nesting. 
            for subkey, subvalue in flat_value.items():
                flat_dict[key + '.' + subkey] = subvalue # after the return of a flattened dictionary, it is appended with keys prepended. 
        else:
            flat_dict[key] = value # if value is not a dictionary, it is added to the flat_dict without any modifications. 

    return flat_dict # after processing all keys and values, the flat_dict having the flattened structure is returned. 

nested_dict = {
    "a": {
        "x": 1, 
        "y": 2},
        
    "b": {"z": 3}
}            

# flatten nested dictionary
flat_dict= flattened_json(nested_dict)

# print it
print("flattened items:", flat_dict)






