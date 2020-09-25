
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
                s += str(curr) + ' '
                curr = curr.next
            s += str(curr)
        # s += ']'
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
        # print('seaitm', data)
        curr = self.head
        status = False
        while curr is not None:
            if curr.data == data:
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

    def remove(self, data): # data have to be str(string)
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


def main():
    ll = Linklist()
    cursor = '|'
    ll.append(cursor)

    user_input = input('Enter Input : ').split(',')
    for i in user_input:
        box = i.split(' ')
        if box[0] == 'I':
            ll.insert_item(cursor, box[1])
        elif box[0] == 'L':
            pos = ll.search_index(cursor)
            ll.remove(cursor)
            if pos == 0:
                ll.insert_index(0, cursor)
            else:
                ll.insert_index(pos - 1, cursor)
        elif box[0] == 'R':
            pos = ll.search_index(cursor)
            ll.remove(cursor)
            if pos == ll.size:
                ll.insert_index(pos, cursor)
            else:
                ll.insert_index(pos + 1, cursor)
        elif box[0] == 'B':
            pos = ll.search_index(cursor)
            if pos != 0:
                status, data = ll.at_node(pos - 1)
                # print(type(data))
                ll.remove(str(data))
        elif box[0] == 'D':
            pos = ll.search_index(cursor)
            # print(pos, ll.size)
            if pos != ll.size - 1:
                status, data = ll.at_node(pos + 1)
                ll.remove(str(data))
        else:
            raise Exception('out of order')
        # status, curr = ll.search_item(cursor)
        # print(ll)
        # print(status, curr.previous)
    print(ll)


def test():
    ll = Linklist()
    cursor = '|'
    ll.append(cursor)
    c6 = 'I Apple,I Bird,I Cat,L,L,R,B'
    c7 = 'I Apple,I Bird,L,L,R,D,D'
    c9 = 'I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate'

    user_input = 'I I,I KMITL,L,L,R,I Love'.split(',')
    for i in user_input:
        box = i.split(' ')
        if box[0] == 'I':
            ll.insert_item(cursor, box[1])
        elif box[0] == 'L':
            pos = ll.search_index(cursor)
            ll.remove(cursor)
            if pos == 0:
                ll.insert_index(0, cursor)
            else:
                ll.insert_index(pos-1, cursor)
        elif box[0] == 'R':
            pos = ll.search_index(cursor)
            ll.remove(cursor)
            if pos == ll.size:
                ll.insert_index(pos, cursor)
            else:
                ll.insert_index(pos+1, cursor)
        elif box[0] == 'B':
            pos = ll.search_index(cursor)
            if pos != 0:
                status, data = ll.at_node(pos-1)
                # print(type(data))
                ll.remove(str(data))
        elif box[0] == 'D':
            pos = ll.search_index(cursor)
            # print(pos, ll.size)
            if pos != ll.size-1:
                status, data = ll.at_node(pos+1)
                ll.remove(str(data))
        else:
            raise Exception('out of order')
        # status, curr = ll.search_item(cursor)
        # print(ll)
        # print(status, curr.previous)
    print(ll)


if __name__ == '__main__':
    main()
