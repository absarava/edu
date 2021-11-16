import re
from collections import Counter

# model

# use naive bayes to determine if a word is good enough to replace identified word. Use the word with the max probability
# Naive-Bayes = P(C|W) = P(W|C)*P(C)/P(W)
# P(W) is negligible, P(C) = word count/total count

# gather a corpus of text for reading common words

# use regex to find all the words, or else Counter will give you all the letter and symbol counts

def words(text): return re.findall(r'\w+', text.lower())
WORDS = (Counter(words(open('C:/Users/arjun.b.saravanan/PycharmProjects/Question AI/corpus.txt').read())))


def prob(word, N=sum(WORDS.values())): return f'{round((WORDS[word] / N)*100,5)}%'
#test
prob("simple")

#editing words
def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

e = edits1('fortet')

def found(word): return set(w for w in word if w in WORDS)


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort

def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
#for i in range(n):
 #   print("%d" % arr[i])


def sort_tuple(list):
    length = len(list)
    for i in range(0,length):
        for j in range(0, length-i-1):
            if(list[j][1]<list[j+1][1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

listedits = []
for x in found(edits1("ove")):
     listedits.append((x, WORDS[str(x)]))
#print(listedits)
srt = sort_tuple(listedits)
print(srt)




# find the probabilities that these edits are the replacement word
# P(Cw|W)