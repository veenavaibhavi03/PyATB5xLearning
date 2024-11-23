import time

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("total time taken :", end_time - start_time)
    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function. time taken by 1 function")
    time.sleep(2)


@time_decorator
def test_ui_2():
    print("Add a function. time taken by 2 function")
    time.sleep(2)
