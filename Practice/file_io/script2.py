try:
    with open('/app/sad.txt', mode='r') as my_file:
        print (my_file.read())
except FileNotFoundError as err:
    print("print doesn't exist")
    raise err
except IOError as err:
    print("IO Error")
    raise err