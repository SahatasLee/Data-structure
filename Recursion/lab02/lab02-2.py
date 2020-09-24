

def length(txt):
    count = 0
    # print('txt :', txt)
    if txt == '':
        # print(txt[0])
        # count = length(txt[1:])
        return 0
    else:
        # print(txt[0], end='')
        # print('txt', txt[1:])
        count = length(txt[0:-1])
        print(txt[-1], end='')
        if count % 2 == 0:
            print('*', end='')
        else:
            print('~', end='')
        count += 1
        return count


def test(txt):
    print(txt[1:] == '')
    print(txt[0])


print("\n", length(input("Enter Input : ")), sep="")
# test('123456')
# test('')
# print('\n', int(length('hello')), sep='')
