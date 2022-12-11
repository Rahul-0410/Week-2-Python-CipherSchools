# dictionaries
# user={'name':'Rahul','age': 24}
# print(user)
# print(type(user))
# user1=dict(name='Harshit',age=24)
# print(user1)

# print(user1['name'])
# print(user1['age'])
# user_info= {
#     'name':'Rahul',
#     'age': 20,
#     'fav_movies':['Avengers','batman'],
#     "fav_tunes":['Death bed','give me'],

# }
# print(user_info)
# print(user_info['fav_movies'])

# user_info1={}
# user_info1['name']='mohit'
# print(user_info1)

# user_info= {
#     'name':'Rahul',
#     'age': 20,
#     'fav_movies':['Avengers','batman'],
#     "fav_tunes":['Death bed','give me'],

# }
# this method is only for keys
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# this method is only for values
# if 'Rahul' in user_info.values():
#     print('present')
# else:
#     print('not present')

# for i in user_info:
#     print(i)
# for j in user_info.values():
#     print(j)
# user_info_values=user_info.values()
# print(user_info_values)
# print(type(user_info_values))
# user_info_keys=user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# for i in user_info:
#     print(user_info[i])
# items method
# usser_items=user_info.items()
# print(usser_items)
# print(type(usser_items))

# for key,value in user_info.items():
#     print(f"Key is {key} and value is {value}")

user_info= {
    'name':'Rahul',
    'age': 20,
    'fav_movies':['Avengers','batman'],
    "fav_tunes":['Death bed','give me'],

}

# how to add data
# user_info['fav_songs']=['song1','song2']
# print(user_info)

# pop method
# popped_item=user_info.pop('fav_tunes')
# print(f"popped item is{popped_item}")
# print(user_info)

#popitem method
# popped_item=user_info.popitem()
# print(user_info)
# print(popped_item)
# print(type(popped_item))

#updating a dictionary

# more_info={'name':'Rahul Gupta','State':'Punjab','hobbies':['coding','reading','listning music']}
# user_info.update(more_info)
# print(user_info)
# fromkeys
# d={'name':'unknown','age':'unknown'}

# d=dict.fromkeys(['name','age','height'],'unknown')
# d=dict.fromkeys(('name','age','height'),'unknown')
# print(d)
# get method
# print(d['name']) # here if the key is wrong it will give an error but get method will not give error but give 'none'
# print(d.get('names'))
# if d.get('name'):
#     print('present')
# else:
#     print('not present')
# d.clear()
# print(d)

#copy
# d1=d.copy()
# print(d1)
# print(d1.popitem())
# print(d1)
# print(d)
user={'name':'Rahul','age':20,'age':34}
# print(user.get('names','not found!'))
print(user)

