import language_check
import random
import numpy.random as rand
import sys

JOIN_FACTOR = 5
POEM_LINE_MEAN = 6
POEM_LINE_STD_DEV = 2

gcheck = None
parts = []
shuffledParts = []
outdir = "./"
if len(sys.argv) < 2:
    outdir = sys.argv[2]
fileName = sys.argv[1]

def isCorrect(text):
    if(len(gcheck.check(text)) == 0):
        return True
    return False

def mapText():
    global parts
    words = []
    text = open(fileName, mode='r+')
    lines = text.readlines()
    for line in lines:
        line = line[:-1]
        lwords = line.split(" ")
        for w in lwords:
            words.append(w)

    i = 0
    while(i < len(words)):
        numberToRead = random.randint(1, JOIN_FACTOR)
        txtToAdd = ""
        for j in range(numberToRead):
            if(i+j < len(words)):
                txtToAdd += words[i+j] + " "
        txtToAdd = txtToAdd[:-1]
        parts.append(txtToAdd)
        i = i + numberToRead


def allPartsMakeSense():
    for p in parts:
        p = camelFirstCase(p) #bc language_check will requires it
        if (not isCorrect(p)):
            return False

    return True


def camelFirstCase(text):
    textArray = list(text)
    textArray[0] = textArray[0].upper()
    return ''.join(textArray)


def assembleParts():
    global shuffledParts
    poem = [] #basically an array of strings

    lineIndex = 0
    while(len(shuffledParts) != 0):
        poem.append("")
        lineWordsNumber = round(rand.normal(POEM_LINE_MEAN, POEM_LINE_STD_DEV))
        while(True):
            if(len(shuffledParts)== 0):
                return poem
            nextPart = shuffledParts.pop(0)
            if(len(nextPart.split()) + len(poem[lineIndex].split()) > lineWordsNumber):
                shuffledParts.insert(0, nextPart)
                break
            poem[lineIndex] = poem[lineIndex] + " " + nextPart
        lineIndex = lineIndex + 1


def shuffleParts():
    global shuffledParts
    shuffledParts = parts.copy()
    random.shuffle(shuffledParts)


def writePoemToFile(poem):
    outputFile=open(outdir+'cut_up_poem.txt','w')

    for line in poem:
        outputFile.write(line)
        outputFile.write('\n')

    outputFile.close()


def main():
    global gcheck
    gcheck = language_check.LanguageTool('en-GB')
    mapText()
    while(not allPartsMakeSense()):
       mapText()
    shuffleParts()
    poem = assembleParts()
    writePoemToFile(poem)


if __name__ == "__main__":
    main()
