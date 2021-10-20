
def count(first, last):
    test = ""
    if first < last:
        for x in range(first,last):
            test += str(x) + " "
    if last< first:
        for x in range(first, last,-1):
            test += str(x) + " "
    return test

def main():
    print(count(9, 6))


if __name__ == '__main__':
    main()
