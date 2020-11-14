

def binary_search(r, arr, x):
    # print(arr, r)

    if not arr:
        return False

    mid = r // 2
    # print('mid is ', mid)
    # print('arr is ', arr[:mid-1:])

    if arr[mid] > x:
        return binary_search(len(arr[:mid-1:])-1, arr[:mid-1:], x)
    elif arr[mid] < x:
        return binary_search(len(arr[mid+1::])-1, arr[mid+1::], x)
    else:
        return True


def main():
    inp = input('Enter Input : ').split('/')
    arr, k = list(map(int, inp[0].split())), int(inp[1])
    print(binary_search(len(arr) - 1, sorted(arr), k))


if __name__ == '__main__':
    main()
