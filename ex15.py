from sys import argv

script, filename = argv

txt = open(filename)

print ("here is your file %r" % filename)
preint (txt.read())

print("type the filename again: ")
file_again = raw_input ("> ")

text_agian = open (file_again)

print (text_agian.read())
