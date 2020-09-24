

def EatUp(n):
    if n > 1:
        EatUp(n-1)
        print('eat 1 ', n)
    elif n == 1:
        print('eat 1 ', n)


def fac(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def pernutation():
    s = [1,2,3]
    for i in range(len(s)):
        print(s[i])
    for i in range(len(s)):
        for j in range(len(s)):
            print(s[i], s[j])


def main():
    EatUp(4)


if __name__ == '__main__':
    n = int(input('Enter Input : '))
    if n == 0:
        print('error')
    else:
        if n > 0:
            for i in range(1, n + 1):
                print('_' * (n - i), end='')
                print('#'*i)
        else:
            for i in range(0, abs(n)):
                print('_' * i, end='')
                print('#' * (abs(n) - i))

