"""Kata - Get All Possible Anagrams from a Hash

completed at: 2024-08-20 12:40:17
by: Jakub Červinka

Given a hash of letters and the number of times they occur, recreate all of the possible anagram combinations that could be created using all of the letters, sorted alphabetically.

The inputs will never include numbers, spaces or any special characters, only lowercase letters a-z.

E.g. get_words({2=>["a"], 1=>["b", "c"]}) => ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"]
"""

from itertools import permutations

def get_words(hash_of_letters):
    word = ''.join(
        letter * n
        for n, letters in hash_of_letters.items()
        for letter in letters
    )
    perms = (''.join(perm) for perm in permutations(word))
    return sorted(set(perms))
