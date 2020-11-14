
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class Hash:

    def __init__(self, size, maxc):
        self.data = [None] * size
        self.size = size
        self.maxc = maxc

    def __str__(self):
        mas = ''

        for i in range(self.size):
            # #1	(1+1, I)
            mas += '#' + str(i + 1) + '	' + str(self.data[i]) + '\n'

        mas += '---------------------------'

        return mas

    def is_empty(self):
        item = 0

        for i in self.data:
            if i is not None:
                item += 1

        return True if item < self.size else False

    def insert(self, x):

        index = hashing(x.key) % self.size

        if self.is_empty():

            for i in range(self.size):

                if self.data[((index + (i ** 2)) % self.size)] is None:

                    self.data[((index + (i ** 2)) % self.size)] = x
                    # print('insert')
                    break

                else:

                    print(f'collision number {i+1} at {((index + (i ** 2)) % self.size)}')

                    if i+1 >= self.maxc:
                        print('Max of collisionChain')
                        break


# 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
# 5 5/one Un,two Deux,three Trois,four Quatre,five Cinq,ten Dix,eleven Onze

def hashing(x):
    value = 0
    for i in x:
        value += ord(i)
    return value


def p_value(val, size):
    n_pa = 4
    for j in range(10*(n_pa+1)):
        print('-', end='')
    print()
    for x in range(10*n_pa):

        if x % 9 == 0:
            print('|', end='')
        elif x == 4+9*0:
            print(val, end='')
            x += len(val)
        elif x == 4+9*1:
            print(hashing(val), end='')
            x += len(str(hashing(i)))
        elif x == 4+9*2:
            print(size, end='')
            x += len(str(size))
        elif x == 4+9*3:
            print(hashing(i)%size, end='')
            x += 1
        else:
            print(' ', end='')

    print()


if __name__ == '__main__':
    print(' ***** Fun with hashing *****')
    user = input('Enter Input : ').split('/')
    size, cnumber = user[0].split()
    data = user[1].split(',')
    ele = [Data(x.split()[0], x.split()[1]) for x in data]

    table = Hash(int(size), int(cnumber))

    # for i in ele:
    #     print(f'i is {i}. hash is {hashing(i.key)}. size is {size}, mod = {hashing(i.key) % int(size)}, type is {type(i)}')

    for i in ele:
        # print(f'i is {i}. hash is {hashing(i.key)}. size is {size}, mod = {hashing(i.key)%int(size)}, type is {type(i)}')
        table.insert(i)
        print(table)

        if not table.is_empty():
            print('This table is full !!!!!!')
            break

