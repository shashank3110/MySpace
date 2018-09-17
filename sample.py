def get_odd_factorials(func):
    def wrapper(*args,**kwargs):
        if args[0]%2==0:
            print("We give only odd-positive factorials")
        else:
            func(*args,**kwargs)
            return func(*args,**kwargs)
    return wrapper

@get_odd_factorials
def display(num):
    f=1
    for x in range(1,num+1): f=f*x
    return f