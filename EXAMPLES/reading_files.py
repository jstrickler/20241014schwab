FILE_PATH = '../DATA/mary.txt'

mary_in = open(FILE_PATH)  # open file for reading
# read file...
mary_in.close()  # close file (easy to forget to do this!)

# with EXPR as VAR:
#   blah
#   blah

with open(FILE_PATH) as mary_in:  # open file for reading
    for raw_line in mary_in:  # iterate over lines in file (line retains \n)
        line = raw_line.rstrip()  # rstrip() removes whitespace (including \n or \r ) from end of string
        print(line)
    # mary_in.close() automagically called
print('-' * 60)

with open(FILE_PATH) as mary_in:
    contents = mary_in.read()  # read entire file into one string
    print("NORMAL:")
    print(contents)
    print("=" * 20)
    print("RAW:")
    print(repr(contents))  # print string in "raw" mode
print('-' * 60)

with open(FILE_PATH) as mary_in:
    lines_with_nl = mary_in.readlines()  # readlines() reads all lines into an array
    print(lines_with_nl)
print('-' * 60)

with open(FILE_PATH) as mary_in:
    lines_without_nl = mary_in.read().splitlines()  # splitlines() splits string on '\n' into lines
    print(lines_without_nl)
print('-' * 60)

FILE_PATH = "../DATA/words.txt"

with open(FILE_PATH) as file_in:
    for raw_word in file_in:
        if (raw_word[0] == 'q') and (raw_word[1] != 'u'):
            word = raw_word.rstrip()
            print(word)
print('-' * 60)

with open("../DATA/computer_people.txt") as people_in:
    for line in people_in:
        first_name, last_name, product, dob = line.rstrip().split(';')
        if first_name.startswith('L'):
            print(f"{first_name} {last_name}")

