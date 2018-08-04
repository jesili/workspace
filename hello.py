print("please tell me your name, enter 'q' to quit" )
while True:
    name = input("what's your name? ")
    if name != 'q':
        print("hello, " + name)
    else:
        break
