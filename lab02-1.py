

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    user_input = int(input('Enter Number : '))
    print(f'fibo({user_input}) = {fibonacci(user_input)}')


def test():
    for i in range(20):
        print(f'{i} : ', fibonacci(i))


if __name__ == '__main__':
    test()
