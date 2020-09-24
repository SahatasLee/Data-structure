

def gcd(x, y):
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    if x == 0:
        return y
    if y == 0:
        return x
    if x % y == 0:
        return y
    elif y % x == 0:
        return x
    elif x > y:
        return gcd(x % y, y)
    elif x < y:
        return gcd(x, y % x)
    else:
        print('error')


def main():
    x, y = map(int, input('Enter Input : ').split())
    f = 0
    s = 0
    if x >= 0 or y >= 0:
        if x > y:
            f = x
            s = y
        else:
            f = y
            s = x
    elif x < 0 and y < 0:
        if abs(x) > abs(y):
            f = x
            s = y
        else:
            f = y
            s = x

    if f == 0 and s == 0:
        print('Error! must be not all zero.')
    else:
        print(f'The gcd of {f} and {s} is : {gcd(x, y)}')


if __name__ == '__main__':
    main()
