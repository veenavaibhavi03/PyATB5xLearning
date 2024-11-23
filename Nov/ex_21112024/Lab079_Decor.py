from curses import wrapper


def call_ui(function):

    def wrapper(): # we can give any name for function but wrapper is easy to remember
        print("Before the running UI TC")
        print("start browser")
        function()
        print("complete running the UI TC")
        print("Quit the browser")
    return  wrapper()


@call_ui
def test_ui():
    print(" >>I will test the UI")