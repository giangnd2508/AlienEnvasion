# with open('C:\\Users\\giang.nguyen\\PycharmProjects\\CrashCoure\\pi_digits.txt') as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#     print(pi_string, len(pi_string))

path = 'C:\\Users\\giang.nguyen\\PycharmProjects\\CrashCoure\\abc.txt'

with open(path, 'w') as abc:
    abc.write('I use python1111111111 \n')

with open(path, 'a') as abc2:
    abc2.write('I use python22222 \n')

with open(path, 'r') as file_object:
    contents = file_object.read()
    print(contents)
