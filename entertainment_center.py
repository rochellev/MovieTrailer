import fresh_tomatoes
import media
""" entertainment_center has all the instances of Movie for the website.  """

#calling the init
toy_story = media.Movie("Toy Story",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=4KPTXpQehio") 


#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "https://en.wikipedia.org/wiki/The_Disaster_Artist_(film)#/media/File:TheDisastorArtistTeaserPoster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print(avatar.storyline)
#avatar.show_trailer()


disaster_artist = media.Movie("The Disaster Artist",
                              "https://filmwonk.files.wordpress.com/2017/12/the-disaster-artist-poster.jpg?w=807",
                              "https://www.youtube.com/watch?v=4qab3TMg42k")



movies = [toy_story, avatar, disaster_artist]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)
