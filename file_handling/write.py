
#WRITING INFORMATION TO FILES
file = open('write.txt', 'w')
#"w" means open file in write mode. it will create a new file if the file does not exist.
file.write('Hello world\n')
file.write('This is a new line of text that is being written to the file.\n')

file.close()

file = open('write.txt', 'r')
content = file.read()
print(content)
file.close()

#"a" is append method used to write inside an existing file without overwriting the existing content. it will create a new file if the file does not exist.
file = open('write.txt', 'a')
file.write('I am learning python file handling.\n')
file.close()

file = open('write.txt', 'r')
content = file.read()
print(content)
file.close()

#"x" is exclusive creation method used to create a new file. it will return an error if the file already exists.
# file_non = open('creat.txt', 'x')
# file_non.write('this is a new file that has been created using the exclusive creation method.\n')
# file= open('write_non.txt', 'x')
# file.write('I am hungry')
# file_non.close()
# file.close()


#READING FILES USING FOR LOOP

file = open('creat.txt', 'w')
file.write('Ahmed\n') 
file.write('Lavis.\n')
file.close()

files = open('creat.txt', 'r')

#for loop is used here for reading content in file line by line. 
for line in files:
    if line.startswith('L'):
        print(line)
files.close()


# with

# Tells Python to manage the file's opening and closing automatically.

# open('creat.txt', 'r')

# Opens creat.txt in read mode.

# as file

# Stores the opened file object in a variable called file.

# The indented lines

# These are the instructions Python performs while the file is open.

with open('write.txt', 'r') as bike:
    content = bike.read()
    print(content)

with open('write.txt', 'a') as file:
    file.write('nahhhh')

with open('write.txt', 'r') as bike:
    content = bike.read()
    print(content)
