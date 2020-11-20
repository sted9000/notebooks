"""
Need to normalize the flops
Rank in decending order: ['A", 'K', 'K']
Rank into numbers : [12, 11, 11] where 'A' = 12, '2' = 0
Suits correspond to there index in the rank order 'scs'
Suits into xyz: scs = 'xyx'
On paired boards the suited cards will be next to each other meaning xxy and xyy but not xyx
"""
flop = [[8, 7, 3],'xyx']

"""
Lowest Level Operations
- Return an array in descending order
"""







"""
Order of the sub-ranges depending on the nuts
- Return an array in descending order
"""


def pairsNotOnBoard(r):
    lst = []
    ranks = [x for x in range(13)][::-1]
    for rank in ranks:
        if rank not in r:
            lst.append([rank, rank])
    return lst


def bestTwoHighCards(r, number_of_hands):
    lst = []
    ranks = [x for x in range(13)][::-1]
    for rank0 in ranks:
        if rank0 not in r:
            for rank1 in ranks:
                if rank1 not in r:
                    if rank0 is not rank1:
                        lst.append([rank0, rank1])
                        if len(lst) == number_of_hands:
                            return lst
    return lst


def quadsOnPairedBoard(r):
    if r[0] == r[1]:
        return [[r[0], r[1]]]
    else:
        return [[r[1], r[2]]]


def allBoats(r):

    # if unpaired card is lower than pair
    if r[0] == r[1]:
        top_boat = [r[1], r[2]]
        bottom_boat = [r[2], r[2]]

    # if unpaired card is higher than pair
    else:
        top_boat = [r[0], r[0]]
        bottom_boat = [r[0], r[1]]

    return [top_boat, bottom_boat]


def overpairs(r):

    lst = []
    ranks = [x for x in range(13)][::-1]
    for a, b in zip(ranks, ranks):
        if (a not in r) and a > r[2]:
            lst.append([a, b])
    return lst


def flushDrawsPairedBoards(r, s, number_of_hands):

    if s not in ['xxy', 'xyy']:
        return []

    lst = []
    ranks = [x for x in range(13)][::-1]

    for rank in ranks:
        if rank not in r:
            if s == 'xxy':
                lst.append([rank, 'x'])
            else:
                lst.append([rank, 'y'])
            if len(lst) == number_of_hands:
                return lst


def sets(r):
    lst = []
    for rank in r:
        lst.append([rank, rank])
    return lst


def twoPairs(r):
    return [[r[0], r[1]], [r[0], r[2]], [r[1], r[2]]]


def flushBlockersOnFlushBoard(r, number_of_hands):
    lst = []
    ranks = [x for x in range(13)][::-1]
    for rank in ranks:
        if rank not in r:
            lst.append([rank, 'x'])
            if len(lst) == number_of_hands:
                return lst


def flushOnFlushBoard(r):
    lst = []
    ranks = [x for x in range(13)][::-1]
    for rank in ranks:
        if rank not in r:
            lst.append([rank, 'x', 'x'])
    return lst


def straightsUnpairedBoard(r):

    # all three flop cards are connected
    if r[0] - r[2] == 2 or r == [12, 1, 0]:
        if r[0] == 12:  # AKQ
            return [[9, 8]]
        elif r[0] == 11:  # KQJ
            return [[12, 8], [8, 7]]
        elif r[2] == 0:  # A32
            return [[3, 2]]
        elif r[2] == 1:  # 432
            return [[4, 3], [12, 3]]
        else:  # no end of deck concerns
            return [[r[0] + 2, r[0] + 1], [r[0] + 1, r[2] - 1], [r[2] - 1, r[2] - 2]]

    # only one gap in flop cards
    # this means you to have the gap cap and one on either side
    elif r[0] - r[2] == 3:
        lst = []
        ranks = [x for x in range(13)][::-1]
        for r0 in ranks:  # top straight
            if r0 - 1 == r[0]:
                for r1 in ranks:
                    if r1 not in r + [r0]:
                        lst.append([r0, r1])
                        break
        for r0 in ranks:  # bottom straight
            if r0 < r[0] and r0 not in r:
                for r1 in ranks:
                    if 0 < r1 < r[2]:
                        lst.append([r0, r1])
                        break
        return lst

    # two gaps
    # only one straight possible
    # cards must be in between r[0] and r[2]
    # no end of deck issues here
    else:
        if r[0] - r[1] == 2 and r[1] - r[2] == 2:  # 864
            return [r[0] - 1, r[1] - 1]
        elif r[0] - r[1] == 1:  # 874
            return [r[1] - 1, r[2] + 1]
        else:  # 854
            return [r[0] - 1, r[1] + 1]


def betterStraights(r):
    # on 876 there are two JT and J9
    # on 875 there are two J9 and T9
    # on 865 there are two T9 and T7
    # on 854 there are two 97 and 96
    # on 864 there are two T9 and 97
    if r[0] == 12:
        return []
    elif r[0] == 11 and r[1] == 10:
        return []
    elif r == [10, 9, 8]:
        return []

    lst = []
    ranks = [x for x in range(13)][::-1]
    for r0, r1 in zip(ranks, ranks[1:]):
        if r0 not in r and r1 not in r and r0 > r[0]:
            new_board = [r0, r1] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 5:
                lst.append([r0, r1])

    for r0, r1 in zip(ranks, ranks[2:]):
        if r0 not in r and r1 not in r and r0 > r[0]:
            new_board = [r0, r1] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 5:
                lst.append([r0, r1])

    for r0, r1 in zip(ranks, ranks[3:]):
        if r0 not in r and r1 not in r and r0 > r[0]:
            new_board = [r0, r1] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 5:
                lst.append([r0, r1])

    return lst


def wrapsNonPairedBoards(r):
    # wraps need to use three of the whole cards
    lst = []
    ranks = [x for x in range(13)][::-1]

    # three connected whole cards (only top)
    for r0, r1, r2 in zip(ranks, ranks[1:], ranks[2:]):
        if r0 not in r and r1 not in r and r2 not in r and r2 > r[0]:
            new_board = [r0, r1, r2] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 4:
                lst.append([r0, r1, r2])

    # one gap at bottom
    for r0, r1, r2 in zip(ranks, ranks[1:], ranks[3:]):
        if r0 not in r and r1 not in r and r2 not in r:
            new_board = [r0, r1, r2] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 4:
                lst.append([r0, r1, r2])

    # one gap at top
    for r0, r1, r2 in zip(ranks, ranks[2:], ranks[3:]):
        if r0 not in r and r1 not in r and r2 not in r:
            new_board = [r0, r1, r2] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 4:
                lst.append([r0, r1, r2])

    # double one gap
    for r0, r1, r2 in zip(ranks, ranks[2:], ranks[4:]):
        if r0 not in r and r1 not in r and r2 not in r:
            new_board = [r0, r1, r2] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 4:
                lst.append([r0, r1, r2])

    # two gap at bottom
    for r0, r1, r2 in zip(ranks, ranks[1:], ranks[4:]):
        if r0 not in r and r1 not in r and r2 not in r:
            new_board = [r0, r1, r2] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 4:
                lst.append([r0, r1, r2])

    # two gap at top
    for r0, r1, r2 in zip(ranks, ranks[3:], ranks[4:]):
        if r0 not in r and r1 not in r and r2 not in r:
            new_board = [r0, r1, r2] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 4:
                lst.append([r0, r1, r2])

    # three connected whole cards (only bottom)
    for r0, r1, r2 in zip(ranks, ranks[1:], ranks[2:]):
        if r0 not in r and r1 not in r and r2 not in r and r2 < r[0]:
            new_board = [r0, r1, r2] + r
            new_board.sort(reverse=True)
            if new_board[0] - new_board[4] == 4:
                lst.append([r0, r1, r2])

    return lst


def straightDrawsNonPairedBoards(r):
    # here we only need use 4 cards (two from flop and two from hand)

    lst = []
    ranks = [x for x in range(13)][::-1]

    # two connected whole cards
    for r0, r1 in zip(ranks, ranks[1:]):
        if r0 not in r and r1 not in r:
            new_board = [r0, r1] + r[:2]
            new_board.sort(reverse=True)
            if new_board[0] - new_board[3] == 4:
                lst.append([r0, r1])
            new_board = [r0, r1] + r[1:]
            new_board.sort(reverse=True)
            if new_board[0] - new_board[3] == 4:
                lst.append([r0, r1])

    # one gap whole cards
    for r0, r1 in zip(ranks, ranks[2:]):
        if r0 not in r and r1 not in r:
            new_board = [r0, r1] + r[:2]
            new_board.sort(reverse=True)
            if new_board[0] - new_board[3] == 4:
                lst.append([r0, r1])
            new_board = [r0, r1] + r[1:]
            new_board.sort(reverse=True)
            if new_board[0] - new_board[3] == 4:
                lst.append([r0, r1])

    # two gap whole cards
    for r0, r1 in zip(ranks, ranks[3:]):
        if r0 not in r and r1 not in r:
            new_board = [r0, r1] + r[:2]
            new_board.sort(reverse=True)
            if new_board[0] - new_board[3] == 4:
                lst.append([r0, r1])
            new_board = [r0, r1] + r[1:]
            new_board.sort(reverse=True)
            if new_board[0] - new_board[3] == 4:
                lst.append([r0, r1])

    return lst

def flushDrawsNonPairedBoards(r, s, number_of_hands):

    if s == 'xyz':
        return []

    elif s == 'xxy':
        same_suit_ranks = r[:2]
    elif s == 'xyy':
        same_suit_ranks = r[1:]
    elif s == 'xyx':
        same_suit_ranks = [r[0], r[2]]

    lst = []
    ranks = [x for x in range(13)][::-1]

    for rank in ranks:
        if rank not in same_suit_ranks:
            suit = 'x' if s in ['xxy', 'xyx'] else 'y'
            lst.append([rank, suit, suit])
            if len(lst) == number_of_hands:
                return lst


def pairs(r):
    return [[r[0]], [r[1]], [r[2]]]

"""
Ranking the order of the sub-ranges and creating them by calling more granular functions.
"""


def subRangesThreeOfAKind(r, s):

    number_1 = [[r[0]]]  # quads

    number_2 = pairsNotOnBoard(r)  # boats

    number_3 = bestTwoHighCards(r, 3)  # kickers

    return number_1 + number_2 + number_3


def subRangesPaired(r, s):

    number_1 = quadsOnPairedBoard(r)  # quads

    number_2 = allBoats(r)  # boats

    number_3 = overpairs(r)  # overpairs (to the lowest card)

    flush_draws = flushDrawsPairedBoards(r, s, 3)  #

    return number_1 + number_2 + number_3 + flush_draws


def subRangesFlush(r, s):

    number_1 = flushOnFlushBoard(r)

    number_2 = sets(r)

    number_3 = twoPairs(r)

    flush_blockers = flushBlockersOnFlushBoard(r, 3)

    return number_1 + flush_blockers + number_2 + number_3


def subRangesStraight(r, s):

    number_1 = straightsUnpairedBoard(r)

    number_2 = sets(r)

    number_3 = twoPairs(r)

    flush_draws = flushDrawsNonPairedBoards(r, s, 3)

    better_straights = betterStraights(r)

    return number_1 + number_2 + number_3 + flush_draws + better_straights


def subRangesNoBigHands(r, s):

    number_1 = sets(r)

    number_2 = twoPairs(r)

    number_3 = overpairs(r)

    flush_draws = flushDrawsNonPairedBoards(r, s, 3)

    wraps = wrapsNonPairedBoards(r)

    straight_draws = straightDrawsNonPairedBoards(r)

    number_4 = pairs(r)

    return number_1 + number_2 + number_3 + flush_draws + wraps + straight_draws + number_4



def subRanges(flop):

    r = flop[0]
    s = flop[1]

    if r[0] == r[1] == r[2]:
        return subRangesThreeOfAKind(r, s)

    elif r[0] == r[1] or r[1] == r[2]:
        return subRangesPaired(r, s)

    elif s[0] == s[1] == s[2]:
        return subRangesFlush(r, s)

    elif r[0] - r[2] <= 4:
        return subRangesStraight(r, s)

    else:
        return subRangesNoBigHands(r, s)


def subRangeIntsToCards(sub_range_lst):

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    sub_range_cards = []
    for int_lst in sub_range_lst:
        sub = []
        for card in int_lst:
            if isinstance(card, int):
                sub.append(cards[card])
            else:
                sub.append(card)
        sub_range_cards.append(''.join(sub))

    return sub_range_cards


def pptRanges(range):
    lst = []
    for i, sub_range in enumerate(range):
        if i == 0:
            lst.append(sub_range)
        else:
            exclude = ', '.join([x for x in range[:i]])
            lst.append(f"{sub_range}!({exclude})")

    return lst

sub_ranges = subRangeIntsToCards(subRanges(flop))
ppt_ranges = pptRanges(sub_ranges)

print(sub_ranges)
print(ppt_ranges)