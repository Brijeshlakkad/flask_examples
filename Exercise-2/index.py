from decorators.do_twice import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return "Hi {}".format(name)


print(return_greeting("Brijesh"))
print(return_greeting.__name__)
