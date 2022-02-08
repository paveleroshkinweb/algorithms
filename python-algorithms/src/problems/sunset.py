def sunsetViews(buildings, direction):
	if len(buildings) == 0:
		return []
	is_east = direction == 'EAST'
	max_value = buildings[-1] if is_east else buildings[0]
	views = [len(buildings) - 1] if is_east else [0]
	start = len(buildings) - 2 if is_east else 1
	end = -1 if is_east else len(buildings)
	step = -1 if is_east else 1
	for i in range(start, end, step):
		if buildings[i] > max_value:
			views.append(i)
			max_value = buildings[i]
	if is_east:
		views.reverse()
	return views
