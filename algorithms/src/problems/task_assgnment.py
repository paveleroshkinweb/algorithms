def taskAssignment(k, tasks):
	tasks_with_indexes = sorted([(idx, task) for idx, task in enumerate(tasks)], key=lambda task: task[1])
	assignments = []
	for i in range(k):
		assignments.append([tasks_with_indexes[i][0], tasks_with_indexes[len(tasks) - i - 1][0]])
	return assignments
