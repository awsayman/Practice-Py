from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("copying from %s to %s" % (from_file, to_file))


in_file = open(from_file)
indata= in_file.read()

print("the input file is %d byts long "% len(indata))

print("does the output file exitst? %r" % exists(to_file))
print("Read hit go so we can contuine, CTRL-C to abouty")
raw_input()

out_file= open(to_file, 'w')
out_file.write(indata)

print ("all done fam")

out_file.close()
in_file.close()
