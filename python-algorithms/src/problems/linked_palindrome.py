def linkedListPalindrome(head):
    length = find_length(head)
    if length <= 1:
        return True
    if length == 2:
        return head.value == head.next.value
    if length == 3:
        return head.value == head.next.next.value
    parts = length // 2
    prev = head
    current = head.next
    prev.next = None
    head1 = None
    head2 = None
    for i in range(1, parts):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        if i == parts - 1:
            head1 = prev
            if length % 2 != 0:
                head2 = current.next
            else:
                head2 = current
    while head1:
        if head1.value != head2.value:
            return False
        head1 = head1.next
        head2 = head2.next
    return True


def find_length(head):
    if not head:
        return 0
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length
