from urllib.request import urlopen as req
from bs4 import BeautifulSoup

urlLetterboxd = "https://letterboxd.com/"

movieSet = set()

file = open("letterboxdLists.txt", "r")
for line in file:
    urlList = line
    while True:
        client = req(urlList)
        pageSoup = BeautifulSoup(client.read(), "html.parser")
        client.close()

        movies = pageSoup.findAll("li", {"class": "poster-container"})
        for movie in movies:
            movieName = movie.find("div", {"class": "poster film-poster really-lazy-load"})['data-film-slug']
            movieSet.add(urlLetterboxd + movieName)

        nextUrl = pageSoup.find("a", {"class": "next"})
        if nextUrl is None:
            break
        urlList = urlLetterboxd + nextUrl['href']

movieList = list(movieSet)
movieList.sort()

file = open("movie-list.txt", "w")
for movie in movieList:
    file.write(movie+"\n")
