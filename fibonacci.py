def fibonacci(x):

    a = 0
    b = 1
    test = "0 1 "
    for p in range(x):
        c = a + b
        a = b
        b = c
        test += str(c) + " "
    return test

def main():
    print(fibonacci(9))

main()
