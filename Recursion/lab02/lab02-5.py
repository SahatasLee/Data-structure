def staircase(n, i=None):

    if i is None:
        i = n

    if n == 0:
        print('Not Draw!')
        return
    else:
        if i == 0:
            return 0
        elif n > 0:
            i = staircase(n, i-1)
            print('_' * (n - i - 1), end='')
            print('#' * (i + 1))
            return i+1
        else:
            i = staircase(n, i+1)
            print('_' * abs(i), end='')
            print('#' * (abs(n) - abs(i)))
            return i-1


staircase(int(input("Enter Input : ")))
