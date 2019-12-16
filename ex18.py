def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" %(arg1, arg2))

def print_two_ag(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

print_two("aex", "Awa")
print_two_ag("23sd", "asd")
