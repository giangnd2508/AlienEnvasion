def main():
    magicians = ['111', '222', '333']
    new_list = make_great(magicians)
    show_magicians(new_list)
    print(magicians)


def make_great(magicians):
    magicians_2 = []
    for magician in magicians:
        magician = 'The Great ' + magician
        magicians_2.append(magician)
    return magicians_2


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


main()
