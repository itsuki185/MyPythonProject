while True:
    try:
        s = input('Input number(q for exit:')
        if s == 'q':
            break
        num = int(s)
        print(100 / num)
    expect ZeroDivisionError as ex:
        print('num is 0')