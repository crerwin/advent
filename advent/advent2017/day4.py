from advent.day import Day


class Day4(Day):
    year = 2017
    day = 4

    def _part1(self):
        return count_valid_passphrases(self.input(), is_valid_passphrase)

    def _part2(self):
        return count_valid_passphrases(self.input(), is_valid_passphrase_2)


def count_valid_passphrases(passphrases, validate_function):
    count = 0
    for passphrase in passphrases.splitlines():
        if validate_function(passphrase):
            count += 1
    return count


def is_valid_passphrase(passphrase):
    words = passphrase.split()
    if len(words) < 2:
        return False
    for word in words:
        if words.count(word) > 1:
            return False
    return True


def is_valid_passphrase_2(passphrase):
    words = passphrase.split()
    if len(words) < 2:
        return False
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                return False
    return True


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in list(word1):
        if list(word1).count(char) != list(word2).count(char):
            return False
    return True
