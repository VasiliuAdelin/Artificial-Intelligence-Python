from django.shortcuts import render
from django.http import HttpResponse
from .algorithms import MySqlConn
from .algorithms import token_String
import numpy
from collections import defaultdict
from .algorithms.Word2Vec import *
from .algorithms.word_net import *
from .algorithms.movieDetailsFetcher import *

def index(request):
    return render(request, 'home.htm',{'name':'Adelin'})

def resultRender(request):
    if request.method == "POST":
        sentenceToSearch = request.POST['searchThis']
        movieIds = MainProcedure(sentenceToSearch)
        movieTitles = MySqlConn.returnMovieTitleFromId(movieIds)
        movieLinks = MySqlConn.returnLinkFromMovieId(movieIds)
        movieDetailsFetcher(movieLinks)
        result = []
        for i in range(0,len(movieTitles)):
            tempList = []
            tempList.append(movieTitles[i][0])
            tempList.append(movieTitles[i][1])
            tempList.append(movieDescriptions[i])
            tempList.append(movieMetascores[i])
            tempList.append(movieYears[i])
            tempList.append(moviePosters[i])
            result.append(tempList)
        


        if len(movieTitles) == 0:
            movieTitles.append("Ne pare rau, nu am gasit nimic.")
    return render(request,'result.htm', {'result' : result,'movieTitles': movieTitles,'movieDescriptions' : movieDescriptions,'movieMetascores' : movieMetascores, 'movieYears' : movieYears, 'moviePosters' : moviePosters})

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
            for movie in initialVec:
                if movie in finalMovieList:
                    finalMovieList[movie] = finalMovieList[movie] + 1 
                else:
                    finalMovieList[movie] = 1
        elif token[1] == "r":
            initialVec = MySqlConn.returnMovieForRating(token[0])
            for movie in initialVec:
                if movie in finalMovieList:
                    finalMovieList[movie] = finalMovieList[movie] + 1 
                else:
                    finalMovieList[movie] = 1
        else:
            tagsMovieIds = MySqlConn.returnMovieIdFromTag(token[0])
            #print(tagsMovieIds)

            genresMovieIds = MySqlConn.returnMovieIdFromGenre(token[0])
            #print(genresMovieIds)

            MovieIdsTagsAndGenres = mergeArrays(tagsMovieIds, genresMovieIds)
            #print(MovieIdsTagsAndGenres)

            word2vecSynonims = give_Word2VecSinonims(token[0])
            wordNetSynonims = wordNet(token[0])

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
    movielistwithoutRating = getMovieListWithoutRating(finalMovieList, len(tokens))
    #movielistwithRating = getMovieListWithRating(finalMovieList, len(token))

    return movielistwithoutRating

    
def getMovieListWithoutRating(finalMovieList, tokens):
    dicDeFrec = defaultdict(list)
    for movie in finalMovieList:
        # rating = MySqlConn.returnRatingForMovieId(movie)
        dicDeFrec[finalMovieList[movie]].append(movie)
    max_films = 6
    movielist = []
    frec = tokens
    for i in range(tokens, 0, -1):
        if dicDeFrec[i] != []:
            for j in dicDeFrec[i]:
                if max_films != 0:
                    movielist.append(j)
                    max_films = max_films - 1 
                else:
                    break
    return movielist