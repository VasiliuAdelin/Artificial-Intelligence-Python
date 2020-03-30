import mysql.connector


mydb = mysql.connector.connect(
  host="ai-project.ctmwtumyxzoi.eu-west-3.rds.amazonaws.com",
  user="admin",
  passwd="Halflife48",
  database = "AI_Project"
)
mycursor = mydb.cursor()


def returnMovieIdFromTag(tag):
    param = "\"%" + tag + "%\""
    sql = "select movieid from Tags where tag like " + param
    mycursor.execute(sql)
    movieIds = []
    
    for x in mycursor:
        movieIds.append(x[0])
    return movieIds

def returnMovieIdFromGenre(tag):
    param = "\"%" + tag + "%\""
    sql = "select movieid, genres from Movies where genres like " + param
    mycursor.execute(sql)
    movieIds = []
    for x in mycursor:
        # print(x)
        movieIds.append(x[0])
    return movieIds

def returnRatingForMovieId(movieID):
    sql = "select rating from Ratings where MovieId =" + str(movieID)
    mycursor.execute(sql)
    ratings = []
    for x in mycursor:
        ratings.append(x[0])
    #print(ratings)
    if len(ratings) >= 1:
        return ratings[0]
    else:
        return 0


def returnMovieTitleFromId(movieIds):
    movieTitles = []
    for movieId in movieIds:
        sql = "select Title,ImbdLink from Movies natural join Links where MovieId like  " + str(movieId)
        mycursor.execute(sql)
        for x in mycursor:
            aux = "https://www.imdb.com/title/tt"
            aux = aux + x[1]
            movieTitles.append([x[0],aux]   )
    return movieTitles

def returnLinkFromMovieId(movieIds):
    movieLinks = []
    for movieId in movieIds:
        sql = "select ImbdLink from Movies natural join Links where MovieId like  " + str(movieId)
        mycursor.execute(sql)
        for x in mycursor:
            movieLinks.append(x[0])
    return movieLinks


def returnMovieForRating(rating):
    sql = "select MovieId from Ratings where Rating =" + str(rating)
    mycursor.execute(sql)
    ratings = []
    for x in mycursor:
        ratings.append(x[0])

    return ratings


def bringAllratings():
    sql = "select MovieID, Rating from Ratings"
    mycursor.execute(sql)
    ratings = []
    for x in mycursor:
        ratings.append( {x[0] : x[1]})
    return ratings
