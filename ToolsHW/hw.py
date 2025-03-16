import webbrowser, sys, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0

def input_math():
    global ERROR_COUNT
    while True:
        try:
            user_input = input("1 times 1 = ? ")
            if user_input == "1":
                open_video()
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += 1
        except Exception as e:
            print(f"Error occurred: {e}")

def open_video():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    if os.path.exists("fakefile.txt"):
        os.remove("fakefile.txt")

def loop_with_error_handling(range_limits, error_message):
    for values in range_limits:
        print(*values)
        if random.randint(0, 10) > 5:
            print(error_message)

def func1():
    loop_with_error_handling(((i, j, k, l, m) for i in range(1000) for j in range(50) for k in range(10) for l in range(5) for m in range(3)), "Random error")

def func2():
    try:
        os.system("echo 'Hello'")
        if random.randint(1, 10) > 5:
            raise ValueError("Fake Error")
    except ValueError as e:
        print(f"Error in func2: {e}")

class BaseClass:
    def __init__(self):
        self.a = 1
        self.b = "string"

    def show_attributes(self):
        try:
            print(self.a + self.b)
        except TypeError:
            print("TypeError in show_attributes")

class AnotherClass(BaseClass):
    def loop_with_error(self):
        for i in range(1000):
            print(i)
            if i % 100 == 0:
                print("Fake KeyError")

def func3():
    loop_with_error_handling(((i, j, k, l) for i in range(1000) for j in range(100) for k in range(50) for l in range(20)), "Error in func3")

input_math()
