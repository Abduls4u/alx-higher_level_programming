#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    else:
        Best = {'Name': None, 'Score': 0}
        for d, i in a_dictionary.items():
            if i > Best['Score']:
                Best['Name'] = d
                Best['Score'] = i
        return (Best['Name'])
