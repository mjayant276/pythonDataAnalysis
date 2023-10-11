'''
This file contains example for Counter
- Counter is used to count the elements in a iterable object.
'''
from collections import Counter

def playWithCounter(str1):
    words = str1.split(' ')
    wordsCounter = Counter(words)
    # most common
    print(wordsCounter.most_common(10))
    #print(Counter(words).elements())
    worEle = wordsCounter.elements()
    count = 0
    num = 10
    for ele in worEle:
        print(ele)
        count += 1
        if count == num:
            break
    ## total elements in the counter
    print(wordsCounter.total())    

if __name__ == '__main__':
    # cntr = Counter()
    # print(cntr)
    wordText = '''Python is a high-level, general-purpose programming language.
    Its design philosophy emphasizes code readability with the use of 
    significant indentation via the off-side rule.
    Python is dynamically typed and garbage-collected. It supports multiple 
    programming paradigms, including structured (particularly procedural),
    object-oriented and functional programming. It is often described as a 
    "batteries included" language due to its comprehensive standard library.
    Guido van Rossum began working on Python in the late 1980s as a 
    successor to the ABC programming language and first released it in 
    1991 as Python 0.9.0.[37] Python 2.0 
    '''
    playWithCounter(wordText)