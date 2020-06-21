from copy import copy


def equivalent_cards(cards):

    def equivalent_cards_helper(cards):
        if len(cards) == 1:
            return {cards[0]: 1}
        middle = len(cards) // 2
        left_cards, right_cards = cards[:middle], cards[middle:]
        left_eq_cards = equivalent_cards_helper(left_cards)
        right_eq_cards = equivalent_cards_helper(right_cards)
        representors = copy(left_eq_cards)
        for representor1, count1 in right_eq_cards.items():
            for representor2 in left_eq_cards:
                if representor1 == representor2:
                    representors[representor2] += count1
                    break
            else:
                representors[representor1] = count1
        return representors

    representors = equivalent_cards_helper(cards)
    for count in representors.values():
        if count > len(cards) / 2:
            return True
    return False


def brute_force(cards):
    max_length = 0
    for i in range(len(cards)):
        current_length = 0
        for j in range(len(cards)):
            if cards[i] == cards[j]:
                current_length += 1
        max_length = max(max_length, current_length)
    return max_length > len(cards) / 2
