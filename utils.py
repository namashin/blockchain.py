import collections


def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(sorted(unsorted_dict.items(), key=lambda d: d[0]))


def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*30} Chain {i} {"="*30}')
        for key, value in chain.items():
            if key == 'transactions':
                print(key)
                for d in value:
                    print(f'{"-"*70}')
                    for kk, vv in d.items():
                        print(f'{kk:30} {vv}')
            else:
                print(f'{key:20} {value}')
    print(f'{"*"*70}')
