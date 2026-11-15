#open() is an in built function that tells python to open a txt file.
file = open('plain.txt', 'r')
#plain.txt is the name of the file that we want to open. 'r' is the mode in which we want to open the file. 'r' stands for read mode.
content = file.read()
#read() is a method that collects the whole content of the txt file and returns it as string. 
#here i created a variable called content that holds the whole content of the txt file.
print(content)
file.close()


#USING readline() and readlines() method.
file = open('plain.txt', 'r')
#readline()is a method that collects the content of the txt file line by line and returns it as string.
#it collects the first line of text and the more it is used it keeps collecting line text in a descebding order.
file.readline()
content = file.readline()
print(content)
file.close()

#here i just printed out the second line of text that is in my plain.txt file.
file = open('plain.txt', 'r')
content = file.readlines()
#readlines() is a method that collects the whole content of the txt file and returns it as a python list.
# the difference is just the "s" at the end of the method.
print(content)
file.close()
