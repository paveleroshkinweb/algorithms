def removeKthNodeFromEnd(head, k):
	link_length = length(head)
	if k > link_length:
		return
	if k == link_length:
		head.value = head.next.value
		head.next = head.next.next
		return
	index_from_start = link_length - k
	prev = head
	current = head.next
	for i in range(index_from_start-1):
		prev = current
		current = current.next
	prev.next = current.next


def length(head):
	if not head:
		return 0
	length = 0
	current = head
	while current:
		length += 1
		current = current.next
	return length