

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def createList(l=None):
    if l is None:
        l = []
        head = None
    else:
        if len(l) == 0:
            head = None
        elif len(l) == 1:
            head = Node(l[0])
        else:
            head = None
            curr = None
            for i in range(len(l)):
                if i == 0:
                    head = Node(l[i])
                    curr = head
                else:
                    curr.next = Node(l[i])
                    curr = curr.next
    return head


def printList(H):
    head = H
    while head is not None:
        print(str(head) + ' ', end='')
        head = head.next


def mergeOrderesList(p, q):
    l1 = p
    l2 = q
    head = None
    curr = None

    if int(l1.data) <= int(l2.data):
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    curr = head
    while l1 is not None and l2 is not None:
        if int(l1.data) <= int(l2.data):
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        # print(curr)

    # print('l1 = ', l1)
    # print('l2 = ', l2)

    if l1 is not None:
        while l1 is not None:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
    else:
        while l2 is not None:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

    return head



def main():
    #################### FIX comand ####################
    # input only a number save in L1,L2
    L1, L2 = input('Enter 2 Lists : ').split(' ')
    LL1 = createList(str(L1).split(','))
    LL2 = createList(str(L2).split(','))
    print('LL1 : ', end='')
    printList(LL1)
    print('\nLL2 : ', end='')
    printList(LL2)
    m = mergeOrderesList(LL1, LL2)
    print('\nMerge Result : ', end='')
    printList(m)


def test():
    l1, l2 = '2,2,2,10 1,1,1,1,5,5,5,6,7,8'.split(' ')
    L1 = createList(str(l1).split(','))
    L2 = createList(str(l2).split(','))
    print('L1 = ', end='')
    printList(L1)
    print('\nL2 = ', end='')
    printList(L2)
    print()
    printList(mergeOrderesList(L1, L2))


if __name__ == '__main__':
    main()
