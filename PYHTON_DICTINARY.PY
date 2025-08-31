print('hellow world ')
my_dict = {}
my_dict ={"name":"harshad","age":16,"collage":"gpmumbai"}
print(my_dict)  # accesiing the all key and value pair in dictionary
print(my_dict["age"]) # accesiing the value of age in dictionary  
keys = my_dict.keys() # accesiing the keys in dictionary
print(keys) # print all the keys in dictionary 
values = my_dict.values() # accesing all values in dictionary 
print(values) # printing all the values in dictionary 

# adding new key value pair in dictionary 

my_dict["district"]="nashik"
print(my_dict)

# removing key-value pair in dictionaries 

del my_dict["age"]
print(my_dict)

# pop operation on dictonary 

print(my_dict.pop("collage","unknown")) # this remove the key-value in dictionary and return the value associate with key 

# returns the shallow copy of the dictionaries 

information = my_dict.copy()
print(information)

# clear all elements in dictionary means it just free the dictinary and its size is 0 

my_dict.clear()
print(my_dict)

name = information.get("name","aakruti") # get the value associated with key in dictionaries 
print(information)
print(name)

items = information.items() # get all items relaetd to dictionaries 
print(items)

keys = information.keys() # returns all keys are assocaiet with the dictionary 
print(keys)

value = information.values() # returns all the value are associate with the dictionary 
print(value)

key , value = information.popitem() # removes and return arbitary values on associate with dictionary 
print(information)

my_dict={"age":16,"gf":"aakruti","district":"nasik","collage":"GPM"} # 
information.update(my_dict)
print(information)

