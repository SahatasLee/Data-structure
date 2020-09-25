class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

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

    def append(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p
            self.dummy.next = self.head
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1

    def __len__(self):
        t = self.head
        count = 0
        while t is not None:
            t = t.next
            count += 1

        return count

    def is_empty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def insert(self, index, data):
        t = self.search(index-1)
        new_node = Node(data)
        new_node.next = t.next
        t.next = new_node
        self.head = self.dummy.next
        self.size += 1

    def search(self, index):
        t = self.dummy
        count = -1
        # print('index = ', index)
        while t is not None:
            if count == index:
                return t
            t = t.next
            count += 1

    def __str__(self):
        t = self.head
        s = 'link list : '
        if self.__len__() == 0:
            return 'List is empty'
        for i in range(len(self)-1):
            s += str(t) + '->'
            t = t.next
        s += str(t)
        return s

    def display(self):
        print(f'ls = {self.__str__()}, len = {len(self)}')


def main():
    c1 = '1 2, 0:0, 3:3'
    c2 = '0 1 2, -1:3, 10:10'
    c3 = '0 1 2 4, 3:3'
    c4 = ',0:0,1:1'
    c5 = ',1:1'
    ll = Linklist()
    user_input = input('Enter Input : ').split(',')
    # print(user_input)
    for i in range(len(user_input)):
        if i == 0:
            # print(len(user_input[0].split(' ')), user_input[0].split(' '))
            for ele in user_input[0].split(' '):
                if ele == '':
                    continue
                ll.append(str(ele))
            print(ll)
        else:
            index, data = user_input[i].split(':')
            try:
                ll.insert(int(index), data)
                print(f'index = {int(index)} and data = {data}')
            except:
                print('Data cannot be added')
            print(ll)


if __name__ == '__main__':
    main()
