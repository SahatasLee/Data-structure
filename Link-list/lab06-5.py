
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


class Linklist:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
        self.dummy = Node('dummy')
        self.dummy.next = self.head

    def __str__(self):
        curr = self.head
        # s = 'linked list : '
        s = ''
        if curr is not None:
            for i in range(self.size-1):
                s += str(curr) + " "
                curr = curr.next
            s += str(curr)
        # s += '->'
        return s

    def str_reverse(self):
        curr = self.tail
        # s = 'reverse : '
        s = ''
        if curr is not None:
            for i in range(self.size-1):
                s += str(curr) + '->'
                curr = curr.previous
            s += str(curr)
        # s += ']'
        return s

    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.tail = new_node
        self.size += 1
        # print(self.__str__())

    def search_item(self, data):
        # print('seaitm', type(data))
        curr = self.head
        status = False
        while curr is not None:
            if str(curr) == data:
                status = True
                break
            else:
                curr = curr.next
            # if cannot found,curr = None
        return status, curr

    def search_index(self, data):
        curr = self.head
        count = 0
        while curr is not None:
            if curr.data == data:
                break
            else:
                count += 1
                curr = curr.next
        return count

    def at_node(self, index):
        curr = self.head
        status = False
        count = 0

        while curr is not None:
            if count == index:
                status = True
                break
            else:
                curr = curr.next
                count += 1
        # if index < -1 or index >= len, curr = None and status = False
        return status, curr

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def remove(self, data):  # data have to be str(string)
        status, curr = self.search_item(data)
        # print(status, curr)
        pre1 = curr.previous
        pre2 = curr.next
        if status:
            if curr.previous is None:
                self.head = curr.next
                if pre2 is not None:
                    pre2.previous = None
                if self.head is None:
                    self.tail = None
            elif pre2 is None:
                pre1.next = None
                curr.previous = None
                if pre1 is not None:
                    self.tail = pre1
            else:
                pre1.next = curr.next
                pre2.previous = curr.previous
            self.size -= 1
        else:
            print('Not Found!')
        # print(self.__str__())
        return curr

    def insert_item(self, item, data):
        new_node = Node(data)
        status, curr = self.search_item(item)
        if status:
            pre1 = curr.previous
            # pre2 = curr.next
            pre2 = curr
            if curr.previous is None:
                new_node.next = curr
                curr.previous = new_node
                self.head = new_node
            else:
                new_node.next = pre1.next
                pre1.next = new_node
                new_node.previous = pre1
                curr.previous = new_node
        else:
            if self.head is None:
                self.tail = new_node
            else:
                new_node.next = None
                new_node.previous = self.tail
                self.tail.next = new_node
                self.tail = new_node

        self.size += 1

        # print(self.__str__())

    def insert_index(self, index, data):
        new_node = Node(data)
        status, curr = self.at_node(index)
        if status:
            pre = curr.previous

            if curr.previous is None:
                new_node.next = curr
                curr.previous = new_node
                self.head = new_node

            else:
                new_node.next = pre.next
                pre.next = new_node
                new_node.previous = pre
                curr.previous = new_node

        else:

            if index < 0 or index > self.size:
                raise Exception('s')

            if self.head is None:
                self.tail = new_node
                self.head = new_node
            else:
                new_node.next = None
                new_node.previous = self.tail
                self.tail.next = new_node
                self.tail = new_node

        self.size += 1

        # print(self.__str__())

    def show_data(self):
        curr = self.head
        print('forward : ', end='')
        while curr is not None:
            print(curr.data + " ", end='')
            curr = curr.next
        print(',backward : ', end='')
        if self.head is not None:
            curr = self.tail
            while curr is not None:
                print(curr.data + " ", end='')
                curr = curr.previous
        print('')


class Queue:
    def __init__(self, data=None):
        self.item = Linklist()
        self.size = 0
        self.last = None

        if data is not None:
            for i in data:
                self.item.append(i)
                self.size += 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def dequeue(self):
        status, data = self.item.at_node(0)
        d = self.item.remove(str(data))
        self.size -= 1
        return str(d)

    def enqueue(self, data):
        self.item.append(data)
        self.size += 1

    def search(self, index):
        status, index = self.item.at_node(index)
        return index

    def insert(self, index, data):
        self.item.insert_index(index, data)
        self.size += 1

    def __str__(self):
        return str(self.item)


def radix_sort(l):
    q = Queue(l)  # สร้างคิว
    before = str(q.item)
    # print(before)
    count = 0
    max_bits = get_max_bits(max(l))  # หาค่าจำนวนหลักมากที่สุด
    qq = [Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()]
    # เก็บหลัก 0-9
    # สร้าง list ของคิวเพื่อเก็บตามค่าหลักของตัวเลข เริ่มจาก qq[0],qq[1],...qq[9]
    print('------------------------------------------------------------')
    for i in range(1, max_bits+2):
        print(f'Round : {i}', end=' ')
        # print('num = ', end='')
        while not q.is_empty():
            num = int(q.dequeue())
            num_digit = get_digit(num, i)
            # qq[num_digit].enqueue(num)
            # print(num_digit, end=' ')
            pos = qq[num_digit]
            if pos.size == 0:
                qq[num_digit].enqueue(num)
            else:
                for k in range(pos.size):
                    if num <= int(str(pos.search(k))):
                        pos.insert(k, num)
                        break
                    elif k+1 == pos.size:
                        pos.enqueue(num)
            # เก็บค่าเลขตั้งต้นตามค่าจำนวนหลักที่ตรวจสอบ
        print()
        for j in range(len(qq)):
            print(f'{j} : {qq[j].__str__()}')
        # print(qq[0].size, len(before.split()))
        af = qq[0].size
        for i in range(10):
            while not qq[i].is_empty():
                q.enqueue(qq[i].dequeue())
                # สร้างคิวใหม่ตามการเรียงของค่าของเลขในแต่ละหลัก
        print('------------------------------------------------------------')
        count += 1
        if af == len(before.split()):
            break
    return q.item, before, count-1


def get_digit(n, d):  # หาค่าหลัก d จาก n
    if n < 0:
        n = n * -1
    for i in range(d-1):
        n //= 10
    return n % 10


def get_max_bits(n):  # หาค่าจำนวนหลักที่มากที่สุด
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


def main():
    c1 = '64 8 216 512 27 729 0 1 343 125'
    c2 = '-123 456 -789 0 27 3645 133 -142 -5038594 15615 668 2 -1 72'
    c7 = '100 0 10'
    user_input = []
    inp = input('Enter Input : ')
    for i in inp.split():
        user_input.append(int(i))
    s, b, times = radix_sort(user_input)
    print(f'{times} Time(s)')
    print(f'Before Radix Sort : ', end='')
    print(' -> '.join(str(b).split()))
    print(f'After  Radix Sort : ', end='')
    print(' -> '.join(str(s).split()))


def test():
    s = [11, 22, 33, 44]
    q = Queue(s)
    for i in range(10):
        q.enqueue(i)
    print(q)
    print(q.size)
    print(q.is_empty())
    for i in range(10):
        print(type(q.dequeue()))
        # print('q = ', q)
    print(q.is_empty())


if __name__ == '__main__':
    main()
