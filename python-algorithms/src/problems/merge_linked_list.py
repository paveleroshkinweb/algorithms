def mergeLinkedLists(headOne, headTwo):
	main_head = headTwo if headOne.value > headTwo.value else headOne
	main = main_head
	prev = None
	second = headTwo if main_head is headOne else headOne
	while main and second:
		if main.value <= second.value:
			prev = main
			main = main.next
		else:
			prev.next = LinkedList(second.value, main)
			second = second.next
			prev = prev.next
	if second:
        prev.next = second
	return main_head