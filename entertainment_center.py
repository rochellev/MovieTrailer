import fresh_tomatoes
import media
""" entertainment_center has all the instances of Movie for the website.
    Modified from Udacity's Programing Foundations with Python coursework. """

#calling the init for several movies
toy_story = media.Movie("Toy Story",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=4KPTXpQehio") 

avatar = media.Movie("Avatar",
                     "https://filmwonk.files.wordpress.com/2009/12/avatar-poster-neytiri.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

disaster_artist = media.Movie("The Disaster Artist",
                              "https://filmwonk.files.wordpress.com/2017/12/the-disaster-artist-poster.jpg?w=807",
                              "https://www.youtube.com/watch?v=4qab3TMg42k")

django = media.Movie("Django Unchained",
                     "https://filmwonk.files.wordpress.com/2012/12/django-unchained-poster.jpg?w=550&h=786",
                     "https://www.youtube.com/watch?v=6pKZbJHa17c")

get_out = media.Movie("Get Out",
                     "https://filmwonk.files.wordpress.com/2017/02/get-out-movie-poster.jpg?w=562",
                     "https://www.youtube.com/watch?v=sRfnevzM9kQ")

lobster = media.Movie("The Lobster",
                      "https://filmwonk.files.wordpress.com/2016/11/thelobsterposter.jpg?w=562",
                      "https://www.youtube.com/watch?v=JmaCMswlaKo")

split = media.Movie("Split",
                    "https://filmwonk.files.wordpress.com/2017/01/split-poster.jpg?w=562",
                    "https://www.youtube.com/watch?v=84TouqfIsiI")

master = media.Movie("The Master",
                     "https://filmwonk.files.wordpress.com/2012/10/the-master-poster.jpg?w=550&h=817",
                     "https://www.youtube.com/watch?v=1WTM8eO1Oec")

gone_girl = media.Movie("Gone Girl",
                        "https://filmwonk.files.wordpress.com/2014/10/gonegirl1.jpg?w=562",
                        "https://www.youtube.com/watch?v=esGn-xKFZdU")


#list of initialized objects for the fresh tomatoes argument
movies = [toy_story, avatar, disaster_artist, django,
          get_out, lobster, split, master, gone_girl]

fresh_tomatoes.open_movies_page(movies)
