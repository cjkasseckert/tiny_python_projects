#!/usr/bin/env python3
"""Make rhyming words"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    start, rest = stemmer(args.word)
    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""

    word = word.lower()
    vowels = 'aeiou'
    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in vowels])
    pattern = f'([{consonants}]+)?([{vowels}])(.*)'
    pattern = f'([{consonants}]+)?([{vowels}])(.*)'

    if not (match := re.match(pattern, word)):
        return (word, '')
    p1 = match[1] or ''
    p2 = match[2] or ''
    p3 = match[3] or ''
    return (p1, p2 + p3)


# --------------------------------------------------
def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
