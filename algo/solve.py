def solve(wordList,target):
    index = 0
    wordListSet = set(wordList)
    for i in wordList:
        if i == target[:len(i)]:
            if target[:len(i)] == target[len(i):]:
                pass
            elif target[len(i):] in wordListSet:
                return (i,target[len(i):])



