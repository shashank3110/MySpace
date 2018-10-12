
#while-else to show how loop_else is used but its not necessary
def add():
    return 5+5
def mul():
    return 5*5
sub="-"
method=[add,sub,mul]
def eval(arg=None):
    funcs=arg or method
    while funcs:
        item=funcs.pop()
        if callable(item):
            print(item())
        elif isinstance(item,str):
            print("it is a string")
        else:
            print("it is a fake function")
    else:
        print("empty")
