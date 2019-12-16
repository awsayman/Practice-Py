from sys import argv

script, user_name = argv
prompt = '> '

print ("hi %s, I'm The %s script" % (user_name, script))
print("I'd rather like ask you qusetions.")
print("do like me %s" % user_name)
likes= raw_input(prompt)

print("where do live %s" % user_name)
lives= raw_input(prompt)

print("what kind of computer do you have ")
computer= raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, Not Sure Where is that.
and you have a %r computer, Nice.
""" % (likes, lives, computer)
