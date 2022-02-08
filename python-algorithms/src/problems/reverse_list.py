def reverseLinkedList(head):
	if not head:
		return
	prev = head
	current = head.next
	prev.next = None
	while current:
		nxt = current.next
		current.next = prev
		prev = current
		current = nxt
	return prev