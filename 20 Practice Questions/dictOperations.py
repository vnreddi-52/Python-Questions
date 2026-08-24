dict_a = {
    "name":"vaishnavi",
    "age": 21
}
print(dict_a['name'])
print(dict_a.get('city'))
# print(dict_a['city'])

dict_a['city']="Belgaum"
print(dict_a)

dict_a['age']=24
print(dict_a)

del dict_a['city']
print(dict_a)

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())


