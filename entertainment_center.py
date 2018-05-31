import fresh_tomatoes
import media
""" entertainment_center has all the instances of Movie for the website.
    Modified from Udacity's Programing Foundations with Python coursework. """

# instantiating several Movie objects, URLS from 5/30/2018
# to be used as arguments for fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "https://bit.ly/2H8fATO",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "https://bit.ly/2smRvEa",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

disaster_artist = media.Movie("The Disaster Artist",
                              "https://bit.ly/2LOeMXD",
                              "https://www.youtube.com/watch?v=4qab3TMg42k")

django = media.Movie("Django Unchained",
                     "https://bit.ly/2xt7FRv",
                     "https://www.youtube.com/watch?v=6pKZbJHa17c")

get_out = media.Movie("Get Out",
                      "https://bit.ly/2H8ezeF",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

lobster = media.Movie("The Lobster",
                      "https://bit.ly/2HbbfPE",
                      "https://www.youtube.com/watch?v=JmaCMswlaKo")

split = media.Movie("Split",
                    "https://bit.ly/2kGkZsC",
                    "https://www.youtube.com/watch?v=84TouqfIsiI")

master = media.Movie("The Master",
                     "https://bit.ly/2J1y0vr",
                     "https://www.youtube.com/watch?v=1WTM8eO1Oec")

gone_girl = media.Movie("Gone Girl",
                        "https://bit.ly/2svcVOD",
                        "https://www.youtube.com/watch?v=esGn-xKFZdU")


# list of movie objects for the fresh tomatoes argument
movies = [toy_story, avatar, disaster_artist, django,
          get_out, lobster, split, master, gone_girl]

fresh_tomatoes.open_movies_page(movies)
