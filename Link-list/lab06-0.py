
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
                s += str(curr) + '->'
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

# from random import randint
# from radsadorn import LinkedList

def main():
    c1 = 'A 3,A 4,Ab 0,I 1:2'
    c2 = 'I -1:0,I 10:10,I 0:0'
    c3 = 'R 0,A 1,A 1,A 2,R 1'
    c4 = 'I 1:1,I 0:0,I 0:1,I 0:2,I 3:-1,I -1:-1,I 10:5,I 2:0'
    c5 = 'R 0,A 1,A 1,A 2,R 1,I 0:0,I 0:0,R 1,R 1,R 2,R 0,R 0,I 0:0'
    c6 = 'A 3,  A 4,  Ab 0,  I 1:2'
    ll = Linklist()
    # user_input = c6.split(',')
    user_input = input('Enter Input : ').split(',')

    for i in user_input:
        box = i.split()
        if box[0] == 'A':
            ll.append(box[1])
        elif box[0] == 'Ab':
            ll.insert_index(0, box[1])
        elif box[0] == 'I':
            index, data = box[1].split(':')
            try:
                ll.insert_index(int(index), data)
                print(f'index = {index} and data = {data}')
            except:
                print('Data cannot be added')
        elif box[0] == 'R':
            try:
                # print('box = ', type(box[1]))
                count = ll.search_index(box[1])
                data = ll.remove(box[1])
                print(f'removed : {data} from index : {count}')
            except:
                print('Not Found!')

        print('linked list : ', end='')
        print(ll)
        print('reverse : ', end='')
        print(ll.str_reverse())


def test():
    # ls = Linklist()
    # status, curr = ls.at_node(-1)
    # print(status, curr)
    # ls.insert_index(0, '0')
    # ls.show_data()
    # ls.insert_index(ls.size, 'A')
    # ls.show_data()
    while True:
        ll = Linklist()
        lls = LinkedList()
        # user_input = c4.split(',')
        #user_input = input('Enter Input : ').split(',')
        size = randint(10, 50)
        case = ['A','Ab','I','R']
        user_input = []
        for _ in range(size):
            x = "" + case[randint(0, 3)]
            if x == 'I':
                x += " " + str(randint(-10, 10)) + ':' + str(randint(-10, 10))
            else:
                x += " " + str(randint(-10, 10))
            user_input.append(x)
        user_input = ','.join(user_input)
        print(user_input)
        user_input = user_input.split(',')
        for i in user_input:
            box = i.split(' ')
            if box[0] == 'A':
                ll.append(box[1])
                lls.append(box[1])
            elif box[0] == 'Ab':
                ll.insert_index(0, box[1])
                lls.add_before(box[1])
            elif box[0] == 'I':
                index, data = box[1].split(':')
                try:
                    lls.insert(int(index), data)
                    ll.insert_index(int(index), data)
                    print(f'index = {index} and data = {data}')
                except:
                    print('Data cannot be added')
            elif box[0] == 'R':
                try:
                    lls.remove(box[1])
                    count = ll.search_index(box[1])
                    data = ll.remove(box[1])
                    print(f'removed : {data} from index : {count}')
                except:
                    print('Not Found!')
        # print(ll)
        # print(ll.str_reverse())

        print(ll)
        print(lls)
        if str(ll) != str(lls):
            break


if __name__ == '__main__':
    main()
