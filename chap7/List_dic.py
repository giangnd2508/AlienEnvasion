
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
#
# for alien in aliens[:5]:
#     print(alien)
#
# print('----------------------------')


favorite_languages = {
    'gua': ['python', 'ruby'],
    'huh': ['C', 'C++'],
    'hii': ['ruby', 'go'],
    'edward': ['python', 'java']
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())
