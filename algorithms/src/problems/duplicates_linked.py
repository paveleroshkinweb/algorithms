def removeDuplicatesFromLinkedList(linkedList):
    prev = linkedList
	current = linkedList.next
	while current:
		while current and prev.value == current.value:
			current = current.next
		prev.next = current
		prev = current
	return linkedList