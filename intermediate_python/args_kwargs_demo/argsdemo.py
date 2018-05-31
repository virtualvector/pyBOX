def demo_func(arg_you_know, *args):
    print arg_you_know
    for i in args:
        print "these are not known",i

demo_func("hello","not","known","before hand")
