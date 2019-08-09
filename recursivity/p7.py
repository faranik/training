"""
Permutations without Dups: Write a method to compute all permutations of a string
of unique characters.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def get_permutations(chars: str) -> list:
    if len(chars) < 1:
        return []
    if len(chars) == 1:
        return [chars]
    else:
        perms = get_permutations(chars[:-1])
        results = []
        for p in perms:
            for i in range(len(p) +1):
                results.append(p[:i] + chars[-1] + p[i:])
        return results
