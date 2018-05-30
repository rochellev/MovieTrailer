import fresh_tomatoes
import media

#calling the init
toy_story = media.Movie("Toy Story", "a story boy toy",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=4KPTXpQehio") 


#print(toy_story.storyline)

avatar = media.Movie("Avatar","alien boys",
                     "https://en.wikipedia.org/wiki/The_Art_of_Avatar#/media/File:Avatar_picture.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print(avatar.storyline)
#avatar.show_trailer()


disaster_artist = media.Movie("The Disaster Artist",
                              "misunderstood actor does bad movie",
                              "https://en.wikipedia.org/wiki/The_Disaster_Artist_(film)#/media/File:TheDisastorArtistTeaserPoster.jpg",
                              "https://www.youtube.com/watch?v=4qab3TMg42k")
#disaster_artist.show_trailer()


movies = [toy_story, avatar, disaster_artist]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)
