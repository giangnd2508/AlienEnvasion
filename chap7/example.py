# my_foods = ['pizza', 'falafel', 'carrot cake']
#
# foods = [value for value in my_foods[:]]
# print(foods)


diction = {
    'name': 'Lucas',
    'age': 18,
    'addr': 'Hanoi'
}

for k in sorted(diction.keys()):
    print(k)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


people = ['giang', 'jen', 'edward']

for name in people:
    if name in favorite_languages.keys():
        print('thanking them for responding')
    else:
        print('inviting them to take the poll')


