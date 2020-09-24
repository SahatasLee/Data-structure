

def perket_normal():
    user_input = input('Enter Input : ').split(',')
    s = 1
    b = 0
    diff = 0
    for i in user_input:
        s *= int(i.split()[0])
        b += int(i.split()[1])
    print(s, b)
    print(abs(s-b))


def perket(s, b):
    if s == [] and b == []:
        return 1, 0, 100000000
    else:
        # print(s)
        # print(b)
        sour = s.pop()
        bitter = b.pop()
        ss, sb, diff = perket(s, b)
        # print(ss, sb, diff, sour, bitter)
        # print(abs((ss * sour) - (sb + bitter)))
        if abs((ss * sour) - (sb + bitter)) > diff:
            return ss, sb, diff
        else:
            return ss*sour, sb+bitter, abs((ss * sour) - (sb + bitter))


def test():
    s = [1, 2, 3, 4]
    rs = s[::-1]
    # print(rs)
    b = [7, 6, 8, 9]
    rb = b[::-1]
    ss, sb, diff = perket(s, b)
    ss, sb, rediff = perket(rs, rb)
    if diff < rediff:
        print(diff)
    else:
        print(rediff)


def main():
    s = []
    b = []
    ans = None
    user_input = input('Enter Input : ').split(',')

    for i in user_input:
        s.append(int(i.split()[0]))
        b.append(int(i.split()[1]))

    for i in range(len(s)):
        # print(s)
        # print(b)
        sc = s.copy()
        bc = b.copy()
        s.append(s.pop(0))
        b.append(b.pop(0))
        ss, sb, diff = perket(sc, bc)
        if ans is None:
            ans = diff
        elif ans > diff:
            ans = diff

    print(ans)


if __name__ == '__main__':
    main()
