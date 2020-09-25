

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)


class Linklist:
    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:

                t = t.next
                self.size += 1
            self.tail = t
        self.dummy = Node('dummy')
        self.dummy.next = self.head

    def __str__(self):
        t = self.head
        s = 'linked list : '
        if self.head is not None:
            for i in range(len(self) - 1):
                s += str(t) + '->'
                t = t.next
            s += str(t)
        return s

    def __len__(self):
        return self.size

    def str_reverse(self):
        t = self.tail
        s = 'reverse : '
        if self.head is not None:
            for i in range(len(self) - 1):
                s += str(t) + '->'
                t = t.previous
            s += str(t)
        return s

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.dummy.next = self.head
            self.tail = self.head
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = new_node
            new_node.previous = t
            self.tail = new_node
        self.size += 1

    def insert(self, index, data):
        curr = self.node_at(index)
        new_node = Node(data)
        if index == len(self) and self.dummy.next is not None:
            last = self.tail
            self.tail = new_node
            last.next = new_node
            new_node.previous = last
        elif self.dummy.next is None and index == 0:
            self.head = new_node
            self.tail = new_node
            self.dummy.next = self.head
        elif curr.previous is None:  # head
            self.head = new_node
            new_node.next = curr
            curr.previous = new_node
        elif curr.next is None:  # tail
            curr.next = new_node
            new_node.previous = curr
            self.tail = new_node
        else:
            pre = curr.previous
            pre.next = new_node
            new_node.previous = pre
            curr.previous = new_node
            new_node.next = curr

        self.size += 1

    def node_at(self, index):
        self.dummy.next = self.head
        curr = self.dummy.next
        count = 0
        while curr is not None:
            if count == index:
                return curr
            curr = curr.next
            count += 1

    def remove(self, data):
        curr, count = self.search(data)
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return curr, count
        if curr.previous is None:
            self.head = curr.next
            self.head.previous = None
        elif curr.next is None:
            self.tail = curr.previous
            self.tail.next = None
        else:
            pre = curr.previous
            n = curr.next
            pre.next = n
            n.previous = pre
        self.size -= 1
        return curr, count

    def search(self, data):
        curr = self.head
        count = 0
        while curr is not None:
            if curr.data == data:
                return curr, count
            curr = curr.next
            count += 1

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


def main():
    c1 = 'A 3,A 4,Ab 0,I 1:2'
    c2 = 'I -1:0,I 10:10,I 0:0'
    c3 = 'R 0,A 1,A 1,A 2,R 1'
    c4 = 'I 1:1,I 0:0,I 0:1,I 0:2,I 3:-1,I -1:-1,I 10:5,I 2:0'
    c5 = 'R 0,A 1,A 1,A 2,R 1,I 0:0,I 0:0,R 1,R 1,R 2,R 0,R 0,I 0:0'
    ll = Linklist()
    user_input = input('Enter Input : ').split(',')
    for i in user_input:
        box = i.split(' ')
        if box[0] == 'A':
            ll.append(box[1])
        elif box[0] == 'Ab':
            ll.insert(0, box[1])
        elif box[0] == 'I':
            index, data = box[1].split(':')
            try:
                ll.insert(int(index), data)
                print(f'index = {index} and data = {data}')
            except:
                print('Data cannot be added')
        elif box[0] == 'R':
            try:
                data, count = ll.remove(box[1])
                print(f'removed : {data} from index : {count}')
            except:
                print('Not Found!')
        else:
            print('error')

        print('linked list : ', end='')
        print(ll)
        print('reverse : ', end='')
        print(ll.str_reverse())


def test():
    ls = Linklist()
    ls.insert(0, 'A')
    ls.show_data()
    print(ls.node_at(0))
    ls.append('D')
    ls.insert(0, 'E')
    ls.insert(1, 'B')
    ls.show_data()
    ls.insert(2, 'C')
    ls.show_data()
    ls.remove('A')
    ls.remove('B')
    ls.remove('C')
    ls.remove('D')
    ls.show_data()
    print(len(ls))
    ls.remove('E')
    ls.show_data()
    ls.insert(0, 'F')
    ls.show_data()
    print(ls)
    print(ls.head)
    print(ls.tail)
    print(len(ls))


if __name__ == '__main__':
    main()
