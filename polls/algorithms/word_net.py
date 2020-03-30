from nltk.corpus import wordnet as wn
import nltk.corpus.reader.wordnet as win
import nltk



def extractWord(word): #synset('black_comedy')
    s = str(word)
    original = s

    start = s.find('(')
    end = s.find('.')
    s = s[start+2:end]

    x = s.find('_')
    if x!=-1:
        s = s[:x] + " " + s[x+1:]
        
    return s

# returneaza un array de cuvinte ~sinomime cu cuvantul dat
def wordNet(word):
    if(len(wn.synsets(word))>0):
        check = wn.synsets(word)[0]   #Synset('dog.n.1'),
        #print(check)

        s = str(check)
        start = s.find('(')
        end = s.find(')')
        s = s[start+2:end-1]

        string = wn.synset(s)
        n = []

        if len(string.hypernyms())>=1:
            n.append(string.hypernyms())

        if len(string.hyponyms())>=1:
            n.append(string.hyponyms())
        cuvinteFinale = []
        #print(n)

        for x in n:
            for y in x:
                cuvinteFinale.append(extractWord(y))
        return cuvinteFinale
    else:
        return []
        
    

    # # for testing the function
    # '''
    # array = wordNet('drama')   # rezultatele, care trebuie parcurse
    # print(array)
    # '''