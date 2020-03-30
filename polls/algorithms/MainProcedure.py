import MySqlConn
import Word2Vec
import token_String
import numpy
import wordnet
from collections import defaultdict


def mergeArrays(list1, list2):
    list1.extend(list2)
    return numpy.unique(list1)

def MainProcedure(sentence):
    tokens = token_String.tokenizer(sentence)
    count = 0
    finalMovieList = {}
    for token in tokens:
        count = count + 1
        if token[1] == "n":
            initialVec = MySqlConn.returnMovieIdFromTag(token[0])
            # print(initialVec)
        else:
            tagsMovieIds = MySqlConn.returnMovieIdFromTag(token[0])
            #print(tagsMovieIds)

            genresMovieIds = MySqlConn.returnMovieIdFromGenre(token[0])
            #print(genresMovieIds)

            MovieIdsTagsAndGenres = mergeArrays(tagsMovieIds, genresMovieIds)
            #print(MovieIdsTagsAndGenres)

            word2vecSynonims = Word2Vec.give_Word2VecSinonims(token[0])
            wordNetSynonims = wordnet.wordNet(token[0])

            synonims = mergeArrays(word2vecSynonims, wordNetSynonims)
            movieIdList = []
            for synonim in synonims:
                movieIdList.extend(MySqlConn.returnMovieIdFromTag(synonim))
            
            movieIdList = numpy.unique(movieIdList)
            movieIds = mergeArrays(list(movieIdList), list(MovieIdsTagsAndGenres))
                #print(tagsMovieIds)
            if count == 1 :
                for movie in movieIds:
                    finalMovieList[movie] = 1
                # print(len(finalMovieList))
            else:
                for movie in movieIds:
                    if movie in finalMovieList:
                        finalMovieList[movie] = finalMovieList[movie] + 1 
                    else:
                        finalMovieList[movie] = 1
    dicDeFrec = defaultdict(list)
    for movie in finalMovieList:
        rating = MySqlConn.returnRatingForMovieId(movie)
        dicDeFrec[finalMovieList[movie]].append({movie: rating})

    max_films = 1
    movielist = []
    frec = len(tokens)
    for i in range(len(tokens), 0, -1):
        if dicDeFrec[i] != []:
            for j in dicDeFrec[i]:
                if max_films != 0:
                    movielist.append(j)
                    max_films = max_films - 1 
                else:
                    break

    # frec = len(tokens)
    # max_films = 5
    # for movie in finalMovieList:
    #     if max_films != 0:
    #         if finalMovieList[movie] == frec:
    #             rating = MySqlConn.returnRatingForMovieId(movie)
    #             dicDeFrec[finalMovieList[movie]].append({movie: rating})
    #             max_films = max_films - 1
    #         else:
    #             pass
    # print(movielist)            
    return movielist


print(MainProcedure("thriller, fun, drama"))    

    # print(len(dicDeFrec))
    # print(dicDeFrec[3])


    # for movie in finalMovieList:
    #     if finalMovieList[movie] >= 3:
    #         print(movie)    
        