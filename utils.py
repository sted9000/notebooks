def kuber_to_monker(kuber_string):
    kuber_lst = kuber_string.split('\n')

    stripped_flops = [x.split(':')[0] for x in kuber_lst]

    return stripped_flops


def order_cards(flops):
    """

    :param flops: list of strings
    :return: list of strings
    """
    sorted_lst = []
    for flop in flops:
        c0 = [flop[0], flop[1]]
        c1 = [flop[2], flop[3]]
        c2 = [flop[4], flop[5]]

        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        f = [c0, c1, c2]
        f.sort(key=lambda x: ranks.index(x[0]), reverse=True)
        f_str = ''.join(f[0] + f[1] + f[2])
        sorted_lst.append(f_str)

    return sorted_lst


def normalize_suits(flops):
    """

    :param flops: list of strings (ordered cards)
    :return: list of strings (suits now in order: c, s, d, h)
    """
    sorted_lst = []
    for flop in flops:
        suit_str = flop[1] + flop[3] + flop[5]
        new_str = suit_str.copy()
        for suit in suit_str:



    return sorted_lst