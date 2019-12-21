class StableMatch:

    def __init__(self, task_preferences_matrix, task_estimation_matrix):
        self.task_preferences_matrix = task_preferences_matrix
        self.task_estimation_matrix = task_estimation_matrix

    def get_stable_pairs(self):
        pairs = {i: [] for i in range(len(self.task_preferences_matrix))}

        def has_empty(list_):
            flag = True
            for i in range(len(list_)):
                flag = flag and list_[i] != []

            return flag

        indexes_prop = [0 for _ in range(len(self.task_preferences_matrix))]
        marked_props = []
        while not has_empty(pairs):
            for i in range(len(pairs)):
                if i not in marked_props:
                    pairs[self.task_preferences_matrix[i][indexes_prop[i]]].append(i)
                    indexes_prop[i] += 1
                    marked_props.append(i)

            for i in range(len(pairs)):
                if len(pairs[i]) > 1:
                    best_proposor, best_priority = None, len(pairs)
                    for j in range(len(pairs[i])):
                        prop_prior = self.task_estimation_matrix[i].index(pairs[i][j])
                        if prop_prior < best_priority:
                            best_proposor, best_priority = pairs[i][j], prop_prior

                    while len(pairs[i]) != 1:
                        for x in pairs[i]:
                            if x != best_proposor:
                                pairs[i].remove(x)
                                marked_props.remove(x)

        return pairs, sum(self.task_estimation_matrix[pairs[x][0]].index(x) for x in pairs), \
               sum(self.task_estimation_matrix[pairs[x][0]].index(x) for x in pairs)

