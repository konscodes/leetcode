'''
1. Convert given words to a linked list
2. Pop elements from the both words until they are empty and add those elements to a new list
'''

from collections import deque

def merge(word1: str, word2: str) -> str:
    word1 = deque(word1)
    word2 = deque(word2)
    result = ''
    while word1 or word2:
        if word1:
            result += word1.popleft()
        if word2:
            result += word2.popleft()
    return result


if __name__ == '__main__':
    print(merge('word1', 'word2'))
