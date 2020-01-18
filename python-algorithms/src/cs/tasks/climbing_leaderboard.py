def climbing_leader_board(scores, alice):
    alice_places = []
    filtered_scores = get_filtered_scores(scores)
    start_index = 0
    current_place = 1
    for index in range(len(alice) - 1, -1, -1):
        alice_score = alice[index]
        for i in range(start_index, len(filtered_scores)):
            if alice_score >= filtered_scores[i]:
                alice_places.append(current_place)
                break
            start_index += 1
            current_place += 1
    for i in range(len(alice) - len(alice_places)):
        alice_places.append(len(filtered_scores) + 1)
    alice_places.reverse()
    return alice_places


def get_filtered_scores(scores):
    filtered_scores = []
    prev_score = None
    for score in scores:
        if prev_score != score:
            filtered_scores.append(score)
            prev_score = score
    return filtered_scores
