

def greater(arr, x):

    for i in arr:
        if i > x:
            return i

    return 'No First Greater Value'


if __name__ == '__main__':
    user = input('Enter Input : ').split('/')
    # print(type(left), ',', right)
    # left = [int(j) for j in user[0].split()]
    left = list(map(int, user[0].split()))
    right = [int(k) for k in user[1].split()]

    for i in right:
        print(greater(sorted(left), i))
