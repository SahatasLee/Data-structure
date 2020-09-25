

def get_digit(n, d):  # หาค่าหลัก d จาก n
    if n < 0:
        n = n * -1
    for i in range(d-1):
        n //= 10
        print(n)
    print(n)
    return n % 10


n = get_digit(-123, 3)
print(n)
print(-123 // 10)
