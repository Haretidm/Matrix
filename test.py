def makeInverseIndex(strlist):
    """
Input: a list of documents as strings
Output: a dictionary that maps each word in any document to the set consisting of the
document ids (ie, the index in the strlist) for all documents containing the word.

Note that to test your function, you are welcome to use the files stories_small.txt
or stories_big.txt included in the download.
"""
    inverseIndex = {}
    for (i, s) in enumerate(strlist):
        for w in s.split():
            if w in inverseIndex:
                inverseIndex[w] |= {i}
            else:
                inverseIndex[w] = {i}
    return inverseIndex

def orSearch(inverseIndex, query):
    """
Input: an inverse index, as created by makeInverseIndex, and a list of words to query
Output: the set of document ids that contain _any_ of the specified words
"""
    solution = set()
    for k in query:
        if k in inverseIndex:
            solution |= inverseIndex[k]
    return solution

def andSearch(inverseIndex, query):
    """
Input: an inverse index, as created by makeInverseIndex, and a list of words to query
Output: the set of all document ids that contain _all_ of the specified words
"""
    isFirstItem = True
    for k in query:
        if k in inverseIndex:
            if isFirstItem:
                solution = inverseIndex[k]
                isFirstItem = False
            else:
                solution &= inverseIndex[k]
    return solution


f = open("stories_small.txt")
inverseIndex = makeInverseIndex(f)
print(orSearch(inverseIndex, ['gear', 'builders']))
print(andSearch(inverseIndex, ['gear', 'builders']))