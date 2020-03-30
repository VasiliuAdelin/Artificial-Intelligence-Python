import http.client
import json

conn = http.client.HTTPSConnection("movie-database-imdb-alternative.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "cf83c2f14emsh4161286bd1fb266p17eb96jsnb548f60e96ed"
    }

# movieIdLinks = ["0114709"]
movieDescriptions = []
movieYears = []
movieMetascores = []
moviePosters = []
def movieDetailsFetcher(movieIdLinks):
    for link in movieIdLinks:
        prepareLink = "/?i=tt" + link + "&r=json"
        conn.request("GET", prepareLink , headers=headers)
        res = conn.getresponse()
        data = res.read()
        y = json.loads(data)
        movieDescriptions.append(y["Plot"])
        movieYears.append(y["Year"])
        movieMetascores.append(y["Metascore"])
        moviePosters.append(y["Poster"])
    # results = []
    # results.append(movieDescriptions)
    # results.append(movieYears)
    # results.append(movieMetascores)
    # results.append(moviePosters)
    # return results


# print(movieDescriptions)
# print(movieMetascores)
# print(moviePosters)
# print(movieYears)