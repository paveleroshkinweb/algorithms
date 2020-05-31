boys_skills = sorted([int(skill) for skill in input().split()])
girls_skills = sorted([int(skill) for skill in input().split()])


def find_available_pairs(boys_skills, girls_skills):
    i = j = 0
    number_of_pairs = 0
    while i < len(boys_skills) and j < len(girls_skills):
        if abs(boys_skills[i] - girls_skills[j]) in [0, 1]:
            number_of_pairs += 1
            j += 1
            i += 1
        elif boys_skills[i] > girls_skills[j]:
            j += 1
        else:
            i += 1
    return number_of_pairs


print(find_available_pairs(boys_skills, girls_skills))
