#**kwargs is used for sending keyworded arguments

def demo_func(**kwargs):
    for name,value in kwargs.items():
        print "{0} = {1}".format(name,value)

demo_func(name="hello",place="bangalore")
