def multiplication_table(number):
    test = ""
    for x in range(1,13):
        test += str(number*x ) + " "
    return test
def main():
   print(multiplication_table(5))

main()