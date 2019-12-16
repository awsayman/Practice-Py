from sys import argv

scipt, filename = argv

print ("we are to ease this %r " % filename)
print ("If we dont want to hot, hit CTRL-C (^C)")
print("If you do want that, hit RETURN. ")

raw_input("?")

print("Opening file ....")
target= open(filename, 'w')

print ("Turncating the file. GOODBYE")
target.truncate()

print ("I am going to ask these files ")
line1= raw_input("line 1: ")
line2= raw_input("line 2: ")
line3= raw_input("line 3: ")

print ("now i will write these files.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("and finally, we can close it ")
target.close()
